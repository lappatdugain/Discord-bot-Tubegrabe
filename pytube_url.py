from pytubefix import YouTube
from moviepy.editor import *

class VideoTooLongExeception(Exception):
    """The video is too long"""


def url_youtube_mp3(url):
    os.mkdir('./tmp')

    yt = YouTube(url)

    title = yt.title
    caractere_speciaux = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '&', '=', '?', '%', '『』', '「」', '$']
    for char in caractere_speciaux:
        edit_title = title.replace(char, '_')

    if  yt.length >= 1620:
        raise VideoTooLongExeception("The video is too long, the limit is 27 minutes")
    
    path = './tmp'
    mp3_filename = f'{title}.mp3'
    mp3_path = os.path.join(path, mp3_filename)

    audio_stream = yt.streams.get_audio_only()
    downloaded_file_path = audio_stream.download(output_path=path)

    # Convert to .mp3
    with AudioFileClip(downloaded_file_path) as audio:
        audio.write_audiofile(mp3_path)

    return mp3_path

