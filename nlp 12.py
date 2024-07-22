import nltk
from nltk.parse import EarleyChartParser

# Define a simple grammar
grammar = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" | "ate" | "walked"
  NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "dog" | "cat" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with"
""")

# Create an Earley parser
parser = EarleyChartParser(grammar)

# Test sentence
sentence = "John saw a man in the park".split()

# Parse the sentence
for tree in parser.parse(sentence):
    print(tree)
