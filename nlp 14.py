import nltk
from nltk import CFG
from nltk.parse import ChartParser

# Define a context-free grammar with agreement rules
grammar = CFG.fromstring("""
  S -> NP[NUM=?n] VP[NUM=?n]
  NP[NUM=?n] -> Det[NUM=?n] N[NUM=?n]
  VP[NUM=?n] -> V[NUM=?n]
  
  Det[NUM=sg] -> 'the' | 'a'
  Det[NUM=pl] -> 'the'
  
  N[NUM=sg] -> 'dog' | 'cat' | 'man'
  N[NUM=pl] -> 'dogs' | 'cats' | 'men'
  
  V[NUM=sg] -> 'barks' | 'runs' | 'eats'
  V[NUM=pl] -> 'bark' | 'run' | 'eat'
""")

# Create a parser
parser = ChartParser(grammar)

# Function to check sentence agreement
def check_agreement(sentence):
    tokens = sentence.split()
    try:
        for tree in parser.parse(tokens):
            print("Sentence is grammatically correct.")
            tree.pretty_print()
            return True
    except ValueError:
        print("Sentence does not conform to the agreement rules.")
        return False

# Test sentences
sentences = [
    "the dog barks",
    "the dogs bark",
    "the cat runs",
    "the cats run",
    "the dog run",  # Incorrect agreement
    "the dogs runs" # Incorrect agreement
]

for sentence in sentences:
    print(f"Checking: '{sentence}'")
    check_agreement(sentence)
    print()
