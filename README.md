# Humanizer KR: 한국어 AI 작성 패턴 제거 도구

LLM이 만든 한국어 문장에서 AI의 흔적을 감지하고 제거하여 자연스러운 인간의 문체로 변환하는 스킬입니다.

## 소개

**Humanizer KR**은 한국어 텍스트에 특화된 AI 생성 문장 패턴 탐지 및 제거 도구입니다. 쉼표 남용, 명사 중심 문구, AI 상투어, 공식적인 서식 등 한국어에서 나타나는 LLM 특유의 언어적 신호를 식별하고 인간다운 표현으로 재작성합니다.

## 핵심 특징

- **한국어 특화**: 띄어쓰기, 품사 다양성, 쉼표 패턴 등 한국어만의 특성을 반영
- **스타일 구분**: 에세이/블로그와 학술논문/보고서 스타일을 구분하여 개별 규칙 적용
- **10가지 패턴 감지**:
  - 쉼표 남용 (가장 강력한 식별자)
  - 명사 중심 구조
  - 룰 오브 쓰리 나열
  - 공식적 서식 (서론/결론 템플릿)
  - AI 고빈도 표현
  - 접속사 남용
  - 의존명사/보조용언 띄어쓰기
  - 개성 부재 (에세이 스타일)
  - 챗봇 커뮤니케이션 아티팩트

- **문체 보존**: 한국어의 다양한 존대법(합쇼체, 해요체, 해체) 유지

## 폴더 구조

```text
.
├── README.md                     # 이 파일
├── humanizer-kr/                 # 한국어 버전
│   ├── Skill.md                  # 상세 스킬 정의 및 처리 규칙
│   └── resources/
│       └── patterns-kr.md        # KatFishNet 연구 데이터 및 상세 참고 자료
├── references/                   # 참고 문서 및 자료
│   ├── SKILL.md                  # 영어 버전 스킬 (원본 아이디어)
│   └── KatFishNet_Detecting_LLM-Generated_Korean_Text.md  # 논문
└── ...
```

### 주요 파일 설명

- **`humanizer-kr/Skill.md`**: 10가지 AI 패턴의 정의, 감지 신호, 에세이/학술 스타일별 처리 방법, 구체적 사례 포함
- **`humanizer-kr/resources/patterns-kr.md`**: KatFishNet 논문의 핵심 수치 데이터, 쉼표 제거/유지 판단 기준, 명사구↔동사절 변환 패턴표

## 연구 기반

### 영어 버전 참고

**[SKILL.md](references/SKILL.md)**는 이 프로젝트의 아이디어 기원입니다. 영어 텍스트에서 AI 패턴을 제거하는 원본 스킬로, 한국어 버전 개발의 이론적 토대가 되었습니다.

### 논문 참고

**[KatFishNet: Detecting LLM-Generated Korean Text through Linguistic Feature Analysis](references/KatFishNet_Detecting_LLM-Generated_Korean_Text.md)**
*Shinwoo Park, Shubin Kim, Do-Kyung Kim, Yo-Sub Han* (Yonsei University, 2024)

이 논문은 한국어 텍스트에서 LLM 생성 신호를 식별하기 위한 핵심 연구 결과를 제공합니다:

- 에세이 장르에서 인간은 쉼표 포함 26.31%, LLM은 61.03% (2.3배 차이)
- 품사 다양성, 띄어쓰기 규칙성, 세그먼트 길이 등 정량적 분석
- 한국어만의 독특한 특성(유연한 띄어쓰기 규칙, 풍부한 형태소 체계, 쉼표 사용 빈도)

[GitHub: katfishnet](https://github.com/Shinwoo-Park/katfishnet)

## Claude Skill 등록 및 사용

### 설치 방법

#### 1. Skill 폴더 구성 확인

- `humanizer-kr/` 폴더 구조가 완성되어 있는지 확인
- 필수 파일: `Skill.md`, `resources/patterns-kr.md`

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

스킬의 구체적인 작업 절차(패턴 감지, 재작성, 검증)는 **[humanizer-kr/Skill.md](humanizer-kr/Skill.md)**를 참고하세요.

## 예시

### 에세이 스타일

**원본 (AI 생성):**
> 인공지능 기술은, 현대 사회에서 매우 중요한 역할을 하는 혁신적인 기술로, 다양한 분야에서 효과적으로 활용되고 있습니다.

**최종본:**
> 인공지능은 의료 진단, 교육 콘텐츠, 제조 자동화까지 이미 들어와 있습니다.

### 학술 스타일

**원본 (AI 생성):**
> 본 연구에서는 인공지능 기술의 다양한 측면에 대해 살펴보고자 한다. 인공지능은, 현대 사회에서 매우 중요한 역할을 하며 다양한 분야에서 효과적으로 활용되고 있다.

**최종본:**
> 본 연구는 인공지능 기술의 주요 응용 분야와 사회적 효과를 분석한다. 의료, 교육, 제조 분야 도입 사례를 중심으로 효율성 향상 효과를 정량적으로 평가하였다.

## 참고 자료

- **[humanizer-kr/Skill.md](humanizer-kr/Skill.md)** - 패턴별 처리 규칙 및 예제 (상세 가이드)
- **[humanizer-kr/resources/patterns-kr.md](humanizer-kr/resources/patterns-kr.md)** - KatFishNet 데이터 및 변환 테이블 (참고용)

---

*Humanizer KR은 Yonsei University의 KatFishNet 연구와 Wikipedia의 "Signs of AI writing" 가이드를 기반으로 한국어화하여 개발되었습니다.*
