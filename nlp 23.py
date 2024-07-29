from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter

def coherence_score(text):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    overall_score = 0

    for i in range(1, len(sentences)):
        prev_words = [word for word in word_tokenize(sentences[i - 1].lower()) if word not in stop_words]
        current_words = [word for word in word_tokenize(sentences[i].lower()) if word not in stop_words]

        common_words = set(prev_words) & set(current_words)
        overall_score += len(common_words)

    return overall_score

text = "The weather is nice today. It is sunny and warm. People are enjoying the sunshine."
print(coherence_score(text))
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter

def coherence_score(text):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    overall_score = 0

    for i in range(1, len(sentences)):
        prev_words = [word for word in word_tokenize(sentences[i - 1].lower()) if word not in stop_words]
        current_words = [word for word in word_tokenize(sentences[i].lower()) if word not in stop_words]

        common_words = set(prev_words) & set(current_words)
        overall_score += len(common_words)

    return overall_score

text = "The weather is nice today. It is sunny and warm. People are enjoying the sunshine."
print(coherence_score(text))
