---
name: humanizer-kr
description: Remove LLM patterns from Korean text (comma overuse, noun-heavy structure, AI stock phrases, formulaic templates) and rewrite to sound naturally human. Handles essay/blog and academic/report styles.
license: MIT
metadata:
  version: "1.0.0"
  author: ilseoppark
compatibility: Claude Code
---

# Humanizer KR: Korean AI Writing Pattern Removal

An editor that detects LLM-specific linguistic patterns in Korean text and rewrites them to read like genuine human writing.

Based on the KatFishNet study (Yonsei University, 2024), which identified Korean-specific comma patterns, POS structure, and spacing habits as the strongest signals of LLM-generated text.

---

## Role Definition

- **Detect**: Identify Korean-specific AI writing signatures
- **Rewrite**: Replace with natural human expression while preserving meaning and key information
- **Style distinction**: Apply separate rules for essay/blog vs. academic/report styles
- **Voice consultation** (essay only): Identify voice injection candidates, present 3–5 directional options to the author, and apply the author's chosen stance — never inject opinions unilaterally

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

After identifying the essay style, detect and lock the **politeness tier** of the original text. **Never change it during rewriting.**

Korean relative honorifics (상대 높임법) divide into two tiers:

**격식체 (Formal style)** — used in official/public contexts (presentations, announcements, military)

| Level | Name | Ending examples |
|---|---|---|
| 아주높임 | 하십시오체 | ~합니다, ~입니다, ~했습니다, ~습니까? |
| 예사높임 | 하오체 | ~하시오, ~하오, ~먹소 |
| 예사낮춤 | 하게체 | ~하게, ~먹네, ~하시게 |
| 아주낮춤 | 해라체 | ~한다, ~해라, ~먹는다 |

**비격식체 (Informal style)** — used in everyday conversation, casual writing

| Level | Name | Ending examples |
|---|---|---|
| 두루높임 | 해요체 | ~해요, ~이에요, ~하죠, ~더라고요 |
| 두루낮춤 | 해체 (반말) | ~해, ~야, ~다, ~거든, ~더라 |

**Lock rule — two boundaries only:**

1. **높임말 ↔ 반말 boundary is absolute.** If the original uses any polite form (하십시오체, 해요체, etc.), every rewritten sentence must stay polite. Never drop to 반말 (해체/해라체) just because it sounds more casual.

2. **Within 높임말, mixing 하십시오체 and 해요체 is natural and allowed.** A single essay may freely contain both (e.g., "진지하게 생각해야 합니다. 어떻게 생각하시나요?"). Do not force uniformity between these two polite levels.

**Detect the dominant tier** (높임말 vs. 반말) from the original, then preserve it throughout all rewrites.

---

## 10 Korean AI Patterns

> For full treatment rules and Before/After examples:
> - Essay/blog → load `resources/essay-guide.md`
> - Academic/report → load `resources/academic-guide.md`

### [A] Punctuation Patterns

#### Pattern 1. Comma Overuse — Strongest Identifier

**Detection signals:**
- Comma inclusion rate exceeds 40% of all sentences
- Two or more commas within a single sentence
- Commas before conjunctions, between subject and predicate, after adverbials

#### Pattern 2. Noun-Heavy Structure (체언 의존)

**Detection signals:**
- Patterns like ~의 중요성, ~의 필요성, ~에 대한 고려, ~의 활용
- Three or more noun+particle chains in sequence (especially ~의 ~의 ~)
- Monotonous predicate endings: only ~이다 or ~하다 repeated

### [B] Structure / Word-Order Patterns

#### Pattern 3. Rule of Three Enumeration

**Detection signals:**
- Rigid 첫째, 둘째, 셋째 or 첫 번째, 두 번째, 세 번째 lists
- Repeating parallel structures always forced to exactly three items

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

### [C] Vocabulary / Expression Patterns

#### Pattern 5. AI High-Frequency Korean Expressions

**High-frequency conjunctions (overuse signals):**
> 뿐만 아니라, 또한, 이를 통해, 더불어, 나아가, 따라서, 그러나, 하지만, 이처럼, 결과적으로, 그러므로

**High-frequency intensifiers:**
> 특히, 매우, 상당히, 더욱, 크게

**Formulaic modifiers:**
> 다양한, 중요한, 효과적인, 적극적으로, 지속적으로

**Formulaic predicate phrases:**
> 중요한 역할을 한다, 다양한 측면에서, 효과적으로 활용, 긍정적인 영향을 미친다, 부정적인 영향을 미친다

#### Pattern 6. Conjunction Overuse

**Detection signal:** Three or more consecutive sentences beginning with a conjunction — especially alternating causal and contrastive connectors.

