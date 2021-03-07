
from asyncio import sleep
from ub import CMD_HELP, BOTLOG, BOTLOG_CHATID, bot
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
from ub.utils import admin_cmd
from os import remove
from ub import bot
from ub import bot as borg
from ub import CMD_HELP, BOTLOG, BOTLOG_CHATID,client
from telethon import events
import asyncio
from datetime import datetime
import time
from ub.utils import register, errors_handler, admin_cmd
import asyncio
import logging
import os
import sys
from telethon.tl import functions, types
from telethon.tl.types import Channel, Chat, User
from ub.javes_main.heroku_var import Config
import os
from distutils.util import strtobool as sb
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.WARN)

NO_PM_LOG_USERS = []
NC_LOG_P_M_S=sb(os.environ.get("NC_LOG_P_M_S", "True"))
PMLOG = sb(os.environ.get("PMLOG", "True"))
PMLOG_CHATID = int(os.environ.get("PMLOG_CHATID",-1001230114424))


@register(outgoing=True, pattern=r"^.save(?: |$)([\s\S]*)")
async def log(log_text):
    """ For .log command, forwards a message or the command argument to the bot logs group """
    if PMLOG:
        if log_text.reply_to_msg_id:
            reply_msg = await log_text.get_reply_message()
            await reply_msg.forward_to(PMLOG_CHATID)
        elif log_text.pattern_match.group(1):
            user = f"#LOG / Chat ID: {log_text.chat_id}\n\n"
            textx = user + log_text.pattern_match.group(1)
            await bot.send_message(PMLOG_CHATID, textx)
        else:
            await log_text.edit("`What am I supposed to log?`")
            return
        await log_text.edit("`Logged Successfully`")
    else:
        await log_text.edit("`This feature requires Logging to be enabled!`")
    await sleep(2)
    await log_text.delete()


@borg.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def monito_p_m_s(event):
    sender = await event.get_sender()
    if NC_LOG_P_M_S and not sender.bot:
        chat = await event.get_chat()
        me = await client.get_me()
        if chat.id not in NO_PM_LOG_USERS and chat.id != me.id:
            try:
                e = await borg.get_entity(int(PMLOG_CHATID))             
                fwd_message = await borg.forward_messages(
                    e,
                    event.message,
                    silent=True
                )
            except Exception as e:
                # logger.warn(str(e))
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print(e) 

@borg.on(admin_cmd(pattern="elog ?(.*)"))
async def set_no_log_p_m(event):
    if PMLOG_CHATID is not None:
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if chat.id in NO_PM_LOG_USERS:
                NO_PM_LOG_USERS.remove(chat.id)
                await event.edit("Will Log Messages from this chat")
                await asyncio.sleep(3)
                await event.delete()


@borg.on(admin_cmd(pattern="nlog ?(.*)"))
async def set_no_log_p_m(event):
    if PMLOG_CHATID is not None:
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if chat.id not in NO_PM_LOG_USERS:
                NO_PM_LOG_USERS.append(chat.id)
                await event.edit("Won't Log Messages from this chat")
                await asyncio.sleep(3)
                await event.delete()
