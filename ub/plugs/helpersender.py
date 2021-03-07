from ub import client, CMD_HELP, CMD_LIST
from telethon import events
from ub.events import javes05, rekcah05, zzaacckkyy, remove_plugin, load_module
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from ub.utils import command, remove_plugin, load_module
from pathlib import Path
from ub import LOAD_PLUG
from datetime import datetime
DELETE_TIMEOUT = 5
import sys, asyncio, traceback, os, importlib
import ub.utils
from ub import CMD_HELP, ALIVE_NAME, PM_MESSAGE, JAVES_NAME, JAVES_MSG, ORI_MSG
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)

@zzaacckkyy(pattern="^!hlprsend (?P<shortname>\w+)$", outgoing=True)
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    input_str = event.pattern_match["shortname"]
    the_plugin_file = "./ub/helpers/{}.py".format(input_str)
    start = datetime.now()
    await event.client.send_file(  # pylint:disable=E0602
        event.chat_id,
        the_plugin_file,
        force_document=True,
        allow_cache=False,
        reply_to=message_id
    )
    end = datetime.now()
    time_taken_in_ms = (end - start).seconds
    await event.edit("Uploaded {} in {} seconds".format(input_str, time_taken_in_ms))
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()









        
CMD_HELP.update({
    "install":
    "`!sqlsend <sqlsname>`\
\n**Usage:** send the sql helper\
\n\n``\
\n****\
"
})