#!/usr/bin/env bash

# Script to extract physcial-chemical information for amino acids

echo Creating virtual environment for amino acid feature extraction...

conda update -n base conda # to update to latest version of conda
conda remove --name feature_extraction --all # to remove any previously installed environments called feature_extraction
conda activate base
conda env create -f environment.yml
conda activate feature_extraction

echo Virtual environment ready

echo Downloading amino acid physical-chemical features from //ftp.genome.jp/pub/db/community/aaindex/...

python3 ./amino_acid_feature_extraction/ftp_call.py

echo Downloading amino acid physical-chemcial features from PubChem...

python3 ./amino_acid_feature_extraction/test_pubchem_api.py
cat test_data.txt # Read the status of the HTML request
rm test_data.txt

DATA_PATH="./data"
OUTPUT_PATH="./output"
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

python3 ./amino_acid_feature_extraction/combine_features.py

ls $OUTPUT_PATH

echo Feature extraction complete

echo Starting data standardisation...

python3 ./amino_acid_feature_extraction/normalisation.py

echo Data standardisation complete

echo Starting one-hot encoding...

python3 ./amino_acid_feature_extraction/one_hot_encoding.py

echo One-hot encoding complete

echo Feature extraction is now complete. Data files generated can be found in

cd $OUTPUT_PATH
pwd

echo and include the following files...

ls
cd ../

conda deactivate

echo Script completed
