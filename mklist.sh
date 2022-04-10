cd out
echo "" > list.txt
for f in `ls audio*.wav`; do echo "file $f" >> list.txt; done;

