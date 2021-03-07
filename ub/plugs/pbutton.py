#modified buy Sh1vam added file support
#    Copyright (C) 2020  sandeep.n(π.$)
# button post makker for catub thanks to uniborg for the base
# by @sandy1709 (@mrconfused)
import os
import re
import shutil
from ub import tebot as tgbot
from telethon import Button
from ub import bot
from ub import CMD_HELP,  client
from ub.javes_main.heroku_var import Config
from .. import CMD_HELP
from ..utils import admin_cmd, edit_or_reply
from ub.javes_main.heroku_var import Var
from ub import bot
import json
import random
import os,re
import urllib
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
from ub import CMD_LIST, CMD_HELP
import io
from ub import bot as borg
try:
  from ub import tebot
except:
   tebot = None
   pass
from ub import CMD_LIST
from ub import tebot as tgbot
from telethon.tl.custom import Button 
from telethon import events
from telethon import sync
import io, os
from ub import CMD_HELP,  client
from ub.events import javes05
# regex obtained from:
# https://github.com/PaulSonOfLars/tgbot/blob/master/tg_bot/plugs/helper_funcs/string_handling.py#L23
BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")
sedpath = "./shivambutton/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)
@bot.on(admin_cmd(pattern=r"psave( (.*)|$)", outgoing=True))
async def sabe(event):
    if event.fwd_from:
        return
    reply_to_id = None
    chat = event.chat_id
    reply_message = await event.get_reply_message()
    await event.edit("Saved Now U Can Use inline mode @yourbotname url and querry")
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
        global img
        img = await borg.download_media(reply_message.media, sedpath)
@bot.on(admin_cmd(pattern="pclear$"))


async def pcls(event):
    if event.fwd_from:
        return
    if not os.path.exists(sedpath):
        await event.edit( "`There is nothing`")
    else:
        shutil.rmtree(sedpath)
        await event.edit(
            "`Noice Cleared all`",
        )
@bot.on(admin_cmd(pattern=r"pbutton( (.*)|$)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = None
    chat = event.chat_id
    reply_message = await event.get_reply_message()
    await event.delete()
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
        global img
        img = await borg.download_media(reply_message.media, sedpath)
    catinput = "".join(event.text.split(maxsplit=1)[1:])



    if not catinput:
        catinput = (await event.get_reply_message()).text
    catinput = "url"+ catinput
    tgbotusername = Config.TG_BOT_USER_NAME_BF_HER
    results = await bot.inline_query(tgbotusername, catinput)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    

if tebot:
 @tebot.on(events.InlineQuery)  
 async def inline_handler(event):
  me = await client.get_me()  
  builder = event.builder
  query = event.text
  split = query.split(' ', 1) 
  result = None 
  hmm = re.compile("secret (.*) (.*)") 
  match = re.findall(hmm, query)
  if event.query.user_id == me.id and query.startswith("url"):
            markdown_note = query[3:]
            prev = 0
            note_data = ""
            buttons = []
            for match in BTN_URL_REGEX.finditer(markdown_note):
                # Check if btnurl is escaped
                n_escapes = 0
                to_check = match.start(1) - 1
                while to_check > 0 and markdown_note[to_check] == "\\":
                    n_escapes += 1
                    to_check -= 1
                # if even, not escaped -> create button
                if n_escapes % 2 == 0:
                    # create a thruple with button label, url, and newline
                    # status
                    buttons.append(
                        (match.group(2), match.group(3), bool(match.group(4)))
                    )
                    note_data += markdown_note[prev : match.start(1)]
                    prev = match.end(1)
                # if odd, escaped -> move along
                else:
                    note_data += markdown_note[prev:to_check]
                    prev = match.start(1) - 1
            else:
                note_data += markdown_note[prev:]
            message_text = note_data.strip()
            tl_ib_buttons = ibuild_keyboard(buttons)
            '''result = builder.article(
                title="Url Button",
                text=message_text,
                buttons=tl_ib_buttons,
                link_preview=False,
            )
            await event.answer([result] if result else None)'''
            try:
                result = builder.photo(
                    img,
                    # title="Shivam",
                    text=message_text,
                    buttons=tl_ib_buttons,
                    link_preview=False,
                )
                await event.answer([result] if result else None)
            except:
                result = builder.document(
                    img,
                    title="Sh1vam",
                    text=message_text,
                    buttons=tl_ib_buttons,
                    link_preview=False,
                )
                await event.answer([result] if result else None)
            else:
                result = builder.article(
                    title="Javes 3.0",
                    text=message_text,
                    buttons=tl_ib_buttons,
                    link_preview=False,
                )
                await event.answer([result] if result else None)
  if not event.query.user_id == me.id:
        s = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/Sh1vam/javes-3.0  ",buttons=[[Button.switch_inline("Search Again", query="url", same_peer=True)],], )
        await event.answer([s])
        return
def ibuild_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb

