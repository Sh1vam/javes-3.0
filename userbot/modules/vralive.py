import platform
import sys
from telethon import version
from userbot import (HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HELP, BOTLOG, BOTLOG_CHATID, JAVES_NAME)
from userbot.events import javes05, rekcah05 
import os
import asyncio
from telethon import events
import heroku3
FULL_SUDO = os.environ.get("FULL_SUDO", None)
from var import Var
rksu = Var.SUDO_USERS
from datetime import datetime
from userbot import CMD_HELP, ALIVE_NAME, PM_MESSAGE, JAVES_NAME, JAVES_MSG, ORI_MSG, ALIVE_S_MESSAGE, ALIVE_E_MESSAGE, ALIVE_S_MSG, ALIVE_E_MSG
client2 = client3 = None
try:
  from userbot import bot, client2 , client3
  from userbot import bot as borg
except:
	pass

ALIVE_MEDIA1=os.environ.get("ALIVE_MEDIA1","https://telegra.ph/file/b18ea7028b1cde8a0c573.mp4")
ALIVE_MEDIA2=os.environ.get("ALIVE_MEDIA2","https://telegra.ph/file/ccc536e748881fbe6ac24.mp4")


SPAM_PROTECT = os.environ.get("SPAM_PROTECT", None)
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)
ALIVE_S_MMSG = str(ALIVE_S_MESSAGE) if ALIVE_S_MESSAGE else str(ALIVE_S_MSG)
ALIVE_E_MMSG = str(ALIVE_E_MESSAGE) if ALIVE_E_MESSAGE else str(ALIVE_E_MSG)
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node

START_TIME = datetime.now()
client = bot


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


@client.on(events.NewMessage(outgoing=True, pattern='!bot'))
async def alive(alive):
    shivam=await borg.get_entity('me')
    miraculous=(""
                    f"**{ALIVE_S_MMSG}**\n\n"                     
                    f" °  `{JAVES_NNAME}`: **{v}**\n"
                    f" °  `User:` ** [{shivam.first_name}](tg://user?id={shivam.id})  **\n"
                    f" °  `Telethon`: ** {version.__version__} **\n"
                    f" °  `Python` : ** {platform.python_version()} **\n"                                                                                     
                    f" °  `Os:` ** Kali GNU/Linux Rolling x86_64   **\n"                                       
                    f" °  `Heroku:` ** {herokurk} **\n"
                    f" °  `LogChat:` ** {logrk} **\n"
                    f" °  `Sudo:` ** {sudork} **\n"           
                    f" °  `SpamProtect:` ** {ss} **\n"       
                    f" °  `Uptime:` ** {str(datetime.now() - START_TIME).split('.')[0]} **\n\n"                                   
                    f"**{ALIVE_E_MMSG}**")

    await bot.send_file(alive.chat_id,ALIVE_MEDIA2,caption=miraculous)
    await alive.delete()



@javes05(outgoing=True, pattern="^\.me$")
@javes05(outgoing=True, pattern="^\!me$")
async def alive(alive):
    await bot.send_file(alive.chat_id,ALIVE_MEDIA1,caption="Iam On type !javes or !help  or  .hlp for more info")
    await alive.delete()













