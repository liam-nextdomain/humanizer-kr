# Humanizer KR: AI로 쓴 글에서 AI 냄새 지우는 스킬

**LLM이 만든 한국어 문장에서 'AI스러운 흔적'을 발견하고 사람이 쓴 글에 가깝도록 수정해 주는 Claude 스킬입니다.**

## 📌 소개

LLM을 이용해 쓴 글에서 'AI가 쓴 티'를 덜 내고 싶으신가요? **Humanizer KR**은 AI가 생성한 한국어 텍스트를 자연스러운 인간의 필체로 전환하는 Claude 스킬입니다.

이 스킬은 작성된 글을 분석하여:

- **AI 패턴 감지**: LLM의 전형적인 10가지 한국어 쓰기 패턴을 자동 식별
- **스타일별 처리**: 에세이/블로그와 학술/보고서 문체를 구분하여 맞춤 규칙 적용
- **대화형 검증**: 감지 결과를 사용자에게 보고하고 승인받아 안전하게 수정 진행
- **맥락 보존**: 원문의 의도와 톤을 최대한 유지하면서 자연스러운 표현으로 개선

LLM과 사람의 글쓰기 패턴을 체계적으로 연구한 두 가지 주요 논문(KatFishNet, Park & Kim 2025)을 바탕으로 개발되었습니다.

**핵심 근거:**

