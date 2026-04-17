# Korean LLM Pattern Reference

Each pattern below leads with curated Before/After pairs. Examples are classification anchors: if a candidate resembles neither a Before example nor a ⚪ Preserve example, default to retention. Numeric heuristics, closed phrase lists, and workflow exceptions remain explicit because they are not inferable from examples alone.

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

English-style comma insertion — strongest AI marker.
Heuristic: `comma_count / sentence_count ≥ 0.40` → aggressive mode. Below → individual-case mode (scan only explicit violations demonstrated below).
Essay: aggressive + sentence split. Academic: English-style commas only.

Before: "이 연구는, 흥미로운 결과를 보여주었고, 향후 연구에, 기여할 것으로 기대된다."
After: "이 연구는 흥미로운 결과를 보여주었다. 향후 연구에 기여할 것으로 기대된다."

Before: "중요하다, 그리고 필요하다."
After: "중요하고 필요하다."

Before: "인공지능은, 현대 사회에서 매우 중요한 역할을 한다."
After: "인공지능은 현대 사회에서 중요한 역할을 한다."

Before: "기후가 변하고 있어서, 대응이 시급하다."
After: "기후가 변하고 있어서 대응이 시급하다."

⚪ Preserve: "A는 B이고, C는 D이다" — 병렬절 연결(학술 관례).
⚪ Preserve: "~는데, ..." / "~지만, ..." / "~니까, ..." — 한국어 연결어미 뒤 쉼표는 영어 직역 아님. 보존이 기본.
⚪ Preserve: "10만 달러, 우리 돈으로 1억 원" — 환산·부연 삽입 구조.

> **Report contract:** Detection Report의 카운트는 반드시 실제 인용 가능한 위반 예시 수와 일치해야 한다. 쉼표가 없거나 P1과 무관한 문장을 카운트에 포함하지 말 것. 애매한 경우 🟡 경계로 분류.

---

## P2. Low Vocab Diversity

Same lemma repeated 3+× (verb / adjective / non-anchor noun). Different collocations of the same lemma still count ("비슷한 구조", "비슷한 심리", "비슷한 이야기" = "비슷한" × 3).
Anchor exempt — a noun is exempt if it (1) appears in title/heading, (2) is the subject of a definitional sentence ("X란 ~이다"), or (3) names the central concept of the piece. Anchors MUST NOT be diversified.
Register match when substituting: everyday → 쓰다/높이다; academic → 도입하다/제고하다.

Before: "다양한 분야에서 다양한 시도가 벌어지며 다양한 결과를 낳고 있다."
After: "여러 분야에서 갖가지 시도가 벌어지며 폭넓은 결과를 낳고 있다."

Before: "이 기법을 활용하고, 저 기법도 활용하며, 새 기법까지 활용한다."
After: "이 기법을 쓰고, 저 기법도 도입하며, 새 기법까지 접목한다."

Before: "이 결과는 중요하다. 저 결과도 중요하다. 앞으로의 과제도 중요하다."
After: "이 결과는 결정적이다. 저 결과도 빼놓을 수 없다. 앞으로의 과제 역시 무겁다."

⚪ Preserve: 제목 "질문에 가격표가 붙으면 생기는 일" → "질문" = anchor → 15+ 회 반복 허용.

---

## P3. Rule of Three & Bullet Enumeration

Rigid 첫째/둘째/셋째, 개조식 outline depth, or three-item comma-separated clausal lists. Fix by breaking uniform lists with asymmetric rhythm — one detailed item + one summary phrase beats three parallel items.

Before: "알아보는 비용, 조건을 협상하는 비용, 결과를 확인하는 비용."
After: "적합한 인재를 찾고 조건을 조율하는 것부터 최종 결과물을 검수하기까지, 모든 과정에는 유무형의 비용이 따릅니다."

Before: "첫째, 속도가 빠르다. 둘째, 비용이 낮다. 셋째, 사용이 간편하다."
After: "속도가 빠를 뿐 아니라 비용이 낮고 사용도 간편하다."

