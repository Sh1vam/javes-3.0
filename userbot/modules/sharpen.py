import os
#MADE BY SHIVAM DONT KANG
from userbot import CMD_HELP
#MADE BY SHIVAM DONT KANG
#MADE BY SHIVAM DONT KANG
from telegraph import upload_file
from telethon.tl.types import MessageMediaPhoto
from userbot.utils import admin_cmd
from userbot import bot 
from userbot import bot as borg
import os , shutil
from wand.image import Image
sedpath = "./s_h_i_v_a_m_sharpen/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)
@borg.on(admin_cmd(pattern=r"sharp"))
async def miraculous(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    await event.delete()
    sed = await event.get_reply_message()
    linc = event.text
    links=linc[7:]
    lb,cb=links.split(",")

    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    #image=cv2.imshow(window_name, image)
    spath = img
    with Image(filename =spath) as img:
        img.sharpen(radius = int(lb), sigma = int(cb))
        img.save(filename ="s_h_i_v_a_m_sharp.jpeg")
    #await borg.send_file(event.chat_id,"s_h_i_v_a_m.png")
    #await event.client.send_file(event.chat_id, "s_h_i_v_a_m.png", force_document=True, reply_to=event.reply_to_msg_id)
    await event.client.send_file(event.chat_id, "s_h_i_v_a_m_sharp.jpeg", force_document=False, reply_to=event.reply_to_msg_id)
    shutil.rmtree(sedpath)
    os.remove("s_h_i_v_a_m_sharp.jpeg")
