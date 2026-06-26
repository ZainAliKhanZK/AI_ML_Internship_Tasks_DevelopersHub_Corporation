# Importing Libraries
import torch
from transformers import pipeline 

from transformers import AutoModelForCausalLM, AutoTokenizer

# Loading the Fine-Tuned Model and Tokenizer
model_path = "empathetic_distilgpt2_final"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)
model.eval()

# Creating a Function for Cleaner Response
def clean_response(text):
    text = text.split("Response:")[-1].strip()
    for stop_word in ["User:", "Situation:", "Bot:"]:
        if stop_word in text:
            text = text.split(stop_word)[0].strip()

    text = text.replace("_comma_", ",")
    text = text.replace(",,", ",")        # fix doubled commas like "_comma__comma_"
    text = text.replace(" ,", ",")        # fix stray space before comma
    text = " ".join(text.split())         # collapse extra whitespace

    return text

# Tokenizing the Input & Generating the Response with the Model
def generate_response(situation):
    prompt = f"Situation: {situation}\nResponse:"
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=50,
            do_sample=True,
            top_p=0.9,
            temperature=0.5,
            repetition_penalty=1.3,
            no_repeat_ngram_size=3,
            pad_token_id=tokenizer.eos_token_id,
        )
    raw = tokenizer.decode(output[0], skip_special_tokens=True)
    return clean_response(raw)

# test_situations = [
#     "I failed my exam and feel like a failure.",
# ]
#      "I got accepted into my dream university!",
#      "I had a huge fight with my parents and feel terrible.",
# ]

# for s in test_situations:
#     print(f"Situation: {s}")
#     print(f"Response: {generate_response(s)}")
#     print("-" * 60)
