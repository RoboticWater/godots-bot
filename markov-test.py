import re
import random


def markov(text, start, steps):
    out = list(start)
    words = re.sub(r'\n', ' ', text).split(' ')
    # add_list = []
    # for i in range(len(words)):
    #     m = re.search(r'[.,/#!$%\^&*;:{}=\-_`~()"]', words[i])
    #     if m is not None:
    #         print(words[i])
    #         words[i] = re.sub(r'[.,/#!$%\^&*;:{}=\-_`~()"]', '', words[i])
    #         add_list.append((i + 1, m.group()))
    # for elem in add_list:
    #     words.insert(elem[0], elem[1])
    # print(words[0:100])
    gram = start
    for i in range(steps):
        out += [next_word(words, gram)]
        gram = [out[i - len(start)] for i in range(len(start))]
    return ' '.join(out)


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
run = True
inp = ''
txt = ''
while run:
    inp = input('Input file: ')
    if inp.lower() == 'q':
        run = False
        break
    else:
        try:
            file = open(inp, 'r', encoding="utf8")
            txt = ''.join([i for i in file])
            break
        except FileNotFoundError:
            print("File not found. Try again or (q)uit.")


while run:
    inp = input('Input starting strings separated by spaces (ex:"He tried") or (q)uit: ')
    if inp.lower() == 'q':
        run = False
        break
    else:
        print("--> " + markov(txt, inp.split(' '), 20))