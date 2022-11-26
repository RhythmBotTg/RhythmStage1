
import json
import glob
import importlib
import platform
from lib import config
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import Message
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputMessageContent, InlineKeyboardButton, InlineKeyboardMarkup,CallbackQuery


print(config.API_HASH)


app = Client(config.SESSION,api_id=int(config.API_ID),api_hash=config.API_HASH ,bot_token=config.TOKEN)


plugins = []
files = glob.glob("./plugins/*.py")
for file in files :
    plugin_ = file.split("/")[2].split(".")[0]
    plugins.append(plugin_)
    print(f"{plugin_} loaded successfully")

print(platform.system())

@app.on_message(filters.command(plugins))
async def commands(bot:Client,event:Message):
    command = event.text.replace("/","").split(" ")[0]
    module = importlib.import_module(f"plugins.{command}")
    plugin = getattr(module,command)
    await plugin(bot,event)



@app.on_callback_query()
async def callback_query(bot:Client,cb:CallbackQuery) :
    main_menu = InlineKeyboardMarkup(
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
                )



    backNclose = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Back",callback_data="back"),
                    InlineKeyboardButton("Close",callback_data="close")
                    ]
                ]
            )


    #BACK
    if cb.data == "help" or cb.data == "back" :
        await cb.edit_message_text("""🇭 🇪 🇱 🇵 

нey тнere clιcĸ oɴ тнe вelow coммαмdѕ тo ĸɴow wнαт αre ιтѕ ғυɴcтιoɴѕ""",reply_markup=main_menu)


    #SEARCH
    elif cb.data == "search" :
        await cb.edit_message_text("""🇸 🇪 🇦 🇷 🇨 🇭

/search hᥱᥣρs ყoᥙ to sᥱᥲᥴh for songs ᥲnd gᥱt ιts sρotιfყ ᥣιnk


ᥱxᥲmρᥣᥱ : /search prettymuch eyes off you""",reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Back",callback_data="back"),
                    InlineKeyboardButton("Close",callback_data="close")
                    ]
                ]
            ))


    #CLOSE
    elif cb.data == "close" :
        await bot.delete_messages(chat_id=cb.message.chat.id,message_ids=cb.message.id)




    #GET
    elif cb.data == "get" :
        await cb.edit_message_text("""🇬 🇪 🇹

/get hᥱᥣρs ყoᥙ to sᥱᥲrᥴh ᥲnd gᥱt thᥱ song foᥙnd bყ mᥱ ᥲs ᥲn mρ3 fιᥣᥱ



ᥱxᥲmρᥣᥱ : /get deepak tharam""",reply_markup=backNclose)




    #GRAB
    elif cb.data == "grab" :
        await cb.edit_message_text("""🇬 🇷 🇦 🇧

hᥱᥣρs ყoᥙ to ᥴonvᥱrt ᥲnყ sρotιfყ ᥣιnk of ᥲnყ song or ρᥣᥲყᥣιst ιnto mρ3 fιᥣᥱ 

ɴᴏᴛᴇ : ყoᥙ ᥴᥲn onᥣყ ᥴonvᥱrt trᥲᥴks ᥲnd ρᥣᥲყᥣιst ιnto mρ3 fιᥣᥱs ᥲnყ othᥱr tყρᥱs or ᥣιnks ᥕont bᥱ ᥲᥴᥴᥱρtᥱd .  


ᥱxᥲmρᥣᥱ : /grab https://open.spotify.com/playlist/3OXuQV6QPwjEJGVJZhTtre?si=u12LD3U8Q4SpE_c9x1DXtw&utm_source=copy-link
ᥱxᥲmρᥣᥱ : /grab https://open.spotify.com/track/1h819b9tDPeqf9oKltPQ2Q?si=qiTp39DXQIuvmGVQA0TlKQ&utm_source=copy-link""",reply_markup=backNclose)





    #INFO
    elif cb.data == "info" :
        await cb.edit_message_text("""🇮 🇳 🇫 🇴 

hᥱᥣρs ყoᥙ to gᥱt ιnfo


ᥱxᥲmρᥣᥱ : /info""",reply_markup=backNclose)




    #START
    elif cb.data == "start" :
        await cb.edit_message_text("""🇸 🇹 🇦 🇷 🇹 

hᥱᥣρs ყoᥙ to knoᥕ ιf ι'm ᥲᥣιvᥱ or not 😅""",reply_markup=backNclose)



    elif cb.data == "about" :
        await cb.edit_message_text("""🇦 🇧 🇴 🇺 🇹

ᴄʀᴇᴀᴛᴏʀ : [sᴘʏᠰᴅᴣᴙ](t.me/nxnd_u)
ᴘʀᴏɢʀᴀᴍᴍɪɴɢ ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](https://www.python.org)
ᴍᴀɪɴ ʟɪʙʀᴀʀʏ : [ᴘʏʀᴏɢʀᴀᴍ](https://pyrogram.org)""",reply_markup=backNclose)







app.run()
