splitted h264 file will be available here. and that will be converted to mp4 with shell script having following command.

ffmpeg -i file1.h264 -c:v libx264 -c:a copy file1.mp4

below command works on windows having ffmpeg in path

ffmpeg -i file1.h264 file1.mp4 

Processed mp4 files are available at following location: 

Due to P frame mismatch these files are having some distortion currently. Trying to related P frames.

https://youtu.be/cgoR-iREu_s 
https://youtu.be/3NXgh7JCjRE
https://youtu.be/lRIo_nIHcSY
https://youtu.be/8E94Fsyaksg

for running h264 file in VLC change the preference of VLC by viewing all settings.
Under "Input/Codecs --> Demuxers" select "H264 Video Demuxer"

h264 files can also be converted by VLC by saving as option but VLC crashes some time, ffmpeg is better option for converting files.
