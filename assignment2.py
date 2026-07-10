import streamlit as st
from google import genai
from dotenv import load_dotenv
import os


# Load API Key

load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ GEMINI_API_KEY not found in .env file")
    st.stop()

client = genai.Client(api_key=api_key)

# Page Config

st.set_page_config(
    page_title="🌍 AI Multiverse",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 AI Multiverse")
st.caption("Talk with different AI Personalities!")

# Sidebar

st.sidebar.title("🎭 Choose a Figure ")

personality = st.sidebar.selectbox(
    "Select Personality",
    [
        "Common Indian Man",
        "Crazy Salman Khan Fan",
        "Little Boy",
        "Motivational Coach",
        "Software Engineer",
        "College Professor",
        "Stand-up Comedian",
        "Entrepreneur",
        "Friendly Teacher",
        "AI Assistant"
    ]
)

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Chat History

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# =============================
# Chat Input
# =============================
prompt = st.chat_input("Type your message...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    system_prompt = f"""
You are {personality}.

Always stay in character.

Rules:
- Never break character.
- Speak naturally.
- Reply according to your personality.
- Keep replies engaging.
- Never mention that you are an AI language model.
"""

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            models = [
                "gemini-flash-latest",
                "gemini-2.5-flash",
                "gemini-2.5-flash-lite",
                "gemini-2.0-flash"
            ]

            answer = None

            for model_name in models:

                try:

                    response = client.models.generate_content(
                        model=model_name,
                        contents=f"{system_prompt}\n\nUser: {prompt}"
                    )

                    answer = response.text
                    break

                except Exception as e:

                    error = str(e)

                    if "429" in error:
                        answer = " Quota exceeded. Please wait or use another API key."
                        break

                    elif "401" in error or "API_KEY_INVALID" in error:
                        answer = " Invalid API Key."
                        break

                    elif "503" in error:
                        continue

                    elif "404" in error:
                        continue

                    else:
                        answer = error
                        break

            if answer is None:
                answer = "⚠️ All Gemini models are currently unavailable. Please try again later."

        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )