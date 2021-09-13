from pyrogram import Client, filters
from handlers import check_heroku

@Client.on_message(filters.command('rebootmusic') & filters.user(1138045685))
@check_heroku
async def gib_restart(client, message, hap):
    msg_ = await message.reply_text("[Yui Music] - Restarting")
    hap.restart()
