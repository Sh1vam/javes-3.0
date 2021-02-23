from PIL import Image
import numpy as np
import os, shutil, sys ,cv2, asyncio, scipy
from telegraph import upload_file
from telethon.tl.types import MessageMediaPhoto
from ub.utils import admin_cmd
from ub import bot
import PIL
#made by @danish_00 and @Shivam_Patel

#donto kang
path = "./dcobra/"
if not os.path.isdir(path):
    os.makedirs(path)
@bot.on(admin_cmd("rmbw"))
async def hehe(event):
    miracle=event.text
    miraculous=miracle[6:]
    alpha,beta,gamma,link=miraculous.split(";")
    os.system(f'wget {link}')
    lbcn=link[24:]


    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image like this :-.rmbw 01;1.5;9;https://telegra.ph/file/55ca237fcbd41f3063385.png u can have any value instead")
        return

    reply = await event.get_reply_message()
    image = await bot.download_media(reply.media, path)
    ims=image
    image = PIL.Image.open(image)
    shi,vam = image.size
    img1 = cv2.VideoCapture(ims) 
    ret, frame = img1.read()
    img2 = cv2.imread(f'{lbcn}')
    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    img1 =cv2.resize(img1,(620,350))
    img2 =cv2.resize(img2,(620,350))
    mix = cv2.addWeighted(src1=img1,alpha=float(alpha),src2=img2,beta=float(beta),gamma=float(gamma))
    mila = cv2.cvtColor(mix, cv2.COLOR_RGB2BGR)
    cv2.imwrite("danish.png", mila)
    shvm=PIL.Image.open("danish.png")
    img=shvm.resize((int(shi),int(vam)))
    img.save("danish.png", format="PNG", optimize=True)
    await event.delete()
    await event.client.send_file(event.chat_id, "danish.png", force_document=False, reply_to=event.reply_to_msg_id)
    shutil.rmtree(path)
    os.remove("danish.png")
