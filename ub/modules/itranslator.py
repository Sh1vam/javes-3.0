#Inline Made By Sh1vam 
from math import ceil
from ub import tebot as tgbot
from ub import bot as borg
import requests
from ub import CMD_HELP, BOTLOG, BOTLOG_CHATID,client
from telethon import Button, custom, events, functions
#Dont kang
#Telegram javes05
from googletrans import LANGUAGES, Translator
from gtts import gTTS
from gtts.lang import tts_langs
from emoji import get_emoji_regexp

from telethon.errors.rpcerrorlist import YouBlockedUserError
@tgbot.on(events.InlineQuery(pattern=r"trt(?: |$)([\s\S]*)"))
async def inline_id_handler(trans: events.InlineQuery.Event):
    builder = trans.builder
    me = await client.get_me()
    if trans.query.user_id == me.id:
        try:
            message,TRT_LANG = trans.pattern_match.group(1).split(";")
        except:
            message = trans.pattern_match.group(1)
            TRT_LANG = "en"
        if TRT_LANG in LANGUAGES:
            translator = Translator()
            reply_text = translator.translate(message, dest=TRT_LANG)
            source_lan = LANGUAGES[f'{reply_text.src.lower()}']
            transl_lan = LANGUAGES[f'{reply_text.dest.lower()}']
            #reply_text = f"From **{source_lan.title()}**\nTo **{transl_lan.title()}:**\n\n{reply_text.text}"
            s = builder.article(title=f"From {source_lan.title()} To {transl_lan.title()}",description=reply_text.text,text=reply_text.text,buttons=[[Button.switch_inline("Search Again", query="trt", same_peer=True)],], )
        else:
            reply_text = f"`Invalid Language code !!`\n`Available language codes for TRT`:\n\n`{LANGUAGES}`"
            s = builder.article(title="Invalid Language code !!",description="Check Your Input",text=reply_text,buttons=[[Button.switch_inline("Search Again", query="trt ", same_peer=True)],], )
        await trans.answer([s])
        return

    if not trans.query.user_id == me.id:
        s = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/Sh1vam/javes-3.0  ",buttons=[[Button.switch_inline("Search Again", query="trt ", same_peer=True)],], )
        await trans.answer([s])
        return
