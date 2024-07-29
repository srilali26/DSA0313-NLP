from sklearn.feature_extraction.text import TfidfVectorizer
documents = [
    "The sky is blue.",
    "The sun is bright.",
    "The sun in the sky is bright.",
    "We can see the shining sun, the bright sun."
]

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

print(tfidf_matrix.toarray())
print(vectorizer.get_feature_names_out())
