#by Sh1vam
#Kangers stay away
import os
from userbot import bot as javes
import subprocess, os , asyncio, shutil
from userbot.utils import admin_cmd

@javes.on(admin_cmd("ctgsmagic"))
async def messup(message):

   await message.edit("`messing....`")
   miraculous = message.text
   tales = miraculous[11:]
   ladybug,catnoir = tales.split(";")
   a,b=int(ladybug),int(catnoir)
   c,d=a+1,b+10
   e,f=c+1,d+10
   g,h=e+1,f+10
   i,j=g+1,h+10
   reply = await message.get_reply_message()
   stkr = await reply.download_media("tgs.tgs")
   process = await asyncio.create_subprocess_shell(f"lottie_convert.py {stkr} json.json",stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
   stdout, stderr = await process.communicate()
   os.remove(stkr)
   if message.reply_to_msg_id:
        message_id = message.reply_to_msg_id
   with open("json.json","r") as json:
       jsn = json.read()      
   jsn = jsn.replace(f'[{a}]',f'[{b}]').replace(f'[{c}]',f'[{d}]').replace(f'[{e}]',f'[{f}]').replace(f'[{g}]',f'[{h}]').replace(f'[{i}]',f'[{j}]')
   with open("json.json","w") as outfile:
       outfile.write(jsn)
   process = await asyncio.create_subprocess_shell("lottie_convert.py json.json tgs.tgs",stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
   stdout, stderr = await process.communicate()
   await message.client.send_file(message.chat_id, "tgs.tgs",force_document=False,reply_to=message_id)
   os.remove("json.json")
   os.remove("tgs.tgs")
   await message.delete()
   
   
   
   
