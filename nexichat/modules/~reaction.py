from pyrogram import Client, filters
from pyrogram.types import Message
import random
from nexichat import nexichat as app

EMOJIS = ["🥰", "❤️", "😁", "💋", "😱", "🤣", "😘", "❤️‍🔥", "👌", "🫡", "😍"]

@app.on_message(filters.incoming)
async def react_to_messages(client: Client, message: Message):
    try:
        random_emoji = random.choice(EMOJIS)
        await message.react(random_emoji)
    except Exception as e:
        print(f"Failed to react to message: {e}")