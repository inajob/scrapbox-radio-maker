set -x

PYTHONUTF8=1 python scrapbox2list.py original.txt > out/converted.txt
python make.py out/converted.txt
sh -x mklist.sh
sh -x mkwav.sh
