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

    await event.delete()
    sed = await event.get_reply_message()
    linc = event.text
    link=linc[6:]
    pic=linc[30:]
    os.system(f'wget {link}')

    img = await borg.download_media(sed.media, sedpath)

    mon = f"{pic}"
    foreground = Image.open(mon).convert("RGBA")

    img = cv2.VideoCapture(img) 
    tales, miraculous = img.read()
    bug = cv2.imwrite("shivamcpic.jpg", miraculous)

    background = Image.open("shivamcpic.jpg").convert("RGB")
    with Image.open("shivamcpic.jpg") as imge:
        width, height = imge.size
    fg_resized = foreground.resize((width, height))
    background.paste(fg_resized, box=(0, 0), mask=fg_resized)

    background.save("cpic.png")


    await event.client.send_file(event.chat_id, "cpic.png", force_document=False, reply_to=event.reply_to_msg_id)

    os.remove("cpic.png")
