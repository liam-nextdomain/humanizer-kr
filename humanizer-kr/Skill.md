---
name: humanizer-kr
description: Remove LLM patterns from Korean text (comma overuse, noun-heavy structure, AI stock phrases, formulaic templates) and rewrite to sound naturally human. Handles essay/blog and academic/report styles.
---

# Humanizer KR: Korean AI Writing Pattern Removal

An editor that detects LLM-specific linguistic patterns in Korean text and rewrites them to read like genuine human writing.

Based on the KatFishNet study (Yonsei University, 2024), which identified Korean-specific comma patterns, POS structure, and spacing habits as the strongest signals of LLM-generated text. Deep reference data, conversion tables, and audit checklists are in `resources/patterns-kr.md`.

---

## Role Definition

- **Detect**: Identify Korean-specific AI writing signatures
- **Rewrite**: Replace with natural human expression while preserving meaning and key information
- **Style distinction**: Apply separate rules for essay/blog vs. academic/report styles
- **Voice injection** (essay only): Beyond pattern removal, give the text a genuine author's voice

---

## Step 0: Style Detection

Before anything else, determine the style of the input text.

**Essay / Blog signals:**
- First-person perspective (나는, 내가, 저는, 우리는)
- Conversational endings (인 것 같다, 라고 생각한다, 더라고요, 거든요)
- Personal experience or emotional commentary
- Addressing the reader directly (어떻게 생각하시나요?)
- Short paragraphs, everyday topics

**Academic / Report signals:**
- Citations, footnotes, or reference sections
- Numbered sections, table of contents, figure/table numbering
- Third-person objective narration (연구 결과, 분석에 따르면, 본 연구는)
- High density of technical/domain terminology
- Abstract, Introduction, Methods, Conclusion structure

**If unclear**, ask the user:
> "이 텍스트는 에세이/블로그 스타일과 논문/보고서 스타일 중 어느 쪽으로 처리할까요?"

### Speech Level Detection (essay style only)

After identifying the essay style, detect and lock the speech level of the original text. **Never change it during rewriting.**

| Speech level | Ending examples | Lock rule |
|---|---|---|
| 합쇼체 (formal polite) | ~합니다, ~입니다, ~했습니다 | All rewrites must end with ~합니다/~입니다 |
| 해요체 (informal polite) | ~해요, ~이에요, ~하죠, ~더라고요 | All rewrites must end with ~해요/~죠 |
| 해체 / 반말 (plain) | ~해, ~야, ~다, ~거든, ~더라 | All rewrites must stay in plain form |

**Critical constraint:** If the original essay uses 합쇼체 (~합니다), every rewritten sentence must also end in 합쇼체. Do not silently drop to 반말 just because it sounds more casual or natural in isolation.

---

## 10 Korean AI Patterns

### [A] Punctuation Patterns

---

#### Pattern 1. Comma Overuse — Strongest Identifier

**Research basis**: Essay genre — human 26.31% vs. LLM 61.03% comma inclusion rate; average segment length human 4.35 vs. LLM 8.56 (KatFishNet).

**Detection signals:**
- Comma inclusion rate exceeds 40% of all sentences
- Two or more commas within a single sentence
- Commas before conjunctions, between subject and predicate, after adverbials

**Before:**
> 현대 사회에서, 기술의 발전은, 인간의 삶을 편리하게 만들고 있지만, 동시에 소외 현상을 초래하기도 한다. 따라서, 이에 대한 대책 마련이 시급한 실정이다.

**Essay treatment:** Remove commas aggressively. Split sentences, use connective endings, or drop the conjunction entirely.

**Academic treatment:** Remove only English-style commas (before conjunctions, between subject and predicate). Preserve enumeration commas (사과, 배, 포도).

**After (essay):**
> 현대 사회에서 기술의 발전은 인간의 삶을 편리하게 만드는 동시에 소외 현상을 초래하기도 한다. 따라서 이에 대한 대책이 시급하다.

**After (academic):**
> 현대 사회에서 기술의 발전은 인간의 삶을 편리하게 만드는 측면이 있는 반면, 동시에 소외 현상을 초래하기도 한다. 따라서 이에 대한 대책 마련이 시급하다.

---

### [B] Structure / Word-Order Patterns

---

#### Pattern 2. Noun-Heavy Structure (체언 의존)

**Detection signals:**
- Patterns like ~의 중요성, ~의 필요성, ~에 대한 고려, ~의 활용
- Three or more noun+particle chains in sequence (especially ~의 ~의 ~)
- Monotonous predicate endings: only ~이다 or ~하다 repeated

**Before:**
> 데이터의 효율적 활용의 중요성에 대한 대중적인 인식의 확산은 기업의 경쟁력의 제고의 기반이다.

**Essay treatment:** Convert noun phrases to verb clauses. Diversify endings. Conversational forms allowed.

**Academic treatment:** Preserve key technical nouns. Dissolve only stacked nominalization chains (~의 ~의).

**After (essay):**
> 데이터를 효율적으로 활용하는 일이 얼마나 중요한지 사람들이 이해하는 것이 기업이 경쟁력을 높이는 밑바탕이 된다.

**After (academic):**
> 데이터를 효율적으로 활용하는 중요성을 대중적으로 확산시키는 과정은 기업 경쟁력을 제고하는 기반이 된다.

---

#### Pattern 3. Rule of Three Enumeration

**Detection signals:**
- Rigid 첫째, 둘째, 셋째 or 첫 번째, 두 번째, 세 번째 lists
- Repeating parallel structures always forced to exactly three items

**Before:**
> 성공적인 프로젝트 수행을 위해서는 세 가지 요소가 중요하다. 첫째, 팀원들 간의 원활한 소통이 이루어져야 한다. 둘째, 명확한 목표 설정과 일정 관리가 필요하다. 셋째, 예상치 못한 변수에 대응할 수 있는 유연한 태도를 갖추어야 한다.

**Essay treatment:** Break the rule-of-three. Keep only the most important point or merge into natural flow.

**Academic treatment:** Keep the enumeration if genuinely needed. Adjust item count to match reality.

**After (essay):**
> 성공적인 프로젝트를 완수하려면 무엇보다 팀원 간의 원활한 소통이 뒷받침되어야 한다. 여기에 명확한 목표 설정과 일정 관리가 유기적으로 맞물릴 때 예상치 못한 변수에도 흔들리지 않는 유연한 대응 능력이 생긴다.

**After (academic):**
> 성공적인 프로젝트 수행을 위한 핵심 요건은 다음과 같다. 첫째, 구성원 간의 원활한 의사소통 체계 구축이다. 둘째, 명확한 목표 설정 및 체계적인 공정 관리이다.

---

#### Pattern 4. Formulaic Template Structure (서론/결론 boilerplate)

**Detection — intro boilerplate:**
- ~에 대해 살펴보겠다
- ~을 알아보고자 한다
- 이 글에서는 ~을 다루겠다

**Detection — conclusion boilerplate:**
- ~이 중요하다는 것을 알 수 있다
- ~해야 할 것이다
- 앞으로도 ~에 관심을 가져야 한다
- 긍정적인 변화를 이끌어 낼 수 있을 것이다

**Detection — "Challenges and Outlook" boilerplate:**
- 물론 과제도 있다, 앞으로의 과제와 가능성, 미래에는 더욱 발전할 것으로 기대된다

**Before:**
> [서론] "이 글에서는 인공지능 기술이 교육 현장에 미치는 영향에 대해 살펴보고자 한다. 인공지능 교육의 필요성을 알아보고 구체적인 활용 방안을 다룰 것이다." 

> [결론] "결론적으로 인공지능 교육이 중요하다는 것을 알 수 있다. 물론 과제도 있지만 앞으로도 이 분야에 관심을 가져야 할 것이다. 그렇게 된다면 교육 현장에서 긍정적인 변화를 이끌어 낼 수 있을 것으로 기대된다."

**Essay treatment:** Remove intro/conclusion boilerplate entirely. Enter content directly, end with author's genuine reaction.

**Academic treatment:** Preserve the academic intro/conclusion structure. Remove only hollow boilerplate; replace with specific content.

**After (essay):**
> [서론] "인공지능은 이제 교실의 풍경을 근본적으로 바꾸어 놓았다. 단순한 기술 도입을 넘어, 아이들의 학습 경험을 어떻게 재설계할 수 있을지에 대한 구체적인 고민이 필요한 시점이다."

> [결론] "기술이 교사를 대신할 수는 없겠지만, 교사의 손에 쥐어진 인공지능은 아이들 한 명 한 명에게 맞춤형 지도를 제공하는 강력한 도구가 된다. 기술의 속도보다 우리 아이들의 성장을 먼저 생각하는 따뜻한 변화가 교육 현장에 자리 잡기를 바란다"

**After (academic):**
> [서론] "본 고는 생성형 인공지능 도입이 개별 맞춤형 학습 성취도에 미치는 영향을 분석하고, 이를 공교육 현장에 적용하기 위한 기술적·제도적 보완 방안을 고찰한다."

> [결론] "분석 결과, 인공지능 기반 학습 시스템은 학습자의 개별 취약점 보완에 유효한 기제로 작용함을 확인하였다. 향후 교사의 에듀테크 역량 강화와 데이터 보안 가이드라인 수립이 뒷받침된다면 공교육의 질적 형평성을 실질적으로 제고할 수 있을 것이다."

---

### [C] Vocabulary / Expression Patterns

---

#### Pattern 5. AI High-Frequency Korean Expressions

**High-frequency conjunctions (overuse signals):**
> 뿐만 아니라, 또한, 이를 통해, 더불어, 나아가, 따라서, 그러나, 하지만, 이처럼, 결과적으로, 그러므로

**High-frequency intensifiers:**
> 특히, 매우, 상당히, 더욱, 크게

**Formulaic modifiers:**
> 다양한, 중요한, 효과적인, 적극적으로, 지속적으로

**Formulaic predicate phrases:**
> 중요한 역할을 한다, 다양한 측면에서, 효과적으로 활용, 긍정적인 영향을 미친다, 부정적인 영향을 미친다

**Before:**
> 특히 인공지능은 다양한 분야에서 중요한 역할을 하며, 교육 현장에서도 효과적으로 활용되고 있습니다. 뿐만 아니라, 이는 학생들에게 긍정적인 영향을 미치며, 결과적으로 학습 성과를 지속적으로 개선할 수 있습니다.

**Treatment:** Delete conjunctions if the flow holds without them. Replace vague modifiers with specific facts.

**After:**
> 인공지능은 교실 안팎에서 학생 개개인의 학습 속도를 세심하게 살피는 조력자가 되었습니다. 학생의 취약한 문제를 실시간으로 분석해 맞춤형 복습 과제를 제시해 주기도 합니다. 이러한 개별 맞춤형 피드백은 아이들이 배움을 포기하지 않고 실력을 차근차근 쌓아 올리도록 돕습니다.

---

#### Pattern 6. Conjunction Overuse

**Detection signal:** Three or more consecutive sentences beginning with a conjunction — especially alternating causal and contrastive connectors.

**Before:**
> 하지만 규칙적인 운동은 신체 건강만을 위한 것이 아니다. 왜냐하면 운동은 뇌의 엔도르핀 분비를 촉진하여 정신적 스트레스를 완화해 주기 때문이다. 그래서 많은 전문가들은 현대인들에게 매일 짧게라도 운동할 것을 권장한다. 또한 이를 통해 업무 효율성까지 함께 높일 수 있다.

**Treatment:** Delete conjunctions where the flow is natural without them. Merge causal relationships into a single clause using -므로 or -서.

**After (essay):**
> 규칙적인 운동은 신체 건강만을 위한 것이 아니다. 뇌의 엔도르핀 분비를 촉진해 정신적 스트레스를 다독여 주는 활동인 까닭이다. 전문가들이 바쁜 현대인에게 매일 짧게라도 몸을 움직이라고 입을 모으는 이유이기도 하다. 운동 습관은 지친 일상에 활력을 불어넣어 업무 효율성까지 기분 좋게 끌어올려 준다.

**After (academic):**
> 규칙적인 운동은 체력 증진뿐만 아니라 뇌의 엔도르핀 분비를 활성화하여 스트레스를 경감시키므로, 전문가들은 현대인의 정신 건강 관리를 위한 규칙적 신체 활동을 강조한다. 이러한 신체 활동은 심리적 안정감을 제공하여 업무 효율성을 제고하는 핵심 요인으로 작용한다.

---

### [D] Word Spacing Patterns — Essay Style Only

> **Important**: Patterns 7 and 8 apply **only** to essay/blog style. Academic/report style must maintain standard Korean spacing throughout.

---

#### Pattern 7. Bound Noun Spacing (의존명사 띄어쓰기)

**Research basis**: LLM bound-noun spacing standard deviation = 0.02 — mechanical consistency. Humans intentionally omit spacing for readability and convenience.

**Essay — acceptable merged forms:**

| LLM standard form | Essay natural form |
|-------------------|--------------------|
| ~는 것이다 | ~는거다 |
| ~할 때 | ~할때 |
| ~는 것 같다 | ~는것 같다 |
| ~ㄹ 뿐이다 | ~ㄹ뿐이다 |

**Treatment:** In essay style, do not enforce standard spacing. Choose whichever form sounds natural in context.

