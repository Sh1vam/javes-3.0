"""
imported from nicegrill
modified by @mrconfused
QuotLy: Avaible commands: .qbot
"""
#ported by sh1vam
import os
from PIL import Image, ImageDraw, ImageFont
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
import PIL.ImageOps
from ub.helpers.functions import convert_tosticker
from ub.helpers.qhelper import process
from ub.util import admin_cmd
from ub import bot
def convert_tosticker(image):
    img = Image.open(image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("./temp/temp.webp", "webp")
    os.remove(image)
    return "./temp/temp.webp"
@bot.on(admin_cmd(pattern="q(?: |$)(.*)", outgoing=True))

async def stickerchat(catquotes):
    if catquotes.fwd_from:
        return
    reply = await catquotes.get_reply_message()
    if not reply:
        await catquotes.edit(  "`I cant quote the message . reply to a message`"
        )
        return
    fetchmsg = reply.message
    repliedreply = None
    if reply.media and reply.media.document.mime_type in ("mp4"):
        await catquotes.edit(  "`this format is not supported now`")
        return
    catevent = await catquotes.edit( "`Making quote...`")
    user = (
        await catquotes.client.get_entity(reply.forward.sender)
        if reply.fwd_from
        else reply.sender
    )
    res, catmsg = await process(fetchmsg, user, catquotes.client, reply, repliedreply)
    if not res:
        return
    outfi = os.path.join("./temp", "sticker.png")
    catmsg.save(outfi)
    endfi = convert_tosticker(outfi)
    await catquotes.client.send_file(catquotes.chat_id, endfi, reply_to=reply)
    await catevent.delete()
    os.remove(endfi)


@bot.on(admin_cmd(pattern="rq(?: |$)(.*)", outgoing=True))

async def stickerchat(catquotes):
    if catquotes.fwd_from:
        return
    reply = await catquotes.get_reply_message()
    if not reply:
        await catquotes.edit(  "`I cant quote the message . reply to a message`"
        )
        return
    fetchmsg = reply.message
    repliedreply = await reply.get_reply_message()
    if reply.media and reply.media.document.mime_type in ("mp4"):
        await catquotes.edit( "`this format is not supported now`")
        return
    catevent = await catquotes.edit(  "`Making quote...`")
    user = (
        await catquotes.client.get_entity(reply.forward.sender)
        if reply.fwd_from
        else reply.sender
    )
    res, catmsg = await process(fetchmsg, user, catquotes.client, reply, repliedreply)
    if not res:
        return
    outfi = os.path.join("./temp", "sticker.png")
    catmsg.save(outfi)
    endfi = convert_tosticker(outfi)
    await catquotes.client.send_file(catquotes.chat_id, endfi, reply_to=reply)
    await catevent.delete()
    os.remove(endfi)




