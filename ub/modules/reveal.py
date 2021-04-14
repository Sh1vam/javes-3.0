import os

from ub import CMD_HELP
from ub.utils import admin_cmd

from ub import bot as borg
@borg.on(admin_cmd(pattern=r"reveal", outgoing=True))

async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    a = open(b, "r")
    c = a.read()
    a.close()
    await event.edit("Reading file...")
    if len(c) > 4095:
        await event.edit("The Total words in this file is more than telegram limits. use .paste or .neko to past to dog bin or neko bin")
    else:
        await event.edit(f"{c}")
        #await a.delete()
    os.remove(b)


'''CMD_HELP.update(
    {
        "reveal": ".reveal <reply to a file>\nUse - Read contents of file and send as a telegram message."
    }
)'''
