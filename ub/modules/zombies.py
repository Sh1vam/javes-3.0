#MADE BY @THE_BL_ACK_HAT
#Api iz Hosted By @THE_BL_ACK_HAT
#ZOmbie work done by @THE_BL_ACK_HAT
#Cv2 Work done by Sh1vam
import cv2   
import os
import base64
import cv2
import numpy as np
import requests
from PIL import Image
from telegraph import upload_file
from telethon.tl.types import MessageMediaPhoto
from ub.utils import admin_cmd
from ub import bot 
from ub import bot as borg
import os
#MADE BY @THE_BL_ACK_HAT
#Api iz Hosted By @THE_BL_ACK_HAT
#ZOmbie work done by @THE_BL_ACK_HAT
#Cv2 Work done by Sh1vam
import cv2
from ub import CMD_HELP
#MADE BY @THE_BL_ACK_HAT
#Api iz Hosted By @THE_BL_ACK_HAT
#ZOmbie work done by @THE_BL_ACK_HAT
#Cv2 Work done by Sh1vam
from telegraph import upload_file
from telethon.tl.types import MessageMediaPhoto
from ub.utils import admin_cmd
from ub import bot 
from ub import bot as borg
import os , shutil
#DONT EVEN THINK TO KANG
'''@borg.on(admin_cmd(pattern="zombie ?(.*)"))
async def hmm(event):

    await event.delete()
    sed = await event.get_reply_message()
    img = await borg.download_media(sed.media)
    import cv2   
    miraculous=cv2.VideoCapture(img)
    ladybug,catnoar = miraculous.read()
    cv2.imwrite("zombie.jpg", catnoar)
    img = "zombie.jpg"
    r = requests.post('https://zombiesop.herokuapp.com/api/zombie', files={'image': open(f'{img}', 'rb')})
    data=base64.b64decode(r.text)
    filename='image.jpg'
    with open(filename, 'wb') as f:
        f.write(data)
    im=Image.open(filename)
    import cv2   
    img = cv2.imread(filename)
    height = img.shape[0]
    width = img.shape[1]
    width_cutoff = width // 2
    s2 = img[:, width_cutoff:]
    cv2.imwrite(filename, s2)
    links="javes 3.0|45;6;7|3|0;500|1"
    text,colors,thicknes,orgs,fontsize=links.split("|")
    a,b,c=colors.split(";")
    c,d=orgs.split(";")
    img = filename
    window_name = 'Made By Shivam'
    image = cv2.imread(img) 
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (int(c),int(d))
    color = (int(a),int(b),int(c))
    thickness=int(thicknes)
    fontScale=int(fontsize)
    image = cv2.putText(image, text, org, font, fontScale,  
                 color, thickness, cv2.LINE_AA)
    #image=cv2.imshow(window_name, image)
    cv2.imwrite("s_h_i_v_a_m.jpg", image)
    await event.client.send_file(event.chat_id, "s_h_i_v_a_m.jpg", force_document=False, reply_to=event.reply_to_msg_id)

    os.remove("image.jpg")
    os.remove("s_h_i_v_a_m.jpg")
    os.remove("zombie.jpg")'''
@borg.on(admin_cmd(pattern="makup ?(.*)"))
async def hmm(event):

    await event.delete()
    sed = await event.get_reply_message()
    img = await borg.download_media(sed.media)
    import cv2   
    miraculous=cv2.VideoCapture(img)
    ladybug,catnoar = miraculous.read()
    cv2.imwrite("zombie.jpg", catnoar)
    img = "zombie.jpg"
    r = requests.post('https://deepgrave-image-processor-no7pxf7mmq-uc.a.run.app/transform', files={'image': open(f'{img}', 'rb')})
    data=base64.b64decode(r.text)
    filename='image.jpg'
    with open(filename, 'wb') as f:
        f.write(data)
    im=Image.open(filename)
    import cv2   
    img = cv2.imread(filename)
    height = img.shape[0]
    width = img.shape[1]
    width_cutoff = width // 2
    s2 = img[:, width_cutoff:]
    cv2.imwrite(filename, s2)
    links="javes 3.0|45;6;7|3|0;500|1"
    text,colors,thicknes,orgs,fontsize=links.split("|")
    a,b,c=colors.split(";")
    c,d=orgs.split(";")
    img = filename
    window_name = 'Made By Shivam'
    image = cv2.imread(img) 
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (int(c),int(d))
    color = (int(a),int(b),int(c))
    thickness=int(thicknes)
    fontScale=int(fontsize)
    image = cv2.putText(image, text, org, font, fontScale,  
                 color, thickness, cv2.LINE_AA)
    #image=cv2.imshow(window_name, image)
    cv2.imwrite("s_h_i_v_a_m.jpg", image)
    await event.client.send_file(event.chat_id, "s_h_i_v_a_m.jpg", force_document=False, reply_to=event.reply_to_msg_id)

    os.remove("image.jpg")
    os.remove("s_h_i_v_a_m.jpg")
    os.remove("zombie.jpg")
@borg.on(admin_cmd(pattern="zombie ?(.*)"))
async def hmm(event):

    await event.delete()
    sed = await event.get_reply_message()
    img = await borg.download_media(sed.media)
    import cv2   
    miraculous=cv2.VideoCapture(img)
    ladybug,catnoar = miraculous.read()
    cv2.imwrite("zombie.jpg", catnoar)
    img = "zombie.jpg"
    r = requests.post('https://zombiesop.herokuapp.com/api/zombie', files={'image': open(f'{img}', 'rb')})
    data=base64.b64decode(r.text)
    filename='image.jpg'
    with open(filename, 'wb') as f:
        f.write(data)
    await event.client.send_file(event.chat_id, "image.jpg", force_document=False, reply_to=event.reply_to_msg_id)

    os.remove("image.jpg")
    os.remove("zombie.jpg")
@borg.on(admin_cmd(pattern="feye ?(.*)"))
async def feye(event):

    await event.delete()
    sed = await event.get_reply_message()
    img = await borg.download_media(sed.media)
    import cv2   
    miraculous=cv2.VideoCapture(img)
    ladybug,catnoar = miraculous.read()
    cv2.imwrite("fummy.jpg", catnoar)
    img = "fummy.jpg"
    r = requests.post('https://zombiesop.herokuapp.com/api/funnyeye', files={'image': open(f'{img}', 'rb')})
    data=base64.b64decode(r.text)
    filename='image.jpg'
    with open(filename, 'wb') as f:
        f.write(data)
    await event.client.send_file(event.chat_id, "fummy.jpg", force_document=False, reply_to=event.reply_to_msg_id)

    os.remove("image.jpg")
    os.remove("fummy.jpg")
@borg.on(admin_cmd(pattern="neye ?(.*)"))
async def hmm(event):

    await event.delete()
    sed = await event.get_reply_message()
    img = await borg.download_media(sed.media)
    import cv2   
    miraculous=cv2.VideoCapture(img)
    ladybug,catnoar = miraculous.read()
    cv2.imwrite("red.jpg", catnoar)
    img = "red.jpg"
    r = requests.post('https://zombiesop.herokuapp.com/api/redeye', files={'image': open(f'{img}', 'rb')})
    data=base64.b64decode(r.text)
    filename='image.jpg'
    with open(filename, 'wb') as f:
        f.write(data)
    await event.client.send_file(event.chat_id, "image.jpg", force_document=False, reply_to=event.reply_to_msg_id)

    os.remove("image.jpg")
    os.remove("red.jpg")