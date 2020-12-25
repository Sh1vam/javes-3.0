#telegram channel @javes05
#from https://t.me/pldhsys

from userbot.modules.cobra import *
from userbot.modules import cobra
import io
import json
import math
import os
import re
import time
from userbot import bot as borg
from userbot import CMD_HELP,  client
from userbot.javes_main.heroku_var import Config
from telethon import Button, custom, events

from userbot import CMD_LIST
from userbot import tebot as tgbot
from telethon.tl.custom import Button 
from telethon import events
from telethon import sync
import io, os
from userbot import CMD_HELP,  client
from userbot.events import javes05

try:
  from userbot import tebot
except:
   tebot = None
   pass
# Darkcobra Original 🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍
# kangers Keep Credits 😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒
# Made by Dc-Team
# Don't remove these lines u fool ,,, 
#
#
#hehehhe
#Making The Back Command Was The Toughest Work #by @Shivam_Patel,@The_Siddharth_Nigam,@danish_00,@ProgrammingError also v changed Pop up or inline help to text
#A stark bhai chori karna aaya ho kya friday me ek bar back btn kang kar k man nahi bhara 
#Agar stark nahi ho to kon hai be tu jo bhi hai kang karna he aaya hai mera back , open btn so get lost
# aur  unload load back close open kang kara ya idea bhi le to credit dena pehli 6 line nahi to bhut bura hoga tumara sath
from math import ceil
import asyncio
from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID,client
import os
from userbot.events import javes05, bot, rekcah05
from userbot.util import admin_cmd
from userbot import tebot as tgbot
from userbot import bot as borg
javes = client = bot
from telethon import events

import json
import random
import os,re
import urllib
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
from userbot import CMD_LIST, CMD_HELP
import io

from userbot.utils import remove_plugin,load_module

import os
import re
import urllib
from math import ceil

import requests
from telethon import Button, custom, events, functions
from youtubesearchpython import SearchVideos
from userbot.javes_main.heroku_var import Var
from userbot import ALIVE_NAME, CMD_HELP, CMD_LIST


 






IN = os.environ.get("INLINE_MODE", None)
BT = os.environ.get("BOT_TOKEN", None)

BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")
if IN:
  @javes05(outgoing=True, pattern="^!help(?: |$|\n)([\s\S]*)")
  async def ban(event):
    if not BT:
       return await event.edit (" Error Add bot token as BOT_TOKEN in heroku var or set inline mode off ")
    mbt = await tebot.get_me()
    try:
       results = await event.client.inline_query(mbt.username, "helpme" )
    except:
       return await  event.edit (" Error go @BotFather and enable inline mode to your bot for use this mode")
    return await results[0].click( event.chat_id, reply_to=event.reply_to_msg_id, hide_via=False )
   

if tebot:

 @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"secret_(.*)")))
 async def on_plug_in_callback_query_handler(event):
        me = await client.get_me()
        timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
        if os.path.exists("./userbot/secrets.txt"):
            jsondata = json.load(open("./userbot/secrets.txt"))
            try:
                message = jsondata[f"{timestamp}"]
                userid = message["userid"]
                ids = [userid, me.id]
                if event.query.user_id in ids:
                    encrypted_tcxt = message["text"]
                    reply_pop_up_alert = encrypted_tcxt
                else:
                    reply_pop_up_alert = "why were you looking at this  go away and do your own work"
            except KeyError:
                reply_pop_up_alert = "This message no longer exists in bot server"
        else:
            reply_pop_up_alert = "This message no longer exists "
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
 '''@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"mywspr_(.*)")))
 async def on_plug_in_callback_query_handler(event):
        me = await client.get_me()
        timestamps = int(event.pattern_match.group(1).decode("UTF-8"))
        if os.path.exists("./userbot/mysecretes.txt"):
            jsondatas = json.load(open("./userbot/mysecretes.txt"))
            try:
                messages = jsondatas[f"{timestamps}"]
                userids = messages["userid"]
                ides = [userids, me.id]
                if event.query.user_id in ides:
                    encrypted_tcxts = messages["text"]
                    reply_pop_up_alert = encrypted_tcxts
                else:
                    reply_pop_up_alert = "why were you looking at this  go away and do your own work"
            except KeyError:
                reply_pop_up_alert = "This message no longer exists in bot server"
        else:
            reply_pop_up_alert = "This message no longer exists "
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)'''
 @tebot.on(events.CallbackQuery)
 async def handler(event):
  try:
    me = await client.get_me()
    if not event.query.user_id == me.id:
        return await event.answer("Sorry, You dont have permission to  Access me!", alert=True)
    et = event.data.decode("UTF-8")
    if et == "back":
        sad = sad2 = sad3 = sad4 = None
        lol = 0
        tbu = [[Button.inline('❌ Close menu', b'close')]] 
        for i in CMD_HELP:
            if lol == 0:
               sad = str(i)
               lol = 1
            elif lol == 1:
                sad2 = str(i)
                lol = 2
            elif lol == 2:
                sad3 = str(i)
                lol = 3
            elif lol == 3:
                sad4 = str(i)
                lol = 0
            if sad and sad2 and sad3 and sad4:
               tbu += [[ Button.inline(f"{sad}" , f"{sad}"), Button.inline(f"{sad2}"  , f"{sad2}"), Button.inline(f"{sad3}" , f"{sad3}"), Button.inline(f"{sad4}" , f"{sad4}")]]   
               sad = sad2 = sad3 = sad4 = None 
        if sad:
	        tbu += [[ Button.inline(f"{sad}"  , f"{sad}")]]   
        if sad2:
	        tbu += [[ Button.inline(f"{sad2}"  , f"{sad2}")]]   
        if sad3:
           tbu += [[ Button.inline(f"{sad3}"  , f"{sad3}")]]   
        return await event.edit ("For Support, Report bugs & help @errorsender_bot and for inline help try @botusername ihelp", buttons=tbu, link_preview=False)   
    if et == "close":
        await event.edit("Help Menu Closed")
    if et in CMD_HELP: 
          fci = [[Button.inline('Go back', 'back'),Button.inline('❌ Close menu', b'close')]]            
          await event.edit(str(CMD_HELP[et]), buttons=fci)

    if et not in CMD_HELP:
        try:
            await event.answer("Please Wait Sir,Or Try Other Btn", alert=True)
        except:
            await event.answer("Please Wait Sir,Or Try Other Btn", alert=True)
  except Exception as e:     
    	return await event.edit(str(e))


        
