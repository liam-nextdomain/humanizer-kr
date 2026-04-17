---
name: humanizer-kr
description: >
  Identifies and removes AI-generated patterns in Korean writing, producing
  natural human-authored text. Covers essay/blog and academic/report styles
  with per-style pattern handling.
when_to_use: >
  Use when the user asks to humanize, de-AI, or naturalize Korean text, or
  references "humanizer" / "humanizer-kr" by name, or asks to remove AI
  patterns from Korean writing. Skip for translation, general editing, or
  non-Korean text.
metadata:
  version: "2.6.0"
  author: ilseoppark
---

# Humanizer KR

Orchestrator for removing AI-generated patterns from Korean writing. This file coordinates the workflow and communicates progress with the user. Pattern knowledge and style rules live in the reference files below.

## Reference Files

| File | When to read |
| --- | --- |
| `references/patterns-kr.md` | Step 2 (pattern scan) and Step 5 (remaining-pattern check) |
| `references/essay-guide.md` | Steps 2–4, only when style = essay/blog |
| `references/academic-guide.md` | Steps 2–3, only when style = academic/report |

> **Example disclaimer (applies to all reference files):** After examples in guides demonstrate correction *techniques* only. MUST match the original author's vocabulary, sentence length, and tone detected in Step 1 — not the example's.

---

## Workflow

Five steps. Each step ends by communicating status to the user and either waits for approval or advances.

### Step 1: Style Detection & Writing Profile

- Determine **essay/blog** vs. **academic/report**. MUST ask if unclear: "에세이/블로그와 논문/보고서 중 어느 쪽으로 처리할까요?"
- For essay: detect and lock **speech level** (높임말 vs. 반말). MUST NOT cross boundary during rewriting. Within 높임말, mixing 하십시오체 and 해요체 is allowed.
- **Ending-level mixing:** If 합쇼체 is mixed with scattered `~거든요/~죠/~네요/~잖아요/~겁니다`, treat as deliberate conversational voice. MUST lock the ratio.

**Writing Profile — detect and lock before rewriting:**

| Trait | Detect | Lock rule |
| --- | --- | --- |
| Vocabulary register | Sino-Korean ratio, everyday vs. technical | MUST rewrite at same register |
| Sentence length | Short (≤30자), long (60자+), or mixed | MUST preserve predominant pattern |
| Tone | Dry/analytical · warm/narrative · conversational | MUST NOT shift tone |
| Syntactic complexity | Simple S-V vs. multi-layered modification | MUST stay within author's range |
| Ending mix ratio | `~습니다` vs `~거든요/~죠/~네요` across source | New sentences MUST match ratio ±20% |
| Thematic anchor nouns | Nouns in title/headings/definitional sentences | MUST exempt from P2 diversification |
| Structural skeleton | H1 + H2 acts/chapters | MUST preserve as simplified H1+H2 |

**Communicate to user:** "스타일은 [essay/academic]으로 판단했습니다. 주요 보존 요소는 [speech level, anchor nouns, structural skeleton...]입니다."

### Step 2: Pattern Scan + Detection Report

**MUST READ:** `references/patterns-kr.md`
**MUST READ (if essay):** `references/essay-guide.md`
**MUST READ (if academic):** `references/academic-guide.md`

- Check all 23 patterns (P1–P14, P15–P23) in order
- Apply style-specific rules (P7, P8, P9 essay-only)
- **Mechanical count first, then classify:** For P2 (lemma repetition), P6 (consecutive conjunctions), P18 (negative parallelism), P20 (rhetorical Q), P22 (anaphora) — run counts before judging thematic intent. Instances count even if motivated.
- **Anchor exception:** Apply P2 thematic anchor rule. Anchor nouns NOT diversified.
- **Header policy:** Author H1+H2 preserved; fractal H3+ and AI-artifact headers removed.

**Present Detection Report + Rewrite Contract + Preserve list, then wait for approval:**

