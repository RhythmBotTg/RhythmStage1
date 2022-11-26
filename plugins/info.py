import os
import time
from yt_dlp import YoutubeDL
from pyrogram import Client
from pyrogram.types.messages_and_media import Message


async def info(bot:Client,msg:Message) :
    start=time.time()
    video_url = "https://youtu.be/4jTy5jnMkYc"
    video_info = YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    stop = time.time()
    await msg.reply_text(f"{stop - start} secs")
