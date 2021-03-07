from ub import client, CMD_HELP, CMD_LIST
from telethon import events
from ub.events import javes05, rekcah05, zzaacckkyy, remove_plugin, load_module
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from ub.utils import command, remove_plugin, load_module
from pathlib import Path
from ub import LOAD_PLUG
import os
@zzaacckkyy(pattern="^!uninstall (?P<shortname>\w+)$", outgoing=True)
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    dir_path =f"/root/ub/ub/modules/{shortname}.py"
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        await event.edit(f"Uninstalled {shortname} successfully")
    except OSError as e:
        await event.edit("Error: %s : %s" % (dir_path, e.strerror))
#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM#SHIVAM