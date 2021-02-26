#by Sh1vam
#Kangers stay away

import os
from ub import bot as javes
import subprocess, os , asyncio, shutil
from ub.utils import admin_cmd

@javes.on(admin_cmd("html"))
async def messup(message):
   await message.edit("`making HTML....`")
   reply = await message.get_reply_message()
   stkr = await reply.download_media("tgs.tgs")
   process = await asyncio.create_subprocess_shell(f"lottie_convert.py --frame 0 -if lottie -of html tgs.tgs shivam.html",stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
   stdout, stderr = await process.communicate()
   os.remove(stkr)
   if message.reply_to_msg_id:
        message_id = message.reply_to_msg_id
  
   await message.client.send_file(message.chat_id, "shivam.html",force_document=False,reply_to=message_id)
   os.remove("shivam.html")
   #os.remove("tgs.tgs")
   await message.delete()
@javes.on(admin_cmd("gif"))
async def messup(message):
   await message.edit("`making GIF....`")
   reply = await message.get_reply_message()
   stkr = await reply.download_media("tgs.tgs")
   process = await asyncio.create_subprocess_shell(f"lottie_convert.py --frame 0 -if lottie -of gif tgs.tgs shivam.gif",stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
   stdout, stderr = await process.communicate()
   os.remove(stkr)
   if message.reply_to_msg_id:
        message_id = message.reply_to_msg_id
  
   await message.client.send_file(message.chat_id, "shivam.gif",force_document=False,reply_to=message_id)
   os.remove("shivam.gif")
   #os.remove("tgs.tgs")
   await message.delete()
   
@javes.on(admin_cmd("png"))
async def messup(message):
   await message.edit("`making PNG....`")
   reply = await message.get_reply_message()
   stkr = await reply.download_media("tgs.tgs")
   process = await asyncio.create_subprocess_shell(f"lottie_convert.py --frame 0 -if lottie -of png tgs.tgs shivam.png",stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
   stdout, stderr = await process.communicate()
   os.remove(stkr)
   if message.reply_to_msg_id:
        message_id = message.reply_to_msg_id
  
   await message.client.send_file(message.chat_id, "shivam.png",force_document=False,reply_to=message_id)
   os.remove("shivam.png")
   #os.remove("tgs.tgs")
   await message.delete()  
@javes.on(admin_cmd("convert"))
async def messup(message):
   convert_to=event.text[9:]
   await message.edit(f"`making {convert_to}....`")
   reply = await message.get_reply_message()
   stkr = await reply.download_media("tgs.tgs")
   process = await asyncio.create_subprocess_shell(f"lottie_convert.py --frame 0 -if lottie -of {convert_to} tgs.tgs shivam.{convert_to}",stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
   stdout, stderr = await process.communicate()
   os.remove(stkr)
   if message.reply_to_msg_id:
        message_id = message.reply_to_msg_id
  
   await message.client.send_file(message.chat_id, f"shivam.{convert_to}",force_document=False,reply_to=message_id)
   os.remove(f"shivam.{convert_to}")
   #os.remove("tgs.tgs")
   await message.delete()  
