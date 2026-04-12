# Essay / Blog Style Guide

> **Example disclaimer:** The After examples below demonstrate correction *techniques* only. They are NOT style targets. When rewriting, match the original author's vocabulary level, sentence length, and tone — not the examples'. See SKILL.md Step 1 Writing Profile for the traits to preserve.

This guide covers **essay-specific exceptions and variations only**. For universal pattern definitions, detection criteria, and Before/After examples, see patterns-kr.md.

## Table of Contents

1. [Speech Level Rule](#speech-level-rule)
2. [Pattern 1. Comma Overuse](#pattern-1-comma-overuse--essay-treatment)
3. [Pattern 2. Low Vocab Diversity](#pattern-2-low-vocab-diversity--not-applicable)
4. [Pattern 3. Rule of Three & Bullet-Point Enumeration](#pattern-3-rule-of-three--bullet-point-enumeration--essay-treatment)
5. [Pattern 5. AI High-Frequency Expressions](#pattern-5-ai-high-frequency-expressions--essay-treatment)
6. [Pattern 6. Conjunction Overuse](#pattern-6-conjunction-overuse--essay-treatment)
7. [Pattern 7. Bound Noun Spacing](#pattern-7-bound-noun-spacing-의존명사-띄어쓰기--essay-only)
8. [Pattern 8. Auxiliary Verb Spacing](#pattern-8-auxiliary-verb-spacing-보조용언-띄어쓰기--essay-only)
9. [Pattern 9. Absence of Voice / Personality](#pattern-9-absence-of-voice--personality--essay-only)
10. [Pattern 10. Communication Artifacts](#pattern-10-communication-artifacts--essay-treatment)
11. [Pattern 11. Inanimate Subject Personification](#pattern-11-inanimate-subject-personification--essay-treatment)
12. [Pattern 12. Unnecessary Passive / Relative Clause Overuse](#pattern-12-unnecessary-passive--relative-clause-overuse--essay-treatment)
13. [Pattern 13. Empty Subject & ~는 것이다 Construction](#pattern-13-empty-subject--는-것이다-construction--essay-treatment)
14. [Pattern 14. Causative 만들다 Direct Translation](#pattern-14-causative-만들다-direct-translation--essay-treatment)
15. [Example 1: Full Worked Example](#example-1-essay-style-full-worked-example)

---

## Speech Level Rule

- MUST preserve the original tier (높임말 or 반말) throughout. MUST NOT cross the boundary.
- Within 높임말, mixing 하십시오체 and 해요체 is allowed.
- The examples below are written in specific speech levels for illustration. When rewriting, always match the original.

### Ending-level mixing detection (v2.4.0)

When a 합쇼체-dominant essay sprinkles 해요체 endings (`~거든요`, `~죠`, `~네요`, `~잖아요`) onto otherwise `~습니다/~입니다` sentences, this is **NOT** an inconsistency to normalize — it is a deliberate **conversational voice signal** the author chose. Detect this in Step 1 and lock it as a preserve item.

| Pattern | Author signal | Generator action |
| --- | --- | --- |
| 합쇼체 + scattered `~거든요` | Conversational warmth, reader-aside | **MUST preserve every `~거든요` instance** |
| 합쇼체 + scattered `~죠` | Soft assertion, shared assumption | **MUST preserve every `~죠` instance** |
| 합쇼체 + scattered `~네요/~잖아요` | Discovery / shared knowledge | **MUST preserve every instance** |
| 합쇼체 + scattered `~겁니다` (the colloquial reduction of `~것입니다`) | Informal aside within formal register | Preserve; do NOT expand to `~것입니다` |

**Generator guard:** When generating a NEW sentence to replace a removed AI sentence, MUST sample the ending tier in proportion to the source text. If the source had 80% `~습니다` / 20% `~거든요/~죠`, replacement sentences MUST roughly match that ratio. Defaulting all new sentences to `~습니다` flattens the author's voice and is a Dimension 2 (Consistency) violation.

**Anti-pattern (do not do this):**

| Original (preserve) | Wrong rewrite (flattens voice) | Correct rewrite |
| --- | --- | --- |
| "그 순간에는 비용 같은 건 없거든요." | "그 순간에는 비용 같은 것이 없습니다." | (leave unchanged) |
| "많이 쓸수록 잘하고 있다는 뜻이 되는 거죠." | "많이 쓸수록 잘하고 있다는 의미입니다." | (leave unchanged) |

---

## Pattern 1. Comma Overuse — Essay Treatment

**Essay-specific rule:** Remove commas aggressively. Split sentences or use connective endings where comma removal alone leaves an awkward join. See patterns-kr.md §1 for universal comma removal/retention criteria.

---

## Pattern 2. Low Vocab Diversity — Not Applicable

Not style-specific. Universal counting rule (same verb/adj 3+ times) applies across all styles. See patterns-kr.md §1 P2.

---

## Pattern 3. Rule of Three & Bullet-Point Enumeration — Essay Treatment

**Before (Rule of Three):**
> 성공적인 프로젝트 수행을 위해서는 세 가지 요소가 중요하다. 첫째, 팀원들 간의 원활한 소통이 이루어져야 한다. 둘째, 명확한 목표 설정과 일정 관리가 필요하다. 셋째, 예상치 못한 변수에 대응할 수 있는 유연한 태도를 갖추어야 한다.

**Treatment:** Break the rule-of-three. Keep only the most important point or merge into natural flow.

**After:**
> 프로젝트를 성공하려면 팀원들 간의 원활한 소통이 이루어져야 한다. 목표를 명확히 설정하고 일정 관리가 뒷받침될 때 예상치 못한 변수에 대응할 수 있는 유연한 태도도 갖출 수 있다.

**Before (개조식 — bullet-point enumeration, Park & Kim, 2025):**
> 복잡계과학의 특징은 다음과 같다.
>
> 1) 비선형성: 원인과 결과가 비례하지 않는다.
> 2) 자기조직화: 외부 통제 없이 질서가 형성된다.
> 3) 창발성: 부분의 합 이상의 새로운 속성이 나타난다.

**Treatment:** Convert bullet-point fragments into connected prose. Develop each point with reasoning or examples instead of one-line declarations.

**After:**
> 복잡계과학의 핵심은 비선형성에 있다. 원인과 결과가 단순히 비례하지 않기 때문에 작은 변화가 거대한 결과를 낳기도 한다. 이런 비선형적 상호작용 속에서 외부의 통제 없이도 스스로 질서가 만들어지는 자기조직화 현상이 일어나며, 개별 요소만으로는 설명할 수 없는 새로운 속성이 전체 수준에서 드러나기도 한다.

**Comma-separated three-item clausal list:**

This is a variant of Rule of Three where three clause-level items are listed with commas instead of 첫째/둘째/셋째. Detect and rewrite into natural prose flow.

**Before:**
> 매뉴얼로 쓸 수 있는 것, 데이터로 표현할 수 있는 것, 규칙으로 정리할 수 있는 일들입니다.

**Treatment:** Merge the three parallel items into flowing prose. Vary sentence structure instead of repeating the same "~할 수 있는 것" pattern three times.

**After:**
> 매뉴얼로 남기거나 데이터로 표현하거나 규칙으로 정리할 수 있는 일들입니다.

---

## Pattern 5. AI High-Frequency Expressions — Essay Treatment

**Essay convention note:** In essay/blog style, formulaic intro/conclusion frames ("~에 대해 살펴보고자 한다", "~임을 알 수 있다") should be removed entirely — enter content directly. For the conclusion's closing stance, apply Pattern 9 voice consultation.

**Essay-specific treatment:** Scan the **entire text** first. Identify expressions that appear **2 or more times** — these are the primary replacement targets. A single occurrence of 다양한/중요한/효과적인 is acceptable; recurring repetition is the signal to act. For universal substitution/deletion strategies, see patterns-kr.md §3.

**Before (높임말 — 해요체):**
> 특히 인공지능은 다양한 분야에서 중요한 역할을 하고 있고요, 교육 현장에서도 효과적으로 활용되고 있어요. 뿐만 아니라, 이를 통해 학생들에게 긍정적인 영향을 주고 있고요, 결과적으로 학습 성과도 지속적으로 좋아지고 있어요.

**After (해요체 유지):**
> 인공지능은 교실 안팎에서 학생 개개인의 학습 속도를 세심하게 살피는 조력자가 되었어요. 학생의 취약한 문제를 실시간으로 분석해서 맞춤형 복습 과제를 제시해 주기도 하고요. 이렇게 학생 개개인에게 맞춘 피드백 덕분에 아이들이 배움을 포기하지 않고 실력을 차근차근 쌓아 올릴 수 있게 돼요.

---

**Essay-specific rhetorical filler treatment:**

Emotive adjectives (흥미로운, 묘한), expansion phrases (~에 그치지 않고, ~을 넘어서), and elevated vocabulary (체득하다, 통찰력) cluster together — a strong AI rhetorical filler signal. In essays, replace with concrete descriptions of what the author actually experienced and felt. See patterns-kr.md §3 for universal density rules and definitions.

**Before:**
> 이 경험은 단순히 기술을 익히는 데 그치지 않고, 협업이라는 묘한 역학 관계를 체득하는 계기가 되었다. 흥미로운 점은 서로 다른 배경을 가진 사람들이 모이면 예상을 넘어서는 결과가 나온다는 것이다. 이런 통찰력은 혼자서는 결코 얻을 수 없다.

**After:**
> 이 경험에서 기술보다 오래 남은 건 협업의 경험 그 자체였다. 배경이 다른 사람들이 모이니 혼자였으면 생각조차 못했을 아이디어가 튀어나왔다. 그건 책에서 읽어서 아는 것과는 다른 종류의 앎이었다.

---

## Pattern 6. Conjunction Overuse — Essay Treatment

**Essay-specific rule:** MUST NOT merge two originally separate sentences using clause connectors that generate new commas (-ㄴ데,/-지만,/-으나,). When removing a sentence-initial conjunction (하지만, 그래서, 그런데 등), keep the sentences separate — delete only the conjunction. For universal conjunction treatment rules, see patterns-kr.md §3.

---

## Pattern 7. Bound Noun Spacing (의존명사 띄어쓰기) — Essay Only

**Acceptable merged forms in essay:**

| LLM standard form | Essay natural form |
| --- | --- |
| ~는 것이다 | ~는거다 |
| ~할 때 | ~할때 |
| ~는 것 같다 | ~는것 같다 |
| ~ㄹ 뿐이다 | ~ㄹ뿐이다 |

**Treatment:** MUST NOT enforce standard spacing. Choose whichever form sounds natural in context.

**Before:**
> 결국 그가 말하고 싶었던 것은 자유라는 것이다. 그럴 때 사람은 비로소 솔직해진다.

**After:**
> 결국 그가 말하고 싶었던 것은 자유라는거다. 그럴때 사람은 비로소 솔직해진다.

---

## Pattern 8. Auxiliary Verb Spacing (보조용언 띄어쓰기) — Essay Only

Allow merged forms wherever they feel natural. MUST NOT normalize back to standard spacing.

**Before:**
> 그는 오랫동안 그 일을 해 왔다. 문제가 저절로 이루어 지는 일은 없다.

**After:**
> 그는 오랫동안 그 일을 해왔다. 문제가 저절로 이루어지는 일은 없다.

---

## Pattern 9. Absence of Voice / Personality — Essay Only

**Treatment — interactive voice consultation (3-step process):**

AI must NOT inject arbitrary opinions. Instead, follow this 3-step process:

### Step A — Scan and identify voice injection candidates

Read the entire text and find 2–4 specific sentences or passages where the author's personal viewpoint, reaction, or stance would naturally strengthen the writing. Mark each candidate with a brief label (e.g., [V1], [V2]).

Criteria for a good candidate:

- A claim the author could personally agree or disagree with
- A fact or finding that warrants an emotional or evaluative reaction
- A turning point in the argument where the author's commitment matters

### Step B — Present options to the author

For each candidate, present **3–5 possible viewpoints** the author could adopt. Options must:

- Cover a range of stances (supportive, skeptical, ambivalent, personal anecdote, forward-looking)
- Be phrased in the detected speech level of the original text
- Be brief enough for the author to scan quickly

Format:
> **[V1]** 원문 문장 발췌
> → 이 부분에 작가님만의 관점을 담을 수 있습니다. 어떤 방향이 가장 가깝나요?
>
> 1. (동의/긍정) 예시 문장
> 2. (회의/비판) 예시 문장
> 3. (개인 경험 연결) 예시 문장
> 4. (열린 물음 제기) 예시 문장
> 5. (직접 의견 입력) 원하시는 관점을 직접 말씀해 주세요.

### Step C — Apply the chosen direction

- If the author selects one of the numbered options → weave that viewpoint into the sentence naturally, matching the surrounding tone and speech level.
- If the author provides their own opinion → apply it directly, adjusting only for natural flow (no AI rewording that dilutes the author's words).
- If the author skips this step → leave the passage unchanged; do not inject any voice unilaterally.

---

## Pattern 10. Communication Artifacts — Essay Treatment

Remove all (greetings, emojis, bold headers, bullet-only content → prose). No essay-specific exceptions. See patterns-kr.md P10 for universal rules.

---

## Pattern 11. Inanimate Subject Personification — Essay Treatment

Rewrite so that the inanimate noun becomes an adverbial or instrumental phrase, and a human subject or natural process takes the agent role. For universal detection criteria and Before/After examples, see patterns-kr.md §8 P11.

**Speech level examples (essay-specific):**

**Before (높임말 — 해요체):**
> 이 분석에서 문제를 직접 짚었어요. 데이터가 우리에게 답을 알려줘요.

**After (해요체 유지):**
> 분석 결과를 보면 이 문제가 바로 드러나요. 데이터를 살펴보면 답을 찾을 수 있어요.

---

## Pattern 12. Unnecessary Passive / Relative Clause Overuse — Essay Treatment

Convert passive constructions (되다/어지다) to active voice. Replace passive modifiers with direct verb phrases. For universal detection criteria, exclusions, and Before/After examples, see patterns-kr.md §8 P12.

**Speech level examples (essay-specific):**

**Before (높임말 — 하십시오체):**
> 최근 발표된 연구에서 제안된 방법론이 적용되었습니다.

**After (하십시오체 유지):**
> 최근 발표한 연구에서 제안한 방법론을 적용했습니다.

---

## Pattern 13. Empty Subject & '~는 것이다' Construction — Essay Treatment

Remove the dummy frame ('이유가 있다', '필요가 있다', '~는 것이다'). State the content directly without the empty subject construction. For universal detection criteria and Before/After examples, see patterns-kr.md §8 P13.

**Speech level examples (essay-specific):**

**Before (높임말 — 해요체):**
> 이게 중요한 이유가 있어요. 다시 생각해 볼 필요가 있어요.

**After (해요체 유지):**
> 이게 왜 중요한지 살펴볼게요. 다시 한번 생각해 봐야 해요.

---

## Pattern 14. Causative '만들다' Direct Translation — Essay Treatment

Replace ~하게 만들다 with state-change expressions (~해지다), adverbs, or indirect cause-effect descriptions. For universal detection criteria and Before/After examples, see patterns-kr.md §8 P14.

**Speech level examples (essay-specific):**

**Before (높임말 — 하십시오체):**
> 이 도구는 작업을 효율적으로 만들어 줍니다.

**After (하십시오체 유지):**
> 이 도구를 쓰면 작업이 훨씬 효율적으로 바뀝니다.

---

## Example 1: Essay Style (Full Worked Example)

**Before (AI-generated):**
> 인공지능 기술은, 현대 사회에서 매우 중요한 역할을 하는 혁신적인 기술로, 다양한 분야에서 효과적으로 활용되고 있습니다. 뿐만 아니라, 이를 통해 우리는 더욱 효율적인 사회를 만들어 나갈 수 있습니다. 따라서, 인공지능의 지속적인 발전이 필요하다고 할 수 있습니다. 첫째, 의료 분야에서의 활용, 둘째, 교육 분야에서의 적용, 셋째, 산업 자동화 분야에서의 기여가 대표적입니다. 이처럼 인공지능은 중요한 역할을 한다는 것을 알 수 있습니다.

**Detected patterns:**

- Pattern 1: Comma overuse (2+ per sentence)
- Pattern 5: AI stock expressions (뿐만 아니라, 따라서, 이처럼, 다양한, 효과적으로, 중요한)
- Pattern 3 Rule of Three: 첫째, 둘째, 셋째
- Pattern 5: Formulaic conclusion with hollow content (중요한 역할을 한다는 것을 알 수 있습니다)
- Pattern 6: Consecutive conjunctions (뿐만 아니라 → 따라서 → 이처럼)
- Speech level detected: **하십시오체** (~합니다 / ~입니다) → must be preserved throughout

### First Draft

> 인공지능은 현대 사회의 핵심 동력으로서 여러 산업 현장에 깊숙이 자리 잡았습니다. 이는 사회 전반의 생산성을 높이고 새로운 가치를 창출하는 기반이 되기에, 관련 기술의 지속적인 고도화가 요구됩니다. 구체적으로는 정밀한 진단을 돕는 의료 서비스와 개인별 맞춤형 교육, 그리고 지능형 산업 자동화가 그 혁신의 흐름을 주도하고 있습니다. 이렇듯 인공지능은 우리 삶의 질을 한 단계 높이는 결정적인 역할을 수행합니다.

---

**[목소리 협의 — 에세이 전용]**

아래 부분에 작가님만의 관점을 담을 수 있습니다. 원하시는 방향을 선택하거나, 직접 의견을 말씀해 주세요.

**[V1]** 이렇듯 인공지능은 우리 삶의 질을 한 단계 높이는 결정적인 역할을 수행합니다.
→ 이 부분에 작가님만의 관점을 담을 수 있습니다. 어떤 방향이 가장 가깝나요?

1. (동의/긍정) 인공지능은 이미 우리 삶의 일부가 되었습니다. 기술의 진보가 인간의 가능성을 확장한다는 것을 이제는 몸소 실감하게 됩니다.
2. (회의/비판) 기술이 삶을 편리하게 만드는 건 사실이지만, 그 혜택이 모두에게 고르게 닿고 있는지는 솔직히 확신하기 어렵습니다.
3. (개인 경험 연결) 직접 써보니 생각보다 훨씬 실용적이었습니다. 막연한 기대가 구체적인 경험으로 바뀌는 순간이었습니다.
4. (열린 물음 제기) 기술이 삶의 질을 높이려면, 기술 그 자체보다 그것을 어떻게 쓸지에 대한 사회적 합의가 먼저 아닐까요?
5. (직접 의견 입력) 원하시는 관점을 직접 말씀해 주세요.

---

### Remaining AI Traces

- 의료, 교육, 자동화 three-item list still echoes rule-of-three
- "지속적인 고도화가 요구됩니다" — vague necessity claim with no specific agent or scope

### Final Version (Author's choice: Option 2 — skeptical/critical)

> 인공지능은 현대 사회의 핵심 동력으로서 여러 산업 현장에 깊숙이 자리 잡았습니다. 의료·교육·산업 자동화에서 분명한 성과를 내고 있고, 기술 고도화도 빠른 속도로 진행 중입니다. 다만 그 혜택이 모두에게 고르게 닿고 있는지는 아직 확신하기 어렵습니다. 기술의 진보만큼이나 그 과실을 나누는 방식에 대한 사회적 논의가 함께 따라와야 할 때입니다.
