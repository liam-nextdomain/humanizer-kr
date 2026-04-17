# Humanizer KR: AI로 쓴 글에서 AI가 쓴 흔적을 지우는 스킬

**LLM이 작성한 한국어 문장에서 'AI스러운 흔적'을 발견하고 사람이 쓴 글에 가깝도록 수정해 주는 Claude 스킬입니다.**

| 버전 | 날짜 | 주요 변경 |
| --- | --- | --- |
| v2.8.0 | 2026-04-17 | **예시 기반 리팩터 + 입력 청킹 도입** — (1) `patterns-kr.md` 전면 재작성: 각 패턴을 Before/After 쌍 + ⚪ Preserve 반례 중심으로 재구성해 클로드가 예시를 분류 앵커로 활용하도록 설계(Anthropic 5Rules "Claude가 이미 아는 건 적지 마라" 원칙 반영). 장황한 정의·제거/보존 테이블·치환 테이블은 삭제하되 숫자 임계값(P1 0.40, P18 1×/2×/3+× tier), 폐쇄 어휘 목록(P5 상투어, P15 구절), 워크플로우 예외(P12 제외, P18 STRICT two-gate, P23 미인용 통계 🟡 분기)는 안전 레일로 유지. (2) 입력 청킹 도입: 신규 `scripts/chunk.py`(stdlib only)가 입력 2,000자 초과 시 H1/H2→문단→문장 경계 우선순위로 1,500자 타겟 분할, 메타포 span 보호, section map과 seam 컨텍스트 출력. (3) SKILL.md Step 2를 2a(청크별 로컬 감지)+2b(글로벌 집계)로 분할, P2·P6·P18/20/22는 글로벌 카운트로 tier 결정, P6 경계 캐리오버(2문장 오버랩) 구현. (4) Step 3에 청크별 재작성 + seam smoothing pass 도입. Step 5에 청킹 활성 시 2-패스 재검증 의무화. (5) code execution 미활성 환경을 위한 fallback 경로 명시. |
| v2.7.0 | 2026-04-17 | **Detection Report 포맷 재설계 + 감지 규칙 정밀화** — (1) SKILL.md Step 2 리포트 템플릿을 per-case 마커(🔴 수정 / 🟡 경계 / ⚪ 보존) + 위치 태그 + 이유 + 수정 방향 동사 형식으로 전면 교체(count-evidence contract 강제), (2) P1을 2단계 프로토콜로 분할(density gate 40% + individual-case classification)하고 Retain 표에 Dependent clause connector / Appositive 행 추가해 한국어 `-는데/-지만/-니까` 연결어미 뒤 쉼표 false positive 차단, (3) P18 감지를 STRICT로 전환 — negation keyword + AI reframing intent 양조건 필수, 양보·단순 대조·문장 간 대조·실체적 대립 예외, (4) P20에 연결 수사구·간접화법·내적 독백 Exclusion 추가, (5) P11에 authorial metaphor Exception 추가(시간이 토큰을 따라간다 유형 보존), (6) P19에 External citations 및 Authorial coinages Exclusion 추가, (7) P22에 thematic anchor noun 예외 도입(P2 규칙과 일치), (8) P15 phrase list에 선언형 결론 class 추가(방향은 분명합니다 유형), (9) P23에 uncited-statistic 저자 확인 분기 추가 |
| v2.6.1 | 2026-04-17 | **사용자 실관찰 패턴 보강** — (1) P5 line 160 "Emotive adj" 항목에 서술형까지 명시(`흥미로운/흥미롭다, 묘한/묘하다`)하여 관형형만 잡히던 누락 위험 제거, (2) P11에 영어 "X reads as Y / X is read as Y" 직역인 `~라/로 읽히다·읽힌다·읽힙니다` 변형을 추가(정의 줄에 Read-as variant 보강 + 표 행 1개 추가). 신규 패턴 ID 신설 없이 기존 패턴 본문만 보강. |
| v2.6.0 | 2026-04-17 | **patterns-kr.md Before/After 예시 검증·보정** — `reference/`의 KatFishNet·Park & Kim 2025 논문 기준 재검토 후 10개 지점 수정. (1) P2 Before의 P12 피동 성분 제거("이루어지며"→"벌어지며"), (2) P5 Before/After를 P2·P17 개념 혼재 제거하고 P5 전용 예시로 재작성, (3) P6 After의 P5 대상어("선택적으로") 제거, (4) P11 Before 구어체 → 격식체 교체, (5) P12 표에서 의미 변형 위험 있던 "학습된 모델" 행을 "연구가 수행되고 있다"로 교체 + Exclusions에 `-된 + 명사` 수식어 예외 보강, (6) P13·P23에 환각·창작 금지 기능적 주석 추가(소스 없을 시 주장 삭제 원칙), (7) P14 After 잔존 사역 "~게 하다" 제거하고 자동사 "-어지다"로 전환, (8) P17 After 조사 교정("가"→"는"), (9) P18 After의 Before/After 등록(register) 불일치 해소(격식 문어→존대 구어) |
| v2.5.0 | 2026-04-17 | **오케스트레이터 구조로 단순화 & 공식 Skills 규격 정렬** — (1) 워크플로우 9단계 → 5단계로 축소 (내부 Generator↔Evaluator 루프 Step 3.0/3.1/3.2/3.3 제거, Step 5 재검증 간소화), (2) `references/output-format.md` 삭제 및 출력 템플릿을 SKILL.md의 각 Step으로 inline 이식, (3) `references/scoring-rubric.md` 삭제 (5차원 채점 루브릭 제거), (4) `patterns-kr.md`를 23 패턴 Before/After 중심으로 재편 (697→479줄, -31%), (5) `essay-guide.md`/`academic-guide.md`에서 중복 면책 및 Generator guard 제거 후 SKILL.md로 이관 (314→205줄, 162→125줄), (6) Frontmatter 정리 — 공식 스키마 외 필드(`license`, `compatibility`) 제거, `when_to_use` 공식 필드 추가하여 트리거 정밀도 강화, description을 기능 front-load 형식으로 수정 |
| v2.4.0 | 2026-04-12 | **트레이드오프 방지 & 작가 자산 보존 강화** — (1) P2에 thematic anchor noun 예외 도입(제목·정의문에 등장하는 핵심 주제어는 다양화 금지), (2) P10 헤더 분기 정책 신설(작가 의도 H1/H2는 보존, fractal H3+와 AI 부산물만 제거), (3) Speech level에 어미 단위 혼용 감지(`~거든요/~죠/~네요` 산발 패턴 보존), (4) Rewrite Contract 템플릿에 Preserve 슬롯 5종 분리, (5) 채점 루브릭에 **Dimension 5 (Structural Readability)** 신설 + Trade-off Audit 도입(P20→P15 치환, 헤더 제거→P15 신규, P11 fix→voice 손실, P2 fix→anchor 분산 4종), (6) Step 2.5에 long-text 청크 룰(800자 초과 시 Detection Report만 단독 응답), (7) Mechanical-count-first 룰을 Step 5에서 Step 2로 전진 배치, (8) 임계 점수 6/8 → 8/10으로 상향 |
| v2.3.0 | 2026-04-06 | **문서 구조 리팩토링 & 패턴 재편성** — P4(Formulaic Template) → P5로 병합, P2 명칭 변경(Low Vocab Diversity), 가이드 파일(essay-guide/academic-guide)에서 중복 Before/After 예시 제거 후 patterns-kr.md를 단일 소스로 통합, P9·P10·P17·P23에 구체적 예시 및 판별 기준 보강 |
| v2.2.0 | 2026-04-02 | **패턴 감지 정밀도 강화** — P2 어간(lemma) 기준 카운팅 규칙 추가 (콜로케이션이 달라도 동일 어간은 동일 카운트), P5 AI 선호 추상 명사 6종(감각/맥락/관점/측면/차원/본질) 감지 추가, P11+P14 복합 감지 규칙(무생물 주어+사역 만들다 동시 출현) 추가, P23 Adjacent Source Halo 규칙(인접 출처가 다른 모호 출처를 검증하지 않음) 추가; Step 5 Mechanical-count-first rule 도입; 채점 루브릭에 Anti-camouflage rule + Step 0 기계적 카운팅 사전 검사 추가; 감사 체크리스트 개선 |
| v2.1.0 | 2026-04-02 | **P5 수사적 관용 표현 확장** — AI rhetorical filler 감지 추가 (감성 형용사·확장 구문·과잉 학술어·논증 클리셰 4유형), 밀도 규칙(동일 유형 2+회 / 전체 4+회), 에세이·학술 가이드에 before/after 예시 추가, 감사 체크리스트 반영 |
| v2.0.0 | 2026-03-29 | **아키텍처 고도화** — Generator/Evaluator 페르소나 분리, 내부 피드백 루프 (Step 3 세분화: 3.0→3.1→3.2→3.3), Rewrite Contract (Step 2.5 확장), 4차원 채점 루브릭(독창성/일관성/자연스러움/완성도) 도입, references/scoring-rubric.md 신규 추가 |
| v1.4.0 | 2026-03-25 | 사용자 글쓰기 특성 보존 강화 — Writing Profile 감지 (어휘 수준, 문장 길이, 톤, 구문 복잡도), Step 3 보존 원칙 명시, 레퍼런스 예시 면책 경고, 대체어 선택 가이드 |
| v1.3.0 | 2026-03-24 | 패턴 23개로 확대 (기존 14개 + 신규 9개, P15–P23), 카테고리 [G] 추가, 가이드 예제·제외 조건 강화 |
| v1.2.1 | 2026-03-24 | 에세이/학술 가이드 예제 개선 및 설명 정제, .gitignore 경로명 수정 |
| v1.2.0 | 2026-03-21 | 영어 직역투 패턴 4개 추가 (P11–P14, [F] 카테고리) |
| v1.1 | 2025-03-21 | SKILL.md 재설계, output-format.md 추가, 폴더 구조 정리 (references/ vs reference/) |
| v1.0 | 2025-03-17 | 최초 릴리즈 — 10가지 AI 패턴, 에세이/학술 스타일 구분, 5단계 워크플로 |

