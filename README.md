MirAI School of Technology - Virtual Summer Internship 2026

Assignment 1

The Identity Echo Interface

A simple interactive web application built using Streamlit as part of the **MirAI School of Technology – Virtual Summer Internship 2026 (AI Builder Track)**.

##  Project Overview

The Identity Echo Interface collects a user's name and message, validates the input, and displays a personalized response. It also includes an optional token Cost Estimator that approximates the number of AI tokens consumed based on the message length.

## Features

-  User-friendly Streamlit interface
-  Name input field
-  Message input field
-  "Transmit" button to trigger processing
-  Error message if the Name field is empty
-  Warning message if the Message field is empty
-  Personalized success message using Python f-strings
-  Token Cost Estimator (1 token ≈ 4 characters)

##  Technologies Used

 Python
 Streamlit

##  How It Works

1. Enter your name.
2. Enter your message.
3. Click the Transmit button.
4. The application validates the inputs.
5. If both fields are valid:
   - Displays a personalized success message.
   - Calculates the message length.
   - Estimates the number of AI tokens required.  

Assignment 2

#  AI Multiverse

An interactive AI chatbot built using **Python**, **Streamlit**, and the **Groq API**. This application allows users to chat with multiple AI personalities, each responding with its own unique style and behavior.

## Features
## ✨ Features

-  Multiple AI Personalities
-  Real-time Chat
-  Chat History
-  Secure API Integration
-  Powered by Gemini
-  Responsive Design
-  Robust Error Handling

## 🛠️ Tech Stack

- Python 3.13
- Streamlit
- Groq API
- python-dotenv

  Assignment 3

  IAI Multiverse Chat Studio

A Streamlit chatbot that lets you talk to different AI personas — each with
its own personality, tone, and behavior guidelines — in your choice of
language. Built on the Groq API and powered by Streamlit's session_state
"Memory Vault" so conversations persist across reruns.


✨ Features


Stateful memory — the full conversation survives every Streamlit rerun
(sending a message, changing the sidebar, etc.) instead of resetting.
Persona system — pick from 8 built-in personalities (The Sage, The
Rebel, The Comedian, The Poet, The Professor, The Pirate, The Therapist,
The Engineer), each with its own system prompt.
Multi-language responses — choose the language the AI should reply in.
Model picker — switch between Groq-hosted models from the sidebar.
Prompt transparency — an expander shows the exact system instruction
sent to the model, for debugging.

🧠 How the Memory Vault works

Streamlit reruns the entire script top-to-bottom on every interaction. To keep
the conversation from vanishing on each rerun, the app stores it in
st.session_state.messages — a list of {"role": ..., "content": ...}
dictionaries that survives reruns for the life of the browser session.

🧰 Tech Stack

Frontend / UI
Streamlit — chat interface and input box
Backend / AI
Groq API — generates chat responses, via the groq Python SDK
Model: openai/gpt-oss-120b
Language & core libraries
streamlit — web app framework
groq — official Groq Python SDK
python-dotenv — loads GROQ_API_KEY from .env
State management
st.session_state — Streamlit's built-in in-memory store, used as the Memory Vault to persist chat history across reruns
No database, no backend server framework — Streamlit + Groq is the whole stack.







GitHub: https://github.com/gaurav-prashant

