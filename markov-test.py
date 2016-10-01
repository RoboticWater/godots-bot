import re
import random


def markov(text, start, steps):
    periods = 0
    out = list(start)
    words = re.sub(r'\n', ' ', text)
    words = re.sub(r'([.,!?();"])', r' \1 ', words)
    words = re.sub('\s{2,}', ' ', words)
    words = [i.lower() for i in words.split(' ') if len(i) > 0]
    gram = start
    #for i in range(steps):
    while periods < steps:
        w = next_word(words, gram)
        if '.' in w:
            periods += 1
        out += [w]
        gram = [out[i - len(start)] for i in range(len(start))]
    out = ' '.join(out)
    out = re.sub(r'\s([.,!?();])', r'\1', out)
    return capitalize(out)


def uppercase(matchobj):
    return matchobj.group(0).upper()


def capitalize(s):
    return re.sub('^([a-z])|[\.|\?|\!]\s*([a-z])|\s+([a-z])(?=\.)', uppercase, s)


def next_word(text, gram):
    # print(gram)
    if len(gram) == 0:
        print("Word not found, going full random.")
        return random.choice(text)
    next_list = [text[i[1] + 1] for i in find_sublist(text, gram) if i[1] + 1 < len(text)]
    if len(next_list) < 1:
        return next_word(text, gram[1:])
    else:
        return random.choice(next_list)


def find_sublist(l, sl):
    out = []
    # for i in range(len(l)):
    #
    sll = len(sl)
    for ind in (i for i, e in enumerate(l) if e == sl[0]):
        if l[ind:ind+sll] == sl:
            out.append((ind, ind+sll-1))
    return out
f = open('gatsby.txt', encoding='utf8')
print(markov(''.join([line for line in f]), ['he', 'tried', 'to'], 10))
# run = True
# inp = ''
# txt = ''
# while run:
#     inp = input('Input file: ')
#     if inp == '':
#         inp = 'gatsby.txt'
#     if inp.lower() == 'q':
#         run = False
#         break
#     else:
#         try:
#             file = open(inp, 'r', encoding="utf8")
#             txt = ''.join([i for i in file])
#             break
#         except FileNotFoundError:
#             print("File not found. Try again or (q)uit.")
#
#
# while run:
#     inp = input('Input starting strings separated by spaces (ex:"He tried") or (q)uit: ')
#     if inp.lower() == 'q':
#         run = False
#         break
#     else:
#         print("--> " + markov(txt, inp.split(' '), 20))