# 💬 Mental Health Support Chatbot — Streamlit Version

An interactive web-based chat interface for the fine-tuned, empathetic mental health support chatbot, built with **Streamlit** and powered by a fine-tuned DistilGPT2 model.

## 🛠️ Model

- **Base Model:** DistilGPT2 (fine-tuned on EmpatheticDialogues)
- **Weights:** Loaded from Hugging Face Hub
- **Interface:** Streamlit web app

## ✨ Features

- Simple, chat-style web interface
- Persistent chat history within the session
- Cleaned, post-processed responses for natural-sounding replies

## 🚀 Getting Started

### Install dependencies
```bash
pip install streamlit transformers torch
```

### Run the app
```bash
streamlit run app.py
```
App will open in your browser at `http://localhost:8501`

## 💬 Example Interaction
You: I've been feeling really stressed lately.

Bot: I'm sorry to hear that you're feeling this way. Stress can be really overwhelming sometimes...

## 🛡️ Safety Note

This chatbot is designed to be gentle and emotionally supportive but is **not a substitute for professional mental health support, therapy, or crisis intervention**. It is intended for educational and demonstration purposes only.