## 📌 소개

LLM을 이용해 글쓰기 많이 하시나요? 물론 LLM의 도움 없이 손수 쓰는 게 바람직하죠. 하지만 때로는 효율적으로 기능적인 글쓰기가 필요한 상황도 있습니다. 이럴 때는 LLM이 참 유용하고요. 그런데 LLM이 쓴 글을 검토하다보면 어딘가 어색하고, '이건 AI가 쓴 티가 난다'는 느낌이 들 때가 있죠. 이런 글은 때로는 성의가 없어 보이기도 하고, 신뢰도를 떨어뜨릴 때도 있습니다. **Humanizer KR**은 AI가 작성한 한국어 텍스트에서 AI가 쓴 패턴을 발견해 'AI가 쓴 흔적'을 조금이나마 줄여주기 위해 만든 Claude 스킬입니다.

이 스킬은 사용자가 제공한 글을 분석하여:

- **AI 패턴 감지**: LLM의 전형적인 23가지 한국어 쓰기 패턴을 자동 식별
- **스타일별 처리**: 에세이/블로그와 학술/보고서 문체를 구분하여 맞춤 규칙 적용
- **대화형 검증**: 감지 결과를 사용자에게 보고하고 승인받아 수정 진행
- **맥락 보존**: 원문의 의도와 톤을 최대한 유지하면서 자연스러운 표현으로 개선
- **관점 삽입 유도**: 필자의 관점을 넣을 수 있는 곳을 포착해 고유한 관점 삽입 유도

LLM이 쓴 글과 한국인의 글쓰기 패턴을 체계적으로 연구한 두 가지 주요 논문(KatFishNet, Park & Kim 2025)의 연구 성과를 참고했습니다.

**참고 자료:**

- **[humanizer](https://github.com/blader/humanizer/tree/main)**: LLM의 영어 글쓰기 패턴 수정 스킬로, 이 스킬의 한국어 버전을 만드는 게 프로젝트의 목표입니다.
- **KatFishNet (2024)**: LLM과 한국 초중고 학생의 에세이 쓰기에서 나타나는 형식적 특성을 비교한 연구입니다.
- **Park & Kim (2025)**: LLM과 한국 대학생의 보고서 쓰기 어휘, 접속사, 문장 구조, 문체, 독자적 사고 등의 특성을 비교한 연구입니다.

## 핵심 특징

- **한국어 특화**: 띄어쓰기, 품사 다양성, 쉼표, 영어식 문장 구조 포착 등 한국어만의 특성을 반영
- **스타일 구분**: 에세이/블로그와 학술논문/보고서 스타일을 구분하여 개별 규칙 적용
- **23가지 패턴 감지** (P1–P23, [A]–[G] 카테고리):
  - 쉼표 남용 (가장 강력한 식별자)
  - 명사 중심 구조 & 어휘 반복 (동사·형용사·부사 다양성 저하)
  - 룰 오브 쓰리 나열 & 개조식 문장 (단문 나열·목차 세분화)
  - 공식적 서식 (서론/결론 템플릿)
  - AI 고빈도 표현 (예시·강조형 접속사 과다, 수사적 관용 표현)
  - 접속사 남용 (조건형 부재)
  - 의존명사 띄어쓰기 (에세이 스타일)
  - 보조용언 띄어쓰기 (에세이 스타일)
  - 개성 부재 (에세이 스타일)
  - 챗봇식 커뮤니케이션 요소
  - 무생물 주어 의인화 (영어 직역투)
  - 불필요한 수동형·관형사절 남용 (영어 직역투)
  - 의미 없는 주어·가주어 구문 (영어 직역투)
  - 사역동사 '만들다' 직역 (영어 직역투)

- **수사적 관용 표현 감지** (v2.1): P5에 AI rhetorical filler 4유형 추가
  - 감성 형용사 (흥미로운, 묘한) — 2회 이상 시 구체적 감정으로 교체
  - 확장 구문 (~에 그치지 않고, ~을 넘어서) — 실질 확장이 없으면 삭제
  - 과잉 학술어 (체득하다, 통찰력) — 일상어로 대체
  - 논증 클리셰 (주장이 약해진다) — 구체적 결과로 서술
  - 밀도 규칙: 동일 유형 2+회 또는 전체 4+회 시 적극 치환
- **패턴 감지 정밀도 강화** (v2.2 신규):
  - **P2 어간 기준 카운팅**: "비슷한 구조 / 비슷한 심리 / 비슷한 이야기"는 콜로케이션이 달라도 "비슷한" × 3으로 카운트
  - **P5 AI 선호 추상 명사**: 감각·맥락·관점·측면·차원·본질 등 6종이 3+회 반복 시 P2+P5 복합 플래그
  - **P11+P14 복합 감지**: 무생물 주어(P11)와 사역 만들다(P14)가 같은 문장에 공존하면 단독 임계값 미달이라도 복합 위반으로 플래그
  - **P23 Adjacent Source Halo**: 인접한 구체적 출처(예: "한국비정규노동센터, 2025")가 있어도 다른 모호한 귀속(예: "임상 정신의학 쪽에서도")은 독립적으로 검증
  - **Step 5 Mechanical-count-first rule**: 정성 평가 전 P2(단어 반복), P18(부정 병렬), P6(접속사 연쇄)를 기계적으로 먼저 카운트
  - **Anti-camouflage rule**: 패턴 인스턴스는 주제 흐름상 정당화되더라도 임계값 카운트에 포함 (의도가 카운트를 감소시키지 않음)
- **문체 보존**: 한국어의 다양한 존대법(합쇼체, 해요체, 해체) 유지, 사용자의 어휘 수준·문장 길이 경향·톤·구문 복잡도 보존

## 폴더 구조

```text
.
├── README.md                     # 이 파일
├── humanizer-kr/                 # 한국어 버전
│   ├── SKILL.md                  # 오케스트레이터 — 5단계 워크플로, Chunking Policy, 출력 템플릿 inline
│   ├── scripts/
│   │   └── chunk.py              # 입력 2,000자 초과 시 결정론적 청크 분할 (stdlib only)
│   └── references/
│       ├── patterns-kr.md        # 23 AI 패턴 예시 기반 (Before/After + ⚪ Preserve 반례), 안전 레일 유지
│       ├── essay-guide.md        # 에세이/블로그 스타일 처리 가이드
│       └── academic-guide.md     # 학술/보고서 스타일 처리 가이드
├── reference/                    # 비운영 참고 문서 (스킬 실행과 무관)
│   ├── SKILL.md                  # 영어 버전 스킬 (원본 아이디어)
│   ├── 5RulesForClaudeSkill.md   # Anthropic 스킬 작성 원칙
│   ├── KatFishNet_Detecting_LLM-Generated_Korean_Text.md  # KatFishNet 논문
│   └── 생성형_AI_텍스트와_인간_텍스트의_내용_및_문체_비교_연구.md  # Park & Kim (2025) 논문
└── ...
```

### 주요 파일 설명

- **`humanizer-kr/SKILL.md`**: 오케스트레이터 — 5단계 워크플로 정의 및 각 Step의 출력 템플릿 inline 제공
  - Step 1: 스타일 감지 & Writing Profile 잠금
  - Step 2: 패턴 스캔 + Detection Report + Rewrite Contract + Preserve list (사용자 승인 대기)
  - Step 3: 재작성 (Draft + Change Brief)
  - Step 4: 음성 협의 (에세이만)
  - Step 5: 남은 패턴 확인 → 최종본 + 최종 브리핑
- **`humanizer-kr/references/patterns-kr.md`**: 23 AI 패턴 Before/After 중심, P1–P23 감지 기준·치환 전략, 스타일별 규칙 테이블, Ending diversification reference
- **`humanizer-kr/references/essay-guide.md`**: 에세이/블로그 스타일 패턴별 처리, 존대법 보존 규칙, P9 음성 협의 3단계 프로세스, Full Worked Example
- **`humanizer-kr/references/academic-guide.md`**: 학술/보고서 스타일 패턴별 처리, 객관성 유지 규칙, Full Worked Example

## 참고 문서

### 영어 버전 참고

**[SKILL.md](references/SKILL.md)**: 이 프로젝트에 아이디어를 제공한 스킬입니다. 영어 텍스트에서 AI 패턴을 제거하는 원본 스킬로, 한국어 버전 스킬의 토대가 되었습니다.

### 주요 논문 두 편

#### 1. KatFishNet (2024) — 쉼표 및 띄어쓰기 패턴

>**[KatFishNet: Detecting LLM-Generated Korean Text through Linguistic Feature Analysis](references/KatFishNet_Detecting_LLM-Generated_Korean_Text.md)**
*Shinwoo Park, Shubin Kim, Do-Kyung Kim, Yo-Sub Han* (Yonsei University, 2024)

**주요 발견**:

- 에세이 장르에서 인간은 쉼표 포함 26.31%, LLM은 61.03% (2.3배 차이)
- 품사 다양성, 띄어쓰기 규칙성, 세그먼트 길이 등 정량적 분석
- 한국어만의 독특한 특성(유연한 띄어쓰기 규칙, 풍부한 형태소 체계, 쉼표 사용 빈도)

[GitHub: katfishnet](https://github.com/Shinwoo-Park/katfishnet)

#### 2. Park & Kim (2025) — 어휘 다양성, 접속사 유형, 개조식 문장

>**[생성형 AI 텍스트와 인간 텍스트의 내용 및 문체 비교 연구](references/생성형_AI_텍스트와_인간_텍스트의_내용_및_문체_비교_연구.md)**
*박종향·김은영* (한성대학교, 동국대학교, 2025)

- 대학교 수업에서 AI 비활용 과제(2021년, 20편) vs AI 활용 과제(2025년, 49편)를 텍스트마이닝으로 비교 분석:

- **주요 발견**:

  - **문장 길이**: 🟢 인간 54.20글자/문장 vs 🔴 AI 48.69글자/문장 (p<.001)
  - **어휘 다양성**: 🟢 인간의 TTR 0.518 vs 🔴 AI 0.427 (특히 동사 🟢 0.545→🔴 0.461, 형용사 🟢 0.525→🔴 0.429, 부사 🟢 0.602→🔴 0.468)
  - **접속사 유형 차이**:
    - 🔴 AI는 예시·강조형(예를 들어, 특히, 예컨대) 과다 사용
    - 🟢 인간은 조건형(한다면, ~라면) 사용 → 🔴 AI에서는 거의 부재
  - **개조식 문장**: 🔴 AI는 서술형 대신 단문 나열·목차 세분화(Ⅰ→1→1)→(1)→①) 경향
  - **사고 획일화**: 🔴 AI 활용 글에서 학생들 간 구조와 문체 유사성 증가

[KCI 논문 상세정보](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003291987)

## Claude Skill 등록 및 사용

### 설치 방법

#### 1. Skill 폴더 구성 확인

- `humanizer-kr/` 폴더 구조가 완성되어 있는지 확인
- 필수 파일: `SKILL.md`, `references/essay-guide.md`, `references/academic-guide.md`, `references/patterns-kr.md`

#### 2. ZIP 파일 생성

```bash
zip -r humanizer-kr.zip humanizer-kr/
```

#### 3. Claude에 업로드

- Claude 웹사이트에서 **Customize > Skills**로 이동
- **"+" 버튼** 클릭
- **"Upload a skill"** 선택
- `humanizer-kr.zip` 파일 선택하여 업로드

#### 4. Skill 활성화

- Skills 목록에서 "humanizer-kr"이 표시됨
- 필요한 경우 토글로 켜고 끌 수 있음

### 사용 방법

Skill 활성화 후 Claude에 다음과 같이 요청합니다:

```markdown
한국어 텍스트를 humanizer-kr 스킬로 정제해 줘.

[정제할 한국어 텍스트]
```

또는:

```markdown
다음 한국어 문장에서 AI 패턴을 제거하고 자연스럽게 다시 써 줄래?

[정제할 한국어 텍스트]
```

### 상세 처리 절차

스킬의 구체적인 작업 절차는 **[humanizer-kr/SKILL.md](humanizer-kr/SKILL.md)**를 참고하세요.

**7단계 + 내부 루프 개요:**

1. **Detect style & writing profile** - 에세이/블로그 vs. 학술/보고서 판별; 에세이일 경우 존대법 탐지·고정; 어휘 수준·문장 길이·톤·구문 복잡도 감지하여 보존
2. **Scan for AI patterns** - 23가지 한국어 AI 패턴 감지, 스타일별 규칙 적용
2.5. **Report & Rewrite Contract** - 감지 결과 리포트, 완료 기준 3가지를 명시적으로 합의 후 사용자 승인
3. **Rewrite with internal feedback loop (Generator ↔ Evaluator)**

   - 3.0: Generator 모드 — 초안 생성
   - 3.1: Evaluator 모드 — 4차원 채점 루브릭 기준 내부 검토 (사용자에게 미노출)
   - 3.2: Generator 모드 — 발견된 문제 수정 (사용자에게 미노출)
   - 3.3: Evaluator 모드 — 최종 1회 검토 (사용자에게 미노출)
   - → 사용자에게는 이미 자체 검토 1-2회를 거친 정제된 초안이 전달됨

3.5. **Draft change brief** — 수정 항목 요약
4. **Consult on voice** (에세이만) - 목소리 주입 후보 제시, 작가 선택 반영
5. **Final re-validation (Auditor persona)** - Rewrite Contract 이행 여부 + 남은 AI 패턴 재검증, 사용자 승인 후 진행
5.5. **Final output & brief** - 최종본 + 수정 요약

**핵심 특징:**

- **Generator/Evaluator 분리**: self-evaluation bias 제거 → Step 3.1 & 5에서 명시적 페르소나 전환
- **내부 피드백 루프**: Step 3 내에서 자동으로 1-2회 자체 검토 및 수정 → 사용자가 받는 초안 품질 향상
- **Rewrite Contract**: Step 2.5에서 명시적으로 "완료 기준"을 합의 → 모든 평가의 바인딩 기준으로 사용

핵심 흐름: 감지 → Rewrite Contract 합의 → 내부 루프 포함 수정 → 목소리 협의 → 재검증 → 최종본

각 스타일별 구체적인 예제와 처리 방법:

- **[에세이/블로그](humanizer-kr/references/essay-guide.md)**: 자연스러운 개인의 목소리 유지, 쉼표 적극 제거
- **[학술/보고서](humanizer-kr/references/academic-guide.md)**: 기술 용어 보존, 열거 쉼표 유지

## 예시

### 에세이 스타일

**원본 (AI 생성):**
> 인공지능 기술은, 현대 사회에서 매우 중요한 역할을 하는 혁신적인 기술로, 다양한 분야에서 효과적으로 활용되고 있습니다. 뿐만 아니라, 이를 통해 우리는 더욱 효율적인 사회를 만들어 나갈 수 있습니다. 따라서, 인공지능의 지속적인 발전이 필요하다고 할 수 있습니다.

**최종본:**
> 인공지능은 단순한 도구를 넘어 현대 사회를 지탱하는 새로운 문법으로 정착하고 있습니다. 비효율을 걷어내고 인간의 잠재력을 확장하는 이 흐름은 더 나은 내일을 향한 진화가 분명합니다. 생명을 지키는 정밀한 의료와 맞춤형 교육, 그리고 지능형 자동화가 주도하는 혁신은 우리 삶의 지형을 근본적으로 바꾸고 있습니다. 이와 같은 기술의 진보는 공동체의 무한한 가능성을 증명하며, 인간다운 삶의 가치를 실현하는 견고한 토대가 될 겁니다.

### 학술 스타일

**원본 (AI 생성):**
> 본 연구에서는 인공지능 기술의 다양한 측면에 대해 살펴보고자 한다. 인공지능은, 현대 사회에서 매우 중요한 역할을 하며, 다양한 분야에서 효과적으로 활용되고 있다. 뿐만 아니라, 이를 통해 사회적 효율성이 크게 향상될 수 있다. 따라서, 지속적인 연구 및 개발이 필요하다고 할 수 있다.

**최종본:**
> 본 고는 생성형 인공지능 기반의 자동화 시스템이 제조 및 서비스 공정의 생산성 지표에 미치는 영향을 분석한다. 인공지능은 알고리즘을 통한 자원 배분의 최적화 기제로 작용하며 산업 전반의 운영 비용 절감과 공정 효율화를 견인한다. 이러한 기술적 전환이 실질적인 경제적 부가가치 창출로 연계되도록 기술 신뢰성 검증과 제도적 지원 체계 수립이 요구된다.

## 문서 및 리소스

### 핵심 문서

- **[humanizer-kr/SKILL.md](humanizer-kr/SKILL.md)**: 6단계 워크플로 정의, 각 단계별 MUST READ 파일 참조 (마스터 가이드)
- **[humanizer-kr/references/patterns-kr.md](humanizer-kr/references/patterns-kr.md)**: 23가지 AI 패턴 인덱스 (P1–P23), 정량 기준, 스타일별 규칙, 연구 데이터, 수사적 관용 표현 치환 테이블, 감사 체크리스트
- **[humanizer-kr/references/essay-guide.md](humanizer-kr/references/essay-guide.md)**: 에세이/블로그 스타일 처리 규칙, 존대법 보존, 음성 협의 프로세스
- **[humanizer-kr/references/academic-guide.md](humanizer-kr/references/academic-guide.md)**: 학술/보고서 스타일 처리 규칙, 객관성 유지

### 참고 자료

- **[references/SKILL.md](references/SKILL.md)**: 원본 영어 스킬 (GitHub: [humanizer](https://github.com/blader/humanizer))
- **[references/KatFishNet_Detecting_LLM-Generated_Korean_Text.md](references/KatFishNet_Detecting_LLM-Generated_Korean_Text.md)**: KatFishNet 논문
- **[references/생성형_AI_텍스트와_인간_텍스트의_내용_및_문체_비교_연구.md](references/생성형_AI_텍스트와_인간_텍스트의_내용_및_문체_비교_연구.md)**: Park & Kim (2025) 논문

## 🎯 프로젝트 상태

- **안정성**: ✅ 프로덕션 준비 완료
- **커버리지**: 한국어 에세이/블로그, 학술/보고서 문체
- **검증**: 2개 주요 연구(KatFishNet, Park & Kim 2025) 기반
