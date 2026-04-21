# TranslationSpreadsheet.csv 한국어 번역 계획

## 목적

`TranslationSpreadsheet.csv`를 한국어 현지화 파일로 완성하기 위한 작업 계획을 정리한다.
이 문서는 [README.md](/Users/taehongkim/Projects/github/lkoiescg2031/liftoff-korean-translation/README.md)를 기준으로 실제 작업 순서, 검수 기준, 우선순위를 명확히 하는 것을 목표로 한다.

## 작업 대상 요약

- 대상 파일: [TranslationSpreadsheet.csv](/Users/taehongkim/Projects/github/lkoiescg2031/liftoff-korean-translation/TranslationSpreadsheet.csv)
- 총 행 수: 2,764행
- 메타데이터 행 이후 실제 번역 대상 문자열: 약 2,760개
- 현재 메타데이터:
  - `Language,English`
  - `Language Code,en`
  - `Author,LuGus Studios`

## 번역 원칙

- `Keys` 열은 수정하지 않는다.
- `Text` 열만 한국어로 번역한다.
- `{0}`, `{1}` 같은 플레이스홀더는 그대로 유지한다.
- `<b>`, `<color=...>` 등 태그는 손상시키지 않는다.
- CSV 형식이 깨지지 않도록 쉼표, 따옴표, 줄바꿈을 주의한다.
- 드론 조작 및 FPV 문맥을 우선하며, 원문을 기계적으로 직역하지 않는다.
- 반복 용어는 전체 파일에서 일관되게 유지한다.
- 짧은 UI 문구는 간결하게, 튜토리얼/설명 문구는 자연스럽고 가르치는 톤으로 번역한다.

## 용어 기준 초안

작업 시작 전에 아래 기준을 잠정 용어집으로 삼고, 번역 중 충돌이 생기면 이 문서를 갱신한다.

- 원어 유지 권장:
  - `FPV`
  - `ACRO`
  - `LEVEL`
  - `yaw`
  - `roll`
  - `pitch`
  - `throttle`
  - `arm`
  - `disarm`
  - `turtle mode`
  - `launch control`
  - `line-of-sight`
- 문맥 번역 후보:
  - `controller` -> `조종기` 또는 `컨트롤러`
  - `flight controller` -> `비행 컨트롤러`
  - `track` -> `트랙` 또는 `코스`
  - `race` -> `레이스`
  - `workbench` -> `워크벤치`

## 우선순위 제안

CSV를 한 번에 처음부터 끝까지 번역하기보다, 사용 빈도와 맥락 일관성이 높은 묶음부터 처리한다.

1. 튜토리얼 계열
   - `tutorial.*`
   - 이유: 문장형 비중이 높아 톤과 용어 기준을 먼저 잡기 좋다.
2. 공통 UI 및 메뉴 계열
   - `generic.*`
   - `options.*`
   - `pausemenu.*`
   - `ingamemenu.*`
3. 입력/조작 설정 계열
   - `input.*`
   - `inputsetup.*`
4. 핵심 게임 기능 계열
   - `multiplayer.*`
   - `store.*`
   - `trackeditor.*`
   - `raceeditor.*`
   - `droneeditor.*`
5. 나머지 세부 기능 계열
   - `tournaments.*`
   - `playerprogression.*`
   - `loadingscreen.*`
   - 기타 잔여 키

## 작업 단계

### 1. 준비 단계

- CSV 원본을 훑어 주요 접두사별 문자열 성격을 파악한다.
- 반복 용어와 문체 기준을 정리한다.
- 메타데이터 변경 시점은 전체 번역 마무리 직전으로 미룬다.

### 2. 1차 번역

- 우선순위 묶음 단위로 진행한다.
- 한 번에 너무 넓게 번역하지 않고, 주제별로 끊어서 진행한다.
- 문장형 문자열은 자연스러운 한국어로, 버튼/메뉴형 문자열은 짧고 명확하게 번역한다.

### 3. 1차 검수

- 같은 화면/기능에서 용어가 통일되었는지 확인한다.
- `ACRO`, `LEVEL`, `yaw`, `roll` 등 핵심 용어가 의도대로 유지되었는지 확인한다.
- 플레이스홀더와 태그 손상 여부를 확인한다.

### 4. 2차 다듬기

- 어색한 직역 표현을 자연스럽게 다듬는다.
- 튜토리얼 문장을 실제 인게임 안내 문구처럼 읽히도록 조정한다.
- 길이가 지나치게 긴 UI 번역을 줄인다.

### 5. 최종 마감

- 메타데이터를 한국어 번역 상태에 맞게 갱신한다.
- 권장 갱신값:
  - `Language` -> `Korean`
  - `Language Code` -> `ko`
  - `Author` -> `lkoiescg2031`
- 최종 CSV 형식 검사를 진행한다.

## 세부 실행 방식

- 작업 단위는 접두사 또는 기능 묶음 기준으로 나눈다.
- 각 작업 단위마다 아래 순서를 반복한다.
  1. 관련 키를 먼저 모아 읽는다.
  2. 반복 용어를 결정한다.
  3. `Text`만 번역한다.
  4. 바로 재독하며 말투와 길이를 정리한다.
  5. 플레이스홀더/태그/CSV 안전성을 확인한다.

## 검수 체크리스트

- `Keys` 값이 변경되지 않았는가
- 플레이스홀더가 보존되었는가
- 태그가 손상되지 않았는가
- 따옴표, 쉼표, 줄바꿈 때문에 CSV가 깨지지 않았는가
- 같은 기능의 용어가 일관적인가
- 튜토리얼 문장이 설명형 톤으로 자연스러운가
- 오류/계정/네트워크 문구가 명확한가

## 커밋 전략 제안

번역 이력 추적과 검수 편의를 위해 의미 있는 단위로 나누어 커밋한다.

- `Translate tutorial strings`
- `Translate options and generic UI`
- `Translate input setup strings`
- `Translate multiplayer strings`
- `Polish terminology consistency`
- `Finalize Korean metadata`

## 완료 기준

아래 조건을 모두 만족하면 번역 작업을 완료로 본다.

- 번역 대상 전 행의 `Text`가 한국어 기준으로 정리되었다.
- 핵심 FPV 용어 사용 기준이 전체 파일에서 일관된다.
- 메타데이터가 한국어 버전에 맞게 갱신되었다.
- CSV 형식 오류가 없다.
- 최종 검수에서 어색한 직역과 중복 용어가 정리되었다.
