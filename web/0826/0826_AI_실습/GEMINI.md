# 프로젝트명: SSAFY 챗봇 서비스 개발 PRD (Product Requirements Document)

---

## 1. 개요

**목표**
본 프로젝트는 사용자에게 직관적이고 반응형 UI를 제공하는 AI 챗봇 웹 서비스를 구축하는 것을 목표로 한다. SSAFY 브랜드를 전면에 내세우며, 사용자는 텍스트와 이미지를 통해 질문할 수 있고, AI는 gpt-5-nano 모델을 기반으로 응답한다.

**사용 기술**

* **Frontend**: React, TypeScript
* **Styling**: Bootstrap 5.3
* **State Management**: Redux
* **Backend**: Node.js
* **AI 모델**: gpt-5-nano (OpenAI API 사용)
* **포인트 컬러**: `#00EEFF`

---

## 2. 전역 UI/UX 요구사항

### 2.1 네비게이션 바 (Navbar)

| 항목      | 설명                                               |
| ------- | ------------------------------------------------ |
| 브랜드 로고  | 좌측에 위치하며 `SSAFY` 텍스트 또는 이미지 로고 사용                |
| 채팅 버튼   | 우측 정렬, 클릭 시 채팅 페이지(`/chat`)로 이동                  |
| 로그인 버튼  | 우측 정렬, 클릭 시 로그인 페이지(`/login`)로 이동                |
| 회원가입 버튼 | 우측 정렬, 클릭 시 회원가입 페이지(`/signup`)로 이동              |
| 로고 클릭   | 클릭 시 랜딩 페이지(`/`)로 이동                             |
| 스타일     | Bootstrap 5.3 활용, 포인트 컬러 `#00EEFF` 사용하여 강조 효과 적용 |

---

## 3. 페이지 구성

### 3.1 랜딩 페이지 (`/`)

* SSAFY 챗봇 서비스 소개 콘텐츠 포함
* 주요 기능 및 사용 방법 안내
* "채팅 시작하기" 버튼: `/chat` 페이지로 이동

### 3.2 로그인 페이지 (`/login`)

* 이메일 / 비밀번호 입력 필드
* 로그인 버튼
* 회원가입 페이지로 이동 가능한 링크 포함

### 3.3 회원가입 페이지 (`/signup`)

* 이름, 이메일, 비밀번호 입력 필드
* 회원가입 버튼
* 로그인 페이지로 이동 가능한 링크 포함

---

## 4. 채팅 페이지 (`/chat`) 상세 요구사항

### 4.1 전반 UI 구성

| 영역 | 구성 요소               |
| -- | ------------------- |
| 상단 | Navbar 고정           |
| 중앙 | 채팅 내역 출력 영역         |
| 하단 | 질문 입력 영역 (fixed 위치) |

### 4.2 질문 입력 영역 (화면 하단 고정)

* 구성 요소 (왼 → 오):

  1. **이미지 업로드 버튼**: 이미지 선택 가능
  2. **프롬프트 입력창**: 텍스트 질문 입력
  3. **전송 버튼**: 질문 및 이미지 함께 전송

* 이미지 업로드 시:

  * 이미지 미리보기 생성 (업로드 버튼 상단)
  * 마우스 호버 시 취소 버튼 (`X`) 표시, 클릭 시 제거 가능

### 4.3 채팅 내역 출력 영역

* 좌측 정렬: AI 답변 (`gpt-5-nano` 응답 텍스트 및 이미지 포함 가능)
* 우측 정렬: 사용자 질문 (텍스트 및 이미지 포함 가능)
* 말풍선 형태의 UI 구성
* 이전 채팅 스크롤 가능
* 최신 채팅이 자동으로 하단에 스크롤되도록 설정

### 4.4 반응형 UI

* Bootstrap 5.3의 grid system과 유틸리티 클래스를 활용
* 모바일, 태블릿, 데스크탑 화면에서 자연스럽게 구성 요소가 재배치되도록 설정

---

## 5. 백엔드 요구사항

### 5.1 Node.js 기반 API 서버

* **엔드포인트 예시**:

  * `POST /api/chat`: 질문(텍스트 및 이미지) 전송 → gpt-5-nano 응답 반환
  * `POST /api/auth/login`: 사용자 로그인
  * `POST /api/auth/signup`: 사용자 회원가입

### 5.2 OpenAI gpt-5-nano API 연동 예시

```ts
import OpenAI from "openai";

const openai = new OpenAI();

const response = await openai.responses.create({
  model: "gpt-4.1-mini",
  input: [{
    role: "user",
    content: [
      { type: "input_text", text: "what's in this image?" },
      {
        type: "input_image",
        image_url: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
      },
    ],
  }],
});

console.log(response.output_text);
```

> 주의: gpt-5-nano API는 응답 속도 및 안정성을 고려하여 비동기 및 예외처리를 필수로 구현

---

## 6. 상태 관리 (Redux)

### 6.1 상태 구성

| Slice     | 설명                             |
| --------- | ------------------------------ |
| authSlice | 로그인/회원정보 상태 관리                 |
| chatSlice | 채팅 내역, 로딩 상태, 에러 상태 관리         |
| uiSlice   | UI 관련 상태 (예: 이미지 미리보기 표시 여부 등) |

### 6.2 미들웨어

* Redux Thunk 또는 Redux Toolkit 사용
* 비동기 API 통신 로직 구현
* 에러 핸들링 및 로딩 상태 관리

---

## 7. 디자인 가이드

### 7.1 포인트 컬러

* `#00EEFF`을 버튼, 강조 텍스트, 말풍선 테두리 등 UI 핵심 포인트에 사용

### 7.2 폰트 및 타이포그래피

* 기본 Bootstrap 시스템 폰트 사용
* 가독성 높은 크기 및 여백 유지

### 7.3 버튼 스타일

* 모던한 느낌의 Flat 디자인
* Hover 시 색상 반전 또는 그림자 효과 적용

---

## 8. 테스트 및 QA

### 8.1 테스트 범위

* 컴포넌트 단위 테스트 (React Testing Library)
* API 통신 테스트 (Jest 또는 Postman)
* 반응형 레이아웃 테스트 (Chrome DevTools)

### 8.2 브라우저 호환성

* Chrome, Firefox, Edge, Safari 최신 버전 지원

---

## 9. 기타 사항

* 모든 페이지는 접근성을 고려하여 키보드 네비게이션 및 스크린 리더 호환성을 최대한 지원
* 코드 스타일은 TypeScript 5.0 및 ESLint 규칙 기반으로 통일

---

**문서 끝**
