# speaktome-loadtests

Load tests for https://github.com/mozilla/speaktome

## Sample data:

To create some sample OPUS files, run `./record.sh` to record some 4 second clips and submit them to the proxy server. You can find the generated `*.opus` files and the proxy server responses in the `tmp/` folder.

## Requirements:

Python 3+
requests
virtualenv

## Setup:

```sh
$ virtualenv venv -p python3
$ source ./venv/bin/activate
$ pip install -r requirements.txt

$ python test.py
```

## Testing (CLI):

```sh
$ curl -H "Content-Type: application/octet-stream" --data-binary @clips/1.opus https://speaktome.stage.mozaws.net/asr
> {"status":"ok","data":[{"confidence":0.91162,"text":"ONE TWO THREE FOUR FIVE SIX SEVEN"},{"confidence":0.915788,"text":"ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT"},{"confidence":0.914959,"text":"ONE TWO THREE FOUR FIVE SIX SEVEN SIX"},{"confidence":0.91876,"text":"ONE TWO THREE FOUR FIVE SIX SEVEN A M"},{"confidence":0.918655,"text":"ONE TWO THREE FOUR FIVE SIX SEVEN P M"},{"confidence":0.914386,"text":"ONE TWO THREE FOUR FIVE SIX SEVEN THREE"},{"confidence":0.918332,"text":"ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT EIGHT"},{"confidence":0.913997,"text":"ONE TWO THREE FOUR FIVE SIX SEVEN PM"},{"confidence":0.913682,"text":"ONE TWO THREE FOUR FIVE SIX SEVEN PLEASE"},{"confidence":0.913729,"text":"ONE TWO THREE FOUR FIVE SIX SEVEN DAYS"}]}
```