---

#### Pattern 8. Auxiliary Verb Spacing (보조용언 띄어쓰기)

**Essay — acceptable merged forms:**

| LLM standard form | Essay natural form |
|-------------------|--------------------|
| 되어 있다 | 되어있다 |
| 해 주다 | 해주다 |
| 해 왔다 | 해왔다 |
| 알아 보다 | 알아보다 |
| 이루어 지다 | 이루어지다 |
| 만들어 지다 | 만들어지다 |

**Treatment:** In essay style, allow merged forms wherever they feel natural. Do not normalize back to standard spacing.

---

### [E] Communication Patterns

---

#### Pattern 9. Absence of Voice / Personality — Essay Style Only

**Detection signal:** Only neutral, encyclopedic statements — no author reaction, opinion, or emotional register.

**Essay treatment options:**
- Add author reaction: 예상보다 인상적인 결과다, 솔직히 이해하기 어려운 부분이 있다
- Allow acknowledged uncertainty: 잘 모르겠지만, 확신하기 어렵지만
- Allow assertive statements: drop ~라고 생각한다, just say ~다
- Use short declarative sentences to anchor the author's perspective

> **Academic treatment:** Do not apply. Maintain objectivity.

---

#### Pattern 10. Communication Artifacts

**Detection signals:**
- Greeting phrases: 안녕하세요, 도움이 되셨으면 합니다, 궁금한 점이 있으시면
- AI handover language: 다음과 같이 작성해 드리겠습니다, 아래와 같이 정리했습니다
- Emoji overuse: ✅ 🔹 💡 ⭐ decorating section headings or bullet points
- Inline bold headers: **핵심 포인트:** description format
- Bullet-only content: meaning presented entirely as bullet lists instead of prose

**Treatment:** Remove all. Delete greeting phrases. Remove emojis. Convert inline bold headers to natural paragraph prose.

---

## Style Rules at a Glance

| Pattern | Essay / Blog | Academic / Report |
|---------|-------------|-------------------|
| Comma overuse | Aggressively remove; split sentences | Remove English-style commas only |
| Noun-heavy structure | Convert to verb clauses; conversational forms OK | Dissolve stacked nominalization only |
| AI stock expressions | Delete or replace with specifics | Delete or substitute precisely |
| Rule of three | Break up; keep only essential | Keep if genuinely needed |
| Formulaic template | Remove boilerplate; enter content directly | Keep structure; remove hollow boilerplate |
| Conjunction overuse | Aggressively delete | Remove only excessive ones |
| Bound noun spacing | Merged forms allowed | Standard spacing required |
| Auxiliary verb spacing | Merged forms allowed | Standard spacing required |
| Absence of voice | Author reaction/opinion may be added | Not applied; maintain objectivity |
| **Speech level** | **Preserve original — never change** | Not applicable |
| Communication artifacts | Remove entirely | Remove entirely |

---

## Processing Workflow (4 Steps)

### Step 1: Style Determination

Identify essay/blog or academic/report. Ask the user if unclear.

### Step 2: Pattern Scan

Check all 10 patterns in order. Apply style-specific rules (patterns 7, 8, 9 for essay only). Internally list detected patterns.

### Step 3: First Rewrite (Draft)

- Remove patterns while preserving meaning
- Essay: inject voice, vary sentence rhythm (mix short and long sentences)
- Academic: maintain objectivity, remove only hollow boilerplate

### Step 4: AI Audit and Final Rewrite

**Internal question 1:** "What AI-generated traces remain in this text?"
→ List 2–3 remaining issues internally

**Internal question 2:** "Remove those traces."
→ Produce final output

---

## Output Format

```
**1차 재작성본 (Draft)**
[rewritten text]

**남은 AI 흔적**
- [issue 1]
- [issue 2]

**최종본**
[final rewritten text]
```

A change summary is available on request.

---

## Example 1: Essay Style

**Before (AI-generated):**
> 인공지능 기술은, 현대 사회에서 매우 중요한 역할을 하는 혁신적인 기술로, 다양한 분야에서 효과적으로 활용되고 있습니다. 뿐만 아니라, 이를 통해 우리는 더욱 효율적인 사회를 만들어 나갈 수 있습니다. 따라서, 인공지능의 지속적인 발전이 필요하다고 할 수 있습니다. 첫째, 의료 분야에서의 활용, 둘째, 교육 분야에서의 적용, 셋째, 산업 자동화 분야에서의 기여가 대표적입니다. 이처럼 인공지능은 중요한 역할을 한다는 것을 알 수 있습니다.

**Detected patterns:**
- Pattern 1: Comma overuse (2+ per sentence)
- Pattern 2: AI stock expressions (뿐만 아니라, 따라서, 이처럼, 다양한, 효과적으로, 중요한)
- Pattern 3 Rule of Three: 첫째, 둘째, 셋째
- Pattern 4: Formulaic conclusion (중요한 역할을 한다는 것을 알 수 있습니다)
- Pattern 5: Consecutive conjunctions (뿐만 아니라 → 따라서 → 이처럼)
- Speech level detected: **합쇼체** (~합니다 / ~입니다) → must be preserved throughout

**Draft:**
> 인공지능은 현대 사회의 핵심 동력으로서 여러 산업 현장에 깊숙이 자리 잡았습니다. 이는 사회 전반의 생산성을 높이고 새로운 가치를 창출하는 기반이 되기에, 관련 기술의 지속적인 고도화가 요구됩니다. 구체적으로는 정밀한 진단을 돕는 의료 서비스와 개인별 맞춤형 교육, 그리고 지능형 산업 자동화가 그 혁신의 흐름을 주도하고 있습니다. 이렇듯 인공지능은 우리 삶의 질을 한 단계 높이는 결정적인 역할을 수행합니다.

**Remaining AI traces:**
- 의료, 교육, 제조업 three-item list still echoes rule-of-three
- Author's perspective could be slightly stronger

**Final:**
> 인공지능은 단순한 도구를 넘어 현대 사회를 지탱하는 새로운 문법으로 정착하고 있습니다. 비효율을 걷어내고 인간의 잠재력을 확장하는 이 흐름은 더 나은 내일을 향한 진화가 분명합니다. 생명을 지키는 정밀한 의료와 맞춤형 교육, 그리고 지능형 자동화가 주도하는 혁신은 우리 삶의 지형을 근본적으로 바꾸고 있습니다. 이와 같은 기술의 진보는 공동체의 무한한 가능성을 증명하며, 인간다운 삶의 가치를 실현하는 견고한 토대가 될 겁니다.
---

## Example 2: Academic / Report Style

**Before (AI-generated):**
> 본 연구에서는 인공지능 기술의 다양한 측면에 대해 살펴보고자 한다. 인공지능은, 현대 사회에서 매우 중요한 역할을 하며, 다양한 분야에서 효과적으로 활용되고 있다. 뿐만 아니라, 이를 통해 사회적 효율성이 크게 향상될 수 있다. 따라서, 지속적인 연구 및 개발이 필요하다고 할 수 있다.

**Detected patterns:**
- Pattern 1: Comma overuse (인공지능은, / 역할을 하며,)
- Pattern 2: Noun-heavy (다양한 측면에 대해)
- Pattern 3: AI stock expressions (다양한, 효과적으로, 크게, 지속적인)
- Pattern 4: Formulaic intro (살펴보고자 한다) and conclusion (필요하다고 할 수 있다)
- Pattern 5: Consecutive conjunctions (뿐만 아니라 → 따라서)

**Draft:**
> 본 연구는 인공지능 기술의 여러 측면을 고찰한다. 인공지능은 현대 사회에서 중추적인 기능을 담당하며 여러 산업 분야에 활용되고 있다. 이러한 기술 활용은 사회적 효율성 향상으로 이어지므로 관련 연구와 개발을 지속해야 한다.

**Remaining AI traces:**
- Vague Modifiers: '여러 측면', '여러 산업 분야' (Lack of specific scope or context)
- Formulaic Predicates: '중추적인 기능을 담당하며' (Filler phrases that lack semantic density)
- Abstract Nouns: '사회적 효율성' (Abstract concepts without measurable or specific indicators)
- Academic Boilerplate: '고찰한다', '지속해야 한다' (Generic structures lacking specific methodology or research objectives)

**Final:**
> 본 고는 생성형 인공지능 기반의 자동화 시스템이 제조 및 서비스 공정의 생산성 지표에 미치는 영향을 분석한다. 인공지능은 알고리즘을 통한 자원 배분의 최적화 기제로 작용하며 산업 전반의 운영 비용 절감과 공정 효율화를 견인한다. 이러한 기술적 전환이 실질적인 경제적 부가가치 창출로 연계되도록 기술 신뢰성 검증과 제도적 지원 체계 수립이 요구된다.

---

## Reference

Deep numerical data, conversion tables, auxiliary verb merge lists, and audit checklists are in:

`resources/patterns-kr.md`
