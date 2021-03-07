#made by @danish_00
#donot cang 
#Team DC



import cv2 , shutil, os
from ub.utils import admin_cmd
from ub import bot 

path = "./dcobra/"
if not os.path.isdir(path):
    os.makedirs(path)
    
@bot.on(admin_cmd("miror"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to media")
        return
    await event.edit("```Processing...```")
    reply = await event.get_reply_message()
    pathh = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(pathh)
    ret,frame = img.read()
    flip = cv2.flip(frame, 1)
    cv2.imwrite("cobra.jpg", frame)
    cv2.imwrite("danish.jpg", flip) 
    dark = cv2.imread("cobra.jpg")
    cobra = cv2.imread("danish.jpg")
    merge = cv2.hconcat([dark, cobra])
    cv2.imwrite('dark.jpg', merge)
    await event.client.send_file(event.chat_id, "dark.jpg" , reply_to=event.reply_to_msg_id) 
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")
    os.remove("dark.jpg")
    os.remove("cobra.jpg")
@bot.on(admin_cmd("imirror"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to media")
        return
    await event.edit("```Processing...```")
    reply = await event.get_reply_message()
    pathh = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(pathh)
    ret,frame = img.read()
    up = cv2.rotate(frame, cv2.ROTATE_180)
    cv2.imwrite("cobra.jpg", frame)
    cv2.imwrite("danish.jpg", up) 
    dark = cv2.imread("cobra.jpg")
    cobra = cv2.imread("danish.jpg")
    merge = cv2.vconcat([dark, cobra])
    cv2.imwrite('dark.jpg', merge)
    await event.client.send_file(event.chat_id, "dark.jpg" , reply_to=event.reply_to_msg_id) 
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")
    os.remove("dark.jpg")
    os.remove("cobra.jpg")
@bot.on(admin_cmd("bmirror"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to media")
        return
    await event.edit("```Processing...```")
    reply = await event.get_reply_message()
    pathh = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(pathh)
    ret,frame = img.read()
    flip = cv2.flip(frame, 1)
    up = cv2.rotate(flip, cv2.ROTATE_180)
    cv2.imwrite("cobra.jpg", frame)
    cv2.imwrite("danish.jpg", up) 
    dark = cv2.imread("cobra.jpg")
    cobra = cv2.imread("danish.jpg")
    merge = cv2.vconcat([dark, cobra])
    cv2.imwrite('dark.jpg', merge)
    await event.client.send_file(event.chat_id, "dark.jpg" , reply_to=event.reply_to_msg_id) 
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")
    os.remove("dark.jpg")
    os.remove("cobra.jpg")