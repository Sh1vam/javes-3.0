
import PIL
import cv2
import numpy as np
import requests, os ,re
from PIL import Image
from telegraph import upload_file
from telethon.tl.types import MessageMediaPhoto
from userbot.utils import admin_cmd
from userbot import bot 
#DONOT KANG

#made by Sh1vam & @danish_00
path = "./dcobra/"
if not os.path.isdir(path):
    os.makedirs(path)
    
@borg.on(admin_cmd(pattern=r"wast"))
async def hmm(event):
    reply = await event.get_reply_message()
    await event.delete()
    #os.system(f'wget https://telegra.ph/file/26d43e25cb2095a931ab1.jpg')
    os.system(f'wget https://telegra.ph/file/b3a6038bc825cc4edc4f0.png')
    img = await borg.download_media(reply.media, path)

    mon = "b3a6038bc825cc4edc4f0.png"
    foreground = Image.open(mon).convert("RGBA")
    img = cv2.VideoCapture(img) 
    tales, miraculous = img.read()
    cv2.imwrite("MiraculousLadybug.png",miraculous)
    shvm=PIL.Image.open("MiraculousLadybug.png")
    shi,vam = shvm.size
    img=shvm.resize((512,512))
    img.save("shivamgta.png", format="PNG", optimize=True)
    img = cv2.VideoCapture("shivamgta.png") 
    tales, miraculousladybug = img.read()
    gray = cv2.cvtColor(miraculousladybug, cv2.COLOR_BGR2GRAY) 
    #gray = cv2.medianBlur(gray, 5)
    bug = cv2.imwrite("shivamgtas.jpg", gray)
    image = cv2.imread("shivamgtas.jpg")
    overlay = image.copy()########################

    x, y, w, h = 0, 210, 800, 100
    overlay =cv2.rectangle(overlay, (x, y), (x+w, y+h), (0,0,0), -1) 

    alpha = 0.5  # Transparency factor.0.8

    # Following line overlays transparent rectangle over the image
    image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
    cv2.imwrite("shivamgta.jpg", image_new)######################################

    background = Image.open("shivamgta.jpg").convert("RGB")
    with Image.open("shivamgta.jpg") as imge:
        width, height = imge.size
    fg_resized = foreground.resize((width, int(height/5)))
    background.paste(fg_resized, box=(0,int(height/2)-50), mask=fg_resized)
    background.save("shivamwasted.png")
    miraculous=PIL.Image.open("shivamwasted.png")
    img=miraculous.resize((int(shi),int(vam)))
    img.save("shivamwastedgta.png", format="PNG", optimize=True)
    await event.client.send_file(event.chat_id, "shivamwastedgta.png", force_document=False, reply_to=event.reply_to_msg_id)
    os.remove("shivamwasted.png")
    os.remove("shivamwastedgta.png")
    os.remove("MiraculousLadybug.png")
    os.remove("shivamgta.png")
