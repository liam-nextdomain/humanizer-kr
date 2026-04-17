# Korean LLM Pattern Reference

## Contents

- [Style Rules at a Glance](#style-rules-at-a-glance)
- [A] Punctuation — [P1](#p1-comma-overuse)
- [B] Structure — [P3](#p3-rule-of-three--bullet-enumeration)
- [C] Vocabulary — [P2](#p2-low-vocab-diversity) · [P5](#p5-ai-high-frequency-expressions) · [P6](#p6-conjunction-overuse)
- [D] Word Spacing (essay only) — [P7](#p7-bound-noun-spacing-essay-only) · [P8](#p8-auxiliary-verb-spacing-essay-only)
- [E] Communication — [P9](#p9-absence-of-voice-essay-only) · [P10](#p10-communication-artifacts)
- [F] English Direct Translation — [P11](#p11-inanimate-subject-personification) · [P12](#p12-unnecessary-passive) · [P13](#p13-empty-subject--는-것이다) · [P14](#p14-causative-만들다)
- [G] English-Origin Rhetoric — [P15](#p15-pedagogical-framing) · [P16](#p16-structural-padding) · [P17](#p17-copula-avoidance) · [P18](#p18-negative-parallelism) · [P19](#p19-invented-concept-labels) · [P20](#p20-rhetorical-self-qa) · [P21](#p21-overloaded-modifiers) · [P22](#p22-repetitive-rhetoric) · [P23](#p23-false-authority--inflation)

> P4 (Academic Convention Comma) was merged into P5 in v2.3.0.

---

## Style Rules at a Glance

| Pattern | Essay / Blog | Academic / Report |
| --- | --- | --- |
| P1 Comma | Aggressively remove; split sentences | Remove English-style commas only |
| P2 Vocab repetition | Diversify verbs/adj; anchor nouns exempt | Same; technical terms kept consistent |
| P3 Rule of three | Break up; 개조식 → prose | Keep if needed; limit outline depth |
| P5 Stock expressions | Delete or replace with specifics | Delete or substitute precisely |
| P6 Conjunction | Aggressively delete | Remove only excessive ones |
| P7/P8 Spacing | Merged forms allowed | Standard spacing required |
| P9 Voice | Scan → propose 3–5 options → apply | Not applied; maintain objectivity |
| Speech level | **MUST preserve — MUST NOT change** | Not applicable |
| P10 Communication artifacts | Remove entirely | Remove entirely |
| P11–P14 English direct translation | Convert to active/human subject | Same |
| P15–P19 Tier 1 rhetoric | Remove on first occurrence | Same |
| P20–P23 Tier 2 rhetoric | Fix when density exceeds threshold | Same |

### Tier System (P18–P23)

| Pattern | 1× | 2× | 3+× |
| --- | --- | --- | --- |
| P18 Negative parallelism "A가 아니라 B" | Tier 3 허용 | Tier 2 수정 | Tier 1 적극 수정 |
| P19 Concept label ("~의 역설") | Tier 3 | Tier 3 (different labels) | Tier 2 |
| P20 Self-Q&A "X란? Y이다" | Tier 3 | Tier 2 | Tier 2 |
| P3 Tricolon | Tier 3 | Tier 2 | Tier 1 |

---

## P1. Comma Overuse

- **Definition:** >40% comma inclusion rate across sentences — strongest AI identifier.
- **Detect:** `comma_count / sentence_count > 0.4`.
- **Treatment:** Essay → aggressive remove/split. Academic → remove English-style only.

**Before:** "이 연구는, 흥미로운 결과를 보여주었고, 향후 연구에, 기여할 것으로 기대된다."
**After:** "이 연구는 흥미로운 결과를 보여주었다. 향후 연구에 기여할 것으로 기대된다."

### Commas to remove (English-style)

| Pattern | Before | After |
| --- | --- | --- |
| Before conjunctions | "중요하다, 그리고 필요하다" | "중요하고 필요하다" |
| Subject–predicate | "인공지능은, 중요하다" | "인공지능은 중요하다" |
| After adverbials | "또한, 이를 통해" | "이를 통해" or delete |
| After long modifiers | "복잡한 상황에서, 우리는" | "복잡한 상황에서 우리는" |
| After causal clauses | "기후가 변하고 있어서, 대응이" | "기후가 변하고 있어서 대응이" |

### Commas to retain

| Pattern | Example | Reason |
| --- | --- | --- |
| Parallel nouns | "사과, 배, 포도" | Standard list comma |
| Vocative | "홍길동, 앞으로" | Grammatical marker |
| Quotation (academic) | "다음과 같이 정의된다, '...'" | Academic convention |
| Coordinate clauses (academic) | "A는 B이고, C는 D이다" | Clarifies parallel clauses |

---

## P2. Low Vocab Diversity

- **Definition:** Same verb/adjective/non-anchor noun repeated 3+ times at lemma level.
- **Detect:** Count lemma occurrences across entire text. Different collocations of same lemma still count ("비슷한 구조", "비슷한 심리", "비슷한 이야기" = "비슷한" × 3).
- **Exception — thematic anchor nouns:** A noun is exempt if it (1) appears in title/heading, (2) is the subject of a definitional sentence ("X란 ~이다"), or (3) names the central concept. Anchor nouns MUST NOT be diversified.

**Before:** "**다양한** 분야에서 **다양한** 시도가 이루어지며 **다양한** 결과를 낳고 있다."
**After:** "**여러** 분야에서 **갖가지** 시도가 이루어지며 **폭넓은** 결과를 낳고 있다."

**Anchor example:** Title "질문에 가격표가 붙으면 생기는 일" → "질문" = anchor → 15+ occurrences allowed.

### Verb alternatives

| AI repeat | Alternatives |
| --- | --- |
| 활용하다 | 쓰다, 도입하다, 적용하다, 끌어오다, 접목하다 |
| 기여하다 | 이바지하다, 뒷받침하다, 힘을 보태다, 보탬이 되다 |
| 미치다 | 작용하다, 좌우하다, 끼치다, 파급되다 |
| 제공하다 | 내놓다, 건네다, 마련하다, 내어주다 |
| 향상시키다 | 높이다, 끌어올리다, 개선하다, 나아지게 하다 |

### Adjective alternatives

| AI repeat | Alternatives |
| --- | --- |
| 다양한 | 여러, 갖가지, 폭넓은, 다채로운 |
| 중요한 | 핵심적인, 결정적인, 빼놓을 수 없는, 무게 있는 |
| 효과적인 | 실질적인, 유용한, 알찬, 성과를 내는 |
| 긍정적인 | 바람직한, 고무적인, 희망적인 |
| 부정적인 | 우려스러운, 해로운, 좋지 않은 |

> **Selection rule:** Match the original register — everyday → 쓰다, 높이다; academic → 도입하다, 제고하다.

---

## P3. Rule of Three & Bullet Enumeration

- **Definition:** Rigid 첫째/둘째/셋째, 개조식 outline depth, three-item comma-separated clausal lists.
- **Detect:** Uniform A, B, C enumerations within a single sentence/passage.
- **Treatment:** Break uniform lists with asymmetric sentence rhythm.

**Before:** "알아보는 비용, 조건을 협상하는 비용, 결과를 확인하는 비용."
**After:** "적합한 인재를 찾고 조건을 조율하는 것부터 최종 결과물을 검수하기까지, 모든 과정에는 유무형의 비용이 따릅니다."

> One detailed item + one summary phrase > three parallel items.

---

## P5. AI High-Frequency Expressions

- **Definition:** Stock modifiers (다양한/중요한/효과적인), example conjunctions (특히/예를 들어), rhetorical filler (흥미로운/통찰력/체득하다), abstract catch-all nouns (감각/맥락/측면/본질).
- **Detect:** Same-type filler 2+× = target. 4+× total across types = aggressive treatment.
- **Treatment:** Delete or replace with specifics.

**Before:** "이 기술은 **매우 중요한** 역할을 하며 **다양한 측면에서 효과적으로 활용**된다."
**After:** "이 기술은 처리 속도를 3배 높이고 저전력 기기에서도 구동된다."

### Intensifier treatment

| Intensifier | Treatment |
| --- | --- |
| 매우 중요하다 | Specify reason: "이 단계를 건너뛰면 X가 작동하지 않는다" |
| 상당히 | Replace with numbers |
| 크게 향상되었다 | "X% 향상", "두 배 빨라졌다" |
| 효과적으로 | State what it is effective for, or delete |
| 적극적으로 | Replace with concrete action |
| 지속적으로 | Specify frequency, or delete |

### Example/emphasis conjunctions (3+× → intervene)

| Expression | Treatment |
| --- | --- |
| 예를 들어 | Replace with direct case: "A의 경우를 보면" or delete |
| 특히 | State why it is special, or delete |
| 예컨대 | Keep only one if 예를 들어 also appears |
| 다시 말해 | Delete if preceding sentence is clear |
| 사실은 | Delete if emphasis is weak |

> **Tip:** Insert conditionals (한다면, ~라면) nearly absent in AI text to reveal human thinking: "예를 들어 A가 발생한다" → "A가 발생한다면".

### Rhetorical filler

| Type | Expressions | Treatment |
| --- | --- | --- |
| Emotive adj | 흥미로운, 묘한 | 1× OK; 2+× → specific emotion (낯선, 의외인, 눈에 띄는) |
| Expansion | 단순히 ~에 그치지 않고, ~을 넘어서 | Direct connection (A이자 B) or delete |
| Elevated vocab | 체득하다, 익히다, 통찰력 | 배우다/몸에 배다, 핵심/요점/감 |
| Argument cliché | 주장이 약해진다, 중요한 역할을 하다 | State the specific consequence |

---

## P6. Conjunction Overuse

- **Definition:** 3+ consecutive sentences starting with conjunctions.
- **Detect:** Count conjunction-initial sentences in any 3-sentence window.
- **Treatment:** Delete at least 1 unless the chain is a required causal/argumentative link ("하지만...그래서...따라서...").

**Before:** "AI는 빠르다. 또한 정확하다. 그러나 비싸다. 따라서 선택적으로 써야 한다."
**After:** "AI는 빠르고 정확하지만 비용이 높아 선택적으로 써야 한다."

### Conjunction treatment

| Type | Conjunction | Treatment |
| --- | --- | --- |
| Additive | 또한, 뿐만 아니라, 더불어, 나아가 | Delete or merge |
| Additive | 이를 통해 | Delete or use direct verb |
| Causal | 따라서, 그러므로 | Delete if causality is clear |
| Contrastive | 그러나, 하지만 | Delete if contrast is weak |
| Summary | 이처럼, 결과적으로 | Almost always delete |

### Anti-pattern: merging sentences with `-인데,` (essay)

Merging to remove a conjunction must not create a new comma (P1 violation).

| | Example |
| --- | --- |
| ❌ Wrong | "~상당수**인데,** 그런 자료는~" — new comma |
| ✅ Correct | "~상당수입니다. 그런 자료는~" — delete initial conjunction only |

---

## P7. Bound Noun Spacing (essay only)

- **Treatment:** LLM always separates; essays allow intentional merging.
- **Academic:** MUST maintain standard spacing.

| LLM standard | Essay natural |
| --- | --- |
| ~는 것이다 | ~는거다 / ~는 거다 |
| ~할 때 | ~할때 |
| ~는 것 같다 | ~는것 같다 |
| ~할 수 있다 | Keep as-is (수 is semantically important) |

---

## P8. Auxiliary Verb Spacing (essay only)

- **Treatment:** Essays allow attached forms; academic MUST maintain standard spacing.

| Standard | Attached (essay) |
| --- | --- |
| 되어 있다 | 되어있다 |
| 해 주다 | 해주다 |
| 해 왔다 / 해 오다 | 해왔다 / 해오다 |
| 알아 보다 | 알아보다 |
| 들어 가다 / 올라 가다 / 내려 가다 | 들어가다 / 올라가다 / 내려가다 |
| 이루어 지다 / 만들어 지다 | 이루어지다 / 만들어지다 |

> **Principle:** Representative list. Same rule applies to any main-verb + auxiliary combination that has solidified into a single semantic unit.

---

## P9. Absence of Voice (essay only)

- **Definition:** Neutral statements without author personality.
- **Treatment:** Scan candidates → propose 3–5 voice options per site → apply author's chosen direction. See essay-guide.md §Pattern 9 for the consultation process.

**Before (AI):** "이 결과는 주목할 만하다. 기존 방식 대비 성능이 크게 향상되었다."
**After (voice):** "이 결과를 보고 솔직히 놀랐다. 기존 방식 대비 성능이 이 정도로 차이 날 줄은 몰랐기 때문이다."

---

## P10. Communication Artifacts

- **Definition:** Greetings, AI handover language, emoji, decorative headers, fractal H3+ depth.
- **Treatment:** Remove entirely. Fold substance into prose.

**AI handover examples:** "도움이 되셨길 바랍니다", "더 궁금한 점이 있으시면 말씀해 주세요", "요약하자면 다음과 같습니다:", "아래에서 자세히 설명드리겠습니다"

### Header policy

| Header type | How to identify | Treatment |
| --- | --- | --- |
| AI artifact | Emoji-prefixed (`📌 핵심 정리`), bolded one-line labels, "요약하자면:" handover | **Remove entirely** |
| Author-intended H1/H2 | Named acts/chapters that carry narrative weight (e.g., "같은 수도꼭지, 다른 몸짓") | **Preserve as plain H2**; strip outline numbering; collapse to ≤2 levels |
| Fractal H3+ | H3 under every H2, each containing one paragraph | **Promote to inline emphasis** or merge into parent paragraph's lead |

> **MUST NOT** flatten a structured essay into prose — H1+H2 skeleton is authorial craft.
> **MUST NOT** introduce pedagogical lead sentences ("~쪽 사정을 들여다봅니다", "한쪽에는 ~ 사람들이 있습니다") to replace removed headings — this re-introduces P15.

---

## P11. Inanimate Subject Personification

- **Definition:** Inanimate nouns as agents of deliberate human action (연구가 보여준다, 분석이 짚었다).
- **Quick test:** If subject is not a person but the verb describes deliberate human action, flag.
- **P11+P14 compound:** When inanimate subject is paired with causative 만들다 in the same sentence, flag as stronger compound violation.

| English source | AI direct | Natural Korean |
| --- | --- | --- |
| "Research shows this." | "연구 하나가 이걸 잘 보여줍니다." | "연구 결과에서 그 차이가 뚜렷이 드러납니다." |
| "The analysis points out this issue." | "분석에서 이 문제를 직접 짚었습니다." | "분석 결과, 이 문제점이 드러났습니다." |
| "The environment creates thoughts." | "환경이 생각을 만든다." | "환경에 따라 생각이 바뀐다." |

---

## P12. Unnecessary Passive

- **Definition:** English P.P. translated as 되다/어지다 (학습된, 선택되는, 공유된).
- **Quick test:** If 되다/어지다 can be replaced by an active verb without losing meaning, flag.
- **Exclusions — NOT P12:** -ㄹ 수 있다/없다 (ability), -게 되다 (change of state), native Korean passives (-이/-히/-리/-기), double passives like 보여지다/쓰여지다 (redundancy errors, not translation passives).
- **Priority:** Inside a P3 three-item list, address list structure first. Items like `-ㄹ 수 있는` are NOT passive.

| English source | AI direct | Natural Korean |
| --- | --- | --- |
| "Models trained on..." | "서양 중심으로 학습된 모델이" | "서양 중심으로 데이터를 익힌 모델이" |
| "Expressions that are selected" | "선택되는 표현" | "자주 쓰는 표현" / "선택하는 표현" |
| "Shared algorithm" | "공유된 알고리즘" | "함께 사용하는 알고리즘" |

---

## P13. Empty Subject & ~는 것이다

- **Definition:** "There is a reason/need ~", "It is ~ that" frames that add no information.
- **Quick test:** If ~이유가 있다, ~필요가 있다, ~것이다 frames the sentence without contributing meaning, flag.

| English source | AI direct | Natural Korean |
| --- | --- | --- |
| "There is a reason this is tricky." | "이 현상이 까다로운 이유가 있습니다." | "이 현상은 변수가 많아서 까다롭습니다." |
| "There is a need to ask." | "물어볼 필요가 있습니다." | "의문을 가져야 합니다." |
| "It was also a process of..." | "이것은 배우는 과정이기도 했습니다." | "시행착오는 배우는 과정이기도 합니다." |

---

## P14. Causative 만들다

- **Definition:** English "Make + O + C" translated as ~하게 만들다.
- **Quick test:** If ~하게 만들다 can be rewritten as ~해지다 or a direct verb, flag.

| English source | AI direct | Natural Korean |
| --- | --- | --- |
| "Makes this point clearer." | "이 지점을 더 선명하게 만들어줍니다." | "이 지점이 더 선명해집니다." |
| "Makes thinking easy." | "어떤 사고방식을 쉽게 만들고" | "어떤 사고방식에 익숙해지게 하고" |

---

## P15. Pedagogical Framing

- **Tier 1 — always fix.** Teacher/suspense voice no Korean writer uses.
- **Quick test:** If removing the framing sentence loses zero information, flag.

| Subpattern | Before | After |
| --- | --- | --- |
| Pedagogical voice | "이제 이 개념을 함께 살펴보겠습니다." | (Delete — enter content directly) |
| False suspense | "여기서 흥미로운 점이 있습니다. 사실은 비용이 더 중요했습니다." | "실제로는 비용이 더 중요했습니다." |
| Teacher mode | "이것을 자판기에 비유해보세요. 동전을 넣으면..." | "자판기처럼 입력이 들어가면 출력이 나오는 구조입니다." |

**Phrase list:** 함께 살펴보겠습니다 · 하나씩 풀어보겠습니다 · 차근차근 알아보겠습니다 · 여기서 핵심이 있습니다 · 흥미로운 지점이 나옵니다 · 바로 이 부분이 중요합니다

---

## P16. Structural Padding

- **Tier 1 — always fix.**
- **Quick test:** If a section can be reduced by 50%+ without losing argument or evidence, flag.

| Subpattern | Before | After |
| --- | --- | --- |
| Fractal summary | "이 섹션에서는 비용 구조를 다루겠습니다. (본문) 이상으로 비용 구조를 살펴보았습니다." | (Delete intro/outro; keep substance) |
| One-point dilution | Same point across 5 paragraphs with different analogies | Consolidate to single strongest statement |
| Fragment litany | "개발자의 일상은 반복입니다. 코드를 읽는 것. 버그를 잡는 것. 회의에 참석하는 것." | "개발자의 일상은 코드 리뷰, 디버깅, 회의가 반복되는 구조입니다." |
| Content duplication | Identical paragraphs reappearing | Remove duplicate |

---

## P17. Copula Avoidance

- **Tier 1 — always fix.**
- **Quick test:** If "~로서 기능하다/역할을 하다" can be replaced with "~이다" without losing meaning, flag.
- **Exception:** Do NOT apply when the verb is genuinely figurative (e.g., "이 사건은 민주주의를 상징한다" — symbolic relationship, not copula avoidance).

| Before (AI) | After (natural) |
| --- | --- |
| "이것은 핵심 도구로서 기능한다" | "이것은 핵심 도구다" |
| "이 지표는 성과의 척도 역할을 한다" | "이 지표는 성과 척도다" |
| "이 프레임워크는 기반을 제공한다" | "이 프레임워크가 기반이다" |

**Detection keywords:** ~로서 기능하다, ~의 역할을 하다, ~을 상징하다, ~을 대변하다, ~으로 자리 잡다, ~을 제공하다 (when simple copula suffices).

---

## P18. Negative Parallelism

- **Tiered:** 1× Tier 3 허용, 2× Tier 2 수정, 3+× Tier 1 적극 수정.
- **Detect:** Count "아니라", "아닙니다", "않습니다... 것입니다" carrying "not X — rather Y" reframe.

**Variants:**

- Basic: "A가 아니라 B이다"
- Extended: "단순히 X만이 아닙니다. ... 이야기입니다"
- Causal: "A 때문이 아니라 B 때문이다"

| Before (AI) | After (natural) |
| --- | --- |
| "착해서가 아니라 그게 더 쌌기 때문이죠." | "사실 조직 형성의 동기는 선의보다 경제적 비용 절감이었습니다." |
| "단순히 효율이 올라갔다는 이야기가 아닙니다. ... 이야기입니다." | "이는 단순한 효율 개선을 넘어, '협력의 필수성' 자체를 재검토할 수 있게 된 셈입니다." |

---

## P19. Invented Concept Labels

- **Tiered:** 1× OK, 2× OK (if different labels), 3+ distinct labels = Tier 2.
- **Quick test:** If 2+ "~의 역설/함정/딜레마/격차" appear without each being argued, flag.

**AI-generated labels:** "감독의 역설", "가속화의 함정", "업무량 크리프", "자동화의 딜레마"

| Before (AI) | After (natural) |
| --- | --- |
| "이것이 바로 '자동화의 역설'입니다. 또한 '효율성의 함정'도 존재합니다." | "자동화가 오히려 관리 부담을 늘리는 경우가 있습니다." |

---

## P20. Rhetorical Self-Q&A

- **Tier 2 — fix at 2+×.**
- **Quick test:** If the question can be deleted and the answer stands alone, flag.

| Before (AI) | After (natural) |
| --- | --- |
| "시장이 이미 있는데 왜 굳이 회사를 만드는가? 코즈의 답은 간단했습니다." | "코즈는 시장이 존재하는 상황에서도 기업이 필요한 이유를 '계약 비용'에서 찾았습니다." |
| "이 균열이 한국 사회에서는 어떤 의미일까요?" | "이러한 기술적 균열은 한국 직장 문화와 만났을 때 더욱 복잡한 양상을 띱니다." |

---

## P21. Overloaded Modifiers

- **Tier 2 — fix at 3+× same class.**

**Magic adverbs:** 근본적으로, 깊이, 주목할 만하게, 사실상, 본질적으로 → delete or replace with concrete fact.

**Grandiose nouns:** 생태계, 패러다임, 지형, 프레임워크, 시너지 → plain noun (분야, 방식, 구조, 협력) unless an established term-of-art.

| Before (AI) | After (natural) |
| --- | --- |
| "이 기술은 **근본적으로** 산업 **생태계**의 **패러다임**을 바꾸고 있습니다" | "이 기술이 산업 구조를 바꾸고 있습니다" |
| "**깊이 있는 시너지**를 창출하는 **프레임워크**" | "실질적인 협력 구조" |

---

## P22. Repetitive Rhetoric

- **Tier 2 — fix based on density.**

| Subpattern | Threshold | Fix |
| --- | --- | --- |
| Anaphora | 3+ consecutive same openings | Vary openings; merge some |
| Dead metaphor | Same metaphor 5+× | Use once for intro, then direct description |
| Historical analogy stacking | 3+ rapid-fire | Keep single strongest; argue in depth |
| Em-dash overuse | 5+× `—` | Replace with commas/parentheses |

**Anaphora example:** "우리는 ~합니다. 우리는 ~합니다. 우리는 ~합니다." → merge.
**Analogy example:** "애플이 그랬고, 구글이 그랬고, 아마존도 그랬습니다..." → one example argued deeply.

---

## P23. False Authority & Inflation

- **Tier 2 — evaluate each attribution independently.**

**Vague attributions:** "전문가들은", "연구에 따르면", "업계에서는", "많은 사람들이" → specify source or delete frame.

> **Adjacent source halo:** A specific nearby citation does NOT validate vague references. Each claim needs its own verifiable source.

**Source specificity:**

- ❌ "전문가들은", "연구에 따르면"
- ✅ "MIT 2024년 연구(Smith et al.)", "한국은행 2025년 1분기 보고서"

**Other subtypes:**

- **Stakes inflation:** Every point inflated to world-historical significance → match tone to topic scope.
- **False vulnerability:** "솔직히 말씀드리면 저도 확신이 없습니다" followed by confident assertion → delete.
- **False ranges:** "X부터 Y까지" where X and Y are not on any real spectrum → state items directly.

| Before (AI) | After (natural) |
| --- | --- |
| "전문가들은 이 기술이 혁명적이라고 평가합니다" | "이 기술은 기존 방식보다 처리 속도가 3배 빠릅니다" |
| "교육부터 의료까지 모든 분야를 변화시킬 것입니다" | "교육과 의료 분야에서 활용 가능성이 높습니다" |

---

## Ending Diversification Reference

When rewriting, vary sentence endings to avoid AI-preferred forms.

| LLM preferred | Natural alternatives |
| --- | --- |
| ~하며 | ~하고, ~해서, ~하는데 |
| ~하여 | ~해서, ~했더니, ~하니까 |
| ~하고 있다 | ~하는 중이다, ~하는 상황이다 |
| ~할 수 있다 | ~된다, ~하게 된다, ~가능하다 |
| ~해야 한다 | ~해야 하는 상황이다, ~안 할 수가 없다 |
| ~됨으로써 / ~함으로써 | ~되어서, ~되면서 / ~해서, ~하면서 |
| ~에 따라 | ~에 맞게, ~을 보면, ~이니까 |

---

## Template Clichés to Remove

**Introduction:** "~에 대해 살펴보겠다" · "~을 알아보고자 한다" · "~에 대해 논의해 보겠다" · "~이 무엇인지 탐구해 보겠다" · "이 글에서는 ~을 다루겠다"

**Conclusion:** "~이 중요하다는 것을 알 수 있다" · "~해야 할 것이다" · "앞으로도 ~에 관심을 가져야 한다" · "~이 필요하다고 할 수 있다" · "이처럼 ~은 중요한 의미를 가진다" · "~가 더욱 중요해질 것으로 전망된다"

**Challenge/outlook:** "물론 과제도 있다" · "앞으로의 과제와 가능성" · "한계와 발전 방향" · "미래에는 더욱 발전할 것으로 기대된다"
