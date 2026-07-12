import streamlit as st
from dotenv import load_dotenv
from groq import Groq
import os

# Load API Key
load_dotenv(override=True)
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("❌ GROQ_API_KEY not found in .env file")
    st.stop()

# Initialize Groq client
client = Groq(api_key=api_key)

# Page Config
st.set_page_config(
    page_title="🌍 AI Multiverse",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 AI Multiverse")
st.caption("Talk with different AI Personalities powered by Groq!")

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
                "llama-3.3-70b-versatile",
                "llama-3.1-8b-instant",
            ]

            answer = None

            for model_name in models:
                try:
                    chat_completion = client.chat.completions.create(
                        model=model_name,
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": prompt}
                        ],
                    )
                    answer = chat_completion.choices[0].message.content
                    break
                except Exception as e:
                    error = str(e)
                    if "429" in error or "rate_limit" in error:
                        continue
                    elif "401" in error or "unauthorized" in error:
                        answer = "❌ Invalid Groq API Key."
                        break
                    else:
                        answer = f"⚠️ Groq API Error: {error}"
                        break

            if answer is None:
                answer = "⚠️ All Groq models are currently unavailable. Please try again later."

        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )