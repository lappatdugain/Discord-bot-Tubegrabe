from pytubefix import YouTube
from moviepy.editor import *

class VideoTooLongExeception(Exception):
    """The video is too long"""


def url_youtube_mp3(url):
    os.mkdir('./tmp')
    yt = YouTube(url)
    title = yt.title
    caractere_speciaux = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '&', '=', '?', '%', '『』', '「」', '$']
    for caractereSpecial in caractere_speciaux:
        title = title.replace(caractereSpecial, '_')
    size_video = yt.length
    if size_video >= 1620:
        raise VideoTooLongExeception("The video is too long, the limit is 27 minutes")
    path = './tmp'
    yt.streams.get_audio_only().download(output_path=path, filename=f'{title}.mp4')
    mp3 = os.path.join(path, f'{title}.mp3')
    with AudioFileClip(os.path.join(path, f'{title}.mp4')) as video:
        video.write_audiofile(mp3)
    return mp3
