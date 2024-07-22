import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser

# Define a context-free grammar
grammar = CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP | V PP
  PP -> P NP
  V -> "saw" | "ate" | "walked"
  NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "dog" | "cat" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with"
""")

# Create a parser
parser = RecursiveDescentParser(grammar)

# Test sentence
sentence = "John saw a man in the park".split()

# Parse the sentence and generate the parse tree
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()

# Optional: Drawing the parse tree
tree.draw()
