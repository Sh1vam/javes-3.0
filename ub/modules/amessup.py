#by Shlbvam
#Kangers stay away
import os
from ub import bot as javes
import subprocess, os , asyncio, shutil
from ub.utils import admin_cmd

@javes.on(admin_cmd("atgsmagic"))
async def messup(message):

   await message.edit("`messing....`")
   miraculous = message.text
   tales = miraculous[11:]
   ladybug,lb,catnoir,cn = tales.split(";")
   a,lb,b,cn=int(ladybug),int(lb),int(catnoir),int(cn)

   c,d=a+lb,b+cn
   e,f=c+lb,d+cn
   g,h=e+lb,f+cn
   i,j=g+lb,h+cn
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
   
   
   
   
