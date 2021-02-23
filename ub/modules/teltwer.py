import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from ub.utils import admin_cmd
from ub import bot 
@bot.on(admin_cmd(pattern="rtwetme?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("Reply to any user message.")
       return
    reply_message = await event.get_reply_message() 

    chat = "TwitterStatusBot"
    sender = reply_message.sender

    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1276223938))
          
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please unblock (@TwitterStatusBot) ")
              return
          if response.text.startswith("Hi!"):
             await event.edit("Can you kindly disable your forward privacy settings")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
@bot.on(admin_cmd(pattern="teletweetme(?: |$)(.*)"))
async def tweetme(okie):
#"""Creates random anime sticker!"""
    what = okie.pattern_match.group(1)
    if not what:
        if okie.is_reply:
            what = (await okie.get_reply_message()).message
        else:
            await okie.edit("`Tweets must contain some text!`")
            return
    sticcers = await bot.inline_query( "TwitterStatusBot", f"{(what)}")
    await sticcers[0].click(okie.chat_id,
                            reply_to=okie.reply_to_msg_id,
                            silent=True if okie.is_reply else False,
                            hide_via=True)
    await okie.delete()
