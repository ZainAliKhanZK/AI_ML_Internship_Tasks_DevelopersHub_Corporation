# 🩺 Health Query Chatbot — FastAPI Version

A simple REST API for the Health Query Chatbot, built with **FastAPI**. Sends user messages to an LLM via Hugging Face and returns a safe, friendly health-related response through a single `/chat` endpoint.

## 🛠️ Tools & Model

- **Framework:** FastAPI
- **LLM:** `moonshotai/Kimi-K2-Instruct-0905` via Hugging Face Router
- **Client:** OpenAI-compatible Python client (`openai`)
- **Validation:** Pydantic

## 🚀 Getting Started

### Install dependencies
```bash
pip install fastapi uvicorn openai python-dotenv
```

### Set up your API key
Create a `.env` file in this folder:

HF=your_api_key_here

### Run the server
```bash
uvicorn main:app --reload
```
API available at `http://127.0.0.1:8000`

## 📡 API Usage

**Endpoint:** `POST /chat`

**Request:**
```json
{
  "message": "What causes a sore throat?"
}
```

**Response:**
```json
{
  "response": "A sore throat is commonly caused by..."
}
```

**Example with curl:**
```bash
curl -X POST "http://127.0.0.1:8000/chat" \
-H "Content-Type: application/json" \
-d '{"message": "Is paracetamol safe for children?"}'
```

Interactive docs available at `http://127.0.0.1:8000/docs`

## 🛡️ Safety Note

The system prompt instructs the model to avoid harmful medical advice and keep responses clear. This is for educational purposes only and not a substitute for professional medical consultation.
