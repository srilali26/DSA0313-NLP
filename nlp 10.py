import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import AffixTagger, UnigramTagger, BigramTagger, TrigramTagger, brill, brill_trainer

# Download required resources
nltk.download('brown')
nltk.download('treebank')
nltk.download('universal_tagset')

# Sample training data
train_sents = nltk.corpus.treebank.tagged_sents(tagset='universal')[:3000]

# Define backoff taggers
affix_tagger = AffixTagger(train_sents, backoff=DefaultTagger('NN'))
unigram_tagger = UnigramTagger(train_sents, backoff=affix_tagger)
bigram_tagger = BigramTagger(train_sents, backoff=unigram_tagger)
trigram_tagger = TrigramTagger(train_sents, backoff=bigram_tagger)

# Define transformation-based tagging templates
templates = brill.fntbl37()
trainer = brill_trainer.BrillTaggerTrainer(trigram_tagger, templates)
brill_tagger = trainer.train(train_sents, max_rules=50)

# Test sentence
sentence = "This is a test sentence."
tokens = word_tokenize(sentence)
tags = brill_tagger.tag(tokens)

print(tags)
