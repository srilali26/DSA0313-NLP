import nltk
from nltk.stem import PorterStemmer

# Download necessary NLTK data files
nltk.download('punkt')

# Initialize the Porter Stemmer
stemmer = PorterStemmer()

# Sample list of words
words = ["running", "jumps", "easily", "fairly", "cats", "happiness"]

# Stem each word
stems = [stemmer.stem(word) for word in words]

# Print the results
print("Word\tStem")
for word, stem in zip(words, stems):
    print(f"{word}\t{stem}")

# Main program
if __name__ == "__main__":
    pass
