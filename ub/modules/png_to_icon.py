from PIL import Image
import os
#MADE BY SHIVAM DONT KANG
import cv2
from ub import CMD_HELP
#MADE BY SHIVAM DONT KANG
#MADE BY SHIVAM DONT KANG
from telegraph import upload_file
from ub.utils import admin_cmd
from ub import bot 
from ub import bot as borg
import os , shutil
op = "./png_to_ico/"
if not os.path.isdir(op):
    os.makedirs(op)
@borg.on(admin_cmd(pattern=r"pti"))
async def miraculous(event):

    await event.delete()
    ico = await event.get_reply_message()
    pti = await borg.download_media(ico.media, op)
    miraculous=cv2.VideoCapture(pti)
    ladybug,catnoar = miraculous.read()
    cv2.imwrite("shivamico.png", catnoar)
    try:
        imgae = Image.open("shivamico.png")
        imgae.save('shivamico.ico')
        await event.client.send_file(event.chat_id, "shivamico.ico", force_document=False, reply_to=event.reply_to_msg_id)
    except Exception as e:
        await event.edit(e)
    shutil.rmtree(op)
    os.remove("shivamico.ico")


