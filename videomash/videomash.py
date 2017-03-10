import os
import requests
from bs4 import BeautifulSoup
import moviepy.editor as mp
import random
import sys

def download_file(url):
    local_filename = url.split('/')[-1]
    if os.path.exists(local_filename):
        return local_filename

    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
    return local_filename


def get_videos(q):
    downloaded_videos = []

    url = 'https://www.shutterstock.com/video/search/?searchterm=' + q
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    videos = soup.select('li.clip-item')
    for video in videos[0:9]:
        src = video.get('data-preview_url')
        src = 'http:' + src
        filename = download_file(src)
        downloaded_videos.append(filename)

    return downloaded_videos


def mash(phrase1, phrase2, outfile=None):
    phrase1_videos = get_videos(phrase1)
    phrase2_videos = get_videos(phrase2)
    videos = phrase2_videos + phrase1_videos
    random.shuffle(videos)

    clips = []
    for video in videos:
        clip = mp.VideoFileClip(video)
        start = clip.duration/2
        clip = clip.subclip(start, start + 0.3)
        clips.append(clip)

    if outfile is None:
        outfile = phrase1+phrase2+'.mp4'
        outfile = outfile.replace(' ', '_')

    composite = mp.concatenate_videoclips(clips, method="compose")
    composite.write_videofile(outfile, fps=24)




if __name__ == '__main__':
    mash(sys.argv[1], sys.argv[2])

