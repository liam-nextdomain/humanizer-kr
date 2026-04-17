---
name: humanizer-kr
description: >
  Identifies and removes AI-generated patterns in Korean writing, producing
  natural human-authored text. Covers essay/blog and academic/report styles
  with per-style pattern handling.
when_to_use: >
  Use when the user asks to humanize, de-AI, or naturalize Korean text, or
  references "humanizer" / "humanizer-kr" by name, or asks to remove AI
  patterns from Korean writing. Skip for translation, general editing, or
  non-Korean text.
metadata:
  version: "2.8.0"
  author: ilseoppark
---

# Humanizer KR

Orchestrator for removing AI-generated patterns from Korean writing. This file coordinates the workflow and communicates progress with the user. Pattern knowledge and style rules live in the reference files below.

## Reference Files

| File | When to read |
| --- | --- |
| `references/patterns-kr.md` | Step 2 (pattern scan) and Step 5 (remaining-pattern check) |
| `references/essay-guide.md` | Steps 2–4, only when style = essay/blog |
| `references/academic-guide.md` | Steps 2–3, only when style = academic/report |
| `scripts/chunk.py` | Step 2 when input > 2,000자 (deterministic input chunking) |

> **Example disclaimer (applies to all reference files):** After examples in guides demonstrate correction *techniques* only. MUST match the original author's vocabulary, sentence length, and tone detected in Step 1 — not the example's.

> **Pattern examples are classification anchors.** patterns-kr.md leads with Before/After pairs and ⚪ Preserve counterexamples. Treat them as canonical exemplars. If a candidate resembles neither a Before example nor a ⚪ Preserve example, the default is retention (mark 🟡 경계 with reasoning, or skip).

---

## Chunking Policy

Long inputs MUST be chunked before pattern scanning to keep each pass within Claude's optimal token window.

- **Activation**: input > 2,000자 triggers chunking. ≤ 2,000자 stays single-pass.
- **Per-chunk target**: 1,500자 (min 800, hard max 2,000, overflow up to 2,800 for unsplittable paragraphs).
- **Soft ceiling**: 12,000자 — warn the user and suggest splitting the source itself.
- **Split priority** (top down, never mid-sentence):
  1. H1/H2 boundary if the resulting chunk lands in [800, 2000].
  2. Blank-line paragraph boundary.
  3. Sentence boundary (`다.`, `요.`, `까?`, `죠.`, `.`, `!`, `?`).
- **Metaphor protection**: Step 1 extracts figurative phrases (e.g., `시간이 토큰을 따라간다`). Pass them via `--metaphors` to prevent splitting across a metaphor span — overflow is preferred over dismembering.

### Invocation

Run `scripts/chunk.py` via bash, piping the source text on stdin:

```bash
python3 humanizer-kr/scripts/chunk.py --metaphors "시간이 토큰을 따라간다;배에서는 꼬르륵"
```

Stdout is JSON:

```json
{
  "total_chars": 5412,
  "activated": true,
  "chunks": [
    {
      "id": 1,
      "char_start": 0,
      "char_end": 1487,
      "text": "...",
      "last_two_sentences": "...",
      "conj_initial_tail": [false, true]
    }
  ],
  "section_map": [{"level": "H2", "title": "...", "char_offset": 812}],
  "warnings": []
}
```

- `chunks[i].last_two_sentences` is the seam context injected into Pass 2 (P6 boundary window) and Step 3 (rewrite rhythm continuity).
- `conj_initial_tail` is a 2-bit flag marking whether each of the last two sentences begins with a conjunction — used to reconstruct P6's 3-sentence window across chunk boundaries.

### Fallback

If `scripts/chunk.py` cannot execute (code-execution disabled or script error), proceed single-pass on the full text and WARN the user: `"청킹 스크립트 실행에 실패해 전체 텍스트를 단일 패스로 처리합니다. 입력이 2,000자를 초과하므로 감지 정확도가 저하될 수 있습니다."`

---

## Workflow

Five steps. Each step ends by communicating status to the user and either waits for approval or advances.

### Step 1: Style Detection & Writing Profile

