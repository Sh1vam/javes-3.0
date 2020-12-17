import os

import cv2
import numpy as np
import requests
from PIL import Image
from telegraph import upload_file
from telethon.tl.types import MessageMediaPhoto
from userbot.utils import admin_cmd
from userbot import bot 
from userbot import bot as borg
sedpath = "./sh1vam/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)
@borg.on(admin_cmd(pattern=r"cpic"))
async def hmm(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    await event.delete()
    sed = await event.get_reply_message()
    linc = event.text
    link=linc[6:]
    pic=linc[30:]
    os.system(f'wget {link}')
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    mon = f"{pic}"
    foreground = Image.open(mon).convert("RGBA")

    background = Image.open(img).convert("RGB")
    with Image.open(img) as img:
        width, height = img.size
    fg_resized = foreground.resize((width, height))
    background.paste(fg_resized, box=(0, 0), mask=fg_resized)

    background.save("./sh1vam/cpic.png")

    file_name = "cpic.png"
    ok = "./sh1vam/" + file_name
    await borg.send_file(event.chat_id, ok)
    for files in (ok, img):
        if files and os.path.exists(ok):
            os.remove(ok)
