from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

data = [
    ("Can you please help me with my homework?", "request"),
    ("Sure, I can help you with that.", "response"),
    ("Thank you so much!", "gratitude"),
    ("You're welcome!", "response")
]

texts, labels = zip(*data)

model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(texts, labels)

test_text = ["Can I get a glass of water?"]
print(model.predict(test_text))
