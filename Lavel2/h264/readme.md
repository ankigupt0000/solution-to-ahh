I was able to convert the whole "20140726_040000_ps.h264" file to single mp4 thorugh ffmpeg.
It was having all four videos in the file and were appearing randomly on screen.

I tried to bread the video in different frames like I did for Level-3/EXE solution and then merge them back.
After search internet I came to know to break h264 encoded video we need to find the start of next frame which is '\x00\x00\x01'.
All frame starts with the same encoding.

After breaking the file into frames (through python), I tried to reassemble the frames in sequential 1,2,3,4 order and crated four files which were having random
fee from all the videos.

Now it was necessary to identify which feed is for which video. I wrote every frame in single file but it didn't work well. Can't open 
single frame in VLC media player.

Then to know information about frames, I searched a lot and got the ffprobe provide information about each frame in a video with command.

ffprobe -show_frame 20140726_040000_ps.h264 | grep pict_type 

Then I started deleting one frame at a time to know what is the first I frame by running above command on edited file again and again.

Then when I figured out first I frame I search the file in hex editor for all I frames through taking initial code of first frame, and I was
able to get all I frame through python.

Then I searched for P frame and got information about it.

Now the most important thing how to reassemble these I frame and P frame. Withe every I frame there is 4 line starting with '\x00\x00\x01' which
are having meta data for I frame and for every P frame there is single line starting with '\x00\x00\x01' for its metadata.

I was able to relate the metadata of I frames.
And was partially able to related different metadata of P frames but not completely.

To some extent I have decode the single .h264 file to multiple .h264 files with having only single video with proper I frame.
The P frames at many places is making the video bad.
Some P frames lot too because not able to relate the p frames.

Some different apporach on python may give a better solution.

I hope I can figure it out.
