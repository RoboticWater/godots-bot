from spacy.en import English
parser = English()
example = "Who are you?"
parsedEx = parser(example)
# shown as: original token, dependency tag, head word, left dependents, right dependents
for token in parsedEx:
    print(token.orth_, token.dep_, token.head.orth_, [t.orth_ for t in token.lefts], [t.orth_ for t in token.rights])