from pyrogram import Client, filters
from pyrogram.types import Message
from nexichat import nexichat as app

@Client.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    await message.reply_text(
                   f"""**❖ Hᴇʏ  {message.from_user.first_name} !, Nɪᴄᴇ Tᴏ Mᴇᴇᴛ Yᴏᴜ !\n\nYᴏᴜ Cᴀɴ Mᴀᴋᴇ Yᴏᴜʀ Oᴡɴ Rᴇᴀᴄᴛɪᴏɴ Bᴏᴛ Bʏ @ReactionCloner_bot.**"""
    )
