# Academic / Report Style Guide

Detailed treatment rules and Before/After examples for each of the 10 patterns in academic/report style.
For pattern detection signals, see the main `SKILL.md`.

---

## Pattern 1. Comma Overuse — Academic Treatment

**Before:**
> 현대 사회에서, 기술의 발전은, 인간의 삶을 편리하게 만들고 있지만, 동시에 소외 현상을 초래하기도 한다. 따라서, 이에 대한 대책 마련이 시급한 실정이다.

**Treatment:** Remove only English-style commas (before conjunctions, between subject and predicate). Preserve enumeration commas (사과, 배, 포도).

**After:**
> 현대 사회에서 기술의 발전은 인간의 삶을 편리하게 만드는 측면이 있는 반면, 동시에 소외 현상을 초래하기도 한다. 따라서 이에 대한 대책 마련이 시급하다.

---

## Pattern 2. Noun-Heavy Structure — Academic Treatment

**Before:**
> 데이터의 효율적 활용의 중요성에 대한 대중적인 인식의 확산은 기업의 경쟁력의 제고의 기반이다.

**Treatment:** Preserve key technical nouns. Dissolve only stacked nominalization chains (~의 ~의).

**After:**
> 데이터를 효율적으로 활용하는 중요성을 대중적으로 확산시키는 과정은 기업 경쟁력을 제고하는 기반이 된다.

---

## Pattern 3. Rule of Three Enumeration — Academic Treatment

**Before:**
> 성공적인 프로젝트 수행을 위해서는 세 가지 요소가 중요하다. 첫째, 팀원들 간의 원활한 소통이 이루어져야 한다. 둘째, 명확한 목표 설정과 일정 관리가 필요하다. 셋째, 예상치 못한 변수에 대응할 수 있는 유연한 태도를 갖추어야 한다.

**Treatment:** Keep the enumeration if genuinely needed. Adjust item count to match reality.

**After:**
> 성공적인 프로젝트 수행을 위한 핵심 요건은 다음과 같다. 첫째, 구성원 간의 원활한 의사소통 체계 구축이다. 둘째, 명확한 목표 설정 및 체계적인 공정 관리이다.

---

## Pattern 4. Formulaic Template Structure — Academic Treatment

**Treatment:** Preserve the academic intro/conclusion structure. The following formulaic expressions are standard academic conventions — **do not remove them**:

| Position | Permitted formulaic expressions |
| --- | --- |
| 서론 | 본 연구는 ~을 목적으로 한다, ~을 분석·고찰한다, ~을 검토하고자 한다, 본 고는 ~을 다룬다 |
| 본론 | ~에 따르면, ~을 바탕으로, ~을 통해 살펴보면, 선행 연구에서는 ~, ~임을 확인할 수 있다 |
| 결론 | ~을 확인하였다, ~임을 시사한다, 향후 ~에 대한 연구가 요구된다, ~의 필요성이 제기된다 |

Remove only **hollow boilerplate with no informational content** (e.g., "긍정적인 변화를 이끌어 낼 수 있을 것으로 기대된다" with no specific referent); replace with specific findings or claims.

**Before:**
> [서론] "이 글에서는 인공지능 기술이 교육 현장에 미치는 영향에 대해 살펴보고자 한다. 인공지능 교육의 필요성을 알아보고 구체적인 활용 방안을 다룰 것이다."
> [결론] "결론적으로 인공지능 교육이 중요하다는 것을 알 수 있다. 물론 과제도 있지만 앞으로도 이 분야에 관심을 가져야 할 것이다. 그렇게 된다면 교육 현장에서 긍정적인 변화를 이끌어 낼 수 있을 것으로 기대된다."

**After:**
> [서론] "본 고는 생성형 인공지능 도입이 개별 맞춤형 학습 성취도에 미치는 영향을 분석하고, 이를 공교육 현장에 적용하기 위한 기술적·제도적 보완 방안을 고찰한다."
> [결론] "분석 결과, 인공지능 기반 학습 시스템은 학습자의 개별 취약점 보완에 유효한 기제로 작용함을 확인하였다. 향후 교사의 에듀테크 역량 강화와 데이터 보안 가이드라인 수립이 뒷받침된다면 공교육의 질적 형평성을 실질적으로 제고할 수 있을 것이다."

---

## Pattern 5. AI High-Frequency Expressions — Academic Treatment

**Before:**
> 특히 인공지능은 다양한 분야에서 중요한 역할을 하며, 교육 현장에서도 효과적으로 활용되고 있습니다. 뿐만 아니라, 이는 학생들에게 긍정적인 영향을 미치며, 결과적으로 학습 성과를 지속적으로 개선할 수 있습니다.

**Treatment:** Logical connectors (뿐만 아니라, 또한, 따라서, 이를 통해 등) serve structural cohesion in academic writing — **keep them** unless they appear 3+ consecutively (covered by Pattern 6). Only replace: (1) decorative intensifiers with no semantic content (특히, 매우, 상당히 used as filler) and (2) empty modifiers that can be grounded in specific evidence (다양한 → enumerate the actual cases, 효과적으로 → specify the mechanism).

**After:**
> 인공지능은 자연어 처리·컴퓨터 비전·강화학습 등 세부 분야에서 활발히 연구되며, 교육 현장에서는 학습자별 오답 패턴 분석과 맞춤형 피드백 제공 용도로 적용되고 있다. 이를 통해 학습 성취도가 평균 15% 향상되었다는 결과가 보고된 바 있으며, 지속적 활용을 위한 제도적 기반 마련이 요구된다.

---

## Pattern 6. Conjunction Overuse — Academic Treatment

**Before:**
> 하지만 규칙적인 운동은 신체 건강만을 위한 것이 아니다. 왜냐하면 운동은 뇌의 엔도르핀 분비를 촉진하여 정신적 스트레스를 완화해 주기 때문이다. 그래서 많은 전문가들은 현대인들에게 매일 짧게라도 운동할 것을 권장한다. 또한 이를 통해 업무 효율성까지 함께 높일 수 있다.

**Treatment:** Delete conjunctions where the flow is natural without them. Merge causal relationships into a single clause using -므로 or -서.

**After:**
> 규칙적인 운동은 체력 증진뿐만 아니라 뇌의 엔도르핀 분비를 활성화하여 스트레스를 경감시키므로, 전문가들은 현대인의 정신 건강 관리를 위한 규칙적 신체 활동을 강조한다. 이러한 신체 활동은 심리적 안정감을 제공하여 업무 효율성을 제고하는 핵심 요인으로 작용한다.

---

## Patterns 7 & 8: Word Spacing — Not Applicable

Academic/report style must maintain **standard Korean spacing throughout**. Do not apply Pattern 7 (bound noun spacing) or Pattern 8 (auxiliary verb spacing) merged-form rules.

---

## Pattern 9: Voice Consultation — Not Applicable

Do not apply Pattern 9. Maintain objectivity throughout. No author's personal viewpoint, reaction, or emotional register.

---

## Pattern 10. Communication Artifacts — Academic Treatment

**Treatment:** Remove all. Delete greeting phrases. Remove emojis. Convert inline bold headers to natural paragraph prose. Convert bullet-only content into flowing prose.

---

## Example 2: Academic / Report Style (Full Worked Example)

**Before (AI-generated):**
> 본 연구에서는 인공지능 기술의 다양한 측면에 대해 살펴보고자 한다. 인공지능은, 현대 사회에서 매우 중요한 역할을 하며, 다양한 분야에서 효과적으로 활용되고 있다. 뿐만 아니라, 이를 통해 사회적 효율성이 크게 향상될 수 있다. 따라서, 지속적인 연구 및 개발이 필요하다고 할 수 있다.

**Detected patterns:**

- Pattern 1: Comma overuse (인공지능은, / 역할을 하며,)
- Pattern 2: Noun-heavy (다양한 측면에 대해)
- Pattern 4: Formulaic intro (살펴보고자 한다) and conclusion (필요하다고 할 수 있다)
- Pattern 5: AI stock expressions (다양한, 효과적으로, 크게, 지속적인)
- Pattern 6: Consecutive conjunctions (뿐만 아니라 → 따라서)

## 1차 재작성본 (Draft)

> 본 연구는 인공지능 기술의 여러 측면을 고찰한다. 인공지능은 현대 사회에서 중추적인 기능을 담당하며 여러 산업 분야에 활용되고 있다. 이러한 기술 활용은 사회적 효율성 향상으로 이어지므로 관련 연구와 개발을 지속해야 한다.

## 남은 AI 흔적

- Vague Modifiers: '여러 측면', '여러 산업 분야' (Lack of specific scope or context)
- Formulaic Predicates: '중추적인 기능을 담당하며' (Filler phrases that lack semantic density)
- Abstract Nouns: '사회적 효율성' (Abstract concepts without measurable or specific indicators)
- Academic Boilerplate: '고찰한다', '지속해야 한다' (Generic structures lacking specific methodology or research objectives)

## 최종본

> 본 고는 생성형 인공지능 기반의 자동화 시스템이 제조 및 서비스 공정의 생산성 지표에 미치는 영향을 분석한다. 인공지능은 알고리즘을 통한 자원 배분의 최적화 기제로 작용하며 산업 전반의 운영 비용 절감과 공정 효율화를 견인한다. 이러한 기술적 전환이 실질적인 경제적 부가가치 창출로 연계되도록 기술 신뢰성 검증과 제도적 지원 체계 수립이 요구된다.
