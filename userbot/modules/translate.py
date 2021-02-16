import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd
from userbot import bot as javes
@javes.on(admin_cmd(pattern="translat ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```Reply to text message```")
       return
    chat = "lang_translate_bot"
    sender = reply_message.sender
    await event.edit("```translating```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=710326518))

              await event.client.forward_messages(chat, reply_message)
              response = await response 

          except YouBlockedUserError: 
              await event.reply("```Please unblock (lang_translate_bot) ```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```Can you kindly disable your forward privacy settings```")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