- Determine **essay/blog** vs. **academic/report**. MUST ask if unclear: "에세이/블로그와 논문/보고서 중 어느 쪽으로 처리할까요?"
- For essay: detect and lock **speech level** (높임말 vs. 반말). MUST NOT cross boundary during rewriting. Within 높임말, mixing 하십시오체 and 해요체 is allowed.
- **Ending-level mixing:** If 합쇼체 is mixed with scattered `~거든요/~죠/~네요/~잖아요/~겁니다`, treat as deliberate conversational voice. MUST lock the ratio.

**Writing Profile — detect and lock before rewriting:**

| Trait | Detect | Lock rule |
| --- | --- | --- |
| Vocabulary register | Sino-Korean ratio, everyday vs. technical | MUST rewrite at same register |
| Sentence length | Short (≤30자), long (60자+), or mixed | MUST preserve predominant pattern |
| Tone | Dry/analytical · warm/narrative · conversational | MUST NOT shift tone |
| Syntactic complexity | Simple S-V vs. multi-layered modification | MUST stay within author's range |
| Ending mix ratio | `~습니다` vs `~거든요/~죠/~네요` across source | New sentences MUST match ratio ±20% |
| Thematic anchor nouns | Nouns in title/headings/definitional sentences | MUST exempt from P2 diversification |
| Structural skeleton | H1 + H2 acts/chapters | MUST preserve as simplified H1+H2 |
| Metaphor spans | Figurative phrases (e.g., `시간이 토큰을 따라간다`) | Pass to `chunk.py --metaphors` to prevent split |
| Section map | H1/H2 offsets in the source | Chunk boundary candidates + location tags |

Profile runs on the FULL source text, not per-chunk. Output is locked before Step 2 chunking.

**Communicate to user:** "스타일은 [essay/academic]으로 판단했습니다. 주요 보존 요소는 [speech level, anchor nouns, structural skeleton...]입니다."

### Step 2: Pattern Scan + Detection Report

**MUST READ:** `references/patterns-kr.md`
**MUST READ (if essay):** `references/essay-guide.md`
**MUST READ (if academic):** `references/academic-guide.md`

If input > 2,000자, run `scripts/chunk.py` per the Chunking Policy above and execute the two-pass architecture (Step 2a + Step 2b). Otherwise, run Step 2b only on the single chunk returned by the script (activated=false).

#### Step 2a: Per-chunk local scan (only when chunking activated)

Announce progress: `"입력 [N]자 → [K]청크로 스캔합니다."` then `"[i/K] 스캔 완료"` per chunk.

For each chunk `C_i`:

- Check all 23 patterns (P1–P14, P15–P23) in order.
- Apply style-specific rules (P7, P8, P9 essay-only).
- Emit a **Local Candidate List** (carry forward to Step 2b, not shown to user):

  ```text
  chunk_id · pattern_id · location_tag · span_text · reason
  P2: lemma="활용" at [C2 · §3. 섹션], occurrence 1 of chunk
  P6: "또한" starts S2 of chunk; conj_initial_tail={S_{k-1}: false, S_k: true}
  P1 local: commas=7, sentences=12, ratio=0.58
  P18/P20/P22: candidate occurrences tagged; tier NOT decided locally
  ```

- Do NOT emit a Detection Report yet. Do NOT wait for user input between chunks.

#### Step 2b: Global aggregation + Detection Report

Merge all Local Candidate Lists into one global view (no reference file re-read needed):

- **P1**: `ratio = Σcommas / Σsentences` across all chunks. Apply 0.40 gate globally.
- **P2**: Group candidates by lemma → global count → apply anchor filter (from Step 1 Profile) → flag at 3+.
- **P6**: Reconstruct 3-sentence windows across boundaries using each chunk's `conj_initial_tail` bits. A window (S_n, S_{n+1}, S_{n+2}) spans two chunks when n is near a boundary — evaluate globally.
- **P18 / P20 / P22**: Sum global occurrences → map to Tier per patterns-kr.md tier table.
- **Mechanical count first, then classify:** For P2, P6, P18, P20, P22 — run counts before judging thematic intent. Instances count even if motivated.
- **Anchor exception:** Apply P2 thematic anchor rule globally. Anchor nouns NOT diversified.
- **Header policy:** Author H1+H2 preserved; fractal H3+ and AI-artifact headers removed.

**Present ONE unified Detection Report + Rewrite Contract + Preserve list, then wait for approval.** Location tags use `[C{i} · §{n}. 섹션]` format when chunking active, `[§{n}. 섹션]` when single-pass.

