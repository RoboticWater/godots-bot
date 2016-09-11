from spacy.en import English
import spacy.en
import os

nlp = English(parser=False, tagger=True, entity=False)


def print_fine_pos(token):
    return token.tag_

def pos_tags(sentence):
    sentence = sentence
    tokens = nlp(sentence)
    tags = []
    for tok in tokens:
        tags.append((tok, print_fine_pos(tok)))
    return tags

a = "Who are you?"
print(pos_tags(a))