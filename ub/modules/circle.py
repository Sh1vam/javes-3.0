# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

#Ported circle cmd by Sh1vam

import asyncio
import io
import sys
import time
import traceback
from asyncio.exceptions import TimeoutError

import cv2
import emoji

from telethon.utils import pack_bot_file_id

from ub import *
from ub.utils import *







@bot.on(admin_cmd(pattern=r"circle"))
async def _(e):
    a = await e.get_reply_message()
    if a is None:
        return await e.edit( "Reply to a gif or audio")
    if a.document and a.document.mime_type == "audio/mpeg":
        z = await e.edit( "**Cʀᴇᴀᴛɪɴɢ Vɪᴅᴇᴏ Nᴏᴛᴇ**")
        toime = time.time()
        try:
            bbbb = await a.download_media(thumb=-1)
            im = cv2.imread(bbbb)
            dsize = (320, 320)
            output = cv2.resize(im, dsize, interpolation=cv2.INTER_AREA)
            cv2.imwrite("img.png", output)
            thumb = "img.png"
        except TypeError:
            thumb = "thumb.jpg"
        c = await a.download_media(
            "./downloads/",
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, z, toime, "**Dᴏᴡɴʟᴏᴀᴅɪɴɢ...**")
            ),
        )
        await z.edit("**Dᴏᴡɴʟᴏᴀᴅᴇᴅ...\nNᴏᴡ Cᴏɴᴠᴇʀᴛɪɴɢ...**")
        cmd = [
            "ffmpeg",
            "-i",
            c,
            "-acodec",
            "libmp3lame",
            "-ac",
            "2",
            "-ab",
            "144k",
            "-ar",
            "44100",
            "comp.mp3",
        ]
        proess = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proess.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
        mcd = [
            "ffmpeg",
            "-y",
            "-i",
            thumb,
            "-i",
            "comp.mp3",
            "-c:a",
            "copy",
            "circle.mp4",
        ]
        process = await asyncio.create_subprocess_exec(
            *mcd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
        taime = time.time()
        await e.client.send_file(
            e.chat_id,
            "circle.mp4",
            thumb=thumb,
            video_note=True,
            reply_to=a,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, z, taime, "**Uᴘʟᴏᴀᴅɪɴɢ...**")
            ),
        )
        await z.delete()
        os.system("rm ./downloads/*")
        os.system("rm circle.mp4 comp.mp3 img.png")
        os.remove(bbbb)
    elif a.document and a.document.mime_type == "video/mp4":
        z = await e.edit( "**Cʀᴇᴀᴛɪɴɢ Vɪᴅᴇᴏ Nᴏᴛᴇ**")
        c = await a.download_media("./downloads/")
        await e.client.send_file(e.chat_id, c, video_note=True, reply_to=a)
        await z.delete()
        os.remove(c)
    else:
        return await e.edit( "**Reply to a gif or audio file only**")


