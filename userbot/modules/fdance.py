"""Emoji

Available Commands:

.isro

built by @r4v4n4 , isse bhi loot lo betichod"""
from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID,client

from userbot.events import javes05, bot, rekcah05

javes = client = bot
from telethon import events

import asyncio

from userbot.util import admin_cmd
from userbot import tebot as tgbot
from userbot import bot as borg


@borg.on(admin_cmd(pattern=r"fdance"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 5)

    #input_str = event.pattern_match.group(1)

  #  if input_str == "isro":

    await event.edit("Connecting..")

    animation_chars = [
        
            "⠀⠀⠀⣶⣿⣶/n⠀⠀⠀⣿⣿⣿⣀/n⠀⣀⣿⣿⣿⣿⣿⣿/n⣶⣿⠛⣭⣿⣿⣿⣿/n⠛⠛⠛⣿⣿⣿⣿⠿/n⠀⠀⠀⠀⣿⣿⣿/n⠀⠀⣀⣭⣿⣿⣿⣿⣀/n⠀⠤⣿⣿⣿⣿⣿⣿⠉/n⠀⣿⣿⣿⣿⣿⣿⠉/n⣿⣿⣿⣿⣿⣿/n⣿⣿⣶⣿⣿/n⠉⠛⣿⣿⣶⣤/n⠀⠀⠉⠿⣿⣿⣤/n⠀⠀⣀⣤⣿⣿⣿/n⠀⠒⠿⠛⠉⠿⣿/n⠀⠀⠀⠀⠀⣀⣿⣿/n⠀⠀⠀⠀⣶⠿⠿⠛/n",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤/n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿/n⠀⠀⣶⠀⠀⣀⣤⣶⣤⣉⣿⣿⣤⣀/n⠤⣤⣿⣤⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣀/n⠀⠛⠿⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⠉⠛⠿⣿⣤/n⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⠛⠀⠀⠀⣶⠿/n⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣤⠀⣿⠿/n⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿/n⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⠿⠉⠉/n⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠿/n⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠉/n⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⣭⣶⣀/n⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿/n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⣿/n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿/n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⠀⣶⠿/n⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠿/n⠀⠀⠀⠀⠀⠀⠀⠛⠿⠛/n",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶/n⠀⠀⠀⠀⠀⣀⣀⠀⣶⣿⣿⠶/n⣶⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤/n⠀⠉⠶⣶⣀⣿⣿⣿⣿⣿⣿⣿⠿⣿⣤⣀/n⠀⠀⠀⣿⣿⠿⠉⣿⣿⣿⣿⣭⠀⠶⠿⠿/n⠀⠀⠛⠛⠿⠀⠀⣿⣿⣿⣉⠿⣿⠶/n⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿/n⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠒/n⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⣿/n⠀⠀⠀⠀⠀⣿⣿⣿⠛⣭⣭⠉/n⠀⠀⠀⠀⠀⣿⣿⣭⣤⣿⠛/n⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⣭/n⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⠿⣶⣤/n⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⣶⣶⠿⠿⠿/n⠀⠀⠀⠀⠀⠀⣿⠛/n⠀⠀⠀⠀⠀⠀⣭⣶/n",
            "⠀⠀⠀⠀⠀⠀⣶⣿⣶/n⠀⠀⠀⣤⣤⣤⣿⣿⣿/n⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣶/n⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿/n⠀⠀⣿⣉⣿⣿⣿⣿⣉⠉⣿⣶/n⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿/n⠀⣤⣿⣿⣿⣿⣿⣿⣿⠿⠀⣿⣶/n⣤⣿⠿⣿⣿⣿⣿⣿⠿⠀⠀⣿⣿⣤/n⠉⠉⠀⣿⣿⣿⣿⣿⠀⠀⠒⠛⠿⠿⠿/n⠀⠀⠀⠉⣿⣿⣿⠀⠀⠀⠀⠀⠀⠉/n⠀⠀⠀⣿⣿⣿⣿⣿⣶/n⠀⠀⠀⠀⣿⠉⠿⣿⣿/n⠀⠀⠀⠀⣿⣤⠀⠛⣿⣿/n⠀⠀⠀⠀⣶⣿⠀⠀⠀⣿⣶/n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿/n⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠉/n",
            "⠀⠀⠀⠀⠀⠀⣤⣶⣶/n⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣀⣀/n⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿/n⣤⣶⣀⠿⠶⣿⣿⣿⠿⣿⣿⣿⣿/n⠉⠿⣿⣿⠿⠛⠉⠀⣿⣿⣿⣿⣿/n⠀⠀⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣤⣤/n⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿/n⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿/n⠀⠀⠀⠀⣀⣿⣿⣿⠿⠉⠀⠀⣿⣿⣿⣿/n⠀⠀⠀⠀⣿⣿⠿⠉⠀⠀⠀⠀⠿⣿⣿⠛/n⠀⠀⠀⠀⠛⣿⣿⣀⠀⠀⠀⠀⠀⣿⣿⣀/n⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠿⣿⣿/n⠀⠀⠀⠀⠀⠉⣿⣿⠀⠀⠀⠀⠀⠀⠉⣿/n⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣀⣿/n⠀⠀⠀⠀⠀⠀⣀⣿⣿/n⠀⠀⠀⠀⠤⣿⠿⠿⠿/n",    


 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 5])



