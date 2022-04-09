echo "" > out/list.txt
for f in `ls out/audio*.wav`; do echo "file $f" >> out/list.txt; done;

