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