#
import os
import re
import urllib
from math import ceil

import requests
from telethon import Button, custom, events, functions
from youtubesearchpython import SearchVideos

from userbot import ALIVE_NAME, CMD_HELP, CMD_LIST


@tgbot.on(events.InlineQuery(pattern=r"tor (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    me = await client.get_me()
    inp = event.pattern_match.group(1)
    if event.query.user_id == me.id:
        sn = urllib.parse.quote_plus(inp)
        results = []
        sl = "https://api.sumanjay.cf/torrent/?query=" + sn
        try:
            op = requests.get(url=sl, timeout=10).json()
        except:
            pass
        ed = len(op)
        if  ed == 0:
            resultm = builder.article(
                title="No Result",
                description="Try Again With correct Spelling",
                text="**No Matching Found**",
                buttons=[
                    [
                        Button.switch_inline(
                            "Search Again", query="torrent ", same_peer=True
                        )
                    ],
                ],
            )
            await event.answer([resultm])
            return
        if  ed > 30:
            for i in range(30):
                ds = op[i]["age"]
                ops = op[i]["leecher"]
                ssk = op[i]["magnet"]
                okk = op[i]["name"]
                sizes = op[i]["size"]
                type = op[i]["type"]
                seeders = op[i]["seeder"]
                ok = f"**Title :** `{okk}` \n**Size :** `{sizes}` \n**Type :** `{type}` \n**Seeder :** `{seeders}` \n**Leecher :** `{ops}` \n**Magnet :** `{ssk}` "
                me = f"Size : {sizes} Type : {type} Age : {ds}"
                results.append(
                    await event.builder.article(
                        title=okk,
                        description=me,
                        text=ok,
                        buttons=Button.switch_inline(
                            "Search Again", query="tor ", same_peer=True
                        ),
                    )
                )
        else:
            for dz in op:
                siz = dz["size"]
                typ = dz["type"]
                seede = dz["seeder"]
                ag = dz["age"]
                leech = dz["leecher"]
                mag = dz["magnet"]
                nam = dz["name"]            
                all = f"**Title :** `{nam}` \n**Size :** `{siz}` \n**Type :** `{typ}` \n**Seeder :** `{seede}` \n**Leecher :** `{leech}` \n**Magnet :** `{mag}` "
                mi = f"Size : {siz} Type : {typ} Age : {ag}"
                results.append(
                    await event.builder.article(
                        title=nam,
                        description=mi,
                        text=all,
                        buttons=[
                            Button.switch_inline(
                                "Search Again", query="tor ", same_peer=True
                            )
                        ],
                    )
                )
        await event.answer(results)
    if not event.query.user_id == me.id:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/Sh1vam/javes-2.0  ",buttons=[[Button.switch_inline("Search Again", query="exec ", same_peer=True)],], )
        await event.answer([resultm])
        return

@tgbot.on(events.InlineQuery(pattern=r"yt (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    testinput = event.pattern_match.group(1)
    urllib.parse.quote_plus(testinput)
    me = await client.get_me()
    if event.query.user_id == me.id:
        results = []
        search = SearchVideos(f"{testinput}", offset=1, mode="dict", max_results=30)
        mi = search.result()
        moi = mi["search_result"]
        if search == None:
            resultm = builder.article(
                title="No Results.",
                description="Try Again With correct Spelling",
                text="**No Matching Found**",
                buttons=[
                    [Button.switch_inline("Search Again", query="yt ", same_peer=True)],
                ],
            )
            await event.answer([resultm])
            return
        for mio in moi:
            mo = mio["link"]
            thum = mio["title"]
            fridayz = mio["id"]
            thums = mio["channel"]
            td = mio["duration"]
            tw = mio["views"]
            kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
            okayz = f"**Title :** `{thum}` \n**Link :** {mo} \n**Channel :** `{thums}` \n**Views :** `{tw}` \n**Duration :** `{td}`"
            hmmkek = f"Channel : {thums} \nDuration : {td} \nViews : {tw}"
            results.append(
                await event.builder.article(
                    title=thum,
                    description=hmmkek,
                    text=okayz,
                    buttons=Button.switch_inline(
                        "Search Again", query="yt ", same_peer=True
                    ),
                )
            )
        await event.answer(results)

    if not event.query.user_id == me.id:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/Sh1vam/javes-2.0  ",buttons=[[Button.switch_inline("Search Again", query="exec ", same_peer=True)],], )
        await event.answer([resultm])
        return

#

#
