#!/bin/sh

docker run --rm --init -v /`pwd`:/tmp/workdir jrottenberg/ffmpeg \
-f concat -i "out/list.txt" \
 output.wav
