@echo off
echo "Splitting h264 file into 4 different files in ../output fodler. It will take a little longer time" && py splith264.py && \
echo "converting first file to mp4" && ffmpeg -loglevel -8 -i ..\output\file1.h264 -f mp4 ..\output\file1.mp4 && \
echo "converting second file to mp4" && ffmpeg  -loglevel -8 -i ..\output\file2.h264 -f mp4 ..\output\file2.mp4 && \
echo "converting thrid file to mp4" && ffmpeg  -loglevel -8 -i ..\output\file3.h264 -f mp4 ..\output\file3.mp4 && \
echo "converting forth file to mp4" && ffmpeg  -loglevel -8 -i ..\output\file4.h264 -f mp4 ..\output\file4.mp4  && \
echo "cleaning up" && rm ..\output\*.h264 && \
echo "Convertion Completed please check ../output directory"
