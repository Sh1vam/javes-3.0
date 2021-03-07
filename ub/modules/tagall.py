# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from ub.utils import admin_cmd
from ub import bot as javes
#MODIFIED BY SH1VAM
@javes.on(admin_cmd(pattern=r"tagall", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    shiv= event.text
    shivam=shiv[8:]
    mentions = f"{shivam}"
    chat = await event.get_input_chat()
    async for x in javes.iter_participants(chat):
        if x.username == None:
            mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
        else :
            mentions +=f" \n [{x.first_name}](tg://user?id={x.id}),( @{x.username} )"
    #await event.edit(mentions)
    await event.delete()
    try:
        if event.reply_to_msg_id:
            await javes.send_message(event.chat_id,mentions,reply_to=event.reply_to_msg_id)
        else:
            await javes.send_message(event.chat_id,mentions)
        #await event.delete()
    except:
        limits = 4096
        ladybug = [mentions[miracul:miracul+limits] for miracul in range(0, len(mentions), limits)]
        for miracul in ladybug:
            chatnoir = f"**{shivam}** \n{miracul}"
            await event.client.send_message(event.chat_id, chatnoir)
@javes.on(admin_cmd(pattern=r"admin", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    shiv= event.text
    shivam=shiv[7:]
    mentions = f"{shivam}"
    chat = await event.get_input_chat()
    async for x in javes.iter_participants(chat, filter=ChannelParticipantsAdmins):
        if x.username == None:
            mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
        else :
            mentions +=f" \n [{x.first_name}](tg://user?id={x.id}),( @{x.username} )"
    #await event.edit(mentions)
    await event.delete()
    try:
        if event.reply_to_msg_id:
            await javes.send_message(event.chat_id,mentions,reply_to=event.reply_to_msg_id)
        else:
            await javes.send_message(event.chat_id,mentions)
    except:
        limits = 4096
        ladybug = [mentions[miracul:miracul+limits] for miracul in range(0, len(mentions), limits)]
        for miracul in ladybug:
            chatnoir = f"**{shivam}** \n{miracul}"
            await event.client.send_message(event.chat_id, chatnoir)
    #await event.delete()
