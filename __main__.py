#SDBOTs <https://t.me/SDBOTs_Inifinity>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SDSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SDSongBot import SDbot as app
from SDSongBot import LOGGER

pm_start_text = """
π Salam! [{}](tg://user?id={}), **MΙn MahnΔ± YΓΌklΙyΙn Botam**
**MΙnΙ Δ°stΙdiyin MahnΔ±nΔ±n AdΔ±n GΓΆndΙr MΙsΙlΙn **
     
Ζmir: : ```/dsong Taladro Kendine Δ°yi Bak```
      
π³π΄ Norway Chat @NorwayChat π₯
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="Kanal πββοΈ", url="https://t.me/NorwayArea"
                    ),
                    InlineKeyboardButton(
                        text="π¨βπ» Sahibim", url="https://t.me/Vusaldeveloper"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("""

βββββββββββββββββββββββββββββββββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββββββββββββββ
βββββββββββββββββββββββ¦ββββββββββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββββββββββββββ
βββββββββββββββββββββββ¦ββββββββββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββββββββββββββ SDSongBot is online.""")
idle()
