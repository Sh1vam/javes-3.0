#BY SH1VAM DONT KANG
from ub import client, CMD_HELP, CMD_LIST
from telethon import events
from ub.events import javes05, rekcah05, zzaacckkyy, remove_plugin, load_module
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from ub.utils import command, remove_plugin, load_module
from pathlib import Path
from ub import LOAD_PLUG
from datetime import datetime
DELETE_TIMEOUT = 5
import sys, asyncio, traceback, os, importlib
import ub.utils
from ub import CMD_HELP, ALIVE_NAME, PM_MESSAGE, JAVES_NAME, JAVES_MSG, ORI_MSG
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)
import os
import re
import urllib
from math import ceil
from ub import tebot as tgbot
from ub import bot as borg
import requests
from telethon import Button, custom, events, functions
  



import aiohttp
import math
import heroku3
fallback = None
from operator import itemgetter
from ub import (HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HELP, BOTLOG, BOTLOG_CHATID, JAVES_NAME)
from ub.events import javes05, rekcah05 as admin_cmd
heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
useragent = (
    'Mozilla/5.0 (Linux; Android 10; SM-G975F) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/81.0.4044.117 Mobile Safari/537.36'
)

@tgbot.on(events.InlineQuery(pattern=r"send (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    me = await client.get_me()
    if event.query.user_id == me.id:
        input_str = event.pattern_match.group(1)
        try:
            sh1vam = builder.document(f"./ub/plugs/{input_str}.py",title=f"{input_str}.py",description=f"Module {input_str} Found",text=f"{input_str}.py use .neko to paste in neko bin",buttons=[[Button.switch_inline("Search Again", query="send ", same_peer=True)],], )
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
@tgbot.on(events.InlineQuery(pattern=r"hsend (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    me = await client.get_me()
    if event.query.user_id == me.id:
        input_str = event.pattern_match.group(1)
        try:
            sh1vam = builder.document(f"./ub/helpers/{input_str}.py",title=f"{input_str}.py",description=f"Module {input_str} Found",text=f"{input_str}.py use .neko to paste in neko bin",buttons=[[Button.switch_inline("Search Again", query="send ", same_peer=True)],], )
            await event.answer([sh1vam])
            return
        except:
            shivamscode = builder.article(title=f"Module {input_str}.py Not Found",description=f"No Such Module",text=f"No Module Named {input_str}.py",buttons=[[Button.switch_inline("Search Again", query="hsend ", same_peer=True)],], )
            await event.answer([shivamscode])
            return
    if not event.query.user_id == me.id:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/Sh1vam/javes-3.0  ",buttons=[[Button.switch_inline("Search Again", query="hsend ", same_peer=True)],], )
        await event.answer([resultm])
        return
@tgbot.on(events.InlineQuery(pattern=r"ssend (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    me = await client.get_me()
    if event.query.user_id == me.id:
        input_str = event.pattern_match.group(1)
        try:
            sh1vam = builder.document(f"./ub/plugs/sqls/{input_str}.py",title=f"{input_str}.py",description=f"Module {input_str} Found",text=f"{input_str}.py use .neko to paste in neko bin",buttons=[[Button.switch_inline("Search Again", query="send ", same_peer=True)],], )
            await event.answer([sh1vam])
            return
        except:
            shivamscode = builder.article(title=f"Module {input_str}.py Not Found",description=f"No Such Module",text=f"No Module Named {input_str}.py",buttons=[[Button.switch_inline("Search Again", query="ssend ", same_peer=True)],], )
            await event.answer([shivamscode])
            return
    if not event.query.user_id == me.id:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/Sh1vam/javes-3.0  ",buttons=[[Button.switch_inline("Search Again", query="ssend ", same_peer=True)],], )
        await event.answer([resultm])
        return
@tgbot.on(events.InlineQuery(pattern=r"logs"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    me = await client.get_me()
    if event.query.user_id == me.id:
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY);app = Heroku.app(HEROKU_APP_NAME)
        except:
            shivamslog = builder.article(title="Cant Get It",description="Configuration Error",text="Please Check Heroku App Name It Must Be Same As Your App Name Or Check Heroku Api Key U Can Regenerate From https://dashboard.heroku.com/account Scroll Down Regenerate And Change In settings Of App U Need To Reveal Config Vars",buttons=[[Button.switch_inline("Search Again", query="logs", same_peer=True)],], )
            await event.answer([shivamslog])
            return
        else:
            with open('logs.txt', 'w') as log:
                log.write(app.get_log())
            shivamlog=builder.document("logs.txt",title="Logs",description="logs of 100+ lines use .paste to past in dogbin",text="use .paste to paste inn dogbin",buttons=[[Button.switch_inline("Search Again", query="logs", same_peer=True)],], )
            await event.answer([shivamlog])
            return os.remove('logs.txt')
    if not event.query.user_id == me.id:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/Sh1vam/javes-3.0  ",buttons=[[Button.switch_inline("Search Again", query="logs", same_peer=True)],], )
        await event.answer([resultm])
        return
