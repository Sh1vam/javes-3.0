# By dark cobra for Dark cobra with logger support
# Kang with credits..
# edited by @danish_00
import asyncio
from asyncio import wait
from userbot import CMD_HELP


from userbot.events import register


@register(outgoing=True, pattern="^!spamall")
async def tiny_pic_spam(e):
    reply = await e.get_reply_message()
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        text = message.split()
        counter = int(text[1])
        media = await e.client.download_media(reply)
        for i in range(1, counter):
            await e.client.send_file(e.chat_id, media)
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP,
                "#PICSPAM \n\n"
                "PicSpam was executed successfully"
                )