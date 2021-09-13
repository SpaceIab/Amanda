__all__ = ["DB", "save_data", "load_data"]

import json
from typing import Dict

from assistant import bot
from pyrogram.errors import MessageNotModified


class DB:
    CHANNEL_ID = id
    WARN_LIMIT_ID = 7
    WARN_MODE_ID = 8
    WARN_DATA_ID = 9
    BLACKLIST_MODE_ID = 10
    BLACKLIST_DATA_ID = 11


async def load_data(msg_id: int) -> Dict:
    msg = await bot.get_messages(DB.CHANNEL_ID, msg_id)
    if msg:
        return json.loads(msg.text)
    return {}


async def save_data(msg_id: int, text: str) -> None:
    try:
        await bot.edit_message_text(
            DB.CHANNEL_ID,
            msg_id,
            f"`{text}`",
            disable_web_page_preview=True
        )
    except MessageNotModified:
        pass
