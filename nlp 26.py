from transformers import MarianMTModel, MarianTokenizer

model_name = 'Helsinki-NLP/opus-mt-en-fr'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

text = "Hello, how are you?"
translated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))

translated_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
print(translated_text[0])
