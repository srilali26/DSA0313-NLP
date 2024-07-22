import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None
text = "The striped bats are hanging on their feet for best."
tokens = word_tokenize(text)
pos_tags = nltk.pos_tag(tokens)
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = []
for token, tag in pos_tags:
    wordnet_pos = get_wordnet_pos(tag) or wordnet.NOUN
    lemmatized_token = lemmatizer.lemmatize(token, pos=wordnet_pos)
    lemmatized_tokens.append((token, tag, lemmatized_token))
print("Token\tPOS\tLemma")
for token, tag, lemma in lemmatized_tokens:
    print(f"{token}\t{tag}\t{lemma}")
if __name__ == "__main__":
    pass
