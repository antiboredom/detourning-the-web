import moviepy.editor as mp

video1 = mp.VideoFileClip('pelosi1.mp4')
video2 = mp.VideoFileClip('pelfunny.mp4')

final_video = mp.concatenate_videoclips([video1, video2])
final_video.write_videofile('composition.mp4')
