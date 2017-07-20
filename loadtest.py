import json
import os
import requests

url = '{0}/asr'.format(os.environ['URL_SERVER'])
print(url)


def post_opus(filename):
    file = open(filename, 'rb').read()
    headers = {'Content-Type': 'application/octet-stream'}

    res = requests.post(url, data=file, headers=headers)
    data = json.loads(res.text)
    assert res.status_code < 400
    assert data['status'] == 'ok'
    return data


res = post_opus('./clips/1.opus')
print(res['status'])
