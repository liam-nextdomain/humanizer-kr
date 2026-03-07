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

Based on two empirical studies:

1. **KatFishNet** (Shinwoo Park et al., Yonsei University, 2024) — identified Korean-specific comma patterns, POS structure, and spacing habits as the strongest signals of LLM-generated text.
2. **Park & Kim (2025)** (박종향·김은영, "생성형 AI 텍스트와 인간 텍스트의 내용 및 문체 비교 연구") — compared 69 university essays (AI-assisted vs. human-only) via text mining, revealing lower vocabulary diversity (TTR), overuse of example/emphasis conjunctions, bullet-point enumeration style (개조식), and thought homogenization in AI-assisted writing.

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

Detect the dominant tier from the original: **높임말** (any polite form — 하십시오체, 하오체, 하게체, 해요체) vs. **반말** (해체/해라체).
For the full register table with ending examples, see `resources/essay-guide.md`.

**Lock rule — two boundaries only:**

1. **높임말 ↔ 반말 boundary is absolute.** If the original uses any polite form, every rewritten sentence must stay polite. Never drop to 반말 just because it sounds more casual.

2. **Within 높임말, mixing 하십시오체 and 해요체 is natural and allowed.** A single essay may freely contain both (e.g., "진지하게 생각해야 합니다. 어떻게 생각하시나요?"). Do not force uniformity between these two polite levels.

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

#### Pattern 2. Noun-Heavy Structure & Low Vocabulary Diversity (체언 의존·어휘 반복)

**Detection signals:**
- Patterns like ~의 중요성, ~의 필요성, ~에 대한 고려, ~의 활용
- Three or more noun+particle chains in sequence (especially ~의 ~의 ~)
- Monotonous predicate endings: only ~이다 or ~하다 repeated
- Same verb repeated 3+ times (e.g., 활용하다, 기여하다, 미치다, 제공하다) — AI verb TTR 0.461 vs. human 0.545 (Park & Kim, 2025)
- Same adjective repeated 3+ times (e.g., 다양한, 중요한, 효과적인, 긍정적인) — AI adjective TTR 0.429 vs. human 0.525
- Extremely limited adverb usage — AI adverb TTR 0.468 vs. human 0.602

### [B] Structure / Word-Order Patterns

#### Pattern 3. Rule of Three & Bullet-Point Enumeration (삼단 나열·개조식 구조)

**Detection signals:**
- Rigid 첫째, 둘째, 셋째 or 첫 번째, 두 번째, 세 번째 lists
- Repeating parallel structures always forced to exactly three items
- Bullet-point enumeration style (개조식): short declarative fragments instead of prose, often using numbered sub-items (Ⅰ → 1 → 1) → (1) → ①)
- Excessive outline depth — AI tends to fragment a single topic into multi-level numbered lists rather than developing it in connected sentences (Park & Kim, 2025)
- Clusters of unusually short sentences (avg < 30 chars) signaling list-like summarization rather than discursive writing

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

**High-frequency conjunctions by type (Park & Kim, 2025):**

| Type | AI-overused expressions | Notes |
|------|------------------------|-------|
| 예시·강조 (example/emphasis) | 예를 들어, 특히, 예컨대, 다시 말해, 사실은 | Strongest AI signal — appears far more frequently in AI text |
| 순접·보충 (additive) | 또한, 그리고, 나아가, 동시에, 뿐만 아니라 | Common in both, but AI uses 또한 and 나아가 more |
| 역접·대조 (contrastive) | 하지만, 그러나, 오히려 | Similar frequency in both |
| 인과·결과 (causal) | 따라서, 때문에, 그 결과, 이로 인해 | AI uses slightly more |
| 요약·정리 (summary) | 즉, 이처럼, 결과적으로, 그러므로 | |
| 조건 (conditional) | 한다면, ~라면 | **Human marker** — nearly absent in AI text |

> **Treatment rule:** When example/emphasis conjunctions (예를 들어, 특히, 예컨대, 다시 말해) appear 3+ times in a passage, replace some with direct case descriptions, conditional framing (한다면/~라면), or remove entirely. Introducing conditional conjunctions where appropriate adds human-like reasoning texture.

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
| Noun-heavy structure & vocab repetition | Convert to verb clauses; diversify repeated verbs/adjectives | Dissolve stacked nominalization; vary repeated terms |
| AI stock expressions | Delete or replace with specifics | Delete or substitute precisely |
| Rule of three & bullet-point style | Break up; convert 개조식 to prose | Keep if genuinely needed; limit outline depth |
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

