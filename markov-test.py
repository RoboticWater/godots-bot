import re
import random


def markov(text, gram, start, steps):
    out = ""
    reg = re.compile('\n')
    words = reg.sub('', text).split(' ')
    reg = re.compile('[.?!]')
    for i in range(len(words)):
        m = reg.match(words[i])
        if m is not None:
            words[i] = reg.sub('', words[i])
            words.insert(i + 1, m.group())
    print(words[0:5])
    return out


def next_word(text, words):
    return random.choice([text[i[1] + 1] for i in find_sublist(text, words)])


def find_sublist(l, sl):
    out = []
    sll = len(sl)
    for ind in (i for i, e in enumerate(l) if e == sl[0]):
        if list[ind:ind+sll]:
            out.append((ind, ind+sll-1))
    return out

markov('''
''', 2, '', 10)