import os

import pybase64
from telegraph import exceptions, upload_file
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from userbot import bot
from userbot import CMD_HELP
from userbot.utils import admin_cmd
from userbot.helpers import *
@bot.on(admin_cmd(pattern="lolice(?: |$)(.*)"))
async def lolce(smss):
    replied = await smss.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await smss.edit("reply to a supported media file")
        return
    if replied.media:
        smss = await smss.edit("passing to telegraph...")
    else:
        await smss.edit("reply to a supported media file")
        return
    download_locatnoarion = await smss.client.download_media(replied, "./temp/")
    if download_locatnoarion.endswith((".webp")):
        download_locatnoarion = convert_toimage(download_locatnoarion)
    size = os.stat(download_locatnoarion).st_size
    if download_locatnoarion.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await smss.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_locatnoarion)
            return
        await smss.edit("generating image..")
    else:
        await smss.edit("the replied file is not supported")
        os.remove(download_locatnoarion)
        return
    try:
        response = upload_file(download_locatnoarion)
        os.remove(download_locatnoarion)
    except exceptions.TelegraphException as exc:
        await smss.edit("ERROR: " + str(exc))
        os.remove(download_locatnoarion)
        return
    catnoar = f"https://telegra.ph{response[0]}"
    catnoar = await lolice(catnoar)
    await smss.delete()
    await smss.client.send_file(smss.chat_id, catnoar, reply_to=replied)

@bot.on(admin_cmd(pattern="awooify(?: |$)(.*)"))
async def awoo(smss):
    replied = await smss.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await smss.edit("reply to a supported media file")
        return
    if replied.media:
        smss = await smss.edit("passing to telegraph...")
    else:
        await smss.edit("reply to a supported media file")
        return
    download_locatnoarion = await smss.client.download_media(replied, "./temp/")
    if download_locatnoarion.endswith((".webp")):
        download_locatnoarion = convert_toimage(download_locatnoarion)
    size = os.stat(download_locatnoarion).st_size
    if download_locatnoarion.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await smss.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_locatnoarion)
            return
        await smss.edit("generating image..")
    else:
        await smss.edit("the replied file is not supported")
        os.remove(download_locatnoarion)
        return
    try:
        response = upload_file(download_locatnoarion)
        os.remove(download_locatnoarion)
    except exceptions.TelegraphException as exc:
        await smss.edit("ERROR: " + str(exc))
        os.remove(download_locatnoarion)
        return
    catnoar = f"https://telegra.ph{response[0]}"
    catnoar = await awooify(catnoar)
    await smss.delete()
    await smss.client.send_file(smss.chat_id, catnoar, reply_to=replied)


@bot.on(admin_cmd(pattern="baguette(?: |$)(.*)"))
async def baguet(smss):
    replied = await smss.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await smss.edit("reply to a supported media file")
        return
    if replied.media:
        smss = await smss.edit("passing to telegraph...")
    else:
        await smss.edit("reply to a supported media file")
        return
    download_locatnoarion = await smss.client.download_media(replied, "./temp/")
    if download_locatnoarion.endswith((".webp")):
        download_locatnoarion = convert_toimage(download_locatnoarion)
    size = os.stat(download_locatnoarion).st_size
    if download_locatnoarion.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await smss.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_locatnoarion)
            return
        await smss.edit("generating image..")
    else:
        await smss.edit("the replied file is not supported")
        os.remove(download_locatnoarion)
        return
    try:
        response = upload_file(download_locatnoarion)
        os.remove(download_locatnoarion)
    except exceptions.TelegraphException as exc:
        await smss.edit("ERROR: " + str(exc))
        os.remove(download_locatnoarion)
        return
    catnoar = f"https://telegra.ph{response[0]}"
    catnoar = await baguette(catnoar)
    await smss.delete()
    await smss.client.send_file(smss.chat_id, catnoar, reply_to=replied)

@bot.on(admin_cmd(pattern="iphonex(?: |$)(.*)"))
async def iphon(smss):
    replied = await smss.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await smss.edit("reply to a supported media file")
        return
    if replied.media:
        smss = await smss.edit("passing to telegraph...")
    else:
        await smss.edit("reply to a supported media file")
        return
    download_locatnoarion = await smss.client.download_media(replied, "./temp/")
    if download_locatnoarion.endswith((".webp")):
        download_locatnoarion = convert_toimage(download_locatnoarion)
    size = os.stat(download_locatnoarion).st_size
    if download_locatnoarion.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await smss.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_locatnoarion)
            return
        await smss.edit("generating image..")
    else:
        await smss.edit("the replied file is not supported")
        os.remove(download_locatnoarion)
        return
    try:
        response = upload_file(download_locatnoarion)
        os.remove(download_locatnoarion)
    except exceptions.TelegraphException as exc:
        await smss.edit("ERROR: " + str(exc))
        os.remove(download_locatnoarion)
        return
    catnoar = f"https://telegra.ph{response[0]}"
    catnoar = await iphonex(catnoar)
    await smss.delete()
    await smss.client.send_file(smss.chat_id, catnoar, reply_to=replied)
