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

  🤖 AI Multiverse Chat Studio

A stateful AI chatbot built with **Streamlit** and the **Groq API** as part of the **MirAI School of Technology – Virtual Summer Internship 2026: The "AI Builder" Track**.

This project upgrades the AI Multiverse Chatbot from a stateless application into a **stateful conversational chatbot** using Streamlit's `st.session_state`. The chatbot remembers the complete conversation history during the active session and supports multiple AI personalities and languages.



## ✨ Features

- 💾 Stateful conversation memory using `st.session_state`
- 💬 Native Streamlit chat interface
- 🧠 Remembers previous conversation messages
- 🎭 Multiple AI personalities
- 🌐 Multiple language options
- ⚡ AI responses powered by Groq
- 🤖 Uses the `llama-3.3-70b-versatile` model
- 🎨 Custom CSS styling
- 📱 Interactive Streamlit interface
- 🔄 Chat history remains visible after Streamlit reruns
- 🛡️ API error and rate-limit handling
- 🔐 Secure API key management using `.env`

---

## 🧠 How the Memory Vault Works

### 1. Initialize the Memory

The application checks whether a `messages` list already exists in Streamlit's session state.

```python
if "messages" not in st.session_state:
    st.session_state.messages = []
```

This prevents the conversation history from being reset every time Streamlit reruns the application.

---

### 2. Render Previous Messages

Every stored message is displayed using Streamlit's native chat interface.

```python
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
```

---

### 3. Accept User Input

The application uses `st.chat_input()` instead of the traditional `st.text_input()` and `st.button()` combination.

```python
if user_message := st.chat_input("Say something..."):
```

The `:=` operator is the Python **walrus operator**, which assigns and checks the user input in a single statement.

---

### 4. Save Messages to Memory

The user's message is stored in the session state:

```python
st.session_state.messages.append(
    {"role": "user", "content": user_message}
)
```

The AI response is also stored:

```python
st.session_state.messages.append(
    {"role": "assistant", "content": reply_text}
)
```

This creates a continuous conversation history.


## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Groq API**
- **Llama 3.3 70B**
- **python-dotenv**
- **HTML/CSS**
- **Streamlit Session State**







GitHub: https://github.com/gaurav-prashant