---

## P5. AI High-Frequency Expressions

Stock modifiers (다양한/중요한/효과적인), example conjunctions (특히/예를 들어), rhetorical filler (흥미로운/통찰력/체득하다), abstract catch-all nouns (감각/맥락/측면/본질).
Heuristic: same-type filler 2+× = target. 4+× total across types = aggressive treatment.

**Closed stock-phrase list** (delete or replace with specifics when density exceeds threshold):

- Intensifiers: 매우, 상당히, 크게, 적극적으로, 지속적으로, 효과적으로
- Example/emphasis connectors: 예를 들어, 특히, 예컨대, 다시 말해, 사실은
- Emotive adjectives: 흥미로운/흥미롭다, 묘한/묘하다
- Expansion frames: 단순히 ~에 그치지 않고, ~을 넘어서
- Elevated vocabulary: 체득하다, 익히다, 통찰력
- Argument clichés: 주장이 약해진다, 중요한 역할을 하다
- Abstract catch-alls: 감각, 맥락, 관점, 측면, 차원, 본질

Before: "특히 이 기술은 효과적으로 쓰이며, 예를 들어 다양한 분야에 적용된다."
After: "이 기술은 의료 영상 판독과 교육용 튜터링에 적용된다."

Before: "매우 중요한 단계이며, 이를 건너뛰면 전체 구조가 흔들릴 수 있다."
After: "이 단계를 건너뛰면 전체 구조가 무너진다."

Before: "흥미로운 현상이 흥미롭게 관찰되었다."
After: "낯선 현상이 눈에 띄게 드러났다."

Before: "예를 들어 A가 발생한다."
After: "A가 발생한다면." (조건형으로 사고 흐름을 드러냄)

Before: "이 기술은 여러 측면에서 본질적인 변화를 만든다."
After: "이 기술은 진료 절차와 환자 동선 두 축에서 구조를 바꾼다."

---

## P6. Conjunction Overuse

3+ consecutive sentences starting with conjunctions within a 3-sentence window. Delete at least 1 unless the chain is a required causal/argumentative link.

Before: "AI는 빠르다. 또한 정확하다. 그러나 비싸다. 따라서 선택적으로 써야 한다."
After: "AI는 빠르고 정확하지만 비용이 높아 꼭 필요한 곳에만 써야 한다."

Before: "이 방법은 유용하다. 뿐만 아니라 간편하다. 더불어 비용도 낮다."
After: "이 방법은 간편하고 비용까지 낮다."

⚪ Preserve: "하지만 ... 그래서 ... 따라서 ..." — 명시적 인과 사슬이 논증 구조에 필수인 경우.

### Anti-pattern: merging sentences with `-인데,` (essay)

Merging to remove a conjunction must not create a new comma (P1 violation).

- ❌ Wrong: "~상당수**인데,** 그런 자료는~" — new comma
- ✅ Correct: "~상당수입니다. 그런 자료는~" — delete initial conjunction only

---

## P7. Bound Noun Spacing (essay only)

LLM always separates; essays allow intentional merging. Academic MUST maintain standard spacing.

Before: "~는 것이다"
After: "~는거다" / "~는 거다" (essay)

Before: "~할 때"
After: "~할때" (essay)

Before: "~는 것 같다"
After: "~는것 같다" (essay)

⚪ Preserve: "~할 수 있다" — 수 is semantically important; keep as-is.

---

## P8. Auxiliary Verb Spacing (essay only)

Essays allow attached forms; academic MUST maintain standard spacing.

Before: "되어 있다", "해 주다", "해 왔다"
After: "되어있다", "해주다", "해왔다" (essay)

Before: "알아 보다", "들어 가다"
After: "알아보다", "들어가다" (essay)

Before: "이루어 지다", "만들어 지다"
After: "이루어지다", "만들어지다" (essay)

> Representative list. The same merging applies to any main-verb + auxiliary combination that has solidified into a single semantic unit.

---

## P9. Absence of Voice (essay only)

Neutral statements without author personality. Scan candidates → propose 3–5 voice options per site → apply author's chosen direction. See `essay-guide.md` §Pattern 9 for the consultation process.

Before (AI): "이 결과는 주목할 만하다. 기존 방식 대비 성능이 크게 향상되었다."
After (voice): "이 결과를 보고 솔직히 놀랐다. 기존 방식 대비 성능이 이 정도로 차이 날 줄은 몰랐기 때문이다."

---

## P10. Communication Artifacts

Greetings, AI handover language, emoji, decorative headers, fractal H3+ depth. Remove entirely; fold substance into prose.

AI handover examples: "도움이 되셨길 바랍니다", "더 궁금한 점이 있으시면 말씀해 주세요", "요약하자면 다음과 같습니다:", "아래에서 자세히 설명드리겠습니다".

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

Inanimate nouns as agents of deliberate human action (연구가 보여준다, 분석이 짚었다).
Read-as variant: `~라/로 읽히다·읽힌다·읽힙니다` = 영어 "X reads as Y"의 직역. Fix to "~라 볼 수 있다", "~로 보인다", "~를 시사한다".
P11+P14 compound: inanimate subject paired with causative 만들다 in the same sentence = stronger compound violation.

Before: "이 연구 결과는 해당 현상을 명확히 보여준다."
After: "이 연구 결과에서 해당 현상이 뚜렷이 드러난다."

Before: "분석에서 이 문제를 직접 짚었습니다."
After: "분석 결과, 이 문제점이 드러났습니다."

Before: "환경이 생각을 만든다."
After: "환경에 따라 생각이 바뀐다."

Before: "이 사건은 위기로 읽힌다."
After: "이 사건은 위기를 시사한다."

⚪ Preserve: "시간이 토큰을 따라가기 시작합니다" — 저자 메타포(일관된 문체로 운용, 영어 P.P. 직역 아님).
⚪ Preserve: "리셋 주기가 하루를 쪼개고 있습니다" — 동일 메타포 운용으로 voice 형성.

> **Authorial metaphor judgement (preserve when all hold):**
>
> 1. No obvious English source ("Research shows", "Analysis points out", "The data reveals") surfaces when back-translating.
> 2. The sentence carries rhythm/voice rather than flat expository report.
> 3. The same personification is used consistently across the piece — an isolated occurrence reads as flourish, not technique.

---

## P12. Unnecessary Passive

English P.P. translated as 되다/어지다 (학습된, 선택되는, 공유된).
Priority: inside a P3 three-item list, address list structure first. Items like `-ㄹ 수 있는` are NOT passive.

**Exclusions — NOT P12:**

- `-ㄹ 수 있다/없다` (ability)
- `-게 되다` (change of state)
- Native Korean passives (`-이/-히/-리/-기`)
- Double passives `보여지다/쓰여지다` (redundancy errors, not translation passives)
- `-된 + 명사` modifiers where the form reflects a genuine result/patient state and active rewriting would shift meaning (e.g., `학습된 모델`, `검증된 자료`)

Before: "~에 관한 연구가 수행되고 있다."
After: "~에 관한 연구를 진행하고 있다."

Before: "선택되는 표현"
After: "자주 쓰는 표현" / "선택하는 표현"

Before: "공유된 알고리즘"
After: "함께 사용하는 알고리즘"

⚪ Preserve: "학습된 모델을 평가했다" — `-된 + 명사`로 결과 상태를 기술, 능동 전환 시 의미 왜곡.

---

## P13. Empty Subject & ~는 것이다

"There is a reason/need ~", "It is ~ that" frames that add no information. If `~이유가 있다`, `~필요가 있다`, `~것이다` frame a sentence without contributing meaning, flag.

Before: "이 현상이 까다로운 이유가 있습니다."
After: "이 현상은 변수가 많아서 까다롭습니다."

Before: "물어볼 필요가 있습니다."
After: "의문을 가져야 합니다."

Before: "이것은 배우는 과정이기도 했습니다."
After: "시행착오는 배우는 과정이기도 합니다."

> **MUST NOT** invent reasons not present in the source text. Replace the empty frame using the actual cause from context; if no specific cause exists, rewrite the claim itself rather than fabricate one.

---

## P14. Causative 만들다

English "Make + O + C" translated as `~하게 만들다`. If the form can be rewritten as `~해지다` or a direct verb, flag.

Before: "이 지점을 더 선명하게 만들어줍니다."
After: "이 지점이 더 선명해집니다."

Before: "어떤 사고방식을 쉽게 만들고"
After: "어떤 사고방식이 쉬워지고"

---

## P15. Pedagogical Framing

Tier 1 — always fix. Teacher/suspense voice no Korean writer uses.
Quick test: removing the framing sentence loses zero information.

**Closed phrase list** (delete the framing sentence or rewrite the substance directly):

- 교수형: 함께 살펴보겠습니다 · 하나씩 풀어보겠습니다 · 차근차근 알아보겠습니다
- 긴장 조성: 여기서 핵심이 있습니다 · 흥미로운 지점이 나옵니다 · 바로 이 부분이 중요합니다
- 선언형 결론: 방향은 분명합니다 · 결론은 명확합니다 · 답은 간단합니다 · 핵심은 하나입니다 · 요점은 이것입니다

Before: "이제 이 개념을 함께 살펴보겠습니다. 첫 번째는..."
After: (교수형 도입 삭제 — 곧장 내용 진입) "첫 번째는..."

Before: "여기서 흥미로운 점이 있습니다. 사실은 비용이 더 중요했습니다."
After: "실제로는 비용이 더 중요했습니다."

Before: "이것을 자판기에 비유해보세요. 동전을 넣으면 음료가 나오는 것처럼..."
After: "자판기처럼 입력이 들어가면 출력이 나오는 구조입니다."

Before: "농담처럼 들리지만 방향은 분명합니다. 토큰 사용량이 곧 업무량이랑 같은 말이 되는 겁니다."
After: "농담 같지만 실질적으로는 토큰 사용량이 업무량의 지표로 자리잡고 있습니다."

---

## P16. Structural Padding

Tier 1 — always fix.
Quick test: if a section can be reduced by 50%+ without losing argument or evidence, flag.

Before: "이 섹션에서는 비용 구조를 다루겠습니다. ... (본문) ... 이상으로 비용 구조를 살펴보았습니다."
After: (인트로·아웃트로 삭제; 본문 substance만 유지)

Before: "개발자의 일상은 반복입니다. 코드를 읽는 것. 버그를 잡는 것. 회의에 참석하는 것."
After: "개발자의 일상은 코드 리뷰, 디버깅, 회의가 반복되는 구조입니다."

Before: 같은 요지를 5개 문단에서 다른 비유로 반복
After: 가장 강한 문단 한 개로 통합

---

## P17. Copula Avoidance

Tier 1 — always fix.
Quick test: if `~로서 기능하다` / `~의 역할을 하다` can be replaced with `~이다` without losing meaning, flag.
Detection keywords: `~로서 기능하다`, `~의 역할을 하다`, `~을 상징하다` (when simple copula suffices), `~을 대변하다`, `~으로 자리 잡다`, `~을 제공하다`.

Before: "이것은 핵심 도구로서 기능한다."
After: "이것은 핵심 도구다."

Before: "이 지표는 성과의 척도 역할을 한다."
After: "이 지표는 성과 척도다."

Before: "이 프레임워크는 기반을 제공한다."
After: "이 프레임워크는 기반이다."

⚪ Preserve: "이 사건은 민주주의를 상징한다" — 진정한 상징 관계 서술이면 P17 아님.

---

## P18. Negative Parallelism

Tiered per global count: 1× Tier 3 허용, 2× Tier 2 수정, 3+× Tier 1 적극 수정.

**STRICT two-gate detection — both conditions MUST hold:**

