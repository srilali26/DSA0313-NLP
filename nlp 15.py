import nltk
from nltk import PCFG
from nltk.parse import pchart

# Define a probabilistic context-free grammar
pcfg = PCFG.fromstring("""
  S -> NP VP [1.0]
  VP -> V NP [0.5] | V NP PP [0.3] | V PP [0.2]
  PP -> P NP [1.0]
  V -> 'saw' [0.5] | 'ate' [0.3] | 'walked' [0.2]
  NP -> 'John' [0.2] | 'Mary' [0.2] | 'Bob' [0.1] | Det N [0.4] | Det N PP [0.1]
  Det -> 'a' [0.5] | 'the' [0.5]
  N -> 'man' [0.1] | 'dog' [0.2] | 'cat' [0.1] | 'telescope' [0.3] | 'park' [0.3]
  P -> 'in' [0.4] | 'on' [0.3] | 'by' [0.2] | 'with' [0.1]
""")

# Create a PCFG parser
parser = pchart.InsideChartParser(pcfg)

# Test sentence
sentence = "John saw a man in the park".split()

# Parse the sentence and print the parse trees with probabilities
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()

    # Print the probability of the parse tree
    print(f"Probability of the parse tree: {tree.prob()}\n")
