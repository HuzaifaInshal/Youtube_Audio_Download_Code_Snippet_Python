from __future__ import unicode_literals 
import yt_dlp as youtube_dl
import os

ydl_opts = {
    'format': 'bestaudio',
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(
        'https://www.youtube.com//watch?v=z8M8YZj71NM', download=False)
    url = info['url']  # Direct download URL
    print("Direct download URL:", url)
    # filename = ydl.prepare_filename(info)
    # os.rename(filename, filename[:-4] + "mp3")  # Rename the file by changing extension
    # print("File downloaded and renamed successfully.")



## USING pytube
##from pytube import YouTube
##import os
##
##yt = YouTube('link')
##
##video = yt.streams.filter(only_audio=True).first()
##
##out_file = video.download(output_path=".")
##
##base, ext = os.path.splitext(out_file)
##new_file = base + '.mp3'
##os.rename(out_file, new_file)




    
## USING yt_dlp AGAIN
##import yt_dlp
##
##def download_audio(url, output_path):
##    ydl_opts = {
##        'format': 'bestaudio/best',
##        'postprocessors': [{
##            'key': 'FFmpegExtractAudio',
##            'preferredcodec': 'mp3',
##            'preferredquality': '192',
##        }],
##        'outtmpl': output_path,
##    }
##
##    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
##        ydl.download([url])
##
##if __name__ == "__main__":
##    video_url = "https://www.youtube.com/watch?v=kXYiU_JCYtU"
##    output_path = "./output_filename.mp3"
##    download_audio(video_url, output_path)
##


