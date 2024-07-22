import nltk
from nltk.probability import FreqDist, ConditionalFreqDist
from nltk.corpus import treebank
from nltk import DefaultTagger, UnigramTagger

# Download the treebank corpus if not already present
nltk.download('treebank')

# Training data
train_sents = treebank.tagged_sents()[:3000]

# Unigram tagger
unigram_tagger = UnigramTagger(train_sents)

# Test sentence
sentence = "This is a test sentence."
tokens = word_tokenize(sentence)
tags = unigram_tagger.tag(tokens)

print(tags)
