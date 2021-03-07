from moviepy.editor import *
import os
#MADE BY SHIVAM DONT KANG
import cv2
from ub import CMD_HELP
#MADE BY SHIVAM DONT KANG
#MADE BY SHIVAM DONT KANG
from telegraph import upload_file
from telethon.tl.types import MessageMediaPhoto
from ub.utils import admin_cmd
from ub import bot 
from ub import bot as borg
import os , shutil

op = "./s_h_i_v_a_m_Video_memify/"
if not os.path.isdir(op):
    os.makedirs(op)
@borg.on(admin_cmd(pattern=r"vedt"))
async def miraculous(event):

    await event.delete()
    sed = await event.get_reply_message()
    linc = event.text
    links=linc[6:]
    loltext,color,fontsize,textduration,position,subclip,volume=links.split("|")
    start,end=subclip.split(";")
    vdio = await borg.download_media(sed.media, op)
    clip = VideoFileClip(vdio)
    clip = clip.subclip(float(start),float(end))   
    clip = clip.volumex(float(volume))
    txt_clip = TextClip(loltext, fontsize = float(fontsize), color = color)   
    txt_clip = txt_clip.set_pos(position).set_duration(float(textduration))  
    video = CompositeVideoClip([clip, txt_clip]) 
    video.write_videofile("shivam.mp4")
    await event.client.send_file(event.chat_id, "shivam.mp4", force_document=False, reply_to=event.reply_to_msg_id)
    shutil.rmtree(op)
    os.remove("shivam.mp4")
@borg.on(admin_cmd(pattern=r"duration"))
async def miraculous(event):


    sed = await event.get_reply_message()
    vdo = await borg.download_media(sed.media, op)
    clip = VideoFileClip(vdo)
    duration = clip.duration
    await event.edit(f"Your Video Duration iz {duration}")
    shutil.rmtree(op)
