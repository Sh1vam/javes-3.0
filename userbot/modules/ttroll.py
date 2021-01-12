import os
import re
import time
import urllib.request
import zipfile
from random import choice
#MADE BY SHIVAM
import PIL.ImageOps
import requests
from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import Channel, PollAnswer
from validators.url import url
#MADE BY SHIVAM
import re
import requests
import os
#MADE BY SHIVAM
import pybase64
from telegraph import exceptions, upload_file
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from userbot import bot
#MADE BY SHIVAM
#MADE BY SHIVAM
from userbot.utils import admin_cmd
from userbot.helpers import *
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
from PIL import ImageEnhance, ImageOps
from userbot import CMD_HELP
from userbot.events import register
if not os.path.isdir("./temp/"):
    os.makedirs("./temp/")
async def purge():
    try:
        os.remove("temp.webp")
        os.remove("temp.webp")
    except OSError:
        pass
async def clyde(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=clyde&text={text}"
    ).json()
    season4= r.get("message")
    miraculous = url(season4)
    if not miraculous:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(season4).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"
async def ship(link1,link2):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=ship&user1={link1}&user2={link2}"
    ).json()
    season4= r.get("message")
    miraculous = url(season4)
    if not miraculous:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(season4).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"
'''async def captcha(url,username):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=captcha&url={url}&username={username}"
    ).json()
    season4= r.get("message")
    miraculous = url(season4)
    if not miraculous:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(season4).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"'''
async def whowouldwin(link1,link2):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=whowouldwin&user1={link1}&user2={link2}"
    ).json()
    season4= r.get("message")
    miraculous = url(season4)
    if not miraculous:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(season4).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"
#######
async def ddlc(character,background,body,face,text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=ddlc&character={character}&background={background}&body={body}&face={face}&text={text}"
    ).json()
    season4= r.get("message")
    miraculous = url(season4)
    if not miraculous:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(season4).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"
##22
async def jpeg(link):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=jpeg&url={link}"
    ).json()
    season4= r.get("message")
    miraculous = url(season4)
    if not miraculous:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(season4).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"
'''async def kms(link):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=kms&url={link}"
    ).json()
    season4= r.get("message")
    miraculous = url(season4)
    if not miraculous:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(season4).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"

async def kidnap(image):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=kidnap&image={image}"
    ).json()
    season4= r.get("message")
    miraculous = url(season4)
    if not miraculous:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(season4).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"'''
async def deepfry(image):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=deepfry&image={image}"
    ).json()
    season4= r.get("message")
    miraculous = url(season4)
    if not miraculous:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(season4).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"
async def blurpify(image):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=blurpify&image={image}"
    ).json()
    season4= r.get("message")
    miraculous = url(season4)
    if not miraculous:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(season4).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"
async def magik(image,intensity):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=magik&image={image}&intensity={intensity}"
    ).json()
    season4= r.get("message")
    miraculous = url(season4)
    if not miraculous:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(season4).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"
'''async def clickforhentai(image,fontsize):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=clickforhentai&image={image}&fontsize={fontsize}"
    ).json()
    season4= r.get("message")
    miraculous = url(season4)
    if not miraculous:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(season4).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"'''
'''async def stickbug(image):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=stickbug&url={image}"
    ).json()
    season4= r.get("message")
    miraculous = url(season4)
    if not miraculous:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(season4).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"'''
@register(outgoing=True, pattern=r"^!clyde(?: |$)(.*)")####################
async def cld(event):
    text = event.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    if not text:
        if event.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            await event.edit("`Give text for to write on `")
            return
    await event.edit("`Your chat is under creation wait a sec...`")

    img = await clyde(text)
    await event.client.send_file(event.chat_id, img, reply_to=reply_to_id)
    await event.delete()
    await purge()
@bot.on(admin_cmd(pattern="ship(?: |$)(.*)"))#######################
async def shp(event):
    input_str = event.pattern_match.group(1)
    replied = await event.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await event.edit("reply to a supported media file")
        return
    if replied.media:
        mlcs4 = await event.edit("passing to telegraph...")
    else:
        await event.edit("reply to a supported media file")
        return

    download_lomlcion = await event.client.download_media(replied, "./temp/")
    if download_lomlcion.endswith((".webp")):
        download_lomlcion = convert_toimage(download_lomlcion)
    size = os.stat(download_lomlcion).st_size
    if download_lomlcion.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await mlcs4.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_lomlcion)
            return
        await mlcs4.edit("generating image..")
    else:
        await mlcs4.edit("the replied file is not supported")
        os.remove(download_lomlcion)
        return
    try:
        response = upload_file(download_lomlcion)
        os.remove(download_lomlcion)
    except exceptions.TelegraphException as exc:
        await mlcs4.edit("ERROR: " + str(exc))
        os.remove(download_lomlcion)
        return
    mlc = f"https://telegra.ph{response[0]}"
    mlc = await ship(mlc,input_str)
    await mlcs4.delete()
    await event.client.send_file(event.chat_id, mlc, reply_to=replied)
