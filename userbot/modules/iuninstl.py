from userbot import client, CMD_HELP, CMD_LIST
from telethon import events
from userbot.events import javes05, rekcah05, zzaacckkyy, remove_plugin, load_module
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from userbot.utils import command, remove_plugin, load_module
from pathlib import Path
from userbot import LOAD_PLUG
from userbot import tebot as tgbot
from userbot import bot
from userbot import bot as borg
from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID,client
from telethon import Button, custom, events, functions
import os
@tgbot.on(events.InlineQuery(pattern=r"uninstall (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    me = await client.get_me()
    builder = event.builder
    if event.query.user_id == me.id:
        shortname = event.pattern_match.group(1)
        dir_path =f"/root/userbot/userbot/modules/{shortname}.py"
        try:
            remove_plugin(shortname)
            os.remove(dir_path)
            await event.answer([builder.article(title="Uninstalled",description=f"Uninstalled {shortname} successfully",text=f"Uninstalled {shortname} successfully", buttons=Button.switch_inline("Search Again", query="uninstall ", same_peer=True),)])
        except OSError as e:
            await event.answer([builder.article(title="Error",description="Error: %s : %s" % (dir_path, e.strerror),text="Error: %s : %s" % (dir_path, e.strerror),buttons=Button.switch_inline("Search Again", query="uninstall ", same_peer=True),)])
    if not event.query.user_id == me.id:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/Sh1vam/javes-3.0  ",buttons=[[Button.switch_inline("Search Again", query="uninstall ", same_peer=True)],], )
        await event.answer([resultm])
        return
#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM
