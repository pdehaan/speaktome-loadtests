#!/usr/bin/env sh

readonly DURATION=500
readonly PROCESSES=( 30 36 42 48 54 )
readonly WORKERS=( 3 )

for p in "${PROCESSES[@]}"
do
  for w in "${WORKERS[@]}"
  do
    echo "----- Now running w/ (-d $DURATION -p $p -w $w) -----"
    molotov -d $DURATION -cx -p $p -w $w loadtest.py
    echo "zzzzz (30s)"
    sleep 30
  done
done
