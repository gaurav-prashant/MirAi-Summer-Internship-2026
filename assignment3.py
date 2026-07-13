import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq, APIError, RateLimitError, AuthenticationError
from personalities import PERSONALITIES
from prompts import LANGUAGES, build_personality_prompt
from utils import load_style, render_sidebar

# Load environment variables from .env
load_dotenv()

st.set_page_config(
    page_title="AI Multiverse Chat Studio",
    page_icon="🤖",
    layout="centered",
)

# Load premium CSS styling
load_style("style.css")

# Main Title (using custom CSS gradient title)
st.markdown("<h1 class='app-title'>🤖 AI Multiverse Chat Studio</h1>", unsafe_allow_html=True)
st.write("Unleash the multiverse of personas. Configure your settings, enter a query, and explore tailored responses.")

# Retrieve the API key
api_key = os.getenv("GROQ_API_KEY")

# Check if the API key is missing or set to placeholder
is_key_missing = (not api_key) or (api_key.strip() in ("", "your_groq_api_key_here"))

if is_key_missing:
    # Render a premium, styled warning container with instructions
    st.markdown(
        "<div class='setup-container'>"
        "<div class='setup-title'>⚠️ Workspace Action Required: Configure API Key</div>"
        "<p>To start using the Multiverse Chat Studio, you need to configure your Groq API Key. "
        "Please complete the following steps:</p>"
        "<ol>"
        "<li>Open the <b>.env</b> file located in your project root folder.</li>"
        "<li style='margin-top: 10px;'>Replace <code>your_groq_api_key_here</code> with your actual key from "
        "<a href='https://console.groq.com/keys' target='_blank' style='color:#38bdf8; font-weight:600;'>the Groq Console</a>.</li>"
        "<li style='margin-top: 10px;'>Save the file. Streamlit will automatically detect the changes and reload the studio dashboard.</li>"
        "</ol>"
        "</div>",
        unsafe_allow_html=True
    )

    st.info("💡 A template `.env` file has been created in your project workspace for your convenience.")

else:
    # Render sidebar and extract selected persona configurations
    personality_name, personality_description, personality_behavior, language = render_sidebar(
        PERSONALITIES, LANGUAGES
    )

    # Task 1: Initialize the Memory Vault
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Task 2: Render the Chat History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Task 3: Upgrade the Input UI
    if user_message := st.chat_input("Say something..."):
        # Display the user message on the screen immediately
        with st.chat_message("user"):
            st.markdown(user_message)

        # Task 4: Save User Message to Memory
        st.session_state.messages.append({"role": "user", "content": user_message})

        # Construct the system instruction for the current personality
        system_instruction = build_personality_prompt(
            personality_name, personality_description, personality_behavior, language
        )


        with st.spinner("🌌 Channeling the Multiverse..."):
            try:
                # Initialize the Groq client
                client = Groq(api_key=api_key)

                # Convert session state messages to Groq/OpenAI chat format,
                # prefixed with the persona's system instruction
                chat_messages = [{"role": "system", "content": system_instruction}]
                for msg in st.session_state.messages:
                    chat_messages.append({"role": msg["role"], "content": msg["content"]})

                # Generate the response
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=chat_messages,
                    temperature=1.0,
                )
                reply_text = response.choices[0].message.content

                # Display assistant response
                with st.chat_message("assistant"):
                    st.markdown(reply_text)

                # Save assistant response to Memory
                st.session_state.messages.append({"role": "assistant", "content": reply_text})

            except AuthenticationError:
                st.error("Groq API Error: your API key was rejected. Double-check it in your .env file.")
            except RateLimitError:
                st.error("Groq API Error: rate limit reached. Wait a moment and try again.")
            except APIError as e:
                st.error(f"Groq API Error: {e}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {str(e)}")