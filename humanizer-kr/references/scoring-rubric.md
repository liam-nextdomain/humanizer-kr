# Scoring Rubric for Evaluator Mode

Used at Steps 3.1, 3.3 (internal review) and Step 5 (re-validation).

This rubric is evaluated in **Evaluator/Auditor mode only**. Do not apply it while generating or rewriting.

---

## How to Use

Score each dimension on a 3-point scale:

| Score | Meaning |
| --- | --- |
| 2 | Passes — no issues found |
| 1 | Marginal — minor issues, no blocking problem |
| 0 | Fails — clear problem; MUST fix before proceeding |

A score of **0 in any dimension** triggers a correction loop (Step 3.2) or must be reported to the user (Step 5).

At Step 3.1/3.3: if total score < 8 OR any single dimension = 0, proceed to Step 3.2. *(v2.4.0: threshold raised from 6/8 to 8/10 to accommodate new Dimension 5.)*

---

## Dimension 1: Originality (독창성)

**Question:** Are there AI-specific clichés, structural templates, or pattern traces still present?

| Score | Criteria |
| --- | --- |
| 2 | No Tier-1 patterns (P15–P23) remain. No formulaic opener/closer. No AI stock phrases (P5). |
| 1 | 1 marginal Tier-2 pattern instance at low density. No Tier-1 traces. |
| 0 | Any Tier-1 pattern remains. Or: AI stock phrase (P5) is present. Or: opener/closer matches a cliché from patterns-kr.md §cliché list. |

**Tier-1 patterns to check (always flag):** P15 (교수법적 프레이밍), P16 (구조적 패딩), P17 (Copula 회피), P18 (부정 병렬), P19 (조어 라벨)

**Anti-camouflage rule:** Tier escalation is a mechanical, count-based check. Count matching structures first, THEN assess quality. A pattern instance counts toward the threshold even if it feels thematically motivated by the essay's argument. The author's intent does not reduce the count.

---

## Dimension 2: Consistency (일관성)

**Question:** Does the rewrite preserve the writing profile locked in Step 1?

| Score | Criteria |
| --- | --- |
| 2 | Vocabulary register, sentence length, tone, and syntactic complexity all match the locked profile. |
| 1 | One trait shows slight drift but stays within the author's plausible range. |
| 0 | Vocabulary register was elevated or simplified. Sentence-length tendency was changed. Tone shifted. Rewrite Contract item regarding style is unmet. |

**Check against Rewrite Contract:** If any contract item specifying style/tone/length is violated → score 0.

---

## Dimension 3: Flow (자연스러움)

**Question:** Do sentences connect naturally without mechanical parallelism or excessive conjunctions?

| Score | Criteria |
| --- | --- |
| 2 | Transitions feel natural. No 3-consecutive-conjunction sequence (P6 rule). No mechanical parallel structure across 3+ consecutive sentences. |
| 1 | One transition feels slightly abrupt or one conjunction chain of 2 is present, but overall readable. |
| 0 | 3+ consecutive conjunctions (P6 threshold). Or: 3+ consecutive sentences with identical syntactic structure (mechanical parallelism). Or: a sentence fragment created by over-splitting. |

---

## Dimension 4: Craft (완성도)

**Question:** Are there awkward word choices or ungrammatical sentences introduced by pattern substitution?

| Score | Criteria |
| --- | --- |
| 2 | All substitutions are natural. No register mismatch. No non-sentence (비문). |
| 1 | One substitution feels slightly unnatural but is grammatically correct. |
| 0 | A pattern swap introduced a non-sentence or clearly unnatural phrasing. Or: a word is used outside its typical register. |

---

## Dimension 5: Structural Readability (구조 가독성) *(v2.4.0)*

**Question:** Did pattern removal damage the author's structural skeleton (headings, section boundaries, conceptual anchors)?

