# Liftoff Korean Translation

`Liftoff` 게임 텍스트를 한국어로 번역하고 관리하기 위한 저장소입니다.
이 저장소의 핵심 작업 대상은 `TranslationSpreadsheet.csv`이며, 번역 작업은 이 파일을 기준으로 진행합니다.

## 이 저장소의 목적

- 대상: `Liftoff` 인게임 텍스트, UI 문자열, 튜토리얼, 안내 문구
- 형식: CSV 스프레드시트
- 현재 포함 파일: `TranslationSpreadsheet.csv`
- 작업 목표: CSV 형식을 유지하면서 영어 원문을 자연스럽고 일관된 한국어로 현지화

이 저장소는 코드 빌드 프로젝트가 아니라 번역 데이터 관리 저장소에 가깝습니다.
따라서 가장 중요한 검수 포인트는 실행 방법보다 다음 세 가지입니다.

- 문자열 정확성
- 용어 일관성
- CSV 형식 보존

## 파일 구조

### `TranslationSpreadsheet.csv`

기본 구조는 아래와 같습니다.

```csv
Keys,Text
Language,English
Language Code,en
Author,LuGus Studios
```

그 아래 행부터는 실제 문자열 리소스가 `키,텍스트` 형식으로 저장됩니다.

예시:

```csv
tutorial.description.cornering,Here you will learn everything about making a good and smooth turn.
workbench.pick,Pick
```

## 번역 작업 가이드

번역할 때는 아래 규칙을 기본 원칙으로 삼습니다.

1. `Keys` 열은 절대 수정하지 않습니다.
2. 번역은 `Text` 값만 변경합니다.
3. `{0}`, `{1}` 같은 플레이스홀더는 그대로 유지합니다.
4. `<b>`, `<color=...>` 같은 태그는 삭제하거나 깨뜨리지 않습니다.
5. `Text` 값은 CSV 형식이 깨지지 않도록 기본적으로 따옴표로 감싸 적는 것을 권장합니다.
6. 반복되는 용어는 가능한 한 하나의 기준 번역으로 통일합니다.
7. 버튼 라벨, 메뉴명, 튜토리얼 제목처럼 짧은 문자열은 UI 맥락에 맞게 짧고 직관적으로 번역합니다.
8. 설명문, 튜토리얼 대사, 안내 메시지는 문장 흐름이 자연스러운 한국어가 되도록 다듬습니다.

## 권장 번역 원칙

### 1. 드론 문맥을 우선합니다

사전적 직역보다 FPV 드론 문맥에서 자연스러운 표현을 우선합니다.

- `controller`: 상황에 따라 `조종기`, `컨트롤러`
- `flight controller`: `비행 컨트롤러`
- `track`: 상황에 따라 `트랙`, `코스`
- `race`: `레이스`
- `freestyle`: `프리스타일`
- `workbench`: 문맥에 따라 `워크벤치` 또는 `정비/설정 화면`에 가까운 의미로 해석

또한 `TranslationSpreadsheet.csv`의 `Text` 열을 보면 아래 드론 핵심 용어가 반복적으로 등장합니다.
이런 조작축, 비행 모드, FPV 기능명은 번역하지 않고 원어 그대로 유지하는 것을 권장합니다.

- 원어 유지 권장 용어: `FPV`, `ACRO`, `LEVEL`, `yaw`, `roll`, `pitch`, `throttle`, `arm`, `disarm`, `turtle mode`, `launch control`, `line-of-sight`

모든 용어를 한 번에 완벽히 고정하기보다, 비슷한 키를 함께 보면서 일관성을 맞추는 방식이 안전합니다.

### 2. 튜토리얼은 "가르치는 말투"로 번역합니다

튜토리얼 문자열은 플레이어에게 조작법을 설명하는 성격이 강합니다.
딱딱한 직역보다, 실제 게임 내 안내 문구처럼 자연스럽고 이해하기 쉬운 문장을 목표로 합니다.

예시:

- 직역투: `여기서 당신은 좋은 부드러운 회전을 만드는 모든 것을 배우게 됩니다.`
- 권장 톤: `여기서는 부드럽고 안정적으로 회전하는 방법을 배웁니다.`

### 3. UI 문구는 짧고 단정하게 유지합니다

버튼, 탭, 메뉴 항목은 길어지면 사용성이 떨어집니다.
가능하면 짧고 즉시 이해되는 표현을 사용합니다.

### 4. 서비스 문구는 명확성이 우선입니다

로그인, 계정, 멀티플레이, 신고, 네트워크 오류 메시지는 문학적으로 번역하기보다 의미 전달이 분명해야 합니다.

## 권장 작업 흐름

1. 작업 범위를 정합니다.
2. 비슷한 키를 묶어서 먼저 읽고, 용어를 대략 통일합니다.
3. `Text` 열만 한국어로 번역합니다.
4. 플레이스홀더, 태그, 문장부호, 줄바꿈 유지 여부를 검수합니다.
5. 번역한 구간을 다시 읽으며 말투와 용어 일관성을 점검합니다.
6. 번역 완료 후 상단 메타데이터를 실제 번역 상태에 맞게 갱신합니다.

예를 들어 한국어 버전으로 전환할 때는 다음 항목을 점검할 수 있습니다.

- `Language` -> `Korean`
- `Language Code` -> `ko`
- `Author` -> `lkoiescg2031`

## 빠른 검수 체크리스트

번역을 저장하거나 커밋하기 전에 아래 항목을 확인하면 좋습니다.

- `Keys` 열이 바뀌지 않았는가
- `{0}`, `{1}` 등의 플레이스홀더가 유지되었는가
- HTML/리치 텍스트 태그가 깨지지 않았는가
- 쉼표, 따옴표, 줄바꿈 때문에 CSV 형식이 망가지지 않았는가
- 같은 기능/화면에서 같은 용어를 일관되게 썼는가
- 튜토리얼 문장이 실제 안내 문구처럼 자연스러운가
- 오류/계정/네트워크 문구가 모호하지 않은가

## Git 관리

번역 작업은 의미 있는 단위로 커밋해 변경 이력을 관리하는 것을 권장합니다.

권장 커밋 예시:

- `Add initial Korean translation base`
- `Translate tutorial strings`
- `Polish workbench and UI text`
- `Normalize multiplayer terminology`

## 참고 자료

아래 공식 자료를 바탕으로 게임 성격을 요약했습니다.

- 공식 제품 소개: [Liftoff: FPV Drone Racing](https://www.liftoff-game.com/liftoff-fpv-drone-racing)
- 공식 홈페이지: [Liftoff](https://www.liftoff-game.com/)
- 스팀 상점 페이지: [Liftoff: FPV Drone Racing on Steam](https://store.steampowered.com/app/410340/Liftoff_FPV_Drone_Racing/)
