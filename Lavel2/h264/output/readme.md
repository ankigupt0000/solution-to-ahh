splitted h264 file will be available here. and that will be converted to mp4 with shell script having following command.

ffmpeg -i file1.h264 -c:v libx264 -c:a copy file1.mp4

for running h264 file in VLC change the preference of VLC by viewing all settings.
Under "Input/Codecs --> Demuxers" select "H264 Video Demuxer"

h264 files can also be converted by VLC by saving as option.
