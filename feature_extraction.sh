#!/usr/bin/env bash

# Script to extract physcial-chemical information for amino acids

echo Downloading amino acid physical-chemical features from //ftp.genome.jp/pub/db/community/aaindex/...

python3 ftp_call.py

echo Downloading amino acid physical-chemcial features from PubChem...

python3 test_pubchem_api.py
cat test_data.txt # Read the status of the HTML request
rm test_data.txt

DATA_PATH="../data"
OUTPUT_PATH="../output"
OUTPUT_FILE_1="predata.txt"
OUTPUT_FILE="data.txt"

rm -rf $OUTPUT_PATH
rm -rf $DATA_PATH
mkdir $DATA_PATH
mkdir $OUTPUT_PATH

mv aaindex1 $DATA_PATH
mv test_data.csv $OUTPUT_PATH

echo Extracting index data...

for file in ${DATA_PATH}/*
do
    sed 's/^ *//' $file | grep -B2 "//" | grep -e '[-\+]' -e "^[0-9]" -e "^NA" | sed -e 's/--//g' | grep . > $OUTPUT_FILE_1
    cat $OUTPUT_FILE_1 | paste --delimiters=" ", - - > $OUTPUT_FILE # Puts two consecutive lines on the same line
done
    mv $OUTPUT_FILE $OUTPUT_PATH"/"
echo Extraction complete

rm $OUTPUT_FILE_1

echo Combining datasets...

python3 combine_features.py

ls $OUTPUT_PATH

echo Feature extraction complete
