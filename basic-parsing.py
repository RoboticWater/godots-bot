import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64
import json


def get_constituency_tree(text, sub_key):
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': sub_key,
    }
    body = {
        "language": "en",
        "analyzerIds": ["22a6b758-420f-4745-8a3c-46835a67c0d2"],
        "text": text
    }
    params = urllib.parse.urlencode({
    })
    try:
        conn = http.client.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/linguistics/v1.0/analyze?%s" % params, json.dumps(body), headers)
        response = json.loads(conn.getresponse().read().decode('utf8'))
        conn.close()
        return response[0]['result']
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def get_keywords(text, sub_key):
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': sub_key,
    }
    body = {
        "documents": [
            {
                "language": "en",
                "id": "1",
                "text": text
            }
        ]
    }
    params = urllib.parse.urlencode({
    })
    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/text/analytics/v2.0/keyPhrases?%s" % params, json.dumps(body), headers)
        response = json.loads(conn.getresponse().read().decode('utf8'))
        conn.close()
        return response['documents'][0]['keyPhrases']
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def main_ui():
    lin_sub_key = 'e58fd4c615d447e1bf626e5d73b9088d'
    txt_sub_key = '18dbe0f88e924120bc39bb9af9f9b5e3'
    inp = input('Input Linguistic Analysis subscription key or (q)uit\n>> ')
    if inp.lower() == 'q':
        print('Program closed')
        return
    elif inp != '':
        lin_sub_key = inp
    inp = input('Input Text Analysis subscription key or (q)uit\n>> ')
    if inp.lower() == 'q':
        print('Program closed')
        return
    elif inp != '':
        txt_sub_key = inp

    while True:
        inp = input("Enter text or (q)uit\n>> ")
        if inp.lower() == 'q':
            print('Program closed')
            return
        con_trees = get_constituency_tree(inp, lin_sub_key)
        keywords = get_keywords(inp, txt_sub_key)
        if len(con_trees) > 1:
            print('Too many sentences')
        elif len(con_trees) < 1:
            print('Input unable to be parsed')
        else:
            print(handle_sentence(con_trees[0], keywords))


def handle_sentence(con_tree, keywords):
    out = ''
    if 'SBARQ' in con_tree or 'SQ' in con_tree:
        out += 'Is a question\nKeywords: '
    else:
        out += 'Not a question\nKeywords: '
    out += ','.join(keywords)
    return out

print(get_constituency_tree('who are you?', 'e58fd4c615d447e1bf626e5d73b9088d'))