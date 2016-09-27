from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000')
while True:
    inp = input("Input an intelligible sentence or (q)uit: ")
    if(inp.lower() == 'q'):
        break
    else:
        out = nlp.annotate(inp, properties={
            'annotators': 'tokenize,ssplit,pos,depparse,parse',
            'outputFormat': 'json'
        })
        if 'SBARQ' in out['sentences'][0]['parse']:
            print("Is a question")
        elif:

        else:
            print("Not a question")
        print(out['sentences'][0]['parse'])