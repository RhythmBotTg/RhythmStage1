from pyrogram import Client, filters
from pyrogram.types.messages_and_media import Message
from pyrogram.types import Update
from lib import config
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


async def help(bot:Client,msg:Message) :
    await msg.reply_photo("https://telegra.ph/file/763d7859d6c8499ff2f3f.jpg",caption="""🇭 🇪 🇱 🇵

нey тнere clιcĸ oɴ тнe вelow coммαмdѕ тo ĸɴow wнαт αre ιтѕ ғυɴcтιoɴѕ""",reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("sᴇᴀʀᴄʜ",callback_data="search"),
                        InlineKeyboardButton("ɢᴇᴛ",callback_data="get"),
                        InlineKeyboardButton("ɢʀᴀʙ",callback_data="grab")
                    ],
                    [
                        InlineKeyboardButton("ɪɴғᴏ",callback_data="info"),
                        InlineKeyboardButton("sᴛᴀʀᴛ",callback_data="start")
                        ],
                    [
                        InlineKeyboardButton("ᴀʙᴏᴜᴛ",callback_data="about"),
                        InlineKeyboardButton("ᴄʟᴏsᴇ",callback_data="close")
                        ]
                    ]
                ))
