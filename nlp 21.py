import spacy

nlp = spacy.load("en_core_web_sm")

text = "The quick brown fox jumps over the lazy dog."

doc = nlp(text)

noun_phrases = [chunk.text for chunk in doc.noun_chunks]
print(noun_phrases)
