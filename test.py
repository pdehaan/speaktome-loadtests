import json
import requests

url = 'https://speaktome.stage.mozaws.net/asr'


def post_opus(filename):
    files = {'file': open(filename, 'rb')}
    headers = {}
    headers['Content-Type'] = 'application/octet-stream'

    res = requests.post(url, files=files, headers=headers)
    print(res.status_code)
    return json.loads(res.text)

res = post_opus('tmp/test2.opus')
print(res['status'])

# curl -H "Content-Type: application/octet-stream" --data-binary @tmp/test$i.opus https://speaktome.stage.mozaws.net/asr
