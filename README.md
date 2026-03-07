# Humanizer KR: 한국어 AI 작성 패턴 제거 도구

LLM이 만든 한국어 문장에서 AI의 흔적을 감지하고 제거하여 자연스러운 인간의 문체로 변환하는 스킬입니다.

## 소개

**Humanizer KR**은 한국어 텍스트에 특화된 AI 생성 문장 패턴 탐지 및 제거 도구입니다. 쉼표 남용, 명사 중심 문구, AI 상투어, 공식적인 서식 등 한국어에서 나타나는 LLM 특유의 언어적 신호를 식별하고 인간다운 표현으로 재작성합니다.

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
  - 의존명사/보조용언 띄어쓰기
  - 개성 부재 (에세이 스타일)
  - 챗봇 커뮤니케이션 아티팩트

- **문체 보존**: 한국어의 다양한 존대법(합쇼체, 해요체, 해체) 유지

## 폴더 구조

```text
.
├── README.md                     # 이 파일
├── humanizer-kr/                 # 한국어 버전
│   ├── SKILL.md                  # 상세 스킬 정의 및 처리 규칙
│   └── resources/
│       ├── patterns-kr.md        # KatFishNet 연구 데이터 및 상세 참고 자료
│       ├── essay-guide.md        # 에세이/블로그 스타일 처리 가이드
│       └── academic-guide.md     # 학술/보고서 스타일 처리 가이드
├── references/                   # 참고 문서 및 자료
│   ├── SKILL.md                  # 영어 버전 스킬 (원본 아이디어)
│   └── KatFishNet_Detecting_LLM-Generated_Korean_Text.md  # 논문
└── ...
```

### 주요 파일 설명

- **`humanizer-kr/SKILL.md`**: 10가지 AI 패턴의 정의, 감지 신호, 스타일 판단 기준, 처리 단계 정의
- **`humanizer-kr/resources/essay-guide.md`**: 에세이/블로그 스타일의 각 패턴별 상세 처리 규칙 및 Before/After 예제
- **`humanizer-kr/resources/academic-guide.md`**: 학술/보고서 스타일의 각 패턴별 상세 처리 규칙 및 Before/After 예제
- **`humanizer-kr/resources/patterns-kr.md`**: KatFishNet 논문의 핵심 수치 데이터, 쉼표 제거/유지 판단 기준, 명사구↔동사절 변환 패턴표

## 연구 기반

### 영어 버전 참고

**[SKILL.md](references/SKILL.md)**는 이 프로젝트의 아이디어 기원입니다. 영어 텍스트에서 AI 패턴을 제거하는 원본 스킬로, 한국어 버전 개발의 이론적 토대가 되었습니다.

### 주요 논문 두 편

#### 1. KatFishNet (2024) — 쉼표 및 띄어쓰기 패턴

**[KatFishNet: Detecting LLM-Generated Korean Text through Linguistic Feature Analysis](references/KatFishNet_Detecting_LLM-Generated_Korean_Text.md)**
*Shinwoo Park, Shubin Kim, Do-Kyung Kim, Yo-Sub Han* (Yonsei University, 2024)

한국어 텍스트에서 LLM 생성 신호를 식별하기 위한 핵심 연구:

- 에세이 장르에서 인간은 쉼표 포함 26.31%, LLM은 61.03% (2.3배 차이)
- 품사 다양성, 띄어쓰기 규칙성, 세그먼트 길이 등 정량적 분석
- 한국어만의 독특한 특성(유연한 띄어쓰기 규칙, 풍부한 형태소 체계, 쉼표 사용 빈도)

[GitHub: katfishnet](https://github.com/Shinwoo-Park/katfishnet)

#### 2. Park & Kim (2025) — 어휘 다양성, 접속사 유형, 개조식 문장

**생성형 AI 텍스트와 인간 텍스트의 내용 및 문체 비교 연구**
*박종향·김은영* (한성대학교, 동국대학교, 2025)

동일 강좌에서 AI 비활용 과제(2021년, 20편) vs AI 활용 과제(2025년, 49편)를 텍스트마이닝으로 비교 분석:

**주요 발견**:
- **문장 길이**: 인간 54.20글자/문장 vs AI 48.69글자/문장 (p<.001)
- **어휘 다양성**: 인간의 TTR 0.518 vs AI 0.427 (특히 동사 0.545→0.461, 형용사 0.525→0.429, 부사 0.602→0.468)
- **접속사 유형 차이**:
  - AI는 예시·강조형(예를 들어, 특히, 예컨대) 과다 사용
  - 인간은 조건형(한다면, ~라면) 사용 → AI에서는 거의 부재
- **개조식 문장**: AI는 서술형 대신 단문 나열·목차 세분화(Ⅰ→1→1)→(1)→①) 경향
- **사고 획일화**: AI 활용 글에서 학생들 간 구조와 문체 유사성 증가

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

스킬의 구체적인 작업 절차(패턴 감지, 재작성, 검증)는 **[humanizer-kr/SKILL.md](humanizer-kr/SKILL.md)**를 참고하세요.

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

## 참고 자료

- **[humanizer-kr/SKILL.md](humanizer-kr/SKILL.md)** - 10가지 패턴 정의, 감지 신호, 스타일 판단 기준 (마스터 가이드, KatFishNet + Park & Kim 최신 연구 반영)
- **[humanizer-kr/resources/essay-guide.md](humanizer-kr/resources/essay-guide.md)** - 에세이/블로그 스타일별 처리 규칙 및 예제 (개조식 변환, 접속사 유형 다양화, 어휘 반복 처리)
- **[humanizer-kr/resources/academic-guide.md](humanizer-kr/resources/academic-guide.md)** - 학술/보고서 스타일별 처리 규칙 및 예제 (개조식 적정 수준, 접속사 유형 분포)
- **[humanizer-kr/resources/patterns-kr.md](humanizer-kr/resources/patterns-kr.md)** - KatFishNet + Park & Kim 연구 데이터, 동사·형용사 다양화 테이블, 예시·강조형 접속사 처리, 감사 체크리스트 (참고용)

---

*Humanizer KR은 영어 버전 스킬([references/SKILL.md](references/SKILL.md))을 바탕으로, 두 가지 주요 연구를 통합하여 개발되었습니다:*

1. *Yonsei University의 **KatFishNet (2024)** — 쉼표, 띄어쓰기, 품사 패턴*
2. *한성대학교·동국대학교의 **Park & Kim (2025)** — 어휘 다양성, 접속사 유형, 개조식 문장, 사고 획일화*

*학술/보고서 스타일 규칙과 voice consultation 프로토콜은 추가로 개발되었습니다.*
