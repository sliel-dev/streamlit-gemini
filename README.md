## 💬 Gemini 챗봇 (Streamlit + Google Gemini API)

이 프로젝트는 **Google Gemini API**를 활용한 간단한 **대화형 챗봇 웹앱**입니다.
Streamlit을 사용해 직관적인 UI로 구성되어 있으며, 사용자가 질문을 입력하면 Gemini 모델이 자연스럽게 답변합니다.

---

### 🧠 주요 기능

* ✅ **Google Gemini API 연동** — `gemini-2.5-flash` 모델 기반
* 💬 **대화형 UI** — Streamlit의 `st.chat_message()`와 `st.chat_input()` 사용
* 🧾 **대화 내역 유지** — 세션 상태(`st.session_state`)를 활용
* ⚡ **실시간 응답 표시** — 로딩 스피너 및 대화창 출력

---

### 🖥️ 실행 화면 예시

| 사용자 입력         | 챗봇 응답                       |
| -------------- | --------------------------- |
| 한국의 수도는 어디인가요? | 한국의 수도는 서울입니다 🇰🇷          |
| 서울의 명소를 추천해줘   | 경복궁, 남산타워, 홍대, 한강공원 등이 있어요! |

---

### 📦 설치 및 실행 방법

#### 1️⃣ 저장소 클론

```bash
git clone https://github.com/yourusername/gemini-chatbot.git
cd gemini-chatbot
```

#### 2️⃣ 필요한 패키지 설치

```bash
pip install -r requirements.txt
```

#### 3️⃣ Streamlit Secrets 설정

`.streamlit/secrets.toml` 파일을 생성하고 아래 내용을 추가하세요 👇

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

> 🔑 API 키는 [Google AI Studio](https://aistudio.google.com/)에서 발급받을 수 있습니다.

#### 4️⃣ 앱 실행

```bash
streamlit run app.py
```

#### 5️⃣ 웹브라우저에서 확인

기본적으로 브라우저에서 자동 실행되며, 주소는 다음과 같습니다:
👉 [http://localhost:8501](http://localhost:8501)

---

### 📁 파일 구조

```
gemini-chatbot/
├── app.py                     # 메인 Streamlit 앱
├── requirements.txt           # 필요 패키지 목록
└── .streamlit/
    └── secrets.toml           # Gemini API 키 저장
```

---

### 🧰 requirements.txt 예시

```txt
streamlit
google-genai
```

---

### ⚙️ 시스템 프롬프트 (옵션)

Gemini의 응답 톤이나 역할을 조정하고 싶다면,
`generate_content()` 호출 부분을 아래처럼 수정하세요 👇

```python
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        {"role": "system", "content": "당신은 친절하고 유머러스한 한국어 챗봇입니다."},
        {"role": "user", "content": prompt},
    ],
)
```

---

### 🧑‍💻 개발자 참고

* Python 3.9 이상 권장
* Streamlit 1.37 이상 사용 시 호환성 좋음
* API 사용량에 따라 과금이 발생할 수 있으므로 Google Cloud 콘솔에서 확인하세요.

---

### 📜 라이선스

이 프로젝트는 **MIT License**를 따릅니다.
자유롭게 수정 및 배포할 수 있습니다.