#!/bin/bash
# flawfinder --csv > ./repo/test_folder.csv ./raw/test_folder
name=./repo/$1.csv
path=$2

if [ ! -f "$name" ]; then
  touch "$name"
fi

flawfinder --csv > ./repo/${1}.csv ${2}
