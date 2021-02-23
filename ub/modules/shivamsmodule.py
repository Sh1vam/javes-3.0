from math import ceil
from ub import tebot as tgbot
from ub import bot as borg
import requests
from ub import CMD_HELP, BOTLOG, BOTLOG_CHATID,client
from telethon import Button, custom, events, functions
#by Shivam don't kang
@tgbot.on(events.InlineQuery(pattern=r"ihelp"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    me = await client.get_me()
    if event.query.user_id == me.id:
            s = builder.article(title="Inline Help",description="For Inline commands",text="for cmd like yt,google and pic u need to specify Querry;number and for base64 :- base64 (en|de) querry;for whisper u need @username Querry and for button see .chkbutton",buttons=[[Button.switch_inline("Inline Help", query="ihelp", same_peer=True),Button.switch_inline("Alive", query="alive", same_peer=True),Button.switch_inline("Javes", query="javes", same_peer=True),Button.switch_inline("Button Url", query="url", same_peer=True)],[Button.switch_inline("Base64", query="base64 ", same_peer=True),Button.switch_inline("Help", query="helpme", same_peer=True),Button.switch_inline("Torrent", query="uninstall ", same_peer=True),Button.switch_inline("You Tube", query="yt ", same_peer=True)],[Button.switch_inline("Pic", query="pic ", same_peer=True),Button.switch_inline("Exec", query="exec ", same_peer=True),Button.switch_inline("Eval", query="eval ", same_peer=True),Button.switch_inline("Bot Logs", query="logs", same_peer=True)],[Button.switch_inline("Hash", query="hash ", same_peer=True),Button.switch_inline("Whisper", query="secret ", same_peer=True),Button.switch_inline("Url Button", query="buttons ", same_peer=True),Button.switch_inline("Send Module", query="send ", same_peer=True)],[Button.switch_inline("Send Helper", query="hsend ", same_peer=True),Button.switch_inline("Send SQL", query="ssend ", same_peer=True),Button.switch_inline("Google Search", query="google ", same_peer=True),Button.switch_inline("Figlet", query="figlet ", same_peer=True)],[Button.switch_inline("Style Fonts", query="fstyle ", same_peer=True),Button.switch_inline("List Font Styles", query="sfonts ", same_peer=True),Button.switch_inline("Pokedex", query="pokedex ", same_peer=True),Button.switch_inline("Pokecard", query="pokecard ", same_peer=True)],[Button.inline('❌ Close menu', b'close')],] )
            await event.answer([s])
            return
    if not event.query.user_id == me.id:
        s = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/Sh1vam/javes-3.0  ",buttons=[[Button.switch_inline("Search Again", query="ihelp", same_peer=True)],], )
        await event.answer([s])
        return