1. **Keyword**: explicit negation marker `아니라`, `아닙니다`, `~가 아닌`.
2. **Intent — AI reframing**: the clause devalues A and elevates B to a grander/deeper meaning. Signature move is "small-to-big" reframing (`단순히 X가 아니라 Y`, `A 차원이 아니라 B 이야기`) to inflate stakes.

**Exclusions — NOT P18:**

- 양보 구문: "A지만 B", "A처럼 들리지만 B", "A이긴 하지만 B" — concessive, not reframing.
- 단순 대조: "A와 B는 다르다", "A는 X지만 B는 Y" — contrastive compare, not reframing.
- 문장 간 대조: two sentences joined by 그러나/그런데/하지만 — sentence-level contrast, not P18.
- 실체적 대립: "몇 시에 자고 일어나느냐가 아니라, 몇 시에 리셋되느냐가" — two concrete alternatives, not reframing. Preserve up to 2 such instances for essay rhythm even at 3+ total count.

Before: "착해서가 아니라 그게 더 쌌기 때문이죠."
After: "조직이 생긴 건 착해서라기보다 그게 더 쌌기 때문이었죠."

Before: "단순히 효율이 올라갔다는 이야기가 아닙니다. 협력 자체를 재정의할 수 있게 된 이야기입니다."
After: "이는 단순한 효율 개선을 넘어, 협력의 필수성 자체를 재검토할 수 있게 된 셈입니다."

⚪ Preserve: "농담처럼 들리지만 방향은 분명합니다" — 양보 구문(A지만 B), 재프레이밍 아님.
⚪ Preserve: "몇 시에 자고 일어나느냐가 아니라, 몇 시에 리셋되느냐가 중요합니다" — 실체적 대립.

---

## P19. Invented Concept Labels

Tiered: 1× OK, 2× OK (if different labels), 3+ distinct labels in the same AI-frame pattern = Tier 2.
Quick test: if 2+ `~의 역설/함정/딜레마/격차` appear without each being argued, flag.

**Exclusions — NOT P19:**

- **External citations**: 외부 출처에서 가져온 기존 용어. 인용 부호나 영문 병기, 기관·저자 명시. 예: 메타의 '클로드노믹스(Claudeonomics)', '토큰 전설(Token Legend)'.
- **Authorial coinages (marked)**: 저자가 자기 조어임을 명시. 예: "저는 이걸 '사용량 문화'라고 부르겠습니다".

Before: "이것이 바로 '자동화의 역설'입니다. 또한 '효율성의 함정'도 존재합니다. '가속화의 딜레마'도 있습니다."
After: "자동화가 오히려 관리 부담을 늘리는 경우가 있습니다."

⚪ Preserve: "메타가 '클로드노믹스(Claudeonomics)'라고 부른 구조" — 외부 출처 인용.

---

## P20. Rhetorical Self-Q&A

Tier 2 — fix at 2+×.
Quick test: if the question can be deleted and the answer stands alone as a complete sentence, flag. P20 applies ONLY to independent Q + independent A across two sentences.

**Exclusions — NOT P20:**

- 연결 수사구: "이게 얼마나 큰 숫자냐면, ...", "~가 무슨 뜻이냐면, ...", "~하는 이유는, ..." — 질문부와 답부가 한 문장 내에서 **분리 불가능**한 연결 장치. 질문을 지우면 답이 문법적으로 서지 않으면 P20 아님.
- 간접화법: "~고 물어 보니", "~고 했더니", "~냐고 답했습니다" — 보고된 대화/인터뷰 서술.
- 서술자 자문: "내가 왜 이걸 하고 있나 싶었다" — 내적 독백은 voice, 제거 대상 아님.

Before: "시장이 이미 있는데 왜 굳이 회사를 만드는가? 코즈의 답은 간단했습니다."
After: "코즈는 시장이 존재하는 상황에서도 기업이 필요한 이유를 '계약 비용'에서 찾았습니다."

Before: "이 균열이 한국 사회에서는 어떤 의미일까요? 이는 직장 문화와 만났을 때 더 복잡해집니다."
After: "이러한 기술적 균열은 한국 직장 문화와 만났을 때 더욱 복잡한 양상을 띱니다."

