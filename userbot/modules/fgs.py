import os
#os.system("pip install validators")
#os.system("pip install collections")
#os.system("pip install Pillow")

import re
import requests
from validators.url import url
from asyncio import sleep
from random import choice, getrandbits, randint
import random
import time
from telethon import events
from userbot import bot
from collections import deque
import sys
import html
import json
from PIL import Image, ImageEnhance, ImageOps
from userbot import CMD_HELP
from userbot.events import register
from userbot.helpers.functions import *
@register(outgoing=True, pattern=r"\!gsrch(?: |$)(.*)")
async def gcs(event):
    text = event.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = event.message
    if "." in text:
        text1, text2 = text.split(".")
    else:
        await event.edit("`What should i do wth blank message use .gsrch search.reasult`")
    await event.edit(f"`Requesting to google...`")
    img = await fakegs(text1, text2)
    await event.delete()
    await event.client.send_file(event.chat_id, img, reply_to=reply_to_id)
    