| Score | Criteria |
| --- | --- |
| 2 | Author-intended H1/H2 headings preserved per [patterns-kr.md P10 Header policy](patterns-kr.md). Section boundaries clear. Anchor noun (Preserve item #3) appears at expected density. Reader can navigate the piece without re-reading. |
| 1 | One author heading collapsed into prose, OR one anchor noun was diversified once. Overall structure still legible. |
| 0 | Multiple author H2 headings removed and content collapsed into a single prose blob. OR: anchor noun was forcibly diversified across the text (e.g., "질문" → "물음/의문/묻는 일" 분산). OR: a "Preserve" Contract item was violated. |

**Trade-off detection rule:** Before scoring Dimension 5, run a **delta check** between the Step 3.0 draft and the original:

- [ ] Did the rewrite **remove** an author heading without restating the heading's phrase in the parent paragraph?
- [ ] Did the rewrite **diversify** an anchor noun more than once?
- [ ] Did the rewrite **introduce a new pedagogical lead sentence** ("~를 들여다봅니다", "~쪽 사정을 살펴봅니다", "~를 따져봅니다") that was not in the original? (See [P15](patterns-kr.md))

If any answer is yes → Dimension 5 = 0.

---

## Trade-off Audit (v2.4.0)

Before finalizing any Evaluator score, run this delta check to catch patterns the Generator **introduced** while removing other patterns:

- [ ] **P20 → P15 swap:** Were rhetorical self-Q&A's replaced with declarative sentences that read as teacher-voice ("따져볼 만합니다", "의심해볼 만합니다", "거슬러 짚어볼 수 있습니다", "한 번 생각해 볼 만합니다")? → Each occurrence is a Dimension 1 = 0 trigger.
- [ ] **Heading removal → P15:** Were removed headings replaced with new lead sentences that frame the section pedagogically? → Dimension 5 = 0.
- [ ] **P11 fix → voice loss:** Did fixing an inanimate-subject sentence flatten an originally voice-rich expression (e.g., `~거든요`/`~죠` ending stripped)? → Dimension 2 = 0.
- [ ] **P2 fix → anchor scattering:** Did adjective/verb diversification reach into a thematic anchor noun? → Dimension 5 = 0.

A trade-off is just as bad as the original violation. The total AI-signal count is what matters, not the count of any single pattern.

---

## Quick Checklist (for Evaluator mode)

Run this before scoring to catch the most common issues fast:

**Step 0 — Mechanical count (run BEFORE qualitative checks):**

- [ ] Count all "아니라/아닙니다/않습니다" carrying "not X — rather Y" reframe → if 2+, P18 Tier escalation applies regardless of thematic fit
- [ ] Count each repeated word/adjective (same lemma) across entire text → if 3+, flag P2 regardless of collocation variety
- [ ] Any sentence starts with "결론적으로", "이처럼", "이를 통해", "~에 대해 알아보겠습니다"? → Dimension 1 = 0
- [ ] Any Tier-1 pattern (P15–P23) still present? → Dimension 1 = 0
- [ ] Did sentence length distribution change significantly? → Dimension 2 = 0
- [ ] Are 3+ consecutive sentences using the same connector (그리고/하지만/또한)? → Dimension 3 = 0
- [ ] Is any rewritten sentence ungrammatical or unnatural due to mechanical substitution? → Dimension 4 = 0
- [ ] Are all Rewrite Contract items (Step 2.5) satisfied? → Dimension 2 = 0 for each unmet item
- [ ] Were any author H2/H3 headings removed without preserving the heading phrase in the resulting paragraph? → Dimension 5 = 0
- [ ] Was any thematic anchor noun (from Preserve list) diversified into 2+ variants? → Dimension 5 = 0
- [ ] Did the rewrite introduce any new "들여다봅니다 / 살펴봅니다 / 따져봅니다" framing that wasn't in the original? → Dimension 1 = 0 (new P15)
- [ ] Did the new sentence ratio of `~습니다` vs `~거든요/~죠` drift more than ±20% from the original? → Dimension 2 = 0
