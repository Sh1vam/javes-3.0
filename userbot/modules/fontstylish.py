from userbot import bot
import asyncio
from userbot.utils import admin_cmd
import random
from userbot import bot
from userbot import bot as borg
from telethon import Button, custom, events
from userbot import CMD_HELP,  client
from userbot import tebot as tgbot
from userbot import tebot
from userbot.helpers.funts import DC_STYLE as DC_FONT_STYLE
from userbot.helpers.funts import DARKFONTS as DCFONTS
from userbot.helpers.funts import SIMPLESTDC as SIMPLEDC
#by @I_am_Banned
#dont kang
#team dc

async def dc_font_maker(dc_type_choice, dc_input):
    if dc_type_choice not in DCFONTS:
        return False
    font_type = list(DCFONTS[dc_type_choice])
    for i in dc_input:
        if i in list(SIMPLEDC):
            new_char = font_type[list(SIMPLEDC).index(i)]
            dc_input = dc_input.replace(i, new_char)
    return dc_input
    
@borg.on(admin_cmd(pattern="sfonts"))
async def teamdc(event):
    await event.edit("serif\nsans\nsans_i\nserif_i\nmedi_b\nmedi\ndouble\ncursive_b\ncursive\nbigsmall\nreverse\ncircle\ncircle_b\nmono\nsquare_b\nsquare\nsmoth\ngoth\nwide\nweb\nweeb\nweeeb\ntwist\ntwist_b\ntwist_c\n")
    
    
@borg.on(admin_cmd(pattern="fstyle (.*)"))
async def teamdc(event):
    reply = await event.get_reply_message()
    sh1vam = event.pattern_match.group(1)
    if ";" in sh1vam:
        rabbit, atul = sh1vam.split(";")
    else:
        rabbit = sh1vam
        atul = ""
    shivam = rabbit or reply.text
    if not shivam:
        await event.edit("Please give some words to Style.")
        return
    await event.edit("Doing some Black Magic")
    if atul:
        font_choice = atul
        dctxt = shivam
        if atul not in DC_FONT_STYLE:
            await event.edit("Please select a valid Font Style!")
            return
    else:
        font_choice = random.choice(DC_FONT_STYLE)
        dctxt = shivam
    dcfontchoice = font_choice.replace(";", "")
    danish = await dc_font_maker(dcfontchoice, dctxt)
    await event.edit(danish)

@tgbot.on(events.InlineQuery(pattern=r"sfonts"))
async def teamdc(event: events.InlineQuery.Event):
    builder = event.builder
    me = await client.get_me()
    if event.query.user_id == me.id:
        resultm = builder.article(title="Fonts",description="Available Fonts.",text="serif\nsans\nsans_i\nserif_i\nmedi_b\nmedi\ndouble\ncursive_b\ncursive\nbigsmall\nreverse\ncircle\ncircle_b\nmono\nsquare_b\nsquare\nsmoth\ngoth\nwide\nweb\nweeb\nweeeb\ntwist\ntwist_b\ntwist_c\n",buttons=[[Button.switch_inline("Search Again", query="sfonts  ", same_peer=True)],],)
        await event.answer([resultm])
    if not event.query.user_id == me.id:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/Sh1vam/javes-3.0  ",buttons=[[Button.switch_inline("Search Again", query="sfonts  ", same_peer=True)],], )
        await e.answer([resultm])
        return
@tgbot.on(events.InlineQuery(pattern=r"fstyle (.*)"))
async def teamdc(event: events.InlineQuery.Event):
    builder = event.builder
    me = await client.get_me()
    if event.query.user_id == me.id:
        sh1vam = event.pattern_match.group(1)
        if ";" in sh1vam:
            rabbit, atul = sh1vam.split(";")
        else:
            rabbit = sh1vam
            atul = ""
        shivam = rabbit
        if not shivam:
            resultm = builder.article(title="Please add some text.",description="Give some Correct input",text="Type some words or text to style.",buttons=[[Button.switch_inline("Search Again", query="fstyle ", same_peer=True)],],)
            await event.answer([resultm])
            return
        #await event.edit("Doing some Black Magic")
        if atul:
            font_choice = atul
            dctxt = shivam
            if atul not in DC_FONT_STYLE:
                resultm = builder.article(title="Invalid Font Choosen",description="Give Some Correct input",text="Send .sfonts to see the available fonts.",buttons=[[Button.switch_inline("Search Again", query="fstyle ", same_peer=True)],],)
                await event.answer([resultm])
                return
        else:
            font_choice = random.choice(DC_FONT_STYLE)
            dctxt = shivam
        dcfontchoice = font_choice.replace(";", "")
        danish = await dc_font_maker(dcfontchoice, dctxt)
        result = builder.article(title=shivam,description=dcfontchoice,text=f"{danish}",buttons=[[Button.switch_inline("Search Again", query="fstyle ", same_peer=True)],],)
        await event.answer([result])
    if not event.query.user_id == me.id:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/Sh1vam/javes-3.0  ",buttons=[[Button.switch_inline("Search Again", query="fstyle ", same_peer=True)],], )
        await event.answer([resultm])
        return
