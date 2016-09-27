import json
import sys
from adapt.entity_tagger import EntityTagger
from adapt.tools.text.tokenizer import EnglishTokenizer
from adapt.tools.text.trie import Trie
from adapt.intent import IntentBuilder
from adapt.parser import Parser
from adapt.engine import IntentDeterminationEngine


tokenizer = EnglishTokenizer()
trie = Trie()
tagger = EntityTagger(trie, tokenizer)
parser = Parser(tokenizer, tagger)

engine = IntentDeterminationEngine()

# define vocabulary
who_keyword = [
    "who"
]

for wk in who_keyword:
    engine.register_entity(wk, "WhoKeyword")

objects = [
    "you",
    "I",
]

for o in objects:
    engine.register_entity(o, "Object")


# structure intent
who_intent = IntentBuilder("WhoIntent")\
    .require("WhoKeyword")\
    .optionally("WeatherType")\
    .require("Location")\
    .build()

engine.register_intent_parser(who_intent)

if __name__ == "__main__":
    for intent in engine.determine_intent(' '.join(sys.argv[1:])):
        if intent and intent.get('confidence') > 0:
            print(json.dumps(intent, indent=4))