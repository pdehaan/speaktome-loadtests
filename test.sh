#!/usr/bin/env sh

readonly DURATION=120
readonly PROCESSES=( 2 12 22 32 42 )
readonly WORKERS=( 1 )

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
