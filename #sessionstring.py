try:
  import telethon
except:
  import os
  os.system("pip install telethon")

print("This IS MADE BY SH1VAM For Use On Computer")
def Javes3():
  from telethon.sync import TelegramClient
  from telethon.sessions import StringSession
  APP_ID = int(input("Enter APP ID here: "))
  API_HASH = input("Enter API HASH here: ")
  with TelegramClient(StringSession(),APP_ID,API_HASH) as client:
    session_str = client.session.save()
    client.send_message("me",str(APP_ID))
    client.send_message("me",str(API_HASH))
    client.send_message("me",session_str)
    client.send_message("me"," 1)APP_ID , 2)API_HASH ,3)StringSession ")
    print("please check your Telegram Saved Messages for 1)APP_ID , 2)API_HASH ,3)StringSession ")
Javes3()
