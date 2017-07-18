#!/bin/sh

while [ 1 ]
do
  rec tmp/_test.wav trim 0 4
  sox tmp/_test.wav -c 1 -r 16000 -b 16 tmp/test$i.wav
  opusenc tmp/test$i.wav tmp/test$i.opus
  curl -H "Content-Type: application/octet-stream" --data-binary @tmp/test$i.opus https://speaktome.stage.mozaws.net/asr  -o tmp/test$i.json
  more tmp/test$i.txt
  rm tmp/_test.wav
  rm tmp/test$i.wav
  i=$[$i+1]
done
