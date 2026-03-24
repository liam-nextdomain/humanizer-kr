# Humanizer KR: AI로 쓴 글에서 AI가 쓴 흔적을 지우는 스킬

**LLM이 작성한 한국어 문장에서 'AI스러운 흔적'을 발견하고 사람이 쓴 글에 가깝도록 수정해 주는 Claude 스킬입니다.**

| 버전 | 날짜 | 주요 변경 |
| --- | --- | --- |
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
  - AI 고빈도 표현 (예시·강조형 접속사 과다)
  - 접속사 남용 (조건형 부재)
  - 의존명사 띄어쓰기 (에세이 스타일)
  - 보조용언 띄어쓰기 (에세이 스타일)
  - 개성 부재 (에세이 스타일)
  - 챗봇식 커뮤니케이션 요소
  - 무생물 주어 의인화 (영어 직역투)
  - 불필요한 수동형·관형사절 남용 (영어 직역투)
  - 의미 없는 주어·가주어 구문 (영어 직역투)
  - 사역동사 '만들다' 직역 (영어 직역투)

- **문체 보존**: 한국어의 다양한 존대법(합쇼체, 해요체, 해체) 유지

## 폴더 구조

```text
.
├── README.md                     # 이 파일
├── humanizer-kr/                 # 한국어 버전
│   ├── SKILL.md                  # 에이전트 페르소나, 태스크, 패턴 정의, 처리 워크플로
│   └── references/
│       ├── patterns-kr.md        # 패턴 인덱스, 정량 기준, 스타일 규칙, 연구 데이터
│       ├── essay-guide.md        # 에세이/블로그 스타일 처리 가이드
│       ├── academic-guide.md     # 학술/보고서 스타일 처리 가이드
│       └── output-format.md      # 각 워크플로 단계별 출력 템플릿
├── reference/                    # 비운영 참고 문서 (스킬 실행과 무관)
│   ├── SKILL.md                  # 영어 버전 스킬 (원본 아이디어)
│   ├── 5RulesForClaudeSkill.md   # Anthropic 스킬 작성 원칙
│   ├── KatFishNet_Detecting_LLM-Generated_Korean_Text.md  # KatFishNet 논문
│   └── 생성형_AI_텍스트와_인간_텍스트의_내용_및_문체_비교_연구.md  # Park & Kim (2025) 논문
└── ...
```

### 주요 파일 설명

- **`humanizer-kr/SKILL.md`**: 6단계 워크플로 정의 (스타일 감지 → 패턴 스캔 → 초안 작성 → 음성 협의(에세이) → 재검증 → 최종 검증), 각 단계별 MUST READ 파일 참조
- **`humanizer-kr/references/patterns-kr.md`**: 23가지 AI 패턴 인덱스 (P1–P23), 정량 기준, 스타일별 규칙 테이블, KatFishNet + Park & Kim 연구 데이터, 감사 체크리스트
- **`humanizer-kr/references/essay-guide.md`**: 에세이/블로그 스타일 패턴별 상세 처리 규칙, 존대법 보존, 음성 협의 프로세스
- **`humanizer-kr/references/academic-guide.md`**: 학술/보고서 스타일 패턴별 상세 처리 규칙, 객관성 유지
- **`humanizer-kr/references/output-format.md`**: 감지 리포트, 수정 브리핑, 재검증 보고서 템플릿

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

**6단계 태스크 개요:**

1. **Detect style** - 에세이/블로그 vs. 학술/보고서 판별; 에세이일 경우 존대법 탐지·고정
2. **Scan for AI patterns** - 23가지 한국어 AI 패턴 감지, 스타일별 규칙 적용
3. **Report and get approval** - 감지 결과를 유형별로 리포트, 사용자 승인 후 진행
4. **Rewrite approved sections** - 승인된 유형만 자연스러운 한국어로 재작성
5. **Consult on voice** (에세이만) - 목소리 주입 후보 제시, 작가 선택 반영
6. **Do a final anti-AI pass** - 남은 패턴 재검증, 사용자 승인 후 최종본 출력

핵심 흐름: 감지 → 승인 → 수정 → 목소리 협의 → 재검증 → 최종본

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
- **[humanizer-kr/references/patterns-kr.md](humanizer-kr/references/patterns-kr.md)**: 23가지 AI 패턴 인덱스 (P1–P23), 정량 기준, 스타일별 규칙, 연구 데이터, 감사 체크리스트
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
