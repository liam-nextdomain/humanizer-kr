# Anthropic이 공개한 SKILL.md Body 작성 규칙 5가지

> Author: Tony Lee
> Published: 2026-02-17
> URL: <https://tonylee.im/ko/blog/anthropic-skill-md-body-writing-rules/>
> Reading time: 3 minutes
> Language: ko
> Tags: ai, claude-code, developer-tools, skills, productivity

## Description

Anthropic 공식 문서에 숨어 있던 SKILL.md body 작성 원칙 5가지를 정리했습니다. description과 body의 역할 분리부터 검증 루프까지.

## Content

Skill은 YAML frontmatter 두 줄이면 만들 수 있습니다. 하지만 body를 어떻게 쓰느냐에 따라 결과물 품질이 완전히 갈립니다.

Anthropic 공식 문서와 엔지니어링 블로그를 교차 검증하면서 작동 구조와 body 작성 원칙을 정리했습니다. 직접 만든 Skill이 간헐적으로 로딩에 실패해서 연휴에 아예 처음부터 검증해본 결과입니다.

## Skill 실행 순서를 모르면 body 설계가 엉망이 됩니다

Skill은 프롬프트처럼 대화에 바로 주입되지 않습니다. 시작 시점에 시스템 프롬프트에 올라가는 건 name과 description뿐입니다.

사용자 요청이 description과 맞을 때 Claude가 Bash 도구로 SKILL.md 전문을 읽어 들이고, 그다음 참조 파일이나 스크립트를 필요한 시점에 추가로 불러옵니다. Anthropic 엔지니어링 블로그에서는 이 구조를 '단계별 공개(progressive disclosure)'라고 부릅니다.

- **1단계**: 메타데이터(name + description)만 상시 로딩. Skill 하나당 약 100토큰
- **2단계**: SKILL.md body는 매칭 시에만 맥락 범위에 진입
- **3단계**: scripts와 references 폴더 파일은 실제 참조 시점에 로딩
- 스크립트 실행 시 코드 자체는 맥락에 올라가지 않고 출력값만 소비

이 구조를 이해하지 못하면 body에 불필요한 정보를 넣게 되고, 정작 필요한 정보는 빠뜨리게 됩니다.

## body에 "언제 쓸지"를 적으면 토큰 낭비입니다

많은 사람이 body에 "When to Use This Skill" 섹션을 넣습니다. 직접 만들어보니 완전히 쓸모없었습니다. body는 Skill이 이미 발동된 뒤에 읽히기 때문입니다.

'언제 쓸지'는 description에만 넣어야 합니다. Anthropic 공식 skill-creator 레포에서도 이 점을 명시하고 있습니다.

- description이 유일한 발동 트리거 (body에 적어도 Claude가 참조 안 함)
- description은 최대 1,024자. 3인칭으로 작성해야 발견 정확도가 올라감
- body에 넣을 것은 작업 규칙, 절차, 기대 출력 형식
- "이 Skill은 ~할 때 사용합니다" 같은 문장은 body에서 삭제

## body는 500줄 안에서 끝내고 나머지는 분리합니다

전체 맥락 범위(Context window)는 공공재라는 게 Anthropic 가이드의 첫 문장입니다. Skill이 로딩되면 대화 기록이나 시스템 프롬프트와 토큰을 나눠 사용해야 합니다.

body를 500줄 이하로 유지하고 상세 내용은 별도 파일로 분리하는 것이 공식 권장사항입니다. SKILL.md가 목차 역할을 하고 참조 파일이 각 장이 되는 구조입니다.

- body 500줄 이하 권장 (Anthropic best practices 명시)
- 참조 파일은 SKILL.md에서 한 단계 깊이로만 링크
- 2단계 이상 중첩 참조 시 Claude가 `head -100`으로 일부만 읽을 위험
- 100줄 넘는 참조 파일에는 목차를 맨 위에 넣을 것

## Claude는 이미 똑똑하다는 전제로 써야 합니다

body에 PDF가 뭔지 설명하는 건 토큰 낭비입니다. Anthropic 가이드에서 반복적으로 강조하는 원칙이 있습니다.

> "Claude가 이미 아는 건 적지 마라."

50토큰짜리 간결한 코드 예시가 150토큰짜리 개념 설명보다 성능이 좋습니다. 같은 PDF 추출 작업에서 간결한 body가 장황한 body보다 정확도가 눈에 띄게 높았습니다.

- 모든 문장에 "이 설명이 토큰값을 하는가?"를 자문할 것
- 개념 설명 대신 코드 예시 + 기대 출력 형식으로 작성
- 작업 자유도를 3단계(높음/중간/낮음)로 구분해서 지시 강도 조절
- DB 마이그레이션 같은 작업은 자유도 낮게, 코드 리뷰는 높게

## 검증 루프를 body에 심어야 품질이 올라갑니다

실행 → 검증 → 수정 → 재검증. Anthropic이 제시하는 body 패턴 중 가장 실용적인 부분입니다. 체크리스트를 body에 넣으면 Claude가 단계를 건너뛰는 일이 눈에 띄게 줄어듭니다.

"MUST filter" 같은 강한 표현이 "always filter"보다 준수율이 높다는 점도 공식 가이드에 나와 있습니다.

- 복잡한 작업에는 체크리스트 형식으로 단계를 명시
- 스크립트 검증 → 오류 수정 → 재검증 루프를 body에 포함
- "always" 대신 "MUST"를 쓰면 Claude 준수율이 올라감
- 에러 메시지는 구체적으로 작성해야 Claude가 자동 수정 가능

## 핵심 정리

description은 '언제 쓸지'를 결정하고, body는 '어떻게 할지'를 결정합니다. 이 두 역할을 섞는 순간 Skill은 발동도 안 되고 품질도 떨어집니다.

좋은 Skill은 좋은 온보딩 문서와 같습니다. 읽는 사람이 똑똑하다는 전제에서 시작하는 문서가 가장 강력합니다.

---

Author: Tony Lee | Website: <https://tonylee.im>
For more articles, visit: <https://tonylee.im/ko/blog/>
This content is original and authored by Tony Lee. Please attribute when quoting or referencing.
