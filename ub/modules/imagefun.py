# DARKCOBRA ORIGINAL 
# by @danish_00
# by #team dc

# Kangers Keep Credits

# Kepp Credits


import cv2
# by @danish_00
import os, scipy, sys, shutil
import numpy as np
import requests, re
from PIL import Image
from telegraph import upload_file
from telethon.tl.types import MessageMediaPhoto
from ub import bot, CMD_HELP
from ub.utils import admin_cmd
from ub import bot as borg

#keep CREDIT LINES ELSE GET LOST

path = "./cv2/"
if not os.path.isdir(path):
    os.makedirs(path)



            

            
            

@bot.on(admin_cmd("grey"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    cv2.imwrite("danish.jpg", gray)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")

# DARKCOBRA ORIGINAL 
# by @danish_00
# by #team dc

# Kangers Keep Credits

# Kepp Credits

    
@bot.on(admin_cmd("blr"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read() 
    blur = cv2.GaussianBlur(frame, (35, 35), 0)
    cv2.imwrite("danish.jpg", blur)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")

@bot.on(admin_cmd("invrt"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    invert = cv2.bitwise_not(frame)
    cv2.imwrite("danish.jpg", invert)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")


@bot.on(admin_cmd("enhance"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return   
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    dtl = cv2.detailEnhance(frame, sigma_s=10, sigma_r=0.15)
    cv2.imwrite("danish.jpg", dtl)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")

@bot.on(admin_cmd("smooth"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return   
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read() 
    smooth = cv2.edgePreservingFilter(frame, flags=1, sigma_s=60, sigma_r=0.4)
    cv2.imwrite("danish.jpg", smooth)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")

@bot.on(admin_cmd("pencil"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return 
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read() 
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3,3), 0)
    output = cv2.Laplacian(blur, -1, ksize=5)
    output = 255 - output
    ret, output = cv2.threshold(output, 150, 255, cv2.THRESH_BINARY)
    cv2.imwrite("danish.jpg", output)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")
    
@bot.on(admin_cmd("imgrey"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return    
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    invert = cv2.bitwise_not(frame)
    gray = cv2.cvtColor(invert, cv2.COLOR_BGR2GRAY) 
    cv2.imwrite("danish.jpg", gray)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")          
    
    


@bot.on(admin_cmd("emboss"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    kernel = np.array([[0,-1,-1],[1,0,-1], [1,1,0]])
    emboss = cv2.filter2D(frame, -1, kernel)                        
    cv2.imwrite("danish.jpg", emboss)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")

@bot.on(admin_cmd("shrp"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharp = cv2.filter2D(frame, -1, kernel)
    cv2.imwrite("danish.jpg", sharp)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")
    
    
@bot.on(admin_cmd("light"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    brt = cv2.convertScaleAbs(frame, beta=90)
    cv2.imwrite("danish.jpg", brt)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")            
# DARKCOBRA ORIGINAL 
# by @danish_00
# by #team dc

# Kangers Keep Credits

# Kepp Credits
        




