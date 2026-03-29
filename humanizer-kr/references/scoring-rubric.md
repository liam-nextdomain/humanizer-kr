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

At Step 3.1/3.3: if total score < 6 OR any single dimension = 0, proceed to Step 3.2.

---

## Dimension 1: Originality (독창성)

**Question:** Are there AI-specific clichés, structural templates, or pattern traces still present?

| Score | Criteria |
| --- | --- |
| 2 | No Tier-1 patterns (P15–P23) remain. No formulaic opener/closer. No AI stock phrases (P5). |
| 1 | 1 marginal Tier-2 pattern instance at low density. No Tier-1 traces. |
| 0 | Any Tier-1 pattern remains. Or: AI stock phrase (P5) is present. Or: opener/closer matches a cliché from patterns-kr.md §cliché list. |

**Tier-1 patterns to check (always flag):** P15 (교수법적 프레이밍), P16 (구조적 패딩), P17 (Copula 회피), P18 (부정 병렬), P19 (조어 라벨)

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

## Quick Checklist (for Evaluator mode)

Run this before scoring to catch the most common issues fast:

- [ ] Any sentence starts with "결론적으로", "이처럼", "이를 통해", "~에 대해 알아보겠습니다"? → Dimension 1 = 0
- [ ] Any Tier-1 pattern (P15–P23) still present? → Dimension 1 = 0
- [ ] Did sentence length distribution change significantly? → Dimension 2 = 0
- [ ] Are 3+ consecutive sentences using the same connector (그리고/하지만/또한)? → Dimension 3 = 0
- [ ] Is any rewritten sentence ungrammatical or unnatural due to mechanical substitution? → Dimension 4 = 0
- [ ] Are all Rewrite Contract items (Step 2.5) satisfied? → Dimension 2 = 0 for each unmet item
