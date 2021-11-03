from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.input_stream import InputAudioStream

from config import API_HASH, API_ID, SESSION_NAME
from . import queues

client = Client(SESSION_NAME, API_ID, API_HASH)
pytgcalls = PyTgCalls(client)


@pytgcalls.on_stream_end()
def on_stream_end(chat_id: int) -> None:
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        pytgcalls.leave_group_call(chat_id)
    else:
        pytgcalls.change_stream(
            chat_id,
            InputAudioStream(
                queues.get(chat_id)["file"],
            ),
        )


run = pytgcalls.start
