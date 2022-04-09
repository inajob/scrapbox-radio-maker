#!/bin/sh

docker run --rm --init -v /`pwd`:/tmp/workdir jrottenberg/ffmpeg \
-f concat -i "list.txt" \
 output.wav
