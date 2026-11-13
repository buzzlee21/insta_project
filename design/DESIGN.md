
## 버전
 - bootstrap 5.3 (CDN 5.3.3), 아이콘은 Bootstrap Icons 1.11.3

## 참고한 화면

 - 인스타그램 웹버전(ref/ref1.jpeg)
   - 위쪽: 이름이 있는 바 / 아래쪽: 아이콘 탭 메뉴(홈, +, 프로필)
 - 전체 화면 배경 느낌(ref/ref2.jpeg)
   - 따뜻한 크림색 폰 테두리 안에 흰 화면이 있는 모양, 주황 · 청록 포인트

## 색
 - 전체 화면 배경: 따뜻한 크림/베이지 `#ecdcc6` (ref/ref2.jpeg의 폰 테두리 색, `style.css`의 `body`)
 - 흰 칸 양옆에는 은은한 갈색 그림자 `box-shadow: 0 0 24px rgba(120, 80, 30, 0.15)` (`.app-main`)
 - 본문 · 위 메뉴 · 아래 탭바 칸: 흰 배경 + 검정 글씨 (Bootstrap 기본, 다크 모드 안 씀)
 - 탭 아이콘에 마우스를 올리면 주황 `#f28c28` (ref2의 주황 포인트)
 - 포인트 색: Bootstrap 기본 파랑(`btn-primary`)은 로그인 버튼 등 꼭 필요한 곳에만

## 글자
 - 본문: Bootstrap 기본 글꼴 사용
 - `insta` 로고 글씨: 인스타그램 같은 필기체 Google Fonts `Grand Hotel` (`.logo` 클래스, `style.css`)
   - 위 메뉴는 `logo fs-2`, 로그인 · 회원가입 카드는 `logo display-4`

## 간격
 - Bootstrap 간격 클래스 사용 (`px-3`, `py-2`, `py-3`, `gap-2`)
 - 아래 탭바가 내용을 가리지 않게 `body`에 `padding-bottom: 64px`

## 게시물 카드
 - 인스타 피드형 (테두리 상자 없이 글 사이를 선으로 나눔)
 - 순서: 글쓴이 이름 → 사진(카드 폭 가득, 정사각형) → 좋아요 버튼·좋아요 수·댓글 수 → 본문 → 올린 시각·상세 링크

## 사진
 - 본문 안에서 폭을 넘지 않게 `max-width: 100%; height: auto`
 - 목록·상세 사진 모두 카드 폭 가득, 정사각형 (`.feed-photo` + `w-100 rounded`)

## 프로필
 - (아직 안 정함)

## 댓글
 - 카드식: 댓글마다 Bootstrap `card`(테두리 + 둥근 모서리)로 감쌈, 최신 순
 - 카드 안: `이름(굵게) 내용` 한 줄 → 아래에 시각(작은 회색 글씨), 내 댓글이면 오른쪽에 삭제 버튼(`btn-outline-danger btn-sm`)
 - 댓글 입력: `input-group` 안에 입력 칸 + `btn-primary` 등록 버튼 (폼 모양은 아직 안 정해서 Bootstrap 기본)

## 폼
 - 로그인 · 회원가입: 가운데 흰 카드(`card p-4`) 안에 `insta` 로고 글씨(`fs-1 fw-bold`) + 제목
 - 입력 칸: `form-floating`(칸 안에 글자가 떠 있는 모양) + `form-control`, 제출 버튼은 `btn btn-primary w-100`
 - 오류 글자: `alert alert-danger` (빨간 경고 상자)
 - 폼 아래에 서로 이동 링크 (로그인 ↔ 회원가입)
 - 새글 · 수정 폼은 아직 안 정함 (Bootstrap 기본 사용)

## 배치
 - 본문 · 위 메뉴 · 아래 탭바 모두 가운데 정렬, 최대 폭 470px (`.app-width`)
 - 크림색 배경 위에 가운데 흰 칸이 세로로 이어지는 모양 (ref2의 폰 화면처럼)
   - `<nav>`에는 배경을 주지 않고, 안쪽 `div.app-width`에 `bg-white`를 줌 (안 그러면 메뉴가 화면 끝까지 흰색)
   - 본문 `main.app-main`은 `min-height: calc(100vh - 120px)`로 글이 적어도 화면 아래까지 흰 칸 유지
 - 위쪽 메뉴: 왼쪽 `insta` 로고, 오른쪽 사용자 이름 + 로그아웃 (로그인 안 했으면 로그인 · 회원가입 버튼)
 - 아래쪽 탭바: 로그인했으면 홈 · 새글 · 내 프로필 / 안 했으면 홈 · 로그인 · 회원가입

## 쓰지 않는 것
 - 검색 탭 (검색 페이지가 없음)
 - 다크 모드
