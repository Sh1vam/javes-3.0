import os,shutil
from userbot.utils import admin_cmd
from userbot import bot 
from userbot import bot as borg
spath="./shivamwriter/"
if not os.path.isdir(spath):
    os.makedirs(spath)
#made by shivam 
# donot kang

# Keep credits

@bot.on(admin_cmd(pattern=r"replace"))
async def replace(event):

    ss=event.text
    shivam=ss[9:]
    place,replace=shivam.split(",")
    kk = await event.delete()

    reply = await event.get_reply_message()
    
    lol = await borg.download_media(reply.media, spath)
    file = open(lol, "rt")
    data = file.read()
    data = data.replace(place,replace)
    file.close()
    file = open(lol, "wt")
    file.write(data)
    file.close()
    await bot.send_file(
            event.chat_id,
            lol)
    shutil.rmtree(spath)
