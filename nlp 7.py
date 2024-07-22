import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample text
text = "This is a sample sentence to demonstrate part-of-speech tagging."

# Tokenize the text
tokens = word_tokenize(text)

# Perform POS tagging
tagged_tokens = pos_tag(tokens)

print(tagged_tokens)
