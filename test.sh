#!/usr/bin/env sh

echo "----- Run #1 (-p 2 -w 1) -----"
molotov -d 60 -cx -p 2 -w 1 loadtest.py
echo "zzzzz (30s)"
sleep 30

echo "----- Run #2 (-p 8 -w 1) -----"
molotov -d 60 -cx -p 8 -w 1 loadtest.py
echo "zzzzz (30s)"
sleep 30

echo "----- Run #4 (-p 14 -w 1) -----"
molotov -d 60 -cx -p 14 -w 1 loadtest.py
echo "zzzzz (30s)"
sleep 30

echo "----- Run #5 (-p 20 -w 1) -----"
molotov -d 60 -cx -p 20 -w 1 loadtest.py
echo "zzzzz (30s)"
sleep 30

echo "----- Run #6 (-p 26 -w 1) -----"
molotov -d 60 -cx -p 26 -w 1 loadtest.py
echo "zzzzz (30s)"
sleep 30

echo "----- Run #7 (-p 32 -w 1) -----"
molotov -d 60 -cx -p 32 -w 1 loadtest.py
echo "zzzzz (30s)"
sleep 30

echo "----- Run #8 (-p 38 -w 1) -----"
molotov -d 60 -cx -p 38 -w 1 loadtest.py
