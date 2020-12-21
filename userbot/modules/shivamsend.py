#BY SH1VAM DONT KANG
from userbot import client, CMD_HELP, CMD_LIST
from telethon import events
from userbot.events import javes05, rekcah05, zzaacckkyy, remove_plugin, load_module
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from userbot.utils import command, remove_plugin, load_module
from pathlib import Path
from userbot import LOAD_PLUG
from datetime import datetime
DELETE_TIMEOUT = 5
import sys, asyncio, traceback, os, importlib
import userbot.utils
from userbot import CMD_HELP, ALIVE_NAME, PM_MESSAGE, JAVES_NAME, JAVES_MSG, ORI_MSG
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)
import os
import re
import urllib
from math import ceil
from userbot import tebot as tgbot
from userbot import bot as borg
import requests
from telethon import Button, custom, events, functions
@tgbot.on(events.InlineQuery(pattern=r"send (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    me = await client.get_me()
    if event.query.user_id == me.id:
        input_str = event.pattern_match.group(1)
        try:
            sh1vam = builder.document(f"./userbot/modules/{input_str}.py",title=f"{input_str}.py",description=f"Module {input_str} Found",text=f"{input_str}.py",buttons=[[Button.switch_inline("Search Again", query="send ", same_peer=True)],], )
            await event.answer([sh1vam])
            return
        except:
            shivamscode = builder.article(title=f"Module {input_str}.py Not Found",description=f"No Such Module",text=f"No Module Named {input_str}.py",buttons=[[Button.switch_inline("Search Again", query="send ", same_peer=True)],], )
            await event.answer([shivamscode])
            return
    if not event.query.user_id == me.id:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/Sh1vam/javes-3.0  ",buttons=[[Button.switch_inline("Search Again", query="send ", same_peer=True)],], )
        await event.answer([resultm])
        return
