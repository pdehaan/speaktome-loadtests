import json
import requests

url = 'https://speaktome.stage.mozaws.net/asr'


def post_opus(filename):
    try:
        files = {'file': open(filename, 'rb')}
        headers = {}
        headers['Content-Type'] = 'application/octet-stream'

        res = requests.post(url, files=files, headers=headers)
        data = json.loads(res.text)
        assert res.status_code < 400
        assert data['status'] == 'ok'
        return data

    except FileNotFoundError:
        print('Unable to find file, {0}'.format(filename))
    except:
        print("huh?")

res = post_opus('tmp/test5.opus')
print(res['status'])

# curl -H "Content-Type: application/octet-stream" --data-binary @tmp/test$i.opus https://speaktome.stage.mozaws.net/asr
