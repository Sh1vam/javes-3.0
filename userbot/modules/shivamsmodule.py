from math import ceil
from userbot import tebot as tgbot
from userbot import bot as borg
import requests
from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID,client
from telethon import Button, custom, events, functions
#by Shivam don't kang
@tgbot.on(events.InlineQuery(pattern=None))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    me = await client.get_me()
    if event.query.user_id == me.id:
            resultm = builder.article(title="Inline Help",description="Inline commands",text="for cmd like yt and pic u need to specify Querry;number and for base64 :- base64 (en|de) querry;for whisper u need @username Querry and for button see .chkbutton",buttons=[[Button.switch_inline("Base64", query="base64 ", same_peer=True),Button.switch_inline("Help", query="helpme", same_peer=True),Button.switch_inline("Torrent", query="tor ", same_peer=True),Button.switch_inline("You Tube", query="yt ", same_peer=True)],[Button.switch_inline("Pic", query="pic ", same_peer=True),Button.switch_inline("Exec", query="exec ", same_peer=True),Button.switch_inline("Eval", query="eval ", same_peer=True)],[Button.switch_inline("Hash", query="hash ", same_peer=True),Button.switch_inline("Whisper", query="secret ", same_peer=True),Button.switch_inline("Url Button", query="secrete ", same_peer=True)],[Button.inline('Go back', 'back'),Button.inline('❌ Close menu', b'close')],] )
            await event.answer([resultm])
            return
    if not event.query.user_id == me.id:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/Sh1vam/javes-3.0  ",buttons=[[Button.switch_inline("Search Again", query=None, same_peer=True)],], )
        await event.answer([resultm])
        return
