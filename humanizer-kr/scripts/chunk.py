#!/usr/bin/env python3
"""Deterministic chunker for humanizer-kr input text.

Reads raw text from stdin, emits JSON plan on stdout.
Stdlib only. Invoked during Step 2 when input > 2,000 chars.

Usage:
    python3 chunk.py < input.txt
    python3 chunk.py --metaphors "시간이 토큰을 따라간다;배에서는 꼬르륵" < input.txt

Splits at H1/H2 > paragraph > sentence boundaries. Never splits mid-sentence.
Metaphor spans are unsplittable; paragraphs containing them may overflow up to 2,800 chars.
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

ACTIVATION_THRESHOLD = 2000
TARGET = 1500
MIN_CHUNK = 800
HARD_MAX = 2000
OVERFLOW_MAX = 2800
SOFT_CEILING_WARN = 12000

SENTENCE_ENDERS = re.compile(r"(?<=[.!?])\s+|(?<=다\.)\s+|(?<=요\.)\s+|(?<=까\?)\s+|(?<=죠\.)\s+|(?<=네\.)\s+")
HEADING_RE = re.compile(r"^(#{1,2})\s+(.+?)\s*$", re.MULTILINE)
CONJ_INITIAL = ("그러나", "하지만", "그런데", "또한", "뿐만 아니라", "더불어", "나아가",
                "따라서", "그러므로", "그래서", "즉", "한편", "결국", "이처럼", "결과적으로")


@dataclass
class Section:
    level: int
    title: str
    char_offset: int


@dataclass
class Chunk:
    id: int
    char_start: int
    char_end: int
    text: str
    last_two_sentences: str = ""
    conj_initial_tail: List[bool] = field(default_factory=list)


def find_metaphor_spans(text: str, metaphors: List[str]) -> List[Tuple[int, int]]:
    spans: List[Tuple[int, int]] = []
    for phrase in metaphors:
        phrase = phrase.strip()
        if not phrase:
            continue
        start = 0
        while True:
            idx = text.find(phrase, start)
            if idx < 0:
                break
            spans.append((idx, idx + len(phrase)))
            start = idx + len(phrase)
    return spans


def split_into_sentences(text: str) -> List[Tuple[int, int, str]]:
    """Return [(start, end, sentence)] without losing boundary whitespace."""
    sentences: List[Tuple[int, int, str]] = []
    cursor = 0
    for m in SENTENCE_ENDERS.finditer(text):
        end = m.start()
        while end < len(text) and text[end] in "\"'”’)]":
            end += 1
        if end > cursor:
            sentences.append((cursor, end, text[cursor:end]))
            cursor = m.end()
    if cursor < len(text):
        tail = text[cursor:].rstrip()
        if tail:
            sentences.append((cursor, cursor + len(tail), tail))
    return sentences


def find_split_candidates(text: str) -> List[int]:
    """Return char offsets that are natural split points, ranked by priority.

    Heading boundaries first, then blank-line paragraph boundaries, then sentence ends.
    """
    candidates: List[Tuple[int, int]] = []  # (offset, priority; lower = stronger)
    for m in HEADING_RE.finditer(text):
        candidates.append((m.start(), 0))
    for m in re.finditer(r"\n\s*\n", text):
        candidates.append((m.end(), 1))
    for start, end, _ in split_into_sentences(text):
        candidates.append((end, 2))
    candidates.sort(key=lambda pair: (pair[0], pair[1]))
    seen = set()
    ordered: List[int] = []
    for offset, _ in candidates:
        if offset not in seen:
            ordered.append(offset)
            seen.add(offset)
    return ordered


def extract_section_map(text: str) -> List[Section]:
    sections: List[Section] = []
    for m in HEADING_RE.finditer(text):
        sections.append(Section(level=len(m.group(1)), title=m.group(2).strip(), char_offset=m.start()))
    return sections


def crosses_metaphor(start: int, end: int, spans: List[Tuple[int, int]]) -> bool:
    for s, e in spans:
        if s < end and e > start:
            if not (start <= s and e <= end):
                return True
    return False


def pick_split_point(text: str, chunk_start: int, candidates: List[int],
                     metaphor_spans: List[Tuple[int, int]]) -> Optional[int]:
    """Pick the best split point in [chunk_start + MIN_CHUNK, chunk_start + HARD_MAX].

    Falls back to overflow window up to OVERFLOW_MAX when no candidate exists.
    Returns absolute char offset, or None if the remainder fits in one final chunk.
    """
    remainder = len(text) - chunk_start
    if remainder <= HARD_MAX:
        return None

    preferred_min = chunk_start + MIN_CHUNK
    preferred_max = chunk_start + HARD_MAX
    target_point = chunk_start + TARGET

    window = [c for c in candidates if preferred_min <= c <= preferred_max]
    window = [c for c in window if not crosses_metaphor(chunk_start, c, metaphor_spans)]

    def with_priority(offset: int) -> int:
        for m in HEADING_RE.finditer(text[max(0, offset - 2):offset + 3]):
            if offset == m.start() + max(0, offset - 2):
                return 0
        if offset >= 2 and text[offset - 2:offset] == "\n\n":
            return 1
        return 2

    if window:
        best = min(window, key=lambda o: (with_priority(o), abs(o - target_point)))
        return best

    overflow_max = chunk_start + OVERFLOW_MAX
    overflow_window = [c for c in candidates
                       if preferred_max < c <= overflow_max
                       and not crosses_metaphor(chunk_start, c, metaphor_spans)]
    if overflow_window:
        return min(overflow_window, key=lambda o: abs(o - (chunk_start + HARD_MAX)))

    hard_fallback = [c for c in candidates if c > chunk_start + MIN_CHUNK]
    if hard_fallback:
        return hard_fallback[0]
    return None


def last_two_sentences(text: str) -> str:
    sents = split_into_sentences(text)
    if not sents:
        return ""
    tail = sents[-2:]
    return " ".join(s[2].strip() for s in tail)


def conj_tail_bits(text: str) -> List[bool]:
    sents = split_into_sentences(text)
    bits = []
    for _, _, sent in sents[-2:]:
        stripped = sent.lstrip()
        bits.append(any(stripped.startswith(c) for c in CONJ_INITIAL))
    while len(bits) < 2:
        bits.insert(0, False)
    return bits


def build_chunks(text: str, metaphor_spans: List[Tuple[int, int]]) -> List[Chunk]:
    candidates = find_split_candidates(text)
    chunks: List[Chunk] = []
    cursor = 0
    chunk_id = 1
    while cursor < len(text):
        split = pick_split_point(text, cursor, candidates, metaphor_spans)
        if split is None:
            end = len(text)
        else:
            end = split
        segment = text[cursor:end].strip("\n")
        if not segment:
            cursor = end
            continue
        chunks.append(Chunk(
            id=chunk_id,
            char_start=cursor,
            char_end=end,
            text=segment,
            last_two_sentences=last_two_sentences(segment),
            conj_initial_tail=conj_tail_bits(segment),
        ))
        chunk_id += 1
        cursor = end
    return chunks


def main() -> int:
    parser = argparse.ArgumentParser(description="humanizer-kr input chunker")
    parser.add_argument("--metaphors", default="",
                        help="Semicolon-separated metaphor spans to protect from splitting.")
    args = parser.parse_args()

    text = sys.stdin.read()
    total = len(text)
    metaphors = [m for m in args.metaphors.split(";") if m.strip()]
    spans = find_metaphor_spans(text, metaphors)

    warnings: List[str] = []
    if total > SOFT_CEILING_WARN:
        warnings.append(f"input exceeds {SOFT_CEILING_WARN} chars; consider splitting the source")

    section_map = [
        {"level": f"H{s.level}", "title": s.title, "char_offset": s.char_offset}
        for s in extract_section_map(text)
    ]

    if total <= ACTIVATION_THRESHOLD:
        payload = {
            "total_chars": total,
            "activated": False,
            "chunks": [{
                "id": 1,
                "char_start": 0,
                "char_end": total,
                "text": text,
                "last_two_sentences": last_two_sentences(text),
                "conj_initial_tail": conj_tail_bits(text),
            }],
            "section_map": section_map,
            "warnings": warnings,
        }
    else:
        chunks = build_chunks(text, spans)
        payload = {
            "total_chars": total,
            "activated": True,
            "chunks": [{
                "id": c.id,
                "char_start": c.char_start,
                "char_end": c.char_end,
                "text": c.text,
                "last_two_sentences": c.last_two_sentences,
                "conj_initial_tail": c.conj_initial_tail,
            } for c in chunks],
            "section_map": section_map,
            "warnings": warnings,
        }

    json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
