from nltk.tokenize import *
import re
from nltk.corpus import wordnet as wn


def get_similar(word):
    # return [syns.lemmas for syns in wordnet.synsets(word)]
    return set([re.sub(r'_', ' ', lem.name()) for syns in wn.synsets(word) for lem in syns.lemmas()])


def weight_sentences(sents, keywords):
    similar = [var for vars in keywords for var in get_similar(vars)]
    for sentence in sents.keys():
        for word in keywords:
            if word + " " in sentence:
                sents[sentence] += 5
        for word in similar:
            if word in sentence:
                sents[sentence] += 1

    return sorted([s for s in sents.keys() if sents[s] > 0], key=sents.get)

f = open('gatsby.txt', encoding='utf8')
text = ''.join([line for line in f])
text = re.sub(r'\n', ' ', text)
sentences = sent_tokenize(text)
weighted_sent = {s : 0 for s in sentences}
kw = ['lower']
for s in weight_sentences(weighted_sent, kw):
    print("{:>3d} | {}".format(weighted_sent[s], s))
print('Similar words:\n' + '\n'.join([k + ': ' + ', '.join(var for var in get_similar(k)) for k in kw]))




'''
print(variants('good'))


# for synset in good:
#     for lemma in synset.lemmas:
#         lemmas.add(lemma.name)
'''