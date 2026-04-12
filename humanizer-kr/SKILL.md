---
name: humanizer-kr
description: >
  Activated when the user asks to humanize, de-AI, or naturalize Korean text,
  or references "humanizer" / "humanizer-kr" by name,
  or asks to remove AI patterns from Korean writing.
  Not intended for translation, general editing, or non-Korean text.
license: MIT
metadata:
  version: "2.4.0"
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
| `references/scoring-rubric.md` | 3.1, 3.3, 5 | 5-dimension quality rubric for Evaluator mode |

---

## Workflow

### Step 1: Style Detection & Writing Profile

- Determine essay/blog vs. academic/report
- MUST ask user if unclear: "에세이/블로그와 논문/보고서 중 어느 쪽으로 처리할까요?"
- For essay: detect and lock speech level (높임말 vs. 반말). MUST NOT change during rewriting. Within 높임말, mixing 하십시오체 and 해요체 is allowed.
- **Ending-level mixing:** If 합쇼체 is mixed with scattered `~거든요/~죠/~네요/~잖아요/~겁니다`, treat it as deliberate conversational voice. MUST lock the ratio. See `references/essay-guide.md` — Ending-level mixing detection.

**Writing profile — detect and lock the following traits before rewriting:**

| Trait | What to detect | Lock rule |
| --- | --- | --- |
| Vocabulary register | Sino-Korean (한자어) ratio, everyday vs. technical diction | MUST rewrite at the same register — do not elevate or simplify |
| Sentence-length tendency | Predominantly short (≤30 chars), long (60+ chars), or mixed | MUST preserve the author's predominant pattern |
| Tone | Dry/analytical vs. warm/narrative vs. conversational | MUST NOT shift tone during rewriting |
| Syntactic complexity | Simple S-V structures vs. multi-layered modification | MUST stay within the author's complexity range |
| Ending mix ratio | Approximate `~습니다` vs `~거든요/~죠/~네요` ratio across the source | MUST sample new sentences in roughly the same ratio (±20%) |
| Thematic anchor nouns | Nouns in the title, headings, or definitional sentences | MUST exempt from P2 diversification — record as Preserve item |
| Author-intended structural skeleton | H1 + H2 headings that organize the piece into named acts/chapters | MUST preserve as simplified H1+H2; only fractal H3+ depth is removed |

### Step 2: Pattern Scan

**MUST READ:** `references/patterns-kr.md` — 23 patterns [A]–[G], quantitative thresholds, style rules table

- MUST check all 23 patterns in order (P1–P14 then P15–P23)
- Apply style-specific rules (P7, P8, P9 for essay only)
- **Mechanical-count-first:** Before classifying any instance, run counts on P2 (lemma repetition), P6 (consecutive conjunctions), P18 (negative parallelism), P20 (rhetorical Q), P22 (anaphora). Instances count even if thematically motivated.
- **Anchor noun guard:** Apply the P2 thematic anchor exception (see `references/patterns-kr.md` P2 Counting rule). Anchor nouns are NOT diversified.
- **Header policy:** Apply the P10 header policy. Author H1+H2 are preserved; only fractal H3+ and AI-artifact headers are removed.

### Step 2.5: Pre-Draft Report & Approval

**MUST READ:** `references/output-format.md` — detection report template

- Present detected issues grouped by pattern category [A]–[G]
- For each category: pattern name, instance count, one representative example
- After the pattern report, present a **Rewrite Contract** (see `references/output-format.md` — Rewrite Contract template):
  - List up to 3 concrete completion criteria derived from the detected issues and the locked writing profile
  - Append a **Preserve list** (5 slots: voice/어미, structure, anchor noun, metaphor, other). Generator MUST treat Preserve items as higher-priority than Contract criteria.
  - End with: "이 방향으로 초안 작업을 시작할까요? 수정이 필요하면 말씀해 주세요."
- MUST wait for user approval. MUST NOT proceed without it.
- If user rejects all, stop here.
- Rewrite Contract is binding: Step 3 Generator and Step 5 Evaluator MUST use it as the Definition of Done.
- **Long-text chunking:** If input > 800 Korean chars, this Step 2.5 response MUST contain only the Detection Report + Contract + Preserve list, then stop for approval. MUST NOT include the Step 3 draft. Shorter inputs MAY include the draft in the next response after approval.

### Step 3: First Rewrite (Draft) — with Internal Correction Loop

**MUST READ:** `references/essay-guide.md` OR `references/academic-guide.md` (per detected style)