'''@bot.on(admin_cmd(pattern="captcha(?: |$)(.*)"))
async def captch(event):
    input_str = event.pattern_match.group(1)
    replied = await event.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await event.edit("reply to a supported media file")
        return
    if replied.media:
        mlcs4 = await event.edit("passing to telegraph...")
    else:
        await event.edit("reply to a supported media file")
        return

    download_lomlcion = await event.client.download_media(replied, "./temp/")
    if download_lomlcion.endswith((".webp")):
        download_lomlcion = convert_toimage(download_lomlcion)
    size = os.stat(download_lomlcion).st_size
    if download_lomlcion.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await mlcs4.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_lomlcion)
            return
        await mlcs4.edit("generating image..")
    else:
        await mlcs4.edit("the replied file is not supported")
        os.remove(download_lomlcion)
        return
    try:
        response = upload_file(download_lomlcion)
        os.remove(download_lomlcion)
    except exceptions.TelegraphException as exc:
        await mlcs4.edit("ERROR: " + str(exc))
        os.remove(download_lomlcion)
        return
    mlc = f"https://telegra.ph{response[0]}"
    mlc = await captcha(mlc,input_str)
    await mlcs4.delete()
    await event.client.send_file(event.chat_id, mlc, reply_to=replied)'''
@bot.on(admin_cmd(pattern="win(?: |$)(.*)"))##############################
async def whowould(event):
    input_str = event.pattern_match.group(1)
    replied = await event.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await event.edit("reply to a supported media file")
        return
    if replied.media:
        mlcs4 = await event.edit("passing to telegraph...")
    else:
        await event.edit("reply to a supported media file")
        return

    download_lomlcion = await event.client.download_media(replied, "./temp/")
    if download_lomlcion.endswith((".webp")):
        download_lomlcion = convert_toimage(download_lomlcion)
    size = os.stat(download_lomlcion).st_size
    if download_lomlcion.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await mlcs4.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_lomlcion)
            return
        await mlcs4.edit("generating image..")
    else:
        await mlcs4.edit("the replied file is not supported")
        os.remove(download_lomlcion)
        return
    try:
        response = upload_file(download_lomlcion)
        os.remove(download_lomlcion)
    except exceptions.TelegraphException as exc:
        await mlcs4.edit("ERROR: " + str(exc))
        os.remove(download_lomlcion)
        return
    mlc = f"https://telegra.ph{response[0]}"
    mlc = await whowouldwin(mlc,input_str)
    await mlcs4.delete()
    await event.client.send_file(event.chat_id, mlc, reply_to=replied)
@bot.on(admin_cmd(pattern="jpeg"))##############################
async def jpg(event):
    #input_str = event.pattern_match.group(1)
    replied = await event.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await event.edit("reply to a supported media file")
        return
    if replied.media:
        mlcs4 = await event.edit("passing to telegraph...")
    else:
        await event.edit("reply to a supported media file")
        return

    download_lomlcion = await event.client.download_media(replied, "./temp/")
    if download_lomlcion.endswith((".webp")):
        download_lomlcion = convert_toimage(download_lomlcion)
    size = os.stat(download_lomlcion).st_size
    if download_lomlcion.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await mlcs4.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_lomlcion)
            return
        await mlcs4.edit("generating image..")
    else:
        await mlcs4.edit("the replied file is not supported")
        os.remove(download_lomlcion)
        return
    try:
        response = upload_file(download_lomlcion)
        os.remove(download_lomlcion)
    except exceptions.TelegraphException as exc:
        await mlcs4.edit("ERROR: " + str(exc))
        os.remove(download_lomlcion)
        return
    mlc = f"https://telegra.ph{response[0]}"
    mlc = await jpeg(mlc)
    await mlcs4.delete()
    await event.client.send_file(event.chat_id, mlc, reply_to=replied)