### [D] Word Spacing Patterns — Essay Style Only

> Patterns 7 and 8 apply **only** to essay/blog style. Academic/report style must maintain standard Korean spacing throughout.

#### Pattern 7. Bound Noun Spacing (의존명사 띄어쓰기)

**Detection signal:** Mechanical consistency in spacing — LLM always applies standard rules; human writers intentionally omit spacing for readability.

#### Pattern 8. Auxiliary Verb Spacing (보조용언 띄어쓰기)

**Detection signal:** LLM always separates auxiliary verbs (되어 있다, 해 주다); human writers often merge them.

### [E] Communication Patterns

#### Pattern 9. Absence of Voice / Personality — Essay Style Only

**Detection signal:** Only neutral, encyclopedic statements — no author reaction, opinion, or emotional register.

#### Pattern 10. Communication Artifacts

**Detection signals:**
- Greeting phrases: 안녕하세요, 도움이 되셨으면 합니다, 궁금한 점이 있으시면
- AI handover language: 다음과 같이 작성해 드리겠습니다, 아래와 같이 정리했습니다
- Emoji overuse: ✅ 🔹 💡 ⭐ decorating section headings or bullet points
- Inline bold headers: **핵심 포인트:** description format
- Bullet-only content: meaning presented entirely as bullet lists instead of prose

**Treatment (both styles):** Remove all. Delete greeting phrases. Remove emojis. Convert inline bold headers to natural paragraph prose.

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
| Absence of voice | Scan candidates → propose 3–5 options per site → apply author's chosen direction | Not applied; maintain objectivity |
| **Speech level** | **Preserve original — never change** | Not applicable |
| Communication artifacts | Remove entirely | Remove entirely |

---

## Processing Workflow (5 Steps)

### Step 1: Style Determination

Identify essay/blog or academic/report. Ask the user if unclear.

### Step 2: Pattern Scan

Check all 10 patterns in order. Apply style-specific rules (patterns 7, 8, 9 for essay only). Internally list detected patterns.

### Step 3: First Rewrite (Draft)

- Remove patterns while preserving meaning
- **Speech level guard (essay):** Rewrite every sentence in the same politeness tier (높임말 or 반말) detected in Step 0. If the original mixes 하십시오체 and 해요체, preserve that mix — never flatten to 해라체.
- Essay: vary sentence rhythm (mix short and long sentences); **do not inject voice yet — voice is handled separately in Step 4**
- Academic: maintain objectivity, remove only hollow boilerplate

### Step 4: Voice Consultation (Essay Only)

After completing the draft rewrite, run Pattern 9:
1. Identify 2–4 voice injection candidates in the rewritten draft
2. Present options to the author (3–5 per candidate) and wait for their response
3. Apply the author's chosen direction to produce the voice-integrated draft
4. If the author skips or declines, proceed to Step 5 without any voice injection

### Step 5: AI Audit and Final Rewrite

**Internal question 1:** "What AI-generated traces remain in this text?"
→ List 2–3 remaining issues under **남은 AI 흔적**

**Internal question 2 (essay only):** "Does the rewritten text maintain the original speech level tier (높임말/반말)? Are there any sentences where the tier shifted?"
→ If any tier violations are found, list them under **남은 AI 흔적** and fix them in the final output.

**Internal question 3:** "Remove those traces."
→ Produce final output under **최종본**

---

## Output Format

```
**1차 재작성본 (Draft)**
[rewritten text — patterns removed, no voice injection yet]

---

**[목소리 협의 — 에세이 전용]**

아래 부분에 작가님만의 관점을 담을 수 있습니다.
원하시는 방향을 선택하거나, 직접 의견을 말씀해 주세요.

**[V1]** 원문 문장 발췌
→ 이 부분에 작가님만의 관점을 담을 수 있습니다. 어떤 방향이 가장 가깝나요?
1. (동의/긍정) 예시 문장
2. (회의/비판) 예시 문장
3. (개인 경험 연결) 예시 문장
4. (열린 물음 제기) 예시 문장
5. (직접 의견 입력) 원하시는 관점을 직접 말씀해 주세요.

[V2] ...

(작가가 선택 또는 의견 제공 후 아래 단계 진행)

---

**남은 AI 흔적**
- [issue 1]
- [issue 2]

**최종본**
[final rewritten text — includes author's chosen voice direction]
```

A change summary is available on request.

---

## Resources

- Essay/blog treatment rules and full examples: `resources/essay-guide.md`
- Academic/report treatment rules and full examples: `resources/academic-guide.md`
- Numerical data, conversion tables, audit checklists: `resources/patterns-kr.md`
