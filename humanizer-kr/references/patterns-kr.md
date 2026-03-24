# Korean LLM Pattern Reference Guide

> **Quick navigation:** [Pattern Index](#23-korean-ai-patterns--index) · [Style Rules](#style-rules-at-a-glance) · [Data & Reference Tables](#table-of-contents--data--reference-tables)

## 23 Korean AI Patterns — Index

### [A] Punctuation

- **P1 Comma Overuse** — comma inclusion rate >40% as attention flag (context-dependent, not an absolute threshold); strongest AI identifier
- **P2 Noun-Heavy / Low Vocab Diversity** — ~의 chains, same verb/adj 3+ times (AI verb TTR 0.461 vs. human 0.545) *(for English-style syntactic translation, see [F] P11–P14)*

### [B] Structure / Word-Order

- **P3 Rule of Three & Bullet-Point Enumeration** — rigid 첫째/둘째/셋째, excessive outline depth (개조식), three-item comma-separated clausal lists
- **P4 Formulaic Template** — 서론 ~에 대해 살펴보겠다 / 결론 ~해야 할 것이다

### [C] Vocabulary / Expression

- **P5 AI High-Frequency Expressions** — 특히/예를 들어 clustering, 다양한/중요한/효과적인 repetition *(for structural translation issues, see [F] P11–P14)*
- **P6 Conjunction Overuse** — 3+ consecutive sentences starting with conjunctions

### [D] Word Spacing — Essay Only

- **P7 Bound Noun Spacing** — mechanical consistency vs. human intentional merging
- **P8 Auxiliary Verb Spacing** — LLM always separates; humans merge

### [E] Communication

- **P9 Absence of Voice** — essay only; neutral statements without author personality
- **P10 Communication Artifacts** — greetings, AI handover language, emoji, bold headers → remove all

### [F] English Direct Translation (영어 직역투)

- **P11 Inanimate Subject Personification** — English S+V+O structure where inanimate nouns act as agents (연구가 보여준다, 분석이 짚었다); Korean naturally uses human subjects or adverbial constructions
- **P12 Unnecessary Passive / Relative Clause Overuse** — English passive (P.P.) translated as 되다/어지다 (학습된, 선택되는, 공유된); Korean reads better in active voice
- **P13 Empty Subject & '~는 것이다' Construction** — 'It is ~ that' / 'There is a reason ~' / 'There is a need to ~' structures making sentences unnecessarily long and unfocused
- **P14 Causative '만들다' Direct Translation** — 'Make + O + C' translated as ~하게 만들다; Korean uses state-change expressions or adverbs

### [G] English-Origin Rhetorical Patterns (영어 기원 수사 패턴)

**Tier 1 — Always fix:**

- **P15 Pedagogical Framing** — "함께 살펴보겠습니다", "여기서 핵심이 있습니다"; teacher/suspense voice that no Korean human writer uses
- **P16 Structural Padding** — fractal summaries (every subsection has intro/body/summary), one-point dilution, content duplication
- **P17 Copula Avoidance** — "~이다" replaced with "~로서 기능한다", "~의 역할을 한다"; repetition penalty artifact
- **P18 Negative Parallelism** — "A가 아니라 B이다" false profundity; 1× = Tier 3 (허용), 2× = fix, 3+× = aggressive fix
- **P19 Invented Concept Labels** — "~의 역설", "~의 함정" without argumentation; 1× = Tier 3, 2× = Tier 3 (if different labels), 3+ distinct labels in same text = Tier 2

**Tier 2 — Fix based on density:**

- **P20 Rhetorical Self-Q&A** — "X란 무엇인가? 바로 Y이다" self-questioning; 1× = Tier 3, 2+× = fix
- **P21 Overloaded Modifiers** — magic adverbs ("근본적으로", "깊이"), grandiose nouns ("생태계", "패러다임"); 3+× same class = fix
- **P22 Repetitive Rhetoric** — anaphora (동일 시작 3연속), dead metaphor (same metaphor 5+×), historical analogy stacking (3+× rapid-fire)
- **P23 False Authority & Inflation** — vague attributions ("전문가들은" without source), stakes inflation, false vulnerability, false ranges ("X부터 Y까지" without real spectrum)

---

## Style Rules at a Glance

| Pattern | Essay / Blog | Academic / Report |
| --- | --- | --- |
| Comma overuse | Aggressively remove; split sentences | Remove English-style commas only |
| Noun-heavy structure & vocab repetition | Convert to verb clauses; diversify repeated verbs/adjectives | Dissolve stacked nominalization; vary repeated terms |
| AI stock expressions | Delete or replace with specifics | Delete or substitute precisely |
| Rule of three & bullet-point style | Break up; convert 개조식 to prose | Keep if genuinely needed; limit outline depth |
| Formulaic template | Remove boilerplate; enter content directly | Keep structure; remove hollow boilerplate |
| Conjunction overuse | Aggressively delete | Remove only excessive ones |
| Bound noun spacing | Merged forms allowed | Standard spacing required |
| Auxiliary verb spacing | Merged forms allowed | Standard spacing required |
| Absence of voice | Scan candidates → propose 3–5 options per site → apply author's chosen direction | Not applied; maintain objectivity |
| **Speech level** | **MUST preserve — MUST NOT change** | Not applicable |
| Communication artifacts | Remove entirely | Remove entirely |
| Inanimate subject personification | Rewrite with human subject or adverbial construction | Same — restructure with appropriate agent or adverbial |
| Unnecessary passive / relative clause | Convert to active voice; simplify relative clauses | Convert to active voice where clarity improves |
| Empty subject & ~는 것이다 | Remove dummy subject; state directly | Remove dummy subject; state directly |
| Causative 만들다 direct translation | Replace with state-change expression or adverb | Replace with state-change expression or adverb |
| Pedagogical framing (T1) | Remove entirely; enter content directly | Remove entirely |
| Structural padding (T1) | Remove repeated summaries; consolidate to single statement | Remove repeated summaries; consolidate |
| Copula avoidance (T1) | Replace with "~이다"; remove ornamental verbs | Replace with "~이다"; remove ornamental verbs |
| Negative parallelism (T1 at 2+) | Merge into single narrative sentence; "~을 넘어" | Same — merge into declarative |
| Invented concept labels (T1 at 2+) | Keep max 1; remove labels without argumentation | Keep max 1; remove labels without argumentation |
| Rhetorical self-Q&A (T2) | Replace with transition or perspective statement | Replace with transition or perspective statement |
| Overloaded modifiers (T2) | Delete or replace with concrete facts | Delete or replace with concrete facts |
| Repetitive rhetoric (T2) | Break repetition; vary structure | Break repetition; vary structure |
| False authority & inflation (T2) | Specify sources; reduce stakes to match topic | Specify sources; reduce stakes to match topic |

---

## Table of Contents — Data & Reference Tables

1. [Comma Removal/Retention Criteria](#1-comma-removalretention-criteria)
2. [AI-Repeated Verb/Adjective Diversification](#2-ai-repeated-verbadjective-diversification-park--kim-2025)
3. [High-Frequency Expression Substitution/Deletion Strategy](#3-high-frequency-expression-substitutiondeletion-strategy)
4. [Auxiliary Verb Attachment Allowlist (Essay Only)](#4-auxiliary-verb-attachment-allowlist-essay-only)
5. [AI Writing Audit Checklist](#5-ai-writing-audit-checklist)
6. [Template Structure — Cliché List](#6-template-structure--cliché-list)
7. [Korean Ending Diversification Reference](#7-korean-ending-diversification-reference)
8. [English Direct Translation Detection Criteria](#8-english-direct-translation-detection-criteria)
9. [English-Origin Rhetorical Patterns](#9-english-origin-rhetorical-patterns)

---

## 1. Comma Removal/Retention Criteria

### Comma patterns to remove (English-style — unnatural in Korean)

| Pattern | Before | After |
| --- | --- | --- |
| Before conjunctions | "중요하다, 그리고 필요하다" | "중요하다 그리고 필요하다" (comma only) / "중요하고 필요하다" (if also applying P6) |
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

## 2. AI-Repeated Verb/Adjective Diversification (Park & Kim, 2025)

> **Selection rule:** Choose alternatives that match the original author's vocabulary register. If the original uses everyday language, prefer simpler alternatives (쓰다, 높이다); if academic, prefer formal alternatives (도입하다, 제고하다). Do NOT default to the first item in the list.

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

## 3. High-Frequency Expression Substitution/Deletion Strategy

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

### Conjunction treatment (deletion-review-first principle)

> Delete only when removing the conjunction preserves both meaning and logical flow. Retain conjunctions that are essential for causal chains or argument progression.

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

**Consecutive conjunction rule**: If 3+ sentences in a row start with conjunctions, SHOULD delete at least 1. Exception: retain all if they form an essential causal or argumentative chain (e.g., "하지만... 그래서... 따라서...").

### Anti-pattern for conjunction removal: merging clauses with connective endings (Essay)

In essays, when removing sentence-initial conjunctions, merging two sentences with `-ㄴ데,` creates a new comma, violating P1 (comma overuse). In academic writing, coordinate clause commas are permitted per P1 retention criteria.

| | Example | Problem |
| --- | --- | --- |
| ❌ Wrong | Before: '**하지만** 파서만으로 디지털화하기 어려운 자료가 상당수입니다. 그런 자료는 사람 손을 탈 수밖에 없습니다.' After: '파서만으로 디지털화하기 어려운 자료가 상당수**인데,** 그런 자료는 사람 손을 탈 수밖에 없습니다.' | Merging with '-인데,' to remove '하지만' → new comma = P1 violation |
| ✅ Correct | After: '파서만으로 디지털화하기 어려운 자료가 상당수입니다. 그런 자료는 사람 손을 탈 수밖에 없습니다.' | Delete only the initial '하지만', keep sentences separate |

### Intensifier treatment (replace with concrete facts)

| Intensifier | Treatment |
| --- | --- |
| 매우 중요하다 | Replace with specific reason: "이 단계를 건너뛰면 X가 작동하지 않는다" |
| 특히 | (See conjunction treatment above) |
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

## 4. Auxiliary Verb Attachment Allowlist (Essay Only)

In essays, human writers often attach auxiliary verbs for readability. **In papers/reports, MUST maintain standard spacing. MUST NOT apply attached forms.**

> **Principle:** This list is representative, not exhaustive. The same attachment rule applies to any main-verb + auxiliary-verb combination that has solidified into a single semantic unit in natural Korean (e.g., 빠져나가다, 돌아오다, 넘어가다).

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

## 5. AI Writing Audit Checklist

### Common items (both styles)

- [ ] AI stock expressions ("중요한 역할", "다양한 측면", "효과적으로 활용") removed?
- [ ] Formulaic introduction/conclusion clichés removed?
- [ ] Greetings, emojis, and communication artifacts removed?
- [ ] Same verb/adjective not repeated 3+ times?
- [ ] No inanimate subjects performing human actions (P11)?
- [ ] Unnecessary 되다/어지다 passives converted to active voice (P12)?
- [ ] Empty subject / ~는 것이다 constructions removed (P13)?
- [ ] ~하게 만들다 causative replaced with state-change expression (P14)?
- [ ] No pedagogical framing (P15)?
- [ ] No fractal summaries at every subsection level (P16)?
- [ ] No copula avoidance — "~로서 기능한다" replaced with "~이다" (P17)?
- [ ] Negative parallelism ("A가 아니라 B") not repeated 2+ times (P18)?
- [ ] No invented concept labels appearing 2+ times without argumentation (P19)?
- [ ] Rhetorical self-Q&A not repeated 2+ times (P20)?
- [ ] No magic adverb / grandiose noun clusters (3+ same class) (P21)?
- [ ] No repetitive rhetoric — anaphora (3+), dead metaphor (5+×), analogy stacking (3+) (P22)?
- [ ] Vague attributions specified with concrete sources (P23)?

### Essay/blog additional items

- [ ] Comma-containing sentences ≤ 30% of total?
- [ ] No 3+ consecutive sentences starting with conjunctions?
- [ ] Example/emphasis conjunctions (예를 들어, 특히, 예컨대) not excessive?
- [ ] Writer's voice or reaction appears at least once?
- [ ] Original speech level (formal/informal) preserved after rewriting?
- [ ] Sentence length varies between short and long sentences?
- [ ] Stacked noun phrases (~의 ~의 ~) converted to verb clauses?
- [ ] Bullet-list sentences converted to prose?

### Paper/report additional items

- [ ] Non-list commas significantly reduced?
- [ ] Technical terms used consistently (no synonym mixing)?
- [ ] Standard spacing maintained?
- [ ] Objective tone maintained throughout?
- [ ] Bullet-list structure limited to paper-appropriate level?

---

## 6. Template Structure — Cliché List

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

## 7. Korean Ending Diversification Reference

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

---

## 8. English Direct Translation Detection Criteria

### Pattern Interaction — Priority Rules

1. **Recognize sentence structure before item-level scanning.** Identify the overall sentence structure (parallel lists, conditional chains, topic-comment pairs) before scanning individual phrases for pattern violations.
2. **P3 takes priority over P12 within list items.** When a sentence contains a three-item enumeration (P3), address the list structure first. Do not flag individual items within the list for P12 passive — the items may be valid active constructions (e.g., -ㄹ 수 있는) that are not passive at all.
3. **P12 exclusions override P12 detection.** Before flagging any construction as P12, check the exclusion list. -ㄹ 수 있다, -게 되다, and native passive suffixes are never P12.

---

### P11 — Inanimate Subject Personification (무생물 주어 의인화)

| English source pattern | AI direct translation | Natural Korean |
| --- | --- | --- |
| "Research shows this well." | "연구 하나가 이걸 잘 보여줍니다." | "연구 결과에서 그 차이가 뚜렷이 드러납니다." / "연구 결과에 이 점이 잘 나타나 있습니다." |
| "The analysis points out this issue." | "분석에서 이 문제를 직접 짚었습니다." | "분석 결과, 이 문제점이 드러났습니다." / "해당 분석은 이 문제를 직접 지적하고 있습니다." |
| "The environment creates thoughts." | "환경이 생각을 만든다." | "환경에 따라 생각이 바뀐다." / "사람의 생각은 환경의 영향을 받는다." |

> **Quick test:** If the subject is not a person (or group of people) but the verb describes a deliberate human action, flag as P11.

---

### P12 — Unnecessary Passive / Relative Clause Overuse (불필요한 수동형·관형사절 남용)

| English source pattern | AI direct translation | Natural Korean |
| --- | --- | --- |
| "Models trained on Western data" | "서양 중심으로 학습된 모델이" | "서양 중심으로 데이터를 익힌 모델이" / "서양 위주의 데이터를 학습한 모델이" |
| "Expressions that are selected" | "선택되는 표현" | "자주 쓰는 표현" / "선택하는 표현" |
| "Shared algorithm" | "공유된 알고리즘" | "함께 사용하는 알고리즘" / "범용적인 알고리즘" |

> **Quick test:** If 되다/어지다 can be replaced by an active verb without losing meaning, flag as P12.
>
> **Exclusions — do NOT flag as P12:**
>
> - **-ㄹ 수 있다 / -ㄹ 수 있는** (ability/potential): active voice expressing capability. e.g., "정리할 수 있는", "표현할 수 있는", "쓸 수 있는"
> - **-ㄹ 수 없다** (inability): same structure, negated
> - **-게 되다** (change of state / involuntary result): not a translation passive. e.g., "알게 되다", "가게 되다"
> - **Native Korean passives** (-이/-히/-리/-기 suffixes): e.g., "읽히다", "잠기다" — standard Korean morphology, not English calques
> - **Double passives** (보여지다, 쓰여지다, 잊혀지다): these ARE errors, but they are redundancy errors, not P12 English-translation passives. Correct by removing the redundant layer (보여지다→보이다), but do not categorize as P12.
>
> P12 targets ONLY: 되다/어지다 passives that are direct translations of English passive voice (be + p.p.), where an active Korean verb is more natural.

---

### P13 — Empty Subject & '~는 것이다' Construction (의미 없는 주어·가주어/보어 구문)

| English source pattern | AI direct translation | Natural Korean |
| --- | --- | --- |
| "There is a reason why this is tricky." | "이 현상이 까다로운 이유가 있습니다." | "이 현상은 다음과 같은 이유로 까다롭습니다." |
| "There is a need to ask." | "물어볼 필요가 있습니다." | "의문을 가져야 합니다." / "질문해 보아야 합니다." |
| "It was also a process of…" | "과정이기도 했습니다." | "과정이기도 합니다." / "씨름하며 배우는 단계였습니다." |

> **Quick test:** If the sentence contains ~이유가 있다, ~필요가 있다, ~것이다 as a frame without adding information, flag as P13.

---

### P14 — Causative '만들다' Direct Translation (사역동사 '만들다' 직역)

| English source pattern | AI direct translation | Natural Korean |
| --- | --- | --- |
| "Makes this point clearer." | "이 지점을 더 선명하게 만들어줍니다." | "이 지점이 덕분에 더 선명해집니다." / "연구 결과를 통해 이 지점이 더욱 뚜렷하게 드러납니다." |
| "Makes a way of thinking easy." | "어떤 사고방식을 쉽게 만들고" | "어떤 사고방식에 익숙해지게 하고" / "특정 방식으로 생각하게 유도하고" |

> **Quick test:** If ~하게 만들다 can be rewritten as ~해지다 or a direct verb without losing meaning, flag as P14. Note: P1 essay examples may contain "편리하게 만들고" — a P14 instance co-occurring with P1.

---

## 9. English-Origin Rhetorical Patterns

These patterns originate from English AI writing tropes but manifest in Korean AI text — either through direct translation habits or because Korean LLMs inherit rhetorical structures from English training data. Each pattern is individually tolerable in small doses; they become strong AI signals when multiple patterns co-occur or a single pattern repeats.

### Tier System

| Tier | Meaning | Action |
| --- | --- | --- |
| Tier 1 | Always AI — human writers virtually never produce this in Korean | Fix on first occurrence |
| Tier 2 | Density-dependent — acceptable once, AI signal when repeated | Fix when exceeding threshold |
| Tier 3 | Permissible — humans use this rhetorical device naturally | Leave alone; escalate to Tier 2 if repeated |

### Tier 3 → Tier 2 → Tier 1 Escalation Rules

| Pattern | 1× | 2× | 3+× |
| --- | --- | --- | --- |
| Negative parallelism "A가 아니라 B" | Tier 3 (허용) | Tier 2 (수정 권고) | Tier 1 (적극 수정) |
| "X도 아니고 Y도 아닌 Z" countdown | Tier 3 | Tier 2 | Tier 1 |
| Rhetorical self-Q&A "X란? Y이다" | Tier 3 | Tier 2 | Tier 2 |
| "상상해보세요" / "생각해보세요" | Tier 3 | Tier 2 | Tier 2 |
| "주목할 점은" transition filler | Tier 3 | Tier 2 | Tier 2 |
| Tricolon (rule of three) | Tier 3 | Tier 2 | Tier 1 |
| Single concept label ("~의 역설") | Tier 3 | Tier 3 (if different labels) | Tier 2 (3 distinct labels in same text) |
| Superficial analysis "~를 반영한다" | Tier 3 | Tier 2 | Tier 2 |

---

### Tier 1 Patterns — Always Fix

---

#### P15 — Pedagogical Framing (교수법적 프레이밍)

Combines pedagogical voice, false suspense, and teacher-mode defaults. The AI assumes a lecturer-student relationship regardless of audience.

**Subpatterns:**

- **Pedagogical voice:** "함께 살펴보겠습니다", "하나씩 풀어보겠습니다", "차근차근 알아보겠습니다"
- **False suspense:** "여기서 핵심이 있습니다", "흥미로운 지점이 나옵니다", "바로 이 부분이 중요합니다"
- **Teacher mode (repeated):** "~라고 생각해보세요", "비유하자면 ~입니다" — single use is Tier 3; repeated use escalates

| AI pattern | Before | After |
| --- | --- | --- |
| Pedagogical voice | "이제 이 개념을 함께 살펴보겠습니다." | (Delete — enter the content directly) |
| False suspense | "여기서 흥미로운 점이 있습니다. 사실은 비용이 더 중요했습니다." | "실제로는 비용이 더 중요했습니다." |
| Teacher mode | "이것을 자판기에 비유해보세요. 동전을 넣으면..." | "자판기처럼 입력이 들어가면 출력이 나오는 구조입니다." (if analogy is needed) / (Delete analogy if original concept is clearer) |

> **Quick test:** If removing the framing sentence loses zero information, flag as P15.

---

#### P16 — Structural Padding (구조적 패딩)

AI inflates word count through repetitive structural patterns rather than adding substance.

**Subpatterns:**

- **Fractal summaries:** Every subsection has its own introduction, body, and summary — "앞으로 말할 것, 지금 말하는 것, 방금 말한 것" applied at every level
- **One-point dilution:** A single argument restated through different metaphors, examples, and framings across hundreds of words to appear "comprehensive"
- **Content duplication:** Identical or near-identical paragraphs/sections reappearing in the same text — model losing track of what it already wrote
- **Fragment litany:** Assertion followed by subject-less noun-phrase fragments: "작은 버그를 잡는 것. 간단한 기능을 작성하는 것. 명확한 티켓을 구현하는 것." — the first sentence already said everything; fragments add only rhythm

| AI pattern | Before | After |
| --- | --- | --- |
| Fractal summary | "이 섹션에서는 비용 구조를 다루겠습니다. (본문) 이상으로 비용 구조를 살펴보았습니다." | (Delete intro/outro — keep only the substance) |
| One-point dilution | Same point in 5 paragraphs with different analogies | Consolidate to single strongest statement |
| Fragment litany | "개발자의 일상은 반복입니다. 코드를 읽는 것. 버그를 잡는 것. 회의에 참석하는 것." | "개발자의 일상은 코드 리뷰, 디버깅, 회의가 반복되는 구조입니다." |

> **Quick test:** If a section can be reduced by 50%+ without losing any argument or evidence, flag as P16.

---

#### P17 — Copula Avoidance (Copula 회피)

AI's repetition penalty pushes it away from simple "~이다" toward ornamental verbs that add no meaning.

| Before (AI) | After (natural) |
| --- | --- |
| "이것은 핵심 도구로서 기능한다" | "이것은 핵심 도구다" |
| "이 지표는 성과의 척도 역할을 한다" | "이 지표는 성과 척도다" |
| "이 사건은 전환점을 상징한다" | "이 사건은 전환점이다" / "이 사건이 전환점이었다" |
| "이 프레임워크는 기반을 제공한다" | "이 프레임워크가 기반이다" |

**Detection keywords:** ~로서 기능하다, ~의 역할을 하다, ~을 상징하다, ~을 대변하다, ~으로 자리 잡다, ~을 제공하다 (when a simple copula suffices)

> **Quick test:** If "~로서 기능하다/역할을 하다" can be replaced with "~이다" without losing meaning, flag as P17.

---

#### P18 — Negative Parallelism (부정 병렬 구문)

"It's not X — it's Y" structure creating false profundity. The strongest single-pattern AI identifier in rhetorical structure. 1× is Tier 3; 2× is Tier 2; 3+× is Tier 1.

**Variants:**

- **Basic:** "A가 아니라 B이다"
- **Extended:** "단순히 X만이 아닙니다. ... 이야기입니다"
- **Causal:** "A 때문이 아니라 B 때문이다"

| Before (AI) | After (natural) | Correction logic |
| --- | --- | --- |
| "착해서가 아니라 그게 더 쌌기 때문이죠." | "사실 조직이 형성된 동기는 선의보다는 경제적 비용 절감에 있었습니다." | "A가 아니라 B" contrast merged into single declarative sentence |
| "단순히 효율이 올라갔다는 이야기가 아닙니다. ... 이야기입니다." | "이는 단순한 효율 개선을 넘어, 이제는 '협력의 필수성' 자체를 원점에서 재검토할 수 있게 된 셈입니다." | "Not just X, but Y" replaced with "~을 넘어", "~인 셈이다" |

> **Quick test:** Count "아니라", "아닙니다", "않습니다... 것입니다" in the text. If 2+× carry the "not X — rather Y" reframe structure, flag as P18.

---

#### P19 — Invented Concept Labels (조어 라벨)

AI attaches abstract problem-nouns (역설, 함정, 딜레마, 격차, 진공, 역전) to domain words, creating analytical-sounding but unsubstantiated compound labels. One label with argumentation is valid analysis; multiple labels without argumentation is rhetorical shortcutting.

**Examples of AI-generated labels:**

- "감독의 역설", "가속화의 함정", "업무량 크리프", "자동화의 딜레마"
- The label names the phenomenon and skips the argument

| Before (AI) | After (natural) |
| --- | --- |
| "이것이 바로 '자동화의 역설'입니다. 또한 '효율성의 함정'도 존재합니다." | "자동화가 오히려 관리 부담을 늘리는 경우가 있습니다." (state the actual argument) |

> **Quick test:** If 2+ "~의 역설/함정/딜레마/격차" labels appear in the same text without each being individually argued, flag as P19.

---

### Tier 2 Patterns — Fix Based on Density

---

#### P20 — Rhetorical Self-Q&A (수사적 자문자답)

AI poses a question nobody asked, then immediately answers it — treating self-Q&A as the essence of elegant writing. 1× is Tier 3; 2+× is Tier 2.

| Before (AI) | After (natural) | Correction logic |
| --- | --- | --- |
| "시장이 이미 있는데 왜 굳이 회사를 만드는가? 코즈의 답은 간단했습니다." | "코즈는 시장이 존재하는 상황에서도 굳이 기업이라는 형태가 필요한 이유를 '계약 비용'에서 찾았습니다." | Self-Q&A replaced with contextual transition |
| "이 균열이 한국 사회에서는 어떤 의미일까요? (이후 설명)" | "이러한 기술적 균열은 한국 특유의 직장 문화와 만났을 때 더욱 복잡한 양상을 띱니다." | Question replaced with perspective statement |

> **Quick test:** If the question can be deleted and the answer still makes sense as a standalone sentence, flag as P20.

---

#### P21 — Overloaded Modifiers (과잉 수식)

**Magic adverbs:** Adverbs that inject false significance into ordinary descriptions.

- AI-overused: "근본적으로", "깊이", "주목할 만하게", "사실상", "본질적으로"
- Fix when 3+× of the same class appear in one text
- Treatment: delete or replace with concrete fact

**Grandiose nouns:** Nouns too large for their referent.

- AI-overused: "생태계" (for any group), "패러다임" (for any approach), "지형" (for any field), "프레임워크" (for any structure), "시너지" (for any cooperation)
- Fix when the term is not an established term-of-art in the domain
- Treatment: replace with plain noun ("분야", "방식", "구조", "협력")

| Before (AI) | After (natural) |
| --- | --- |
| "이 기술은 근본적으로 산업 생태계의 패러다임을 바꾸고 있습니다" | "이 기술이 산업 구조를 바꾸고 있습니다" |
| "깊이 있는 시너지를 창출하는 프레임워크" | "실질적인 협력 구조" |

---

#### P22 — Repetitive Rhetoric (수사 장치 반복)

**Anaphora overuse:** Same sentence opening repeated 3+ consecutive times.

- Example: "우리는 ~합니다. 우리는 ~합니다. 우리는 ~합니다."
- Fix: vary sentence openings; merge some into compound sentences

**Dead metaphor:** One metaphor introduced and repeated 5+ times throughout the text.

- Fix: use the metaphor once for introduction, then switch to direct description

**Historical analogy stacking:** 3+ rapid-fire historical examples in sequence.

- Example: "애플이 그랬고, 구글이 그랬고, 아마존도 그랬습니다..."
- Fix: keep the single most relevant example; argue it in depth rather than listing

**Em-dash overuse:** 5+× long dashes (—) in one text. Weaker signal in Korean than in English, but increasing in Korean AI text.

- Fix: replace some with commas, parentheses, or separate sentences

---

#### P23 — False Authority & Inflation (거짓 권위·과장)

**Vague attributions:** Claims attributed to unnamed authorities.

- AI-overused: "전문가들은", "연구에 따르면", "업계에서는", "많은 사람들이"
- Fix: specify source or delete attribution frame; state the claim directly

**Stakes inflation:** Every point inflated to world-historical significance.

- Example: API pricing blog post becomes meditation on the fate of civilization
- Fix: match tone to actual scope of the topic

**False vulnerability:** Performative self-awareness that poses no actual risk.

- Example: "솔직히 말씀드리면 저도 확신이 없습니다" (followed by confident assertion)
- Real vulnerability is specific and uncomfortable; AI vulnerability is polished
- Fix: delete if the "admission" leads to a confident conclusion anyway

**False ranges:** "X부터 Y까지" where X and Y are not on any real spectrum.

- Legitimate use implies meaningful midpoints; AI uses it to list two loosely related things
- Fix: state the two items directly without the range framing

| Before (AI) | After (natural) |
| --- | --- |
| "전문가들은 이 기술이 혁명적이라고 평가합니다" | "이 기술은 기존 방식보다 처리 속도가 3배 빠릅니다" (state the fact) |
| "교육부터 의료까지 모든 분야를 변화시킬 것입니다" | "교육과 의료 분야에서 활용 가능성이 높습니다" |

---

### P3 Correction Addendum — Tricolon (삼중 구문 교정 보충)

This addendum extends P3 (Rule of Three) with a restructuring approach for tricolon patterns that originate from English rhetorical habits.

| Before (AI) | After (natural) | Correction logic |
| --- | --- | --- |
| "...알아보는 비용, 조건을 협상하는 비용, 결과가 제대로 나왔는지 확인하는 비용." | "적합한 인재를 찾고 조건을 조율하는 것부터 최종 결과물을 검수하기까지, 모든 과정에는 유무형의 비용이 따릅니다." | "A의 비용, B의 비용, C의 비용" uniform listing replaced with comprehensive narration and asymmetric sentence rhythm |

> **Correction principle:** Break the uniform A/B/C enumeration with asymmetric sentence lengths and a wrapping statement. One detailed item + one summary phrase is more natural than three parallel items.
