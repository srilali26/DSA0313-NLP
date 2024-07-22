import random
import nltk
from nltk.util import ngrams
from collections import defaultdict, Counter

# Sample text
text = "the quick brown fox jumps over the lazy dog"

# Tokenize the text into words
tokens = nltk.word_tokenize(text)

# Generate bigrams
bigrams = list(ngrams(tokens, 2))

# Build the bigram model
model = defaultdict(Counter)
for w1, w2 in bigrams:
    model[w1][w2] += 1

# Function to generate text using the bigram model
def generate_text(model, start_word, length=10):
    current_word = start_word
    generated_text = [current_word]
    
    for _ in range(length - 1):
        next_word_choices = list(model[current_word].keys())
        next_word_weights = list(model[current_word].values())
        current_word = random.choices(next_word_choices, weights=next_word_weights, k=1)[0]
        generated_text.append(current_word)
    
    return ' '.join(generated_text)

# Main program
if __name__ == "__main__":
    start_word = 'the'
    generated_text = generate_text(model, start_word, length=10)
    print(generated_text)