⚪ Preserve: "이게 얼마나 큰 숫자냐면, 서울 전체 인구의 두 배입니다" — 연결 수사구.

---

## P21. Overloaded Modifiers

Tier 2 — fix at 3+× same class. Delete magic adverbs (근본적으로, 깊이, 주목할 만하게, 사실상, 본질적으로) or replace with concrete fact. Replace grandiose nouns (생태계, 패러다임, 지형, 프레임워크, 시너지) with plain nouns unless term-of-art.

Before: "이 기술은 근본적으로 산업 생태계의 패러다임을 바꾸고 있습니다."
After: "이 기술이 산업 구조를 바꾸고 있습니다."

Before: "깊이 있는 시너지를 창출하는 프레임워크."
After: "실질적인 협력 구조."

Before: "본질적으로 주목할 만한 변화가 일어나고 있다."
After: "매출 비중이 분기마다 2%p씩 이동하고 있다."

---

## P22. Repetitive Rhetoric

Tier 2 — fix based on density.
**Anchor exception** (inherits from P2): a noun that (1) appears in title/heading or (2) is the central subject of the section is an anchor — exempt from repetition counts. Only non-anchor repetition is P22. Example: 섹션 "쉬는 시간까지 따라오는 한도" 내에서 "리셋/한도"는 anchor이므로 8회 반복도 보존.

| Subpattern | Threshold | Fix |
| --- | --- | --- |
| Anaphora | 3+ consecutive same openings | Vary openings; merge some |
| Dead metaphor | Same metaphor 5+× (non-anchor) | Use once for intro, then direct description |
| Historical analogy stacking | 3+ rapid-fire | Keep single strongest; argue in depth |
| Em-dash overuse | 5+× `—` | Replace with commas/parentheses |

Before: "우리는 효율을 높여왔습니다. 우리는 비용을 줄여왔습니다. 우리는 속도를 끌어올렸습니다."
After: "우리는 효율과 비용, 속도 모두를 개선해 왔습니다."

Before: "애플이 그랬고, 구글이 그랬고, 아마존도 그랬습니다. 마이크로소프트도 마찬가지입니다."
After: "애플의 사례가 가장 뚜렷합니다. 초기 iPod 도입기에 ..." (하나를 깊게 논증)

---

## P23. False Authority & Inflation

Tier 2 — evaluate each attribution independently.
Vague attributions like `전문가들은`, `연구에 따르면`, `업계에서는`, `많은 사람들이` → specify source or delete frame.

> **Adjacent source halo:** A specific nearby citation does NOT validate other vague references. Each claim needs its own verifiable source.

> **Uncited-statistic branch (🟡 workflow):** Before applying the deletion rule, flag uncited statistics ("열 명 중 여덟 명", "절반 넘게", "대부분의 경영진이") as 🟡 author-clarification items in the Step 2 Detection Report. Ask the author: if a source exists, the author adds an inline citation and P23 is resolved; if no source exists, apply the deletion rule below. Do NOT silently delete before asking — an author's paraphrase of real data and an AI fabrication are surface-indistinguishable.

Before: "전문가들은 이 기술이 혁명적이라고 평가합니다."
After: "MIT 2024년 연구(Smith et al.)는 이 기술의 처리 속도가 기존 방식보다 3배 빠르다고 보고했습니다." (출처가 실제로 있을 때)

Before: "교육부터 의료까지 모든 분야를 변화시킬 것입니다."
After: "교육과 의료 분야에서 활용 가능성이 높습니다."

Before: "솔직히 말씀드리면 저도 확신이 없습니다. 하지만 이 기술이 게임 체인저라는 건 분명합니다."
After: "이 기술이 게임 체인저라는 점은 지표상 명확합니다." (false vulnerability 제거)

> **MUST NOT** fabricate statistics or sources to replace vague attributions. If no verifiable number or source exists, delete the claim rather than substitute invented figures.

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
