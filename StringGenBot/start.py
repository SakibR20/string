import time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
uptime = get_readable_time((time.time() - StartTime))
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""🥀 ʜᴇʏ {msg.from_user.mention},

ᴛʜɪs ɪs {me2},
ᴀ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ,\nᴀʟɪᴠᴇ sɪɴᴄᴇ {uptime}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🙄 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 🙄", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("❣️ sᴜᴘᴘᴏʀᴛ ❣️", url="https://t.me/SankiWorldMF"),
                    InlineKeyboardButton("🥀 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🥀", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
