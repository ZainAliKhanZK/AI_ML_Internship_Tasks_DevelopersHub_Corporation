# 🩺 Health Query Chatbot — Streamlit Version

An interactive web-based chatbot UI for the Health Query Chatbot, built with **Streamlit**. Provides a friendly chat interface where users can ask general health questions and get safe, LLM-generated responses.

## 🌐 Live Demo

👉 **[Try it here](https://myaidoctor.streamlit.app/)**

## 🛠️ Tools & Model

- **Framework:** Streamlit
- **LLM:** `moonshotai/Kimi-K2-Instruct-0905` via Hugging Face Router
- **Client:** OpenAI-compatible Python client (`openai`)

## ✨ Features

- Clean, custom-styled chat interface (custom CSS)
- Sidebar for app info/settings
- Persistent chat history within the session
- Error handling for failed API calls

## 🚀 Getting Started

### Install dependencies
```bash
pip install streamlit openai python-dotenv
```

### Set up your API key
Create a `.env` file in this folder:

HF=your_api_key_here

### Run the app
```bash
streamlit run app.py
```
App will open in your browser at `http://localhost:8501`

## 💬 Example Queries

- "What causes a sore throat?"
- "Is paracetamol safe for children?"

## 🛡️ Safety Note

The system prompt instructs the model to avoid harmful medical advice and keep responses clear. This is for educational purposes only and not a substitute for professional medical consultation.
