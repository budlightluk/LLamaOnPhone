from transformers import AutoModelForCausalLM, AutoTokenizer

def load_model():
    tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-2.7B")
    model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-2.7B")
    return model, tokenizer

model, tokenizer = load_model()
