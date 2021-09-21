import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from callsmusic.callsmusic import client as Yui
from config import SUDO_USERS

@Client.on_message(filters.command(["gst"]))
async def broadcast(_, message: Message):
    if message.from_user.id not in SUDO_USERS:
        return

    wtf = await message.reply("`Starting broadcast...`")
    if not message.reply_to_message:
        await wtf.edit("Please reply to a message to start broadcast!")
        return
    lmao = message.reply_to_message.text
    sent=0
    failed=0
    async for dialog in Yui.iter_dialogs():
        try:
            await Yui.send_message(dialog.chat.id, lmao)
            sent += 1
            await wtf.edit(f"`Broadcasting...` \n\n**Sent to:** `{sent}` chats \n**Failed in:** {failed} chats")
            await asyncio.sleep(3)
        except:
            failed += 1
    await message.reply_text(f"`Gcast succesfully` \n\n**Sent to:** `{sent}` chats \n**Failed in:** {failed} chats")
