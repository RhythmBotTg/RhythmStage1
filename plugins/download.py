import os
from pytube import YouTube
from pyrogram import Client
from pyrogram.types.messages_and_media import Message


async def download(bot:Client,msg:Message) :
    data = YouTube(msg.text.replace("/get ",""))
    video = data.streams.filter(only_audio=True).first()
    await msg.reply("ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ...")
    raw_file = video.download(output_path=".")
    base, ext = os.path.splitext(raw_file)
    document = f"{base}.mp3"
    os.rename(raw_file,document)
    await msg.reply("sending")
    await msg.reply_document(document)
    os.remove(document)



