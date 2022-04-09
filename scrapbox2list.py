# -*- coding: utf-8 -*-

import re
import os
import sys
import codecs

yomi = {
"scrapbox": "スクラップボックス",
"project": "プロジェクト",
"discord": "ディスコード",
"line": "ライン",
"openexternalbrowser": "オープンエクスターナルブラウザ",
"vim": "ビム",
"jp": "ジェーピー",
"slack": "スラック",
"evernote": "エバーノート",
"bot": "ボット",
}
speakerMap = [
  3,8,10,9,11,12,13,14,16,
  1,15
]

midashi = yomi.keys()
if(len(sys.argv) != 2):
    print("usage: %s filename" % (sys.argv[0]))
    os.exit()
fileName = sys.argv[1]

with open(fileName, encoding="utf8") as f:
    level = 0
    unknowns = {}
    authorSpeakerMap = {}
    speakerIndex = 0

    for i, line in enumerate(f):
        author = []
        kind = ""
        speakerNo = 2;
        line = line.rstrip()
        # インデントを数える
        for c in line:
            if c == "\t" or c == " " or c == "　":
                level = level + 1;
            else:
                break;
        line = re.sub('^[ \t　]+', '', line)
        # 話者を記録
        # 末尾にあるicon記法を除去
        authorRe = re.compile(r'\[([^\]]*)\.icon\]$')
        while(True):
            m = authorRe.search(line)
            if m:
                author.append(m.group(1))
                line = authorRe.sub("", line)
                continue
            break;

        # アルファベットを読みに変換
        for w in midashi:
            line = re.sub(w, yomi[w], line, flags=re.IGNORECASE)

        # 辞書にない未知の単語を探す
        for w in re.findall(r"[a-zA-Z]{2,}", line):
            unknowns[w] = True

        if i == 0:
            kind = "title"
        else:
            if len(author) > 0:
                kind = "speak"
                if authorSpeakerMap.get(author[0]) == None:
                    authorSpeakerMap[author[0]] = speakerIndex
                    speakerIndex = speakerIndex + 1
                    if speakerIndex >= len(speakerMap):
                        speakerIndex = 0
                speakerNo = speakerMap[authorSpeakerMap[author[0]]]
            else:
                if len(line) == 0:
                    kind = "silence"
                    speakerNo = 0
                else:
                    kind = "narration"
        #print(level, speakerNo, kind, line, author)
        print(str(speakerNo) + "," + line)

    if(len(unknowns.keys()) > 0):
        print("unknowns", unknowns.keys())
