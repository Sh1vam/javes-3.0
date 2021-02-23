import platform
import sys
from telethon import version
from ub import (HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HELP, BOTLOG, BOTLOG_CHATID, JAVES_NAME)
from ub.events import javes05, rekcah05 
import os
import asyncio
from telethon import events
import heroku3
FULL_SUDO = os.environ.get("FULL_SUDO", None)
from var import Var
rksu = Var.SUDO_USERS
from datetime import datetime
from ub import CMD_HELP, ALIVE_NAME, PM_MESSAGE, JAVES_NAME, JAVES_MSG, ORI_MSG, ALIVE_S_MESSAGE, ALIVE_E_MESSAGE, ALIVE_S_MSG, ALIVE_E_MSG
client2 = client3 = None
try:
  from ub import bot, client2 , client3
except:
	pass

SPAM_PROTECT = os.environ.get("SPAM_PROTECT", None)
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)
ALIVE_S_MMSG = str(ALIVE_S_MESSAGE) if ALIVE_S_MESSAGE else str(ALIVE_S_MSG)
ALIVE_E_MMSG = str(ALIVE_E_MESSAGE) if ALIVE_E_MESSAGE else str(ALIVE_E_MSG)
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
START_TIME = datetime.now()
client = bot
S2_NAME = os.environ.get("S2_NAME", JAVES_NNAME)
S3_NAME = os.environ.get("S3_NAME", JAVES_NNAME)
S2_USER = os.environ.get("S2_USER", DEFAULTUSER)
S3_USER = os.environ.get("S3_USER", DEFAULTUSER)
from telethon import Button, custom, events
from ub import CMD_LIST
from ub import tebot as tgbot
from ub import tebot
from telethon.tl.custom import Button
import os
from telethon import sync
from ..utils import admin_cmd
from ub.events import javes05
from ub import CMD_HELP,  client
import re
TG_BOT_USER_NAME_BF_HER=os.environ.get("TG_BOT_USER_NAME_BF_HER",None)
CUSTOM_CMD2=os.environ.get("CUSTOM_CMD2","!sh1vam")
PROFILE_PPP = os.environ.get("PROFILE_PPP" , "https://telegra.ph/file/5d084db1197c6e7f0db59.jpg")
ALIVE_PHOTTO = PROFILE_PPP
@javes05(outgoing=True, pattern=f"^{CUSTOM_CMD2}(?: |$|\n)([\s\S]*)")
async def glost(event):
    await event.delete()
    mt = await tebot.get_me()
    results = await event.client.inline_query(mt.username, "javes" )
    return await results[0].click( event.chat_id, reply_to=event.reply_to_msg_id, hide_via=False )
v = "0.0.0"

if rksu:
 if FULL_SUDO:
    sudork = 'Full access'
 else:
    sudork = 'Normal access'
else:
	sudork = 'NotSet'


if SPAM_PROTECT:
	ss = "True"
else:
	ss = "False"

try:
   Heroku = heroku3.from_key(HEROKU_API_KEY)                         
   app = Heroku.app(HEROKU_APP_NAME)
   herokurk = 'connected'
except:
	herokurk = '[Failed to connect](https://telegra.ph/RkPavi-06-09-6)'
	pass


if BOTLOG_CHATID:
	logrk = 'connected'
else:
	logrk = '[Failed to connect](https://telegra.ph/RkPavi-06-09-3)'

_s_h_i_v_v_m_=(""
                    f"**{ALIVE_S_MMSG}**\n\n"                     
                    f" °  `{JAVES_NNAME}`: **{v}**\n"
                    f" °  `User:` ** {DEFAULTUSER} **\n"
                    f" °  `Telethon`: ** {version.__version__} **\n"
                    f" °  `Python` : ** {platform.python_version()} **\n"                                                                                     
                    f" °  `Os:` ** Kali GNU/Linux Rolling x86_64   **\n"                                       
                    f" °  `Heroku:` ** {herokurk} **\n"
                    f" °  `LogChat:` ** {logrk} **\n"
                    f" °  `Sudo:` ** {sudork} **\n"           
                    f" °  `SpamProtect:` ** {ss} **\n"       
                    f" °  `Uptime:` ** {str(datetime.now() - START_TIME).split('.')[0]} **\n\n"                                   
                    f"**{ALIVE_E_MMSG}**")
if TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        me = await client.get_me()
        if query.startswith("javes") and event.query.user_id == me.id:
            buttons = [
                (
                    Button.url("Repo", "https://github.com/Sh1vam/javes-3.0"),
                    Button.url("Deploy", "https://heroku.com/deploy?template=https://github.com/Sh1vam/javes-3.0/blob/master"),
                    Button.url("String", "https://repl.it/@Danish00/DarkCobra#main.py"),
                    Button.url("Channel", "https://t.me/plugines"),
                )
            ]
            if ALIVE_PHOTTO and ALIVE_PHOTTO.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALIVE_PHOTTO,
                    # title="Shivam",
                    text=_s_h_i_v_v_m_,
                    buttons=buttons,
                )
            elif ALIVE_PHOTTO:
                result = builder.document(
                    ALIVE_PHOTTO,
                    title="Sh1vam",
                    text=_s_h_i_v_v_m_,
                    buttons=buttons,
                )
            else:
                result = builder.article(
                    title="Javes 3.0",
                    text=_s_h_i_v_v_m_,
                    buttons=buttons,
                )
            await event.answer([result] if result else None)
        if not event.query.user_id == me.id:
            resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/Sh1vam/javes-3.0  ",buttons=[[Button.switch_inline("Search Again", query="exec ", same_peer=True)],], )
            await event.answer([resultm])
            return