**Report format rules (MUST follow):**

1. **No "N건 — 예시" single-line summaries.** Each detected case is an independent bullet.
2. **Count breakdown:** `수정 N건 / 경계 M건 / 보존 K건` — the sum MUST equal the actual bullet count under that pattern (count-evidence contract).
3. **Three markers:**
   - 🔴 **수정 권장** — clear AI pattern, fix recommended
   - 🟡 **경계** — borderline; requires user confirmation
   - ⚪ **보존 권장** — anchor noun, authorial metaphor, cited term, natural Korean rhetoric, etc.
4. **Location tag required:** `[0. 섹션]`, `[3. 섹션]`, `[인트로]`, `[결말]` — so the user can locate it in the source immediately.
5. **One-line reason required:** each bullet states *what* and *why*.
6. **Action verb required for 🔴:** "삭제", "분할", "능동형 전환", "직접 서술로 전환", "삼단 나열 해체" etc.
7. If a pattern has zero detections, omit its bullet entirely — do not print empty rows.

**Template:**

```text
**[패턴 감지 결과]**

**[A] 구두점 패턴**
- **P1 쉼표 남용** · 수정 3건 / 경계 2건 / 보존 0건
  - 🔴 [0. 섹션] "경험했기 때문에, 최상급 모델을" — 원인절 뒤 영어식 쉼표. **삭제 권장**
  - 🔴 [3. 섹션] "오래 앉아 있는 대신, AI를 많이" — 부사절 뒤 영어식 쉼표. **삭제 권장**
  - 🟡 [4. 섹션] "확인하니, 이제 10%" — 의존절 연결어미 쉼표. **보존 권장 (경계)**

**[G] 영어 기원 수사 패턴**
- **P18 부정 병렬** · 수정 1건 / 보존 2건
  - 🔴 [2. 섹션] "단순히 많이 사용한다는 건 아니라는 거죠" — AI 재프레이밍. **직접 서술로 전환**
  - ⚪ [0. 섹션] "농담처럼 들리지만 방향은 분명합니다" — 양보 구문(A지만 B). **자연 한국어, 보존**
  - ⚪ [4. 섹션] "몇 시에 자고 ... 아니라, 몇 시에 한도가 리셋되느냐가" — 실체적 대립. **에세이 리듬, 보존**

[...다른 감지 패턴도 동일 포맷...]

---

**[수정 목표 계약 (Rewrite Contract)]** *(🔴 항목만 포함. 🟡은 사용자 협의 결과에 따라 추가·제외.)*
1. [카테고리/패턴] — 예: [G] P18 AI 재프레이밍 1건 직접 서술로 전환
2. [스타일 유지] — 예: 하십시오체 + `~거든요` 산발 비율 보존
3. [톤/방향] — 예: 에세이 톤 유지

**[보존 자산 (Preserve)]** *(⚪ 항목 및 앵커·메타포·인용 명시. Rewrite Contract보다 우선한다.)*
1. voice/어미 — 예: 합쇼체 + `~거든요/~죠` 비율
2. 구조 — 예: H1 + H2 보존, 마지막 단락 단문 리듬 보존
3. 어휘 anchor — 예: 핵심 주제어 `질문/토큰`은 P2·P22 카운팅 제외
4. 메타포 — 예: `시간이 토큰을 따라간다` 메타포 보존
5. 인용 — 예: `클로드노믹스`, `토큰 전설` 외부 출처 인용 보존
6. 기타 — 작가 명시 보존 요구

이 방향으로 초안 작업을 시작할까요? 🟡 경계 항목은 어떻게 처리할지 함께 말씀해 주세요.
```

- MUST wait for user approval. MUST NOT proceed without it.
- If user rejects all, stop here.
- Rewrite Contract is binding for Step 3. Preserve items override Contract when they conflict.
- **Step 2b output contract:** This Step 2b response MUST contain only the Detection Report + Contract + Preserve list, then stop. Step 3 draft is deferred to the next response after approval.

### Step 3: Rewrite

**Prerequisite:** User approved at least one category in Step 2.

**Chunked rewrite (when chunking was active in Step 2):**

Rewrite each chunk independently, then concatenate. Each chunk rewrite call receives:

1. **Writing Profile** from Step 1 (locked).
2. **Rewrite Contract** (approved 🔴 items, scoped to this chunk's candidates).
3. **Preserve list** (global — applies to every chunk).
4. **Seam context**: the previous chunk's `last_two_sentences` from the chunk.py output — reference for rhythm and ending-ratio continuity. Do NOT copy its vocabulary.
5. **Global anchor noun list** from Step 1 Profile — prevents cross-chunk diversification drift.

After concatenation, run a **seam smoothing pass** on the 2-sentence overlap at each boundary: verify the transition reads naturally (no abrupt topic shift, consistent speech level, no re-introduced conjunction chain). Adjust only the seam, never the chunk bodies.

**Generator guards (all MUST hold):**

| Guard | Rule |
| --- | --- |
| Speech level | MUST rewrite every sentence in the Step 1 tier. For mixed 하십시오체+해요체, preserve the mix. |
| Ending mix | NEW sentences sample the Step 1 ratio ±20%. Do NOT default new sentences to `~습니다`. |
| Writing profile | MUST preserve register, sentence length, tone, syntactic complexity from Step 1. Guide examples show *what* to fix, not *how* the author writes. MUST NOT copy the guide's vocabulary/rhythm. |
| Preserve override | Preserve items outrank Contract fixes. If a fix would violate a Preserve item, skip the fix. |
| Trade-off | When removing P20 or P10, MUST NOT substitute pedagogical lead sentences (`~를 들여다봅니다`, `~쪽 사정을 살펴봅니다`) — that re-introduces P15. Use plain declarative continuation. |
| Anchor noun | Thematic anchor nouns stay in canonical form. Do NOT diversify. |
| Essay rhythm | If original varies rhythm, preserve it; if monotonous, add mild variation within author's predominant length. MUST NOT inject voice (voice = Step 4). |
| Academic objectivity | Maintain objective tone; remove only hollow boilerplate. |

**Output Draft + Change Brief:**

```text
**1차 재작성본 (Draft)**
[rewritten text]

**[1차 수정 브리핑]**
- [A] ...
- [C] ...
```

### Step 4: Voice Consultation (Essay Only)

**MUST READ:** `references/essay-guide.md` — Pattern 9 voice consultation process

1. Identify 2–4 voice injection candidates
2. Present 3–5 options per candidate; wait for author's choice
3. Apply the chosen direction; if author declines, proceed to Step 5 without voice injection

Voice option template:

```text
**[목소리 협의 — 에세이 전용]**

**[V1]** 원문 문장 발췌
→ 이 부분에 작가님만의 관점을 담을 수 있습니다. 어떤 방향이 가장 가깝나요?

1. (동의/긍정) 예시 문장
2. (회의/비판) 예시 문장
3. (개인 경험 연결) 예시 문장
4. (열린 물음 제기) 예시 문장
5. (직접 의견 입력) 원하시는 관점을 직접 말씀해 주세요.
```

Academic style: MUST skip Step 4 entirely.

### Step 5: Remaining-Pattern Check

**MUST READ:** `references/patterns-kr.md`

Re-scan the Step 3/4 output for patterns. If Step 2 was chunked, run the same two-pass architecture on the JOINED final output — Pass 1 per chunk (re-run `chunk.py` on the rewritten text), Pass 2 global aggregation. **Global re-count of P2, P6, P18, P20, P22 is mandatory** because per-chunk recheck cannot validate tier thresholds.

Run mechanical counts first (P2, P6, P18, P20, P22). Check:

- [ ] Approved-category patterns still present?
- [ ] (essay) Every sentence in original speech-level tier?
- [ ] (essay) `~습니다` vs `~거든요/~죠` ratio matches Step 1 ±20%?
- [ ] Rewrite Contract items satisfied?
- [ ] Preserve items satisfied?
- [ ] Trade-off: did the rewrite introduce P15 lead sentences, anchor diversification, or new comma clusters?

**If remaining issues exist:**

```text
**[재검증 결과]**
- P_X (설명): N건 — 예시: "..."

추가 수정을 진행할까요? 그대로 제출하실 수도 있습니다.
```

- If user requests more fixes → return to Step 3 with narrowed scope.
- If user says "그대로 제출" or no issues remain → output final version + brief.

**Final output:**

```text
**최종본**
[final rewritten text]

**[최종 수정 브리핑]**
- [category] ...
```