```text
**[패턴 감지 결과]**

**[A] 구두점 패턴**
- P1 (쉼표 남용): N건 — 예시: "..."

**[B] 구조/어순 패턴**
- P3 (삼단 나열·개조식): N건 — 예시: "..."

**[C] 어휘/표현 패턴**
- P2 (어휘 반복): N건 — 예시: "..."
- P5 (AI 상투 표현): N건 — 예시: "..."
- P6 (접속사 남용): N건 — 예시: "..."

**[D] 띄어쓰기 패턴** *(에세이 전용)*
- P7 (의존명사): N건

**[E] 소통 패턴**
- P10 (소통 부산물): N건 — 예시: "..."

**[F] 영어 직역투 패턴**
- P11 (무생물 주어 의인화): N건 — 예시: "..."
- P12 (불필요한 수동형): N건
- P13 (가주어/보어 구문): N건
- P14 (사역동사 만들다 직역): N건

**[G] 영어 기원 수사 패턴**
- P15–P19 Tier-1: N건 (각 패턴별 내역)
- P20–P23 Tier-2: N건 (각 패턴별 내역)

---

**[수정 목표 계약 (Rewrite Contract)]**
1. [카테고리/패턴] — 예: [G] Tier-1 패턴(P15·P18) 100% 제거
2. [스타일 유지] — 예: 하십시오체 + `~거든요` 산발 비율 보존
3. [톤/방향] — 예: 에세이 톤 유지

**[보존 자산 (Preserve)]** *(Rewrite Contract보다 우선한다)*
1. voice/어미 — 예: 합쇼체 + `~거든요/~죠` 비율
2. 구조 — 예: H1 + H2 보존, 마지막 단락 단문 리듬 보존
3. 어휘 anchor — 예: 핵심 주제어 `질문/토큰`은 P2 카운팅 제외
4. 메타포 — 예: `수도꼭지`·`계산기` 메타포 보존
5. 기타 — 작가 명시 보존 요구

이 방향으로 초안 작업을 시작할까요? 수정이 필요하면 말씀해 주세요.
```

- MUST wait for user approval. MUST NOT proceed without it.
- If user rejects all, stop here.
- Rewrite Contract is binding for Step 3. Preserve items override Contract when they conflict.
- **Long-text chunking:** If input > 800자, this Step 2 response MUST contain only the Detection Report + Contract + Preserve list, then stop. Shorter inputs MAY include Step 3 draft in the next response after approval.

### Step 3: Rewrite

**Prerequisite:** User approved at least one category in Step 2.

**Generator guards (all MUST hold):**

| Guard | Rule |
| --- | --- |
| Speech level | MUST rewrite every sentence in the Step 1 tier. For mixed 하십시오체+해요체, preserve the mix. |
| Ending mix | NEW sentences sample the Step 1 ratio ±20%. Do NOT default new sentences to `~습니다`. |
| Writing profile | MUST preserve register, sentence length, tone, syntactic complexity from Step 1. Guide examples show *what* to fix, not *how* the author writes. MUST NOT copy the guide's vocabulary/rhythm. |
| Preserve override | Preserve items outrank Contract fixes. If a fix would violate a Preserve item, skip the fix. |
| Trade-off | When removing P20 or P10, MUST NOT substitute pedagogical lead sentences (`~를 들여다봅니다`, `~쪽 사정을 살펴봅니다`) — that re-introduces P15. Use plain declarative continuation. |
| Anchor noun | Thematic anchor nouns stay in canonical form. Do NOT diversify. |
| Essay rhythm | If original varies rhythm, preserve it; if monotonous, add mild variation within author's predominant length. MUST NOT inject voice (voice = Step 4). |
| Academic objectivity | Maintain objective tone; remove only hollow boilerplate. |

**Output Draft + Change Brief:**

```text
**1차 재작성본 (Draft)**
[rewritten text]

**[1차 수정 브리핑]**
- [A] ...
- [C] ...
```

### Step 4: Voice Consultation (Essay Only)

**MUST READ:** `references/essay-guide.md` — Pattern 9 voice consultation process

1. Identify 2–4 voice injection candidates
2. Present 3–5 options per candidate; wait for author's choice
3. Apply the chosen direction; if author declines, proceed to Step 5 without voice injection

Voice option template:

```text
**[목소리 협의 — 에세이 전용]**

**[V1]** 원문 문장 발췌
→ 이 부분에 작가님만의 관점을 담을 수 있습니다. 어떤 방향이 가장 가깝나요?

1. (동의/긍정) 예시 문장
2. (회의/비판) 예시 문장
3. (개인 경험 연결) 예시 문장
4. (열린 물음 제기) 예시 문장
5. (직접 의견 입력) 원하시는 관점을 직접 말씀해 주세요.
```

Academic style: MUST skip Step 4 entirely.

### Step 5: Remaining-Pattern Check

**MUST READ:** `references/patterns-kr.md`

Re-scan the Step 3/4 output for patterns. Run mechanical counts first (P2, P6, P18, P20, P22). Check:

- [ ] Approved-category patterns still present?
- [ ] (essay) Every sentence in original speech-level tier?
- [ ] (essay) `~습니다` vs `~거든요/~죠` ratio matches Step 1 ±20%?
- [ ] Rewrite Contract items satisfied?
- [ ] Preserve items satisfied?
- [ ] Trade-off: did the rewrite introduce P15 lead sentences, anchor diversification, or new comma clusters?

**If remaining issues exist:**

```text
**[재검증 결과]**
- P_X (설명): N건 — 예시: "..."

추가 수정을 진행할까요? 그대로 제출하실 수도 있습니다.
```

- If user requests more fixes → return to Step 3 with narrowed scope.
- If user says "그대로 제출" or no issues remain → output final version + brief.

**Final output:**

```text
**최종본**
[final rewritten text]

**[최종 수정 브리핑]**
- [category] ...
```
