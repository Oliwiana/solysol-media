#!/bin/bash
# finish.sh <id>  – podkład (bez lektora), loudnorm -14, reel.mp4 < 4 MB
id=$1; d=/home/claude/gw/$id; T=$(python3 -c "import json;print(json.load(open('$d/timeline.json'))['total'])")
ffmpeg -loglevel error -y -stream_loop 1 -i /home/claude/gw/noir-bed.mp3 -t $T -af "volume=0.8,afade=t=in:d=0.3,afade=t=out:st=$(python3 -c "print($T-1.8)"):d=1.8,loudnorm=I=-14:TP=-1.5:LRA=11" -ar 44100 $d/audio.m4a
for crf in 28 30 32; do
ffmpeg -loglevel error -y -i $d/video.mp4 -i $d/audio.m4a -map 0:v -map 1:a -c:v libx264 -preset veryfast -crf $crf -maxrate 450k -bufsize 900k -pix_fmt yuv420p -c:a aac -b:a 96k -shortest -movflags +faststart $d/reel.mp4
s=$(stat -c %s $d/reel.mp4); echo "crf $crf size $s"; [ $s -lt 4000000 ] && break; done
