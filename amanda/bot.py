__all__ = ["bot", "START_TIME"]

import time

from pyrogram import Client

from . import Config, logging

_LOG = logging.getLogger(__name__)
START_TIME = time.time()

bot = Client(":memory:",
             api_id=Config.APP_ID,
             api_hash=Config.API_HASH,
             bot_token=Config.BOT_TOKEN,
             plugins={'root': "amanda.plugins",
                      'exclude': ['antiflood', 'blacklist', 'gadmin',  # 😟😞
                                  'report', 'warn', 'verify_new_members']})

_LOG.info("amanda-bot!")