Check all 10 patterns in order. Apply style-specific rules (patterns 7, 8, 9 for essay only). Internally list all detected patterns with counts and example sentences. Refer to `resources/patterns-kr.md` for quantitative thresholds (e.g., comma inclusion rate >40%, TTR benchmarks) and the post-rewrite audit checklist.

### Step 2.5: Pre-Draft Report & Approval

Present detected issues to the user **before writing any draft**. Group by pattern category [A]–[E]:

- For each category, list detected pattern names, instance counts, and one representative example sentence
- End with an approval request: "전체 수정을 진행할까요? 특정 유형만 선택하실 수도 있고, 거부하실 수도 있습니다."
- **Wait for the user's response before proceeding.**
- Apply only the categories the user approves. If the user rejects all, stop here.

### Step 3: First Rewrite (Draft)

**Prerequisite:** User has approved at least one category in Step 2.5.

- Remove only the patterns from approved categories while preserving meaning
- **Speech level guard (essay):** Rewrite every sentence in the same politeness tier (높임말 or 반말) detected in Step 0. If the original mixes 하십시오체 and 해요체, preserve that mix — never flatten to 해라체.
- Essay: vary sentence rhythm (mix short and long sentences); **do not inject voice yet — voice is handled separately in Step 4**
- Academic: maintain objectivity, remove only hollow boilerplate

### Step 3.5: Draft Change Brief

Immediately after the draft, output a concise change summary grouped by category:

- List what was changed per category (e.g., "[A] 쉼표 5개 제거, 문장 2개 분리")
- Keep it brief — bullet points only

### Step 4: Voice Consultation (Essay Only)

After completing the draft rewrite, run Pattern 9:
1. Identify 2–4 voice injection candidates in the rewritten draft
2. Present options to the author (3–5 per candidate) and wait for their response
3. Apply the author's chosen direction to produce the voice-integrated draft
4. If the author skips or declines, proceed to Step 5 without any voice injection

### Step 5: Re-Validation Report & Approval

Internally re-scan the draft for remaining AI patterns. Then:

**Internal question 1:** "What AI-generated traces remain in this text?"

**Internal question 2 (essay only):** "Does the rewritten text maintain the original speech level tier (높임말/반말)? Are there any sentences where the tier shifted?"

**Report remaining issues to the user** grouped by pattern category, with instance counts and example sentences. Ask for approval to fix them:
- "아래 패턴이 아직 남아 있습니다. 추가 수정을 진행할까요?"
- **Wait for the user's response before producing the final output.**
- Apply only the items the user approves. If the user rejects all, present the current draft as the final output without further changes.

### Step 5.5: Final Change Brief

Immediately after the final output, produce a brief summary of what was fixed in this final pass — grouped by category, bullet points only.

---

## Output Format

```
**[패턴 감지 결과]**

발견된 AI 패턴을 유형별로 정리했습니다. 수정할 항목을 선택해 주세요.

**[A] 구두점 패턴**
- Pattern 1 (쉼표 남용): N건 발견
  예시: "..."

**[B] 구조/어순 패턴**
- Pattern 3 (삼단 나열·개조식 구조): N건 발견
  예시: "..."

**[C] 어휘/표현 패턴**
- Pattern 5 (AI 상투 표현): N건 발견
  예시: "..."

**[D] 띄어쓰기 패턴** *(에세이 전용)*
- Pattern 7 (의존명사 띄어쓰기): N건 발견
  예시: "..."

**[E] 소통 패턴**
- Pattern 10 (소통 부산물): N건 발견
  예시: "..."

전체 수정을 진행할까요? 특정 유형만 선택하실 수도 있고, 거부하실 수도 있습니다.

---

(사용자 승인 후 아래 단계 진행)

**1차 재작성본 (Draft)**
[rewritten text — approved patterns removed, no voice injection yet]

---

**[1차 수정 브리핑]**
- [A] ...
- [C] ...

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

**[재검증 결과]**

아래 패턴이 아직 남아 있습니다. 추가 수정을 진행할까요?

- Pattern X (설명): N건
  예시: "..."

---

(사용자 승인 후 아래 단계 진행)

**최종본**
[final rewritten text — includes author's chosen voice direction and final fixes]

---

**[최종 수정 브리핑]**
- [category] ...
```

---

## Resources

- Essay/blog treatment rules and full examples: `resources/essay-guide.md`
- Academic/report treatment rules and full examples: `resources/academic-guide.md`
- Numerical data, conversion tables, audit checklists: `resources/patterns-kr.md`
