#!/bin/bash

#Include

'''
mkdir -p temp/negs/
mkdir -p temp/poss/
FILES=$(find /mnt/hgfs/medium/Benign/ -type f -name '*.pcap')
FILES2=$(find /mnt/hgfs/medium/Adware/ -type f -name '*.pcap')

for filename in $FILES; do
    input_path="$filename"
    output_path="${input_path%.pcap}.gz"
    echo "Processing ${input_path##*/}"
    ../joy/bin/joy bidir=1 tls=1 dist=1 "$input_path" > "temp/negs/${output_path##*/}"
done

for filename in $FILES2; do
    input_path="$filename"
    output_path="${input_path%.pcap}.gz"
    echo "Processing ${input_path##*/}"
    ../joy/bin/joy bidir=1 tls=1 dist=1 "$input_path" > "temp/poss/${output_path##*/}"
done

echo "================================================================================="
echo "Done Processing files"
echo "================================================================================="
echo " "
echo " "

#input_path="$1"
#output_path="${input_path%.pcap}.gz"



#../joy/bin/joy bidir=1 tls=1 dist=1 "$input_path" > "temp/${output_path}"
'''

#echo "$output_path" 
echo "Running Python Script"
python trench.py temp/poss/ temp/negs/
