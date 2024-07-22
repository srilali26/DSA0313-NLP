import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger

# Define regex patterns
patterns = [
    (r'.*ing$', 'VBG'),  # gerunds
    (r'.*ed$', 'VBD'),   # simple past
    (r'.*es$', 'VBZ'),   # 3rd person singular present
    (r'.*ould$', 'MD'),  # modals
    (r'.*\'s$', 'NN$'),  # possessive nouns
    (r'.*s$', 'NNS'),    # plural nouns
    (r'^-?[0-9]+(\.[0-9]+)?$', 'CD'),  # cardinal numbers
    (r'.*', 'NN')        # default to noun
]

# Create a RegexpTagger
regexp_tagger = RegexpTagger(patterns)

# Sample text
text = "This is a test sentence containing numbers like 123 and verbs like running."

# Tokenize the text
tokens = word_tokenize(text)

# Apply the tagger
tags = regexp_tagger.tag(tokens)

print(tags)
