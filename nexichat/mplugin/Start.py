from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from nexichat import nexichat as app

@Client.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton('🔍 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url='https://t.me/SuperToppers0'),
            InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇ ɢʀᴏᴜᴘ', url='https://t.me/SuperToppers')
        ]
    ])
    await message.reply_text(
        f"""❖ Hᴇʏ  {message.from_user.first_name} !, Nɪᴄᴇ Tᴏ Mᴇᴇᴛ Yᴏᴜ !\n\nYᴏᴜ Cᴀɴ Mᴀᴋᴇ Yᴏᴜʀ Oᴡɴ Rᴇᴀᴄᴛɪᴏɴ Bᴏᴛ Bʏ @ReactionCloner_bot.""",
        reply_markup=buttons
    )
