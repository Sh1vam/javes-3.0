from userbot.events import javes05, rekcah05 
import os
from userbot import bot as shivam
ALIVE_MEDIA_PIC=os.environ.get("ALIVE_MEDIA_PIC","https://telegra.ph/file/b18ea7028b1cde8a0c573.mp4")



javes05(outgoing=True, pattern="^\.valive$")
@javes05(outgoing=True, pattern="^\!valive$")
async def alive(alive):
    await shivam.send_file(alive.chat_id,ALIVE_MEDIA_PIC,caption="Iam On type` !javes `or` !help `for more info")
    await alive.delete()





