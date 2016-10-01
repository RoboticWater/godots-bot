import http.client, urllib.request, urllib.parse, urllib.error, base64, json

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'e58fd4c615d447e1bf626e5d73b9088d',
}
body = {
    "language": "en",
    "analyzerIds": ["22a6b758-420f-4745-8a3c-46835a67c0d2"],
    "text": "Hi, Tom! How are you today?"
}
# "4fa79af1-f22c-408d-98bb-b7d7aeef7f04",
params = urllib.parse.urlencode({
})
try:
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/linguistics/v1.0/analyze?%s" % params, json.dumps(body), headers)
    response = conn.getresponse()
    data = response.read().decode('utf8')
    obj = json.loads(data)
    print(obj[0])
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))