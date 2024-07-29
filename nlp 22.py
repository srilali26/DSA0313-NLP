import neuralcoref
import spacy

nlp = spacy.load("en_core_web_sm")
neuralcoref.add_to_pipe(nlp)

text = "Alice and Bob went to the park. She said it was her favorite place."

doc = nlp(text)

if doc._.has_coref:
    for cluster in doc._.coref_clusters:
        print(cluster)
