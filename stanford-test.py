from pycorenlp import StanfordCoreNLP
import time
start = time.time()
print("[{}] Start".format(time.time() - start))
# java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer <-- Run this
# in Terminal within the stanford-corenlp-full-2015-12-09
nlp = StanfordCoreNLP('http://localhost:9000')
print("[{}] Started Server".format(time.time() - start))
text_items = ["Who are you?", "What is this?", "What is wrong with you?", "Who you?", "What?", "Who", "why"]
output = []
for text in text_items:
    output += [nlp.annotate(text, properties={
      'annotators': 'tokenize,ssplit,pos,depparse,parse',
      'outputFormat': 'json'
      })]
    print("[{}] Completed item".format(time.time() - start))
for item in output:
    print(item['sentences'][0]['parse'])