# 💬 Mental Health Support Chatbot (Fine-Tuned)

A supportive chatbot fine-tuned to generate gentle, empathetic responses for everyday stress, anxiety, and emotional wellness conversations, built by fine-tuning DistilGPT2 on real empathetic human dialogues.

## 🎯 Objective

To fine-tune a small language model so it responds with empathy and emotional warmth, rather than relying solely on prompt engineering — learning conversational tone directly from human-to-human supportive dialogue data.

## 🛠️ Model & Dataset

- **Base Model:** DistilGPT2
- **Fine-Tuning Dataset:** [EmpatheticDialogues](https://github.com/facebookresearch/EmpatheticDialogues) (Facebook AI)
- **Training Framework:** Hugging Face `Trainer` API
- **Hosting:** Fine-tuned model weights hosted on Hugging Face Hub

## 🛠️ Project Workflow

1. **Dataset Preparation** – Loaded and preprocessed the EmpatheticDialogues dataset for conversational fine-tuning.
2. **Fine-Tuning** – Fine-tuned DistilGPT2 using Hugging Face's `Trainer` API to learn empathetic response patterns from real human dialogues.
3. **Generation Quality Improvements** – Tuned generation parameters (`no_repeat_ngram_size`, `repetition_penalty`) to reduce repetitive and low-quality outputs.
4. **Post-Processing** – Cleaned up dataset-specific artifacts (e.g., `_comma_` tokens) from generated responses using a dedicated `clean_response()` function, rather than retraining the model.
5. **Interface Development** – Built two separate interfaces to interact with the fine-tuned model:
   - `CLI_Based/` — Command-line chatbot interface
   - `Streamlit_Based/` — Web-based chatbot interface using Streamlit

## 🧠 Skills Demonstrated

- Model fine-tuning with Hugging Face Transformers
- Emotional tone design for safe chatbots
- Conversation modeling
- Deployment using CLI and simple web apps

## 📦 Tech Stack

| Tool / Library | Purpose |
|---|---|
| Python | Core programming language |
| `transformers` | Model fine-tuning (Trainer API) and inference |
| `datasets` | Loading and processing EmpatheticDialogues |
| `torch` | Underlying deep learning framework |
| Hugging Face Hub | Hosting fine-tuned model weights |
| Streamlit | Web-based chatbot interface |

## 📁 Repository Structure

├── CLI_Based/             # Command-line chatbot interface

├── Streamlit_Based/       # Streamlit web app chatbot interface

├── fine_tuning.ipynb      # Notebook for fine-tuning DistilGPT2 on EmpatheticDialogues

├── README.md              # Project documentation (this file)

└── requirements.txt        # Python dependencies

> 📌 **Note:** `CLI_Based` and `Streamlit_Based` each have their own dedicated README with setup and usage instructions specific to that interface. This README covers the fine-tuning process shared across both.

## 🚀 Getting Started

### Prerequisites

```bash
pip install transformers datasets torch
```

### Fine-Tuning

Run the fine-tuning notebook to reproduce training on EmpatheticDialogues:
```bash
jupyter notebook fine_tuning.ipynb
```

### Using the Chatbot

Refer to the README inside `CLI_Based/` or `Streamlit_Based/` depending on which interface you'd like to run.

## 🛡️ Safety & Tone Considerations

- The model is fine-tuned to be **gentle and emotionally supportive**, not clinical or diagnostic.
- This chatbot is **not a substitute for professional mental health support, therapy, or crisis intervention**.
- It is intended for educational and demonstration purposes only.
