import streamlit as st
from google import genai

# 앱 제목
st.set_page_config(page_title="Gemini 챗봇", page_icon="💬", layout="centered")

def main():
    st.title("💬 Gemini 챗봇")

    # Gemini API 클라이언트 설정
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

    # 대화 상태 저장 (Streamlit 세션)
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 기존 대화 표시
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # 사용자 입력창
    if prompt := st.chat_input("질문을 입력하세요..."):
        # 사용자 메시지 추가 및 표시
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Gemini 응답 생성
        with st.chat_message("assistant"):
            with st.spinner("답변 생성 중..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                )
                answer = response.text
                st.markdown(answer)

        # 모델 응답 저장
        st.session_state.messages.append({"role": "assistant", "content": answer})


if __name__ == "__main__":
    main()