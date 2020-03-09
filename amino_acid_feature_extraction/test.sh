#!/usr/bin/env bash

# Script to extract physcial-chemical information for amino acids

DATA_PATH="../data"
OUTPUT_PATH="../output"
OUTPUT_FILE="data.txt"

echo Extracting index data...

for file in "${DATA_PATH}/*"
do
    sed 's/^ *//' $file | grep "^[0-9]" > $OUTPUT_FILE # To remove white space at the beginning of the line and then to select only lines beginning with numbers
done
    mv $OUTPUT_FILE $OUTPUT_PATH"/"
echo Extraction complete

#for file in "${DATA_PATH}/"*
#do
#    echo Extracting index data...
#    grep "^ATOM.*CA\|^END\|^ENDMDL\|^MODEL" "${DATA_PATH}/${TARGET}.pdb" > "${OUTPUT_PATH}/${TARGET}_index_data.txt"
#    echo ${file}
#done


#list="$(find . -name '*.pdb')"
#for file in $list
#do
#	TARGET=$(echo "${file##*/}"| cut -f 1 -d '.')
#	TARGET_PATH="${TARGET}/contacts"  # Path to the directory with the target input data.
#
#	grep "^ATOM.*CA\|^END\|^ENDMDL\|^MODEL" "${TARGET_PATH}/${TARGET}.pdb" > "${TARGET_PATH}/${TARGET}_backbone_carbon_alpha.pdb"
#done
