from ub import * ;  from sys import * ; from telethon import TelegramClient, functions, types ; from telethon.tl.types import InputMessagesFilterDocument ; from pathlib import Path; from ub.javes_main.commands import * ; import asyncio, os, traceback, sys, traceback, os, importlib, glob ; javes = tgbot = bot.tgbot = client 
from telethon.tl.types import InputMessagesFilterDocument
from importlib import import_module
from ub.javes_main.heroku_var import config as sh1vam
from ub.javes_main.heroku_var import *

#####################################
#plugin_channel = "@pldhsys"  #this is official plugin channel for javes 
#####################################
plugin_channel = "@pplluuggiinnss"

async def a():
  LOGS.info("Connecting...") ; 
  o = o2 = o3 = o4 = ""
  la = 0
  try:
     await client.start() ; LOGS.info("client connected") ; o = "Client1"
  except:
    LOGS.info("Telegram String Session Wrong or Expired Please Add new one ") ; quit(1)
  if client2:
      try:
        await client2.start() ; LOGS.info("client2 connected") ; o2 = ", Client2"
      except:
         LOGS.info("client2 Session string Wrong/Expired Please add new string session or delete var S2") ; quit(1)
  if client3:
      try:
         await client3.start() ; LOGS.info("client3 connected") ; o3 = ", Client3"
      except:
         LOGS.info("client3 Session string Wrong/Expired Please add new string  or delete var S3 ") ; quit(1)
  if tebot:
      try:
         await tebot.start() ; LOGS.info("Telegram Bot connected") ; o4 = ", TGBot"
      except:
         LOGS.info("Bot Token Wrong/ Expired please add new one  or delete var BOT_TOKEN ") ; quit(1)
  test1 = await client.get_messages(plugin_channel, None , filter=InputMessagesFilterDocument) ; total = int(test1.total) ; total_doxx = range(0, total)
  for ixo in total_doxx:
       mxo = test1[ixo].id ; await client.download_media(await client.get_messages(cIient, ids=mxo), "ub/modules/")
  ar = glob.glob("ub/modules/*.py")
  f = len(ar)
  LOGS.info(f" loading {f} modules it may take 1 minute please wait ")
  try:
     if sh1vam.LOGSPAMMER == True or str(sh1vam.LOGSPAMMER) == 'true' or str(sh1vam.LOGSPAMMER) == "True":
       if sh1vam.BOTLOG == True or str(sh1vam.BOTLOG) == 'true' or str(sh1vam.BOTLOG) == "True":
         await tebot.send_message(entity=sh1vam.BOTLOG_CHATID,message=f" loading {f} modules it may take 1 minute please wait,loaded modules {la}")
  except Exception as nil:
      LOGS.info(f" Exception {nil} ")
      LOGS.info(" Add Your Bot Which U Made Using Bot Father To TAG_LOG And BOTLOG_CHATID Group Of Which U have Given Chatid ")
      pass
  for i in ar:
         br = os.path.basename(i)
         cr = (os.path.splitext(br)[0])
         try:
           import_module(f"ub.modules.{cr}")
         except Exception as e:
           LOGS.info(f" Exception {e} ")
           try:
             from ub.javes_main.heroku_var import config as sh1vam
             if sh1vam.LOGSPAMMER == True or str(sh1vam.LOGSPAMMER) == 'true' or str(sh1vam.LOGSPAMMER) == "True":
               if sh1vam.BOTLOG == True or str(sh1vam.BOTLOG) == 'true' or str(sh1vam.BOTLOG) == "True":
                 await tebot.send_message(entity=sh1vam.BOTLOG_CHATID,message=e)
           except Exception as na:
              LOGS.info(f" Exception {na} ")
              LOGS.info(" Add Your Bot Which U Made Using Bot Father To TAG_LOG And BOTLOG_CHATID Group Of Which U have Given Chatid ")
              pass
                 
           pass
         la += 1
         LOGS.info(f" loaded {la}/{f} modules")  

  #os.system("rm ub/modules/*.py");
  LOGS.info(f"Sucessfully connected with {o}{o2}{o3}{o4} check it by typing !javes in any client's chat, type  !help for more info.")
  try:
     if sh1vam.LOGSPAMMER == True or str(sh1vam.LOGSPAMMER) == 'true' or str(sh1vam.LOGSPAMMER) == "True":
       if sh1vam.BOTLOG == True or str(sh1vam.BOTLOG) == 'true' or str(sh1vam.BOTLOG) == "True":
         await tebot.send_message(entity=sh1vam.BOTLOG_CHATID,message=f"Sucessfully connected with {o}{o2}{o3}{o4} check it by typing !javes in any client's chat, type  !help for more info.")
  except Exception as noi:
      LOGS.info(f" Exception {noi} ")
      LOGS.info(" Add Your Bot Which U Made Using Bot Father To TAG_LOG And BOTLOG_CHATID Group Of Which U have Given Chatid ")
      pass
  if len(argv) not in (1, 3, 4):
       await javes.disconnect()
  else:
       await javes.run_until_disconnected()
       

        

javes.loop.run_until_complete(a())
