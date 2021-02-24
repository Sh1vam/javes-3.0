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
   os.remove("tgs.tgs")
   await message.delete()
   
   
   
   
