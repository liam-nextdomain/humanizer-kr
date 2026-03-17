# Korean LLM Pattern Reference Guide

**Source**: KatFishNet: Detecting LLM-Generated Korean Text through Linguistic Feature Analysis
Shinwoo Park et al., Yonsei University, 2024
GitHub: <https://github.com/Shinwoo-Park/katfishnet>

## Table of Contents

1. [KatFishNet Key Statistics](#1-katfishnet-key-statistics)
2. [Comma Removal/Retention Criteria](#2-comma-removalretention-criteria)
3. [AI-Repeated Verb/Adjective Diversification](#3-ai-repeated-verbadjective-diversification-park--kim-2025)
4. [High-Frequency Expression Substitution/Deletion Strategy](#4-high-frequency-expression-substitutiondeletion-strategy)
5. [Auxiliary Verb Attachment Allowlist (Essay Only)](#5-auxiliary-verb-attachment-allowlist-essay-only)
6. [AI Writing Audit Checklist](#6-ai-writing-audit-checklist)
7. [Template Structure — Cliché List](#7-template-structure--cliché-list)
8. [Park & Kim (2025) Research Statistics](#8-park--kim-2025-research-statistics)
9. [Korean Ending Diversification Reference](#9-korean-ending-diversification-reference)

---

## 1. KatFishNet Key Statistics

### Comma Usage Pattern Comparison — Essay Genre

| Metric | Human | LLM | Ratio |
| --- | --- | --- | --- |
| Sentence ratio with commas | 26.31% | 61.03% | ×2.3 |
| Comma-to-morpheme ratio | 1.13% | 2.56% | ×2.3 |
| Mean relative comma position | 0.09 | 0.18 | ×2 (LLM skews later) |
| Mean segment length | 4.35 | 8.56 | ×2 |
| POS diversity around commas | 24.38 | 59.39 | ×2.4 |

### Comma Usage Pattern Comparison — Abstract Genre

| Metric | Human | LLM |
| --- | --- | --- |
| Sentence ratio with commas | 47.48% | 65.21% |
| Mean segment length | 9.07 | 11.55 |
| POS diversity around commas | 42.85 | 61.95 |

### Spacing Pattern — Essay Genre

| Metric | Characteristics |
| --- | --- |
| LLM BN (dependent noun) spacing std dev | 0.02 (mechanical consistency) |
| Human | Frequent intentional omission for readability |
| LLM | Strictly follows NIKL standard rules |

### POS N-gram Diversity

| Item | Human | LLM |
| --- | --- | --- |
| POS combination diversity | High | Low |
| Ending/predicate usage ratio | High | Low |
| Noun/pronoun usage ratio | Low | High |
| Sentence structure | Varied | Repetitive patterns |

---

## 2. Comma Removal/Retention Criteria

### Comma patterns to remove (English-style — unnatural in Korean)

| Pattern | Before | After |
| --- | --- | --- |
| Before conjunctions | "중요하다, 그리고 필요하다" | "중요하고 필요하다" |
| Between subject and predicate | "인공지능은, 중요하다" | "인공지능은 중요하다" |
| After adverbials | "또한, 이를 통해" | "이를 통해" or remove |
| After long modifier clauses | "복잡한 상황에서, 우리는" | "복잡한 상황에서 우리는" |
| After causal clauses | "기후가 변하고 있어서, 대응이" | "기후가 변하고 있어서 대응이" |

### Comma patterns to retain

| Pattern | Example | Reason |
| --- | --- | --- |
| Parallel noun lists | "사과, 배, 포도" | Standard Korean list comma |
| Vocative marker | "홍길동, 앞으로" | Grammatical vocative |
| Before quotations (papers) | "다음과 같이 정의된다, '...'" | Academic convention |
| Coordinate clause separation (papers) | "A는 B이고, C는 D이다" | Clarifies long parallel clauses |

---

## 3. AI-Repeated Verb/Adjective Diversification (Park & Kim, 2025)

AI tends to repeat specific verbs and adjectives. When the same expression appears 3+ times, use the alternatives below.

| AI repeated verb | Alternatives |
| --- | --- |
| 활용하다 | 쓰다, 도입하다, 적용하다, 끌어오다, 접목하다 |
| 기여하다 | 이바지하다, 뒷받침하다, 힘을 보태다, 보탬이 되다 |
| 미치다 (영향을) | 작용하다, 좌우하다, 끼치다, 파급되다 |
| 제공하다 | 내놓다, 건네다, 마련하다, 내어주다 |
| 향상시키다 | 높이다, 끌어올리다, 개선하다, 나아지게 하다 |

| AI repeated adjective | Alternatives |
| --- | --- |
| 다양한 | 여러, 갖가지, 폭넓은, 다채로운 |
| 중요한 | 핵심적인, 결정적인, 빼놓을 수 없는, 무게 있는 |
| 효과적인 | 실질적인, 유용한, 알찬, 성과를 내는 |
| 긍정적인 | 바람직한, 고무적인, 희망적인 |
| 부정적인 | 우려스러운, 해로운, 좋지 않은 |

---

## 4. High-Frequency Expression Substitution/Deletion Strategy

### Conjunction overuse by type — AI summary (Park & Kim, 2025)

| Type | AI-overused expressions | Notes |
| --- | --- | --- |
| Example/emphasis | 예를 들어, 특히, 예컨대, 다시 말해, 사실은 | Strongest AI signal — appears far more frequently in AI text |
| Additive | 또한, 그리고, 나아가, 동시에, 뿐만 아니라 | Common in both, but AI uses 또한 and 나아가 more |
| Contrastive | 하지만, 그러나, 오히려 | Similar frequency in both |
| Causal | 따라서, 때문에, 그 결과, 이로 인해 | AI uses slightly more |
| Summary | 즉, 이처럼, 결과적으로, 그러므로 | |
| Conditional | 한다면, ~라면 | **Human marker** — nearly absent in AI text |

> **Treatment rule:** When example/emphasis conjunctions (예를 들어, 특히, 예컨대, 다시 말해) appear 3+ times in a passage, replace some with direct case descriptions, conditional framing (한다면/~라면), or remove entirely.

### Conjunction treatment (deletion-first principle)

| Type | Conjunction | Treatment | Example |
| --- | --- | --- | --- |
| Additive | 또한 | Delete if flow is natural | "또한 중요하다" → "중요하다" |
| Additive | 뿐만 아니라 | Delete and merge sentences | "A다. 뿐만 아니라 B다" → "A이고 B다" |
| Additive | 이를 통해 | Delete or use direct verb | "이를 통해 개선된다" → "개선된다" |
| Additive | 더불어 | Delete | → delete and connect sentences |
| Additive | 나아가 | Delete or start new sentence | → mostly delete |
| Causal | 따라서 | Delete if causality is clear | "중요하다. 따라서 필요하다" → "중요하므로 필요하다" |
| Contrastive | 그러나 | Delete if contrast is weak | → retain only when contrast is strong |
| Contrastive | 하지만 | Delete if contrast is weak | → same as 그러나 |
| Summary | 이처럼 | Almost always delete | → "이처럼 중요하다" → "중요하다" |
| Summary | 결과적으로 | Delete and state directly | → mostly delete |
| Causal | 그러므로 | Same as 따라서 | |

### Example/emphasis conjunction treatment (strongest AI overuse type — Park & Kim, 2025)

The most prominent overuse type in AI text. Intervene actively when 3+ occurrences appear within the same passage.

| Conjunction | Treatment | Example |
| --- | --- | --- |
| 예를 들어 | Replace some with direct case descriptions when frequency is high | "예를 들어 A가 있다" → "A의 경우를 보면" or delete and present case directly |
| 특히 | Specify what is special, or delete | "특히 중요하다" → state why it is important directly |
| 예컨대 | Delete one when used interchangeably with 예를 들어 | Keep only one if both appear |
| 다시 말해 | Delete if the preceding sentence is already clear | Rewrite preceding sentence more clearly to remove repetition |
| 사실은 | Delete if emphasis intent is weak | "사실은 A다" → "A다" |

> **Conditional conjunction tip**: Inserting conditionals nearly absent in AI text (한다면, ~라면, 만약) reveals a human thinking pattern. e.g., "예를 들어 A가 발생한다" → "A가 발생한다면"

**Consecutive conjunction rule**: If 3+ sentences in a row start with conjunctions, MUST delete at least 1.

### Anti-pattern for conjunction removal: merging clauses with connective endings

When removing sentence-initial conjunctions, merging two sentences with `-ㄴ데,` creates a new comma, violating P1 (comma overuse).

| | Example | Problem |
| --- | --- | --- |
| ❌ Wrong | Before: '**하지만** 파서만으로 디지털화하기 어려운 자료가 상당수입니다. 그런 자료는 사람 손을 탈 수밖에 없습니다.' After: '파서만으로 디지털화하기 어려운 자료가 상당수**인데,** 그런 자료는 사람 손을 탈 수밖에 없습니다.' | Merging with '-인데,' to remove '하지만' → new comma = P1 violation |
| ✅ Correct | After: '파서만으로 디지털화하기 어려운 자료가 상당수입니다. 그런 자료는 사람 손을 탈 수밖에 없습니다.' | Delete only the initial '하지만', keep sentences separate |

### Intensifier treatment (replace with concrete facts)

| Intensifier | Treatment |
| --- | --- |
| 매우 중요하다 | Replace with specific reason: "이 단계를 건너뛰면 X가 작동하지 않는다" |
| 특히 | Specify what is special, or delete |
| 상당히 | Replace with numbers or specific expression |
| 크게 향상되었다 | Specify: "X% 향상", "두 배 빨라졌다" |
| 효과적으로 | State what it is effective for, or delete |
| 적극적으로 | Replace with concrete action |
| 지속적으로 | Specify frequency or duration, or delete |

### Stock modifier treatment

| Expression | Treatment |
| --- | --- |
| 다양한 측면에서 | Specify which aspects, or delete |
| 중요한 역할을 한다 | State the role directly |
| 긍정적인 영향을 미친다 | State specifically what impact |
| 부정적인 영향을 미친다 | Same as above |
| 효과적으로 활용 | State how it is used directly |

---

## 5. Auxiliary Verb Attachment Allowlist (Essay Only)

In essays, human writers often attach auxiliary verbs for readability. **In papers/reports, MUST maintain standard spacing. MUST NOT apply attached forms.**

| Standard form (LLM usage) | Allowed attached form (essay) |
| --- | --- |
| 되어 있다 | 되어있다 |
| 해 주다 | 해주다 |
| 해 왔다 | 해왔다 |
| 해 오다 | 해오다 |
| 알아 보다 | 알아보다 |
| 들어 가다 | 들어가다 |
| 나가 있다 | 나가있다 |
| 올라 가다 | 올라가다 |
| 내려 가다 | 내려가다 |
| 이루어 지다 | 이루어지다 |
| 만들어 지다 | 만들어지다 |
| 나타나 있다 | 나타나있다 |

### Dependent noun adjacent expression treatment (essay)

| LLM standard form | Essay natural form | Notes |
| --- | --- | --- |
| ~는 것이다 | ~는거다 / ~는 거다 | Colloquial allowed |
| ~할 때 | ~할때 | Attached form allowed |
| ~는 것 같다 | ~는것 같다 | Intermediate form allowed |
| ~할 수 있다 | Keep as-is | "수" separation is semantically important |

---

## 6. AI Writing Audit Checklist

### Essay/blog audit items (check after rewriting)

- [ ] Comma-containing sentences ≤ 30% of total?
- [ ] No 3+ consecutive sentences starting with "뿐만 아니라", "또한", "따라서", "이처럼"?
- [ ] "중요한 역할", "다양한 측면", "효과적으로 활용" removed?
- [ ] No "~에 대해 살펴보겠다", "~을 알아보고자 한다" in the introduction?
- [ ] No "~이 중요하다는 것을 알 수 있다", "~해야 할 것이다" in the conclusion?
- [ ] Writer's voice or reaction appears at least once?
- [ ] Original speech level (formal/informal) preserved after rewriting?
- [ ] Sentence length varies between short and long sentences?
- [ ] Greetings, emojis, and bold-text headers removed?
- [ ] Stacked noun phrases (~의 ~의 ~) converted to verb clauses?
- [ ] Bullet-list sentences (short enumeration, numbered sub-points) converted to prose?
- [ ] Same verb/adjective not repeated 3+ times?
- [ ] Example/emphasis conjunctions (예를 들어, 특히, 예컨대) not excessive?

### Paper/report audit items (check after rewriting)

- [ ] Non-list commas significantly reduced?
- [ ] "다양한", "효과적인", "중요한" not repeated without content?
- [ ] Technical terms used consistently (no synonym mixing)?
- [ ] Introduction does not start with "~에 대해 고찰하고자 한다"?
- [ ] Conclusion does not end only with "~이 중요함을 알 수 있다"?
- [ ] Standard spacing maintained?
- [ ] Objective tone maintained throughout?
- [ ] Greetings and emojis removed?
- [ ] Bullet-list structure limited to paper-appropriate level?
- [ ] Excessive repetition of the same expressions resolved?

---

## 7. Template Structure — Cliché List

### Introduction clichés (to remove)

- "~에 대해 살펴보겠다"
- "~을 알아보고자 한다"
- "~에 대해 논의해 보겠다"
- "~이 무엇인지 탐구해 보겠다"
- "이 글에서는 ~을 다루겠다"
- "~에 대한 이해를 높이고자 한다"

### Conclusion clichés (to remove)

- "~이 중요하다는 것을 알 수 있다"
- "~해야 할 것이다"
- "앞으로도 ~에 관심을 가져야 한다"
- "~이 필요하다고 할 수 있다"
- "이처럼 ~은 중요한 의미를 가진다"
- "~가 더욱 중요해질 것으로 전망된다"
- "긍정적인 변화를 이끌어 낼 수 있을 것이다"

### Challenge/outlook clichés (remove or specify)

- "물론 과제도 있다"
- "앞으로의 과제와 가능성"
- "한계와 발전 방향"
- "미래에는 더욱 발전할 것으로 기대된다"

---

## 8. Park & Kim (2025) Research Statistics

**Source**: 박종향·김은영, "생성형 AI 텍스트와 인간 텍스트의 내용 및 문체 비교 연구", 2025
D대학교 교양과목 과제물 69편(인간 20편, AI 활용 49편) 비교 분석

### Sentence length comparison

| Metric | Human (2021) | AI-assisted (2025) | Statistics |
| --- | --- | --- | --- |
| Mean sentences per document | 82.06 | 114.85 | |
| Mean characters per sentence | 54.20 | 48.69 | t=4.874, p<.001 |

> AI-assisted texts segment sentences more frequently: more sentences overall, but shorter individual sentences.

### Lexical diversity by POS (TTR / MATTR)

| POS | Human TTR | AI TTR | Human MATTR | AI MATTR | TTR t-test |
| --- | --- | --- | --- | --- | --- |
| Noun | 0.398 | 0.351 | 0.701 | 0.720 | 3.39** |
| Verb | 0.545 | 0.461 | 0.656 | 0.576 | 5.74*** |
| Adjective | 0.525 | 0.429 | 0.558 | 0.483 | 4.56*** |
| Adverb | 0.602 | 0.468 | 0.602 | 0.468 | 3.53*** |
| All content words | 0.518 | 0.427 | 0.629 | 0.562 | 6.20*** |

*p<0.05, **p<0.01, ***p<0.001

> Humans use significantly more diverse vocabulary than AI in verbs, adjectives, and adverbs. Nouns differ in TTR but not significantly in MATTR.

### Top conjunction expressions by type

| Type | Human (2021) top expressions | AI-assisted (2025) top expressions |
| --- | --- | --- |
| Additive | 또한(61), 그리고(54), 나아가(22), 동시에(13) | 그리고(157), 또한(19), 동시에(71), 나아가(70) |
| Contrastive | 하지만(55), 그러나(23), 한편(9) | 하지만(96), 그러나(73), 오히려(12) |
| Causal | 따라서(26), 때문에(22), 그 결과(5) | 따라서(78), 때문에(57), 그 결과(18), 이로 인해(16) |
| Conditional | 한다면(9), 라면(6) | — (not in top) |
| Temporal/sequential | 결국(21), 먼저(17) | 결국(58), 먼저(23) |
| Example/emphasis | 즉(48), 특히(14), 예를 들어(11) | 특히(147), 예를 들어(131), 즉(99), 예컨대(21), 다시 말해(17) |
| Alternative | 혹은(15), 또는(14) | 혹은(25), 또는(231) |

> Biggest difference: AI uses example/emphasis type (특히, 예를 들어) overwhelmingly more. Humans use conditionals (한다면, ~라면) but they are nearly absent in AI.

### Bullet-list tendency (qualitative analysis)

- AI-assisted texts: significantly higher proportion of short enumeration/summary statements (bullet-list style) instead of prose
- Heading fragmentation pattern: Ⅰ → 1 → 1) → (1) → ① multi-level structure
- Human texts: majority develop arguments in continuous prose
- AI-assisted texts: majority follow a uniform format of dividing and summarizing sub-topics

---

## 9. Korean Ending Diversification Reference

LLM repeats specific ending patterns. When rewriting, diversify endings to increase POS diversity.

### LLM overused endings

| LLM preferred ending | Natural alternatives |
| --- | --- |
| ~하며 (concurrent parallel) | ~하고, ~해서, ~하는데 |
| ~하여 (cause/means) | ~해서, ~했더니, ~하니까 |
| ~하고 있다 (progressive) | ~하는 중이다, ~하는 상황이다, ~하는 중 |
| ~할 수 있다 (potential) | ~된다, ~하게 된다, ~가능하다 |
| ~해야 한다 (obligation) | ~해야 하는 상황이다, ~안 할 수가 없다 |
| ~됨으로써 | ~되어서, ~되면서 |
| ~함으로써 | ~해서, ~하면서 |
| ~에 따라 | ~에 맞게, ~을 보면, ~이니까 |
