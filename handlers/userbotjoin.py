# Credit DaisyXMusic, Changes By UserLazy, Improve Code By zYxDevs

from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from helpers.decorators import authorized_users_only, errors
from callsmusic.callsmusic import client as USER
from config import SUDO_USERS, BOT_USERNAME

@Client.on_message(filters.command(["userbotjoin", f"userbotjoin@{BOT_USERNAME}"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Add me admin first</b>",
        )
        return
    try:
        user = await USER.get_me()
    except:
        user.first_name = "@JinakuShibagen"
    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "🤖: I'm joined here for playing music on voice chat")
    except UserAlreadyParticipant:
        await message.reply_text(
            f"<b>{user.first_name} Already join this Group</b>",
        )
#
        return
#
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>Flood Wait Error\n{user.first_name} can't join your group due to many join requests for userbot! Make sure the user is not banned in the group."
            f"\n\nOr manually add @JinakuShibagen to your Group and try again.</b>",
        )
        return
    await message.reply_text(
        f"<b>{user.first_name} Join Seccsesfully</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave", f"userbotleave@{BOT_USERNAME}"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.send_message(message.chat.id, "🤖: I'm leaving now, goodbye everyone 😭. Join @CyberSupportGroup and @CyberMusicProject for support.")
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>Users cannot leave your group! Probably waiting for floodwaits."
            "\n\nOr manually remove me from your Group</b>",
        )
        return

    
@Client.on_message(filters.command(["userbotleaveall", f"userbotleaveall@{BOT_USERNAME}"]))
async def bye(client, message):
    if message.from_user.id not in SUDO_USERS:
        return

    left=0
    failed=0
    lol = await message.reply("**Assistant leaving all chats**")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
        except:
            failed += 1
            await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
        await asyncio.sleep(0.7)
    await client.send_message(message.chat.id, f"Left {left} chats. Failed {failed} chats.")