if tebot:
 @tebot.on(events.InlineQuery)  
 async def inline_handler(event):

  me = await client.get_me()  
  builder = event.builder
  query = event.text
  
  split = query.split(' ', 1) 
  result = None
  #results = None
  hmm = re.compile("secret (.*) (.*)") 
  match = re.findall(hmm, query)

  if event.query.user_id == me.id and query.startswith("buttons"):
            markdown_note = query[7:]
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
            result = builder.article(
                title="Url Button",
                text=message_text,
                buttons=tl_ib_buttons,
                link_preview=False,
            )
            await event.answer([result] if result else None)
  if event.query.user_id == me.id and match:
            #r_msg = await event.get_reply_message()
            query = query[7:]
            user, txct = query.split(" ", 1)
            builder = event.builder
            secret = os.path.join("./userbot", "secrets.txt")

            try:
                jsondata = json.load(open(secret))
            except:
                jsondata = False
            try:
                # if u is user id
                u = int(user)
                try:
                    u = await event.client.get_entity(u)
                    if u.username:
                        sandy = f"@{u.username}"
                    if not u.username:
                        sandy = f"[{u.first_name}](tg://user?id={u.id})"
                except ValueError:
                    # ValueError: Could not find the input entity
                    sandy = f"[user](tg://user?id={u})"
            except ValueError:
                # if u is username
                try:
                    u = await event.client.get_entity(user)
                except ValueError:
                    return
                if u.username:
                    sandy = f"@{u.username}"
                if not u.username:
                    sandy = f"[{u.first_name}](tg://user?id={u.id})"
                u = int(u.id)
            except:
                return
            timestamp = int(time.time() * 2)
            newsecret = {str(timestamp): {"userid": u, "text": txct}}

            buttons = [
                custom.Button.inline("Show Message 🔐", data=f"secret_{timestamp}")
            ]
            result = builder.article(
                title=f"Whisper Message to {sandy}",
                text=f"🔒 A Whisper Message To {sandy}, Only He/She Can Open It.",
                buttons=buttons,
            )
            await event.answer([result] if result else None)
            if jsondata:
                jsondata.update(newsecret)
                json.dump(jsondata, open(secret, "w"))
            else:
                json.dump(newsecret, open(secret, "w"))
  '''if event.query.user_id == me.id and rmatch:
	    r_msg = await event.get_reply_message()
            querys = querys[7:]
            txcts = querys
            builder = event.builder
            mysecrets = os.path.join("./userbot", "mysecretes.txt")
            try:
                jsondatas = json.load(open(mysecrets))
            except:
                jsondatas = False
	    shivam = f"[{rmatch.first_name}](tg://user?id={rmatch})"
            timestamps = int(time.time() * 2)
            newsecrets = {str(timestamps): {"userid": rmatch, "text": txcts}}
            buttons = [
                custom.Button.inline("Show Message 🔐", data=f"secret_{timestamps}")
            ]
            resultse = builder.article(
                title=f"Whisper Message to {shivam}",
                text=f"🔒 A Whisper Message To {shivam}, Only He/She Can Open It.",
                buttons=buttons,
            )
            await event.answer([resultse] if resultse else None)
            if jsondatas:
                jsondatas.update(newsecrets)
                json.dump(jsondatas, open(mysecrets, "w"))
            else:
                json.dump(newsecrets, open(mysecrets, "w"))'''
  if not event.query.user_id == me.id:      
      return
  if query.startswith("helpme"):
      sad = sad2 = sad3 = sad4 = None
      lol = 0
      tbu = [[Button.inline('❌ Close menu', b'close')]]
      for i in CMD_HELP:
            if lol == 0:
               sad = str(i)
               lol = 1
            elif lol == 1:
                sad2 = str(i)
                lol = 2
            elif lol == 2:
                sad3 = str(i)
                lol = 3
            elif lol == 3:
                sad4 = str(i)
                lol = 0
            if sad and sad2 and sad3 and sad4:
               tbu += [[ Button.inline(f"{sad}" , f"{sad}"), Button.inline(f"{sad2}"  , f"{sad2}"), Button.inline(f"{sad3}" , f"{sad3}"), Button.inline(f"{sad4}" , f"{sad4}")]]   
               sad = sad2 = sad3 = sad4 = None 
      if sad:
	        tbu += [[ Button.inline(f"{sad}"  , f"{sad}")]]   
      if sad2:
	        tbu += [[ Button.inline(f"{sad2}"  , f"{sad2}")]]   
      if sad3:
	       tbu += [[ Button.inline(f"{sad3}"  , f"{sad3}")]]   
      result = builder.article("Help menu", text = "For Support, Report bugs & help @errorsender_bot and for inline help try @botusername ihelp", buttons=tbu, link_preview=False)      
      return await event.answer([result])
  return

def ibuild_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb



#some codes taken form Cat bot Fixing them to javes was a task

