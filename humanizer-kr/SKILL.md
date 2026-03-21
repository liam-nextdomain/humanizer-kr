---
name: humanizer-kr
description: >
  Activated when the user asks to humanize, de-AI, or naturalize Korean text,
  or references "humanizer" / "humanizer-kr" by name,
  or asks to remove AI patterns from Korean writing.
  Not intended for translation, general editing, or non-Korean text.
license: MIT
metadata:
  version: "1.2.0"
  author: ilseoppark
compatibility: Claude Code
---

# Humanizer KR

Writing editor that identifies and removes AI-generated patterns in Korean text to make it sound naturally human. Supports essay/blog and academic/report styles.

| File | Step | Purpose |
| --- | --- | --- |
| `references/patterns-kr.md` | 2, 5 | Pattern index, quantitative thresholds, style rules, audit checklists |
| `references/essay-guide.md` | 3, 4 | Essay/blog treatment rules, speech level rules, voice consultation |
| `references/academic-guide.md` | 3 | Academic/report treatment rules |
| `references/output-format.md` | 2.5, 3.5, 4, 5.5 | Output templates for each workflow phase |

---

## Workflow

### Step 1: Style Detection

- Determine essay/blog vs. academic/report
- MUST ask user if unclear: "에세이/블로그와 논문/보고서 중 어느 쪽으로 처리할까요?"
- For essay: detect and lock speech level (높임말 vs. 반말). MUST NOT change during rewriting. Within 높임말, mixing 하십시오체 and 해요체 is allowed.

### Step 2: Pattern Scan

**MUST READ:** `references/patterns-kr.md` — 14 patterns [A]–[F], quantitative thresholds, style rules table

- MUST check all 14 patterns in order
- Apply style-specific rules (P7, P8, P9 for essay only)

### Step 2.5: Pre-Draft Report & Approval

**MUST READ:** `references/output-format.md` — detection report template

- Present detected issues grouped by pattern category [A]–[F]
- For each category: pattern name, instance count, one representative example
- End with: "전체 수정을 진행할까요? 특정 유형만 선택하실 수도 있고, 거부하실 수도 있습니다."
- MUST wait for user approval. MUST NOT proceed without it.
- If user rejects all, stop here.

### Step 3: First Rewrite (Draft)

**MUST READ:** `references/essay-guide.md` OR `references/academic-guide.md` (per detected style)

**Prerequisite:** User has approved at least one category.

- Remove only patterns from approved categories while preserving meaning
- **Speech level guard (essay):** MUST rewrite every sentence in the same politeness tier detected in Step 1. If original mixes 하십시오체 and 해요체, MUST preserve that mix.
- Essay: vary sentence rhythm (mix short and long); MUST NOT inject voice yet — voice is Step 4
- Academic: maintain objectivity, remove only hollow boilerplate

### Step 3.5: Draft Change Brief

**MUST READ:** `references/output-format.md` — change brief template

- Concise change summary grouped by category (bullet points only)

### Step 4: Voice Consultation (Essay Only)

**MUST READ:** `references/essay-guide.md` — Pattern 9 voice consultation process

1. Identify 2–4 voice injection candidates
2. Present options (3–5 per candidate), wait for author's response
3. Apply author's chosen direction
4. If author declines, proceed to Step 5 without voice injection

### Step 5: Re-Validation

**MUST READ:** `references/patterns-kr.md` — audit checklist

MUST answer before presenting to user:

- [ ] What AI-generated traces remain in this text?
- [ ] (essay) Does every sentence maintain the original speech level tier?
- [ ] Are any approved-category patterns still present?

**MUST READ:** `references/output-format.md` — re-validation report template

- Report remaining issues grouped by category with instance counts and examples
- "아래 패턴이 아직 남아 있습니다. 추가 수정을 진행할까요?"
- MUST wait for user response. MUST NOT produce final output without approval.
- If user rejects all, present current draft as final.

### Step 5.5: Final Change Brief

**MUST READ:** `references/output-format.md` — final brief template

- After final output, produce brief summary of fixes — grouped by category, bullet points only.
