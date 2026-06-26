# 🩺 General Health Query Chatbot (Prompt Engineering Based)

A conversational chatbot that answers general health-related questions using a Large Language Model (LLM), built with a focus on prompt engineering and safe, responsible response handling.

## 🎯 Objective

To build a chatbot that can answer general health-related queries in a friendly, clear, and safe manner, using carefully designed prompts and safety guardrails rather than fine-tuning — leveraging an existing LLM's general knowledge through prompt engineering.

## 🛠️ Tools & Model

- **LLM Provider:** Hugging Face Router
- **Model:** `moonshotai/Kimi-K2-Instruct-0905`
- **API Client:** OpenAI-compatible Python client (`openai` library), pointed at the Hugging Face router endpoint

## 🛠️ Project Workflow

1. **API Setup** – Configure the OpenAI Python client to communicate with the Hugging Face router, with API keys managed securely via a `.env` file.
2. **Prompt Engineering** – Design a system prompt that instructs the model to act as a helpful, friendly medical assistant, ensuring responses are clear and approachable.
3. **Safety Handling** – Add safety constraints within the system prompt to prevent the chatbot from giving harmful, diagnostic, or prescriptive medical advice, and to encourage users to consult a healthcare professional for serious concerns.
4. **Query Testing** – Test the chatbot with example health queries such as:
   - *"What causes a sore throat?"*
   - *"Is paracetamol safe for children?"*
5. **Response Evaluation** – Review chatbot outputs for clarity, friendliness, and safety compliance.

## 🧠 Skills Demonstrated

- Prompt design and testing
- Using APIs for LLMs (Hugging Face router via OpenAI-compatible client)
- Safety handling in chatbot responses
- Building simple conversational agents

## 📦 Tech Stack

| Tool / Library | Purpose |
|---|---|
| Python | Core programming language |
| `openai` | API client for LLM communication |
| Hugging Face Router | LLM inference endpoint |
| `python-dotenv` | Secure API key management via `.env` |

## 📁 Repository Structure

This repository contains three implementations of the chatbot, each demonstrating a different way of interacting with the same underlying LLM logic:

├── With_Streamlit/      # Chatbot with an interactive Streamlit web UI

├── With_FastAPI/        # Chatbot exposed as a REST API using FastAPI

├── basic_chatbot.py/.ipynb   # Core script/notebook version (prompt engineering + safety filters)

├── README.md            # Project documentation (this file)

└── requirements.txt      # Python dependencies

> 📌 **Note:** `With_Streamlit` and `With_FastAPI` each have their own dedicated README files with setup and usage instructions specific to those implementations. This README covers the core chatbot logic shared across all versions.

## 🚀 Getting Started

### Prerequisites

```bash
pip install openai python-dotenv
```

### Setup

1. Clone the repository:
```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
```
2. Create a `.env` file in the root directory and add your Hugging Face API key:

HF_API_KEY=your_api_key_here

3. Run the basic script/notebook:
```bash
   python basic_chatbot.py
```

## 💬 Example Queries

| Query | Expected Behavior |
|---|---|
| "What causes a sore throat?" | General, educational explanation of common causes |
| "Is paracetamol safe for children?" | General safety information with a recommendation to consult a doctor/pharmacist for dosing |

## 🛡️ Safety Considerations

- The chatbot is designed to provide **general educational information only** — not diagnosis, prescriptions, or personalized medical advice.
- The system prompt explicitly instructs the model to recommend consulting a licensed healthcare professional for any serious, urgent, or personal health concerns.
- This project is intended for educational and demonstration purposes only and should not be used as a substitute for professional medical consultation.
