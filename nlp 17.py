from nltk.corpus import wordnet as wn
word = "bank"

synsets = wn.synsets(word)
for synset in synsets:
    print(f"Synset: {synset.name()}")
    print(f"Definition: {synset.definition()}")
    print(f"Examples: {synset.examples()}")
    print()
from nltk.corpus import wordnet as wn
word = "bank"
synsets = wn.synsets(word)
for synset in synsets:
    print(f"Synset: {synset.name()}")
    print(f"Definition: {synset.definition()}")
    print(f"Examples: {synset.examples()}")
    print()