'''@bot.on(admin_cmd(pattern="kms"))
async def kms_kms(event):
    #input_str = event.pattern_match.group(1)
    replied = await event.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await event.edit("reply to a supported media file")
        return
    if replied.media:
        mlcs4 = await event.edit("passing to telegraph...")
    else:
        await event.edit("reply to a supported media file")
        return

    download_lomlcion = await event.client.download_media(replied, "./temp/")
    if download_lomlcion.endswith((".webp")):
        download_lomlcion = convert_toimage(download_lomlcion)
    size = os.stat(download_lomlcion).st_size
    if download_lomlcion.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await mlcs4.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_lomlcion)
            return
        await mlcs4.edit("generating image..")
    else:
        await mlcs4.edit("the replied file is not supported")
        os.remove(download_lomlcion)
        return
    try:
        response = upload_file(download_lomlcion)
        os.remove(download_lomlcion)
    except exceptions.TelegraphException as exc:
        await mlcs4.edit("ERROR: " + str(exc))
        os.remove(download_lomlcion)
        return
    mlc = f"https://telegra.ph{response[0]}"
    mlc = await kms(mlc)
    await mlcs4.delete()
    await event.client.send_file(event.chat_id, mlc, reply_to=replied)


@bot.on(admin_cmd(pattern="kidnap"))
async def kidnaps(event):
    #input_str = event.pattern_match.group(1)
    replied = await event.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await event.edit("reply to a supported media file")
        return
    if replied.media:
        mlcs4 = await event.edit("passing to telegraph...")
    else:
        await event.edit("reply to a supported media file")
        return

    download_lomlcion = await event.client.download_media(replied, "./temp/")
    if download_lomlcion.endswith((".webp")):
        download_lomlcion = convert_toimage(download_lomlcion)
    size = os.stat(download_lomlcion).st_size
    if download_lomlcion.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await mlcs4.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_lomlcion)
            return
        await mlcs4.edit("generating image..")
    else:
        await mlcs4.edit("the replied file is not supported")
        os.remove(download_lomlcion)
        return
    try:
        response = upload_file(download_lomlcion)
        os.remove(download_lomlcion)
    except exceptions.TelegraphException as exc:
        await mlcs4.edit("ERROR: " + str(exc))
        os.remove(download_lomlcion)
        return
    mlc = f"https://telegra.ph{response[0]}"
    mlc = await kidnap(mlc)
    await mlcs4.delete()
    await event.client.send_file(event.chat_id, mlc, reply_to=replied)'''
@bot.on(admin_cmd(pattern="deep"))
async def fry(event):
    #input_str = event.pattern_match.group(1)
    replied = await event.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await event.edit("reply to a supported media file")
        return
    if replied.media:
        mlcs4 = await event.edit("passing to telegraph...")
    else:
        await event.edit("reply to a supported media file")
        return

    download_lomlcion = await event.client.download_media(replied, "./temp/")
    if download_lomlcion.endswith((".webp")):
        download_lomlcion = convert_toimage(download_lomlcion)
    size = os.stat(download_lomlcion).st_size
    if download_lomlcion.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await mlcs4.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_lomlcion)
            return
        await mlcs4.edit("generating image..")
    else:
        await mlcs4.edit("the replied file is not supported")
        os.remove(download_lomlcion)
        return
    try:
        response = upload_file(download_lomlcion)
        os.remove(download_lomlcion)
    except exceptions.TelegraphException as exc:
        await mlcs4.edit("ERROR: " + str(exc))
        os.remove(download_lomlcion)
        return
    mlc = f"https://telegra.ph{response[0]}"
    mlc = await deepfry(mlc)
    await mlcs4.delete()
    await event.client.send_file(event.chat_id, mlc, reply_to=replied)
@bot.on(admin_cmd(pattern="brpify"))
async def blurpifry(event):
    #input_str = event.pattern_match.group(1)
    replied = await event.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await event.edit("reply to a supported media file")
        return
    if replied.media:
        mlcs4 = await event.edit("passing to telegraph...")
    else:
        await event.edit("reply to a supported media file")
        return

    download_lomlcion = await event.client.download_media(replied, "./temp/")
    if download_lomlcion.endswith((".webp")):
        download_lomlcion = convert_toimage(download_lomlcion)
    size = os.stat(download_lomlcion).st_size
    if download_lomlcion.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await mlcs4.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_lomlcion)
            return
        await mlcs4.edit("generating image..")
    else:
        await mlcs4.edit("the replied file is not supported")
        os.remove(download_lomlcion)
        return
    try:
        response = upload_file(download_lomlcion)
        os.remove(download_lomlcion)
    except exceptions.TelegraphException as exc:
        await mlcs4.edit("ERROR: " + str(exc))
        os.remove(download_lomlcion)
        return
    mlc = f"https://telegra.ph{response[0]}"
    mlc = await blurpify(mlc)
    await mlcs4.delete()
    await event.client.send_file(event.chat_id, mlc, reply_to=replied)
