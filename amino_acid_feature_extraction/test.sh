#!/usr/bin/env bash

# Script to extract physcial-chemical information for amino acids

DATA_PATH="../data"
OUTPUT_PATH="../output"
OUTPUT_FILE_1="predata.txt"
OUTPUT_FILE="data.txt"

echo Extracting index data...

for file in ${DATA_PATH}/*
do
    sed 's/^ *//' $file | grep -B2 "//" | grep -e '[-\+]' -e "^[0-9]" -e "^NA" | sed -e 's/--//g' | grep . > $OUTPUT_FILE_1
    cat $OUTPUT_FILE_1 | paste --delimiters=" ", - - > $OUTPUT_FILE # Puts two consecutive lines on the same line
done
    mv $OUTPUT_FILE $OUTPUT_PATH"/"
echo Extraction complete