**Prerequisite:** User has approved at least one category.

#### Step 3.0: Generate Draft (Generator mode)

- Remove only patterns from approved categories while preserving meaning
- **Speech level guard (essay):** MUST rewrite every sentence in the same politeness tier detected in Step 1. If the original mixes 하십시오체 and 해요체, MUST preserve that mix.
- **Ending mix guard (essay):** For any NEW sentence (not in source), MUST sample its ending in the Step 1 ratio (±20%). Do NOT default new sentences to `~습니다`.
- **Writing-profile guard:** MUST preserve the author's vocabulary register, sentence length, tone, and syntactic complexity from Step 1. Guide After examples show *what* to fix, not *how* the author writes — MUST NOT copy their vocabulary, rhythm, or tone.
- **Preserve guard:** Preserve items (Step 2.5) override Contract fixes. If a fix would violate a Preserve item, skip the fix.
- **Trade-off guard:** When removing P20 or P10, MUST NOT replace with pedagogical lead sentences (`~를 들여다봅니다`, `~쪽 사정을 살펴봅니다`, `~를 따져봅니다`, `~을 한 번 짚어봅니다`) — they re-introduce P15. Use plain declarative continuation.
- **Anchor noun guard:** Thematic anchor nouns (Preserve item #3) MUST stay in canonical form. Do NOT diversify into variants.
- Essay: if the original already varies sentence rhythm, preserve it; if monotonous, introduce mild variation within the author's predominant length. MUST NOT inject voice yet — voice is Step 4.
- Academic: maintain objectivity, remove only hollow boilerplate

#### Step 3.1: Internal Review (Evaluator mode — do NOT show to user)

**MUST READ:** `references/scoring-rubric.md`

**Persona switch:** You are now a critical Auditor, not the Generator. Your job is to find flaws in the Step 3.0 draft. Treat it with suspicion.

- Score the draft on all 5 dimensions in `references/scoring-rubric.md`
- Check Rewrite Contract items AND Preserve items from Step 2.5 one by one
- Run **Trade-off Audit** (see scoring-rubric.md). Patterns introduced while removing others count as failures.
- If any Tier-1 trace (P15–P23 Tier 1) remains → MUST proceed to Step 3.2
- If any Contract or Preserve item is unmet → MUST proceed to Step 3.2
- If any trade-off is detected → MUST proceed to Step 3.2
- If all checks pass and no Tier-1 traces remain → skip to Step 3.5

#### Step 3.2: Internal Correction (Generator mode — do NOT show to user)

**Persona switch:** Return to Generator mode. Apply the Evaluator's Step 3.1 critique. Fix only the flagged items — do not over-correct.

#### Step 3.3: Final Internal Check (Evaluator mode — do NOT show to user, 1 pass only)

**Persona switch:** Auditor again. Confirm Step 3.2 corrections resolved the flagged issues. No further internal loops after this.

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
**MUST READ:** `references/scoring-rubric.md` — 5-dimension rubric

**Persona switch:** You are now an independent Auditor. You did NOT write this text. Find every flaw the Generator missed. Assume the draft has problems until proven otherwise.

**Mechanical-count-first:** Before qualitative assessment, run pattern-specific counts (P2 lemma repetition, P18 negative parallelism, P6 conjunction chains). Tier escalation is count-based — an instance counts even if thematically justified. Count first, then assess.

MUST answer before presenting to user:

- [ ] What AI-generated traces remain in this text?
- [ ] (essay) Does every sentence maintain the original speech-level tier?
- [ ] (essay) Does the `~습니다` vs `~거든요/~죠` ratio match the Step 1 ratio (±20%)?
- [ ] Are any approved-category patterns still present?
- [ ] Are all Rewrite Contract items from Step 2.5 satisfied?
- [ ] Are all Preserve items from Step 2.5 satisfied?
- [ ] Did the rewrite introduce any new patterns (P15 lead sentences, anchor noun diversification, etc.)? Run Trade-off Audit.
- [ ] Does the scoring rubric (all 5 dimensions) confirm the draft is acceptable?

**MUST READ:** `references/output-format.md` — re-validation report template

- Report remaining issues grouped by category with instance counts and examples
- "아래 패턴이 아직 남아 있습니다. 추가 수정을 진행할까요?"
- MUST wait for user response. MUST NOT produce final output without approval.
- If user rejects all, present current draft as final.

### Step 5.5: Final Change Brief

**MUST READ:** `references/output-format.md` — final brief template

- After final output, produce brief summary of fixes — grouped by category, bullet points only.