@bot.on(admin_cmd(pattern="magik(?: |$)(.*)"))####################
async def magic(event):
    input_str = event.pattern_match.group(1)
    replied = await event.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await event.edit("reply to a supported media file")
        return
    if replied.media:
        mlcs4 = await event.edit("passing to telegraph...")
    else:
        await event.edit("reply to a supported media file")
        return

    download_lomlcion = await event.client.download_media(replied, "./temp/")
    if download_lomlcion.endswith((".webp")):
        download_lomlcion = convert_toimage(download_lomlcion)
    size = os.stat(download_lomlcion).st_size
    if download_lomlcion.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await mlcs4.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_lomlcion)
            return
        await mlcs4.edit("generating image..")
    else:
        await mlcs4.edit("the replied file is not supported")
        os.remove(download_lomlcion)
        return
    try:
        response = upload_file(download_lomlcion)
        os.remove(download_lomlcion)
    except exceptions.TelegraphException as exc:
        await mlcs4.edit("ERROR: " + str(exc))
        os.remove(download_lomlcion)
        return
    mlc = f"https://telegra.ph{response[0]}"
    mlc = await magik(mlc,int(input_str))
    await mlcs4.delete()
    await event.client.send_file(event.chat_id, mlc, reply_to=replied)
'''@bot.on(admin_cmd(pattern="clickht(?: |$)(.*)"))
async def clickfor(event):
    input_str = event.pattern_match.group(1)
    replied = await event.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await event.edit("reply to a supported media file")
        return
    if replied.media:
        mlcs4 = await event.edit("passing to telegraph...")
    else:
        await event.edit("reply to a supported media file")
        return

    download_lomlcion = await event.client.download_media(replied, "./temp/")
    if download_lomlcion.endswith((".webp")):
        download_lomlcion = convert_toimage(download_lomlcion)
    size = os.stat(download_lomlcion).st_size
    if download_lomlcion.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await mlcs4.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_lomlcion)
            return
        await mlcs4.edit("generating image..")
    else:
        await mlcs4.edit("the replied file is not supported")
        os.remove(download_lomlcion)
        return
    try:
        response = upload_file(download_lomlcion)
        os.remove(download_lomlcion)
    except exceptions.TelegraphException as exc:
        await mlcs4.edit("ERROR: " + str(exc))
        os.remove(download_lomlcion)
        return
    mlc = f"https://telegra.ph{response[0]}"
    mlc = await clickforhentai(mlc,int(input_str))
    await mlcs4.delete()
    await event.client.send_file(event.chat_id, mlc, reply_to=replied)'''
'''@bot.on(admin_cmd(pattern="bug(?: |$)(.*)"))
async def stick(event):
    #input_str = event.pattern_match.group(1)
    replied = await event.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await event.edit("reply to a supported media file")
        return
    if replied.media:
        mlcs4 = await event.edit("passing to telegraph...")
    else:
        await event.edit("reply to a supported media file")
        return

    download_lomlcion = await event.client.download_media(replied, "./temp/")
    if download_lomlcion.endswith((".webp")):
        download_lomlcion = convert_toimage(download_lomlcion)
    size = os.stat(download_lomlcion).st_size
    if download_lomlcion.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await mlcs4.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_lomlcion)
            return
        await mlcs4.edit("generating image..")
    else:
        await mlcs4.edit("the replied file is not supported")
        os.remove(download_lomlcion)
        return
    try:
        response = upload_file(download_lomlcion)
        os.remove(download_lomlcion)
    except exceptions.TelegraphException as exc:
        await mlcs4.edit("ERROR: " + str(exc))
        os.remove(download_lomlcion)
        return
    mlc = f"https://telegra.ph{response[0]}"
    mlc = await stickbug(mlc)
    await mlcs4.delete()
    await event.client.send_file(event.chat_id, mlc, reply_to=replied)'''