- **[humanizer](https://github.com/blader/humanizer/tree/main)**: LLM의 영어 글쓰기 패턴 수정 스킬 (원본 개념)
- **KatFishNet (2024)**: LLM과 사람의 한국어 에세이 쓰기 형식 특성 비교 연구
- **Park & Kim (2025)**: LLM과 사람의 한국어 보고서 쓰기 어휘, 접속사, 구조 특성 비교 연구

## 핵심 특징

- **한국어 특화**: 띄어쓰기, 품사 다양성, 쉼표 패턴 등 한국어만의 특성을 반영
- **스타일 구분**: 에세이/블로그와 학술논문/보고서 스타일을 구분하여 개별 규칙 적용
- **10가지 패턴 감지**:
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

- **문체 보존**: 한국어의 다양한 존대법(합쇼체, 해요체, 해체) 유지

## 폴더 구조

```text
.
├── README.md                     # 이 파일
├── humanizer-kr/                 # 한국어 버전
│   ├── SKILL.md                  # 에이전트 페르소나, 태스크, 패턴 정의, 처리 워크플로
│   └── resources/
│       ├── patterns-kr.md        # KatFishNet 연구 데이터 및 상세 참고 자료
│       ├── essay-guide.md        # 에세이/블로그 스타일 처리 가이드
│       └── academic-guide.md     # 학술/보고서 스타일 처리 가이드
├── references/                   # 참고 문서 및 자료
│   ├── SKILL.md                  # 영어 버전 스킬 (원본 아이디어)
│   ├── KatFishNet_Detecting_LLM-Generated_Korean_Text.md  # KatFishNet 논문
│   └── 생성형_AI_텍스트와_인간_텍스트의_내용_및_문체_비교_연구.md  # Park & Kim (2025) 논문
└── ...
```

### 주요 파일 설명

- **`humanizer-kr/SKILL.md`**: 에이전트 페르소나 및 6단계 태스크 정의, 10가지 AI 패턴의 감지 신호, 스타일 판단 기준, 처리 워크플로(감지 리포트 → 승인 → 초안 → 재검증 → 최종본), 출력 형식 정의
- **`humanizer-kr/resources/essay-guide.md`**: 에세이/블로그 스타일의 각 패턴별 상세 처리 규칙, 존대법 유지 방법, Before/After 예제
- **`humanizer-kr/resources/academic-guide.md`**: 학술/보고서 스타일의 각 패턴별 상세 처리 규칙, 기술 용어 보존 방법, Before/After 예제
- **`humanizer-kr/resources/patterns-kr.md`**: KatFishNet + Park & Kim 연구 데이터, 쉼표 제거/유지 판단 기준, 어휘 다양성 참고표, 감사 체크리스트

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
- 필수 파일: `SKILL.md`, `resources/essay-guide.md`, `resources/academic-guide.md`, `resources/patterns-kr.md`

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
2. **Scan for AI patterns** - 10가지 한국어 AI 패턴 감지, 스타일별 규칙 적용
3. **Report and get approval** - 감지 결과를 유형별로 리포트, 사용자 승인 후 진행
4. **Rewrite approved sections** - 승인된 유형만 자연스러운 한국어로 재작성
5. **Consult on voice** (에세이만) - 목소리 주입 후보 제시, 작가 선택 반영
6. **Do a final anti-AI pass** - 남은 패턴 재검증, 사용자 승인 후 최종본 출력

핵심 흐름: 감지 → 승인 → 수정 → 목소리 협의 → 재검증 → 최종본

각 스타일별 구체적인 예제와 처리 방법:

- **[에세이/블로그](humanizer-kr/resources/essay-guide.md)**: 자연스러운 개인의 목소리 유지, 쉼표 적극 제거
- **[학술/보고서](humanizer-kr/resources/academic-guide.md)**: 기술 용어 보존, 열거 쉼표 유지

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

- **[humanizer-kr/SKILL.md](humanizer-kr/SKILL.md)**: 에이전트 페르소나, 6단계 워크플로, 10가지 AI 패턴 정의, 처리 규칙 및 출력 형식 (마스터 가이드)
- **[humanizer-kr/resources/essay-guide.md](humanizer-kr/resources/essay-guide.md)**: 에세이/블로그 스타일 처리 규칙, 존대법 유지 방법, Before/After 예제
- **[humanizer-kr/resources/academic-guide.md](humanizer-kr/resources/academic-guide.md)**: 학술/보고서 스타일 처리 규칙, 기술 용어 보존 방법, Before/After 예제
- **[humanizer-kr/resources/patterns-kr.md](humanizer-kr/resources/patterns-kr.md)**: 연구 데이터, 통계 벤치마크, 감사 체크리스트

### 참고 자료

- **[references/SKILL.md](references/SKILL.md)**: 원본 영어 스킬 (GitHub: [humanizer](https://github.com/blader/humanizer))
- **[references/KatFishNet_Detecting_LLM-Generated_Korean_Text.md](references/KatFishNet_Detecting_LLM-Generated_Korean_Text.md)**: KatFishNet 논문
- **[references/생성형_AI_텍스트와_인간_텍스트의_내용_및_문체_비교_연구.md](references/생성형_AI_텍스트와_인간_텍스트의_내용_및_문체_비교_연구.md)**: Park & Kim (2025) 논문

## 🔄 버전 히스토리

### v1.0 (현재) — 2025년 3월

**주요 기능:**

- 10가지 AI 패턴 감지 및 자동 식별
- 에세이/블로그 vs. 학술/보고서 스타일 구분
- 6단계 워크플로: 감지 → 승인 → 수정 → 목소리 주입 → 재검증 → 최종본
- 한국어 존대법(합쇼체, 해요체, 해체) 보존
- 대화형 검증 프로세스 (승인 게이트 포함)

**포함 내용:**

- KatFishNet 연구 통합: 쉼표, 띄어쓰기, 품사 패턴 분석
- Park & Kim (2025) 연구 통합: 어휘 다양성, 접속사 유형, 개조식 문장, 사고 획일화 감지
- 스타일별 상세 처리 가이드 및 예제

**최근 업데이트:**

- **2025-03-17 (현재)**: 토큰 효율화 리팩토링
  - 불필요한 설명 제거 (상대높임법 테이블, 명사구→동사절 변환 패턴표, 중복된 Pattern 10 설명)
  - essay-guide.md: 24줄 감소 (266줄)
  - academic-guide.md: 1줄 감소 (182줄)
  - patterns-kr.md: 49줄 감소 (344줄)
  - 총 74줄 절감 (5RulesForClaudeSkill 지침 준수)

- **2025-03-17**: 스킬 문서 및 리소스 최종 정비
  - README 구조 개선 및 문서화 완성
  - 페르소나 및 태스크 구조 명확화
  - 처리 워크플로 최적화

### 개발 히스토리

**주요 마일스톤:**

- **2025-03-17**: 토큰 효율화 및 README 갱신
- **2025-03-16**: 페르소나 및 태스크 구조 명확화 (`255f53f`)
- **2025-03-15**: 스킬 구조 재설계 (`8c0333a`)
- **2025-03-13**: Park & Kim (2025) 연구 통합 (`ad7e4b6`, `d4342ab`)
- **2025-03-05**: 존대법 검증 로직 추가 (`12cc0ff`)
- **2025-03-01**: 존대법 예제 및 가이드 추가 (`b8dabdb`)
- **2025-02-28**: 스피치 레벨 가드 기능 추가 (`f9ee3d2`)
- **2025-02-25**: 에세이/학술 가이드 완성 (`ebb106f`)
- **2025-02-20**: SKILL.md 파일 구조 정리 (`beb3bf8`)

## 🎯 프로젝트 상태

- **안정성**: ✅ 프로덕션 준비 완료
- **커버리지**: 한국어 에세이/블로그, 학술/보고서 문체
- **검증**: 2개 주요 연구(KatFishNet, Park & Kim 2025) 기반
- **사용성**: Claude Skills API를 통한 직관적 인터페이스
