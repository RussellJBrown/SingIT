#Run this code from whatever folder
#you want the data to be in.
from __future__ import unicode_literals
import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=La4Dcd1aUcE'])
    ydl.download(['https://www.youtube.com/watch?v=Kvgz6swo-vY'])
