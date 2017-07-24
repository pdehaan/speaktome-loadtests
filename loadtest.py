# import json
import os
import molotov

_FILENAME = 'clips/speech_orig.opus'

url_server = url_server = os.getenv('URL_SERVER', 'https://speaktome.stage.mozaws.net').rstrip('/')
url = url_server + '/asr'
print(url)


@molotov.scenario()
async def upload_file(session):
    headers = {'Content-Type': 'audio/opus'}

    with open(_FILENAME, 'rb') as file:
        async with session.post(url, data=file, headers=headers) as res:
            assert res.status < 400
            data = await res.json()
            assert data['status'] == 'ok'
            return data
