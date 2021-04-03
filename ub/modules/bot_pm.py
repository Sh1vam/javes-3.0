from ub import tebot,client,bot
from ub.utils import register
from telethon import events
from telethon.tl import functions, types
from telethon.tl.types import Channel, Chat, User
@tebot.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def _(event):
    me = await client.get_me()
    sendr = event.chat_id
    if me.id!=sendr:
        from ub.modules.sql_helper.bot_pm_ban_sql import is_botpmbanned
        if sendr not in is_botpmbanned(sendr):
            x=await tebot.forward_messages(me.id,event.message)
            await x.reply(f'`userid` **=** {sendr} , `profile` **=** [UserProfile](tg://user?id={sendr})\n __To reply to user__ **Use** !reply {sendr};(your message or reply to a message)')

@register(outgoing=True, pattern=r"^!reply")
async def sh1vam(event):
    try :
        lb,cn=event.text[7:].split(";")
        await tebot.send_message(entity=int(lb),message=cn)
        await event.edit(f"Message sent to [User](tg://user?id={lb})")

    except:
        lb =event.text[7:]
        reply = await event.get_reply_message()
        await tebot.send_message(entity=int(lb),message=reply)
        await event.edit(f"Your Message sent to [User](tg://user?id={lb})")

        '''else:
        lb =event.text[7:]
        reply = await event.get_reply_message()
        await tebot.forward_messages(int(lb),reply)
        await event.edit(f"Your Message sent to [User](tg://user?id={lb})")
        return'''
@register(outgoing=True, pattern=r"^!botban")
async def shivam(event):
    me = await client.get_me()
    try:
       cn=event.text[8:]
       try:
          from ub.modules.sql_helper.bot_pm_ban_sql import botban     ####      bot_pm_ban_sql           botban
          botban(int(cn))
       except:
   	     pass 
       try:
           if botban(int(cn)) is False:
                return await tebot.send_message(entity=me.id,message=f"[User](tg://user?id={cn}) iz already banned")###################
       except:
            pass
       return await tebot.send_message(entity=me.id,message=f"[User](tg://user?id={cn}) iz now banned") 
    except :
       cn=event.text[8:]
       try:
           if botban(int(cn)) is False:
                return await tebot.send_message(entity=me.id,message=f"[User](tg://user?id={cn}) iz already banned")###################
       except:
            pass
       return await tebot.send_message(entity=me.id,message=f"[User](tg://user?id={cn}) iz now banned") 
    else :
        
        await tebot.send_message(entity=me.id,message=f"Unknown [User](tg://user?id={cn}) Check Your Command")
@register(outgoing=True, pattern=r"^!botunban")
async def shivam(event):
    me = await client.get_me()
    try:
       cn=event.text[8:]
       try:
          from ub.modules.sql_helper.bot_pm_ban_sql import botunban     ####      bot_pm_ban_sql           botunban
          botunban(int(cn))
       except:
   	     pass 
       try:
           if botunban(int(cn)) is False:
                return await tebot.send_message(entity=me.id,message=f"[User](tg://user?id={cn}) iz already unbanned")###################
       except:
            pass
       return await tebot.send_message(entity=me.id,message=f"[User](tg://user?id={cn}) iz now unbanned") 
    except :
       cn=event.text[8:]
       try:
           if botunban(int(cn)) is False:
                return await tebot.send_message(entity=me.id,message=f"[User](tg://user?id={cn}) iz already unbanned")###################
       except:
            pass
       return await tebot.send_message(entity=me.id,message=f"[User](tg://user?id={cn}) iz now unbanned") 
    else :
        
        await tebot.send_message(entity=me.id,message=f"Unknown [User](tg://user?id={cn}) Check Your Command")
