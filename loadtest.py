import os
import molotov

_FILENAME = 'clips/speech_orig.opus'

PROD_SERVER = 'https://speaktome.services.mozilla.com'
STAGE_SERVER = 'https://speaktome.stage.mozaws.net'

url_server = os.getenv('URL_SERVER', STAGE_SERVER).rstrip('/')
url = url_server + '/asr'
print(url)


@molotov.scenario()
async def upload_file(session):
    headers = {'Content-Type': 'audio/opus'}

    with open(_FILENAME, 'rb') as file:
        async with session.post(url, data=file, headers=headers) as res:
            print(res.status)
            data = await res.json()
            # print(data)
            assert res.status == 200
            assert data['status'] == 'ok'
            return data
