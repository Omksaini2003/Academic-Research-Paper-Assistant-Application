# from transformers import LlamaForCausalLM, LlamaTokenizer
# from transformers import LlamaForCausalLM, LlamaTokenizer

HUGGINGFACE_TOKEN = "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"

model_name = "meta-llama/Llama-2-7b-hf"  # Example of a public model
cache_dir = "./local_model_dir"

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

# tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
# model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf")


# Once downloaded, you can reuse the local path:
# print(f"Model and tokenizer saved in {cache_dir}")



class LlamaService:
    def __init__(self):
        model_name = "openlm-research/open_llama_7b"  # Replace with a smaller model if resources are limited
        model_name2 = "meta-llama/Llama-2-7b-hf"  # Replace with a smaller model if resources are limited
        
      #   self.tokenizer = LlamaTokenizer.from_pretrained("./local_model_dir")
      #   self.model = LlamaForCausalLM.from_pretrained("./local_model_dir")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate_answer(self, question, context):
        input_text = f"Question: {question}\nContext: {context}\nAnswer:"
        inputs = self.tokenizer(input_text, return_tensors="pt")
        outputs = self.model.generate(inputs["input_ids"], max_length=500, num_return_sequences=1)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
    def generate_future_works(self, topic):
        prompt = f"Suggest future research directions for the topic: {topic}."
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs["input_ids"], max_length=300, num_return_sequences=1)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
