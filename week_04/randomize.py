import moviepy.editor as mp
import random

video = mp.VideoFileClip('animals.mp4')

final_clips = []
segment_duration = 1 
total_duration = video.duration

starttime = 0

while starttime < 5:
    endtime = starttime + segment_duration
    print(starttime, endtime)

    clip = video.subclip(starttime, endtime)
    final_clips.append(clip)

    starttime = endtime

random.shuffle(final_clips)

final_video = mp.concatenate_videoclips(final_clips)
final_video.write_videofile('random.mp4')

# clip1 = video.subclip(1, 2)
# clip2 = video.subclip(4, 5)
# clip3 = video.subclip(6, 7)
#
# final_video = mp.concatenate_videoclips([clip1, clip2, clip3])
# final_video.write_videofile('comp.mp4')
