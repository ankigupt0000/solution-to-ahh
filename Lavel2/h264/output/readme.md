splitted h264 file will be available here. and that will be converted to mp4 with shell script having following command.

ffmpeg -i file1.h264 -c:v libx264 -c:a copy file1.mp4
