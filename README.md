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

 # 🤖 AI Multiverse Chat Studio

A stateful AI chatbot built with **Streamlit** and the **Groq API** as part of the **MirAI School of Technology – Virtual Summer Internship 2026: The "AI Builder" Track**.

This project upgrades the AI Multiverse Chatbot from a stateless application into a **stateful conversational chatbot** using Streamlit's `st.session_state`. The chatbot remembers the complete conversation history during the active session and supports multiple AI personalities and languages.

---

## 📌 Assignment

### The Memory Vault (Stateful Chatbot)

The objective of this assignment is to solve the problem of conversation history being lost whenever a Streamlit application reruns.

The application uses:

```python
st.session_state
```

to store and preserve user and assistant messages throughout the conversation.

---

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

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Groq API**
- **Llama 3.3 70B**
- **python-dotenv**
- **HTML/CSS**
- **Streamlit Session State**

---

## 📂 Project Structure

```text
AI-Multiverse-Chat-Studio/
│
├── app.py
├── personalities.py
├── prompts.py
├── utils.py
├── style.css
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

> The `.env` file should never be uploaded to GitHub because it contains your private API key.

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

Move into the project folder:

```bash
cd <your-project-folder>
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file, install the required packages manually:

```bash
pip install streamlit groq python-dotenv
```

---

### 3. Configure the Groq API Key

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_actual_groq_api_key_here
```

Replace:

```text
your_actual_groq_api_key_here
```

with your actual Groq API key.

> ⚠️ Never share or upload your actual API key to GitHub.

---

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your web browser.

---

## 📝 Requirements File

Your `requirements.txt` can contain:

```text
streamlit
groq
python-dotenv
```

---

## 🔒 Recommended `.gitignore`

Create a `.gitignore` file and add:

```text
.env
__pycache__/
*.pyc
.venv/
venv/
```

This prevents your API key and unnecessary Python files from being uploaded to GitHub.

---

## 🎯 Assignment Requirements Completed

| Task | Requirement | Status |
|------|-------------|--------|
| Task 1 | Initialize `st.session_state.messages` | ✅ Completed |
| Task 2 | Render previous chat history | ✅ Completed |
| Task 3 | Replace old input UI with `st.chat_input()` | ✅ Completed |
| Task 4 | Save user messages to memory | ✅ Completed |
| Task 4 | Save assistant responses to memory | ✅ Completed |
| Bonus | Send conversation history to the AI model | ✅ Completed |
| Bonus | Multiple personalities and languages | ✅ Completed |

---

## 🎥 Assignment Demonstration

The screen recording demonstrates:

1. Starting a conversation with the AI chatbot.
2. Sending at least three continuous messages.
3. Displaying all previous user and assistant messages.
4. Demonstrating that the chatbot retains conversation history.
5. Changing the personality or sidebar settings without wiping the visible chat history.

### Example Conversation

```text
User: My name is Prashant.

Assistant: Nice to meet you, Prashant!

User: I am learning AI and Python.

Assistant: That's great! AI and Python are a powerful combination.

User: What is my name and what am I learning?

Assistant: Your name is Prashant, and you are learning AI and Python.
```

---

## 📸 Screenshots

Add your project screenshot inside a folder named `images`:

```text
images/
└── chatbot-screenshot.png
```

Then display it in this README using:

```markdown
![AI Multiverse Chat Studio](images/chatbot-screenshot.png)
```

---

## 🚀 Future Improvements

- Add a clear chat history button
- Add persistent database storage
- Add user authentication
- Add more AI personalities
- Add conversation export functionality
- Add voice input and text-to-speech
- Deploy the application online

---

## 👨‍💻 Author

**Prashant Kumar Gaurav**

- GitHub: `gaurav-prashant`
- Project: AI Multiverse Chat Studio
- Internship: MirAI School of Technology – Virtual Summer Internship 2026
- Track: The "AI Builder" Track

---

## 📜 Acknowledgement

This project was developed as part of the **MirAI School of Technology Virtual Summer Internship 2026 – The "AI Builder" Track**.

The assignment focuses on understanding state management in Streamlit and building a continuous conversational AI experience using `st.session_state`.

---

⭐ If you found this project useful, consider giving the repository a star!






GitHub: https://github.com/gaurav-prashant

