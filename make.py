# -*- coding: utf-8 -*-

import voicevox
import re
import sys
import os
import shutil

if(len(sys.argv) != 2):
    print("usage: %s filename" % (sys.argv[0]))
    os.exit()
fileName = sys.argv[1]

with open(fileName ,encoding="utf8") as f:
    count = 0
    for line in f:
        l = line.rstrip()
        parts = l.split(',')
        print(parts)
        audioFileName = ('out/audio%03d.wav' % (count))
        if(parts[0] == '0'):
            shutil.copyfile("silence.wav", audioFileName)
        else:
            speaker = int(parts[0])
            voicevox.generate_wav(parts[1], speaker=speaker, filepath=audioFileName)
        count = count + 1
