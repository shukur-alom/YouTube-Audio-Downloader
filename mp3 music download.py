import subprocess
import youtube_dl #youtube-dl==2020.5.29


def run():
    video_url = input("Please enter the YouTube Video URL: ")
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False
    )
    filename = f"{video_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    subprocess.call(["open", filename])


if __name__ == '__main__':
    try:run()
    except: pass