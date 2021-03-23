import os
import asyncio
from getpass import getuser
from subprocess import PIPE
from subprocess import run as runapp
import pybase64
from os import remove
from sys import executable
from ub import CMD_HELP, BOTLOG, BOTLOG_CHATID,client
from ub.events import javes05, bot, rekcah05
javes = client = bot
from ub import CMD_HELP, ALIVE_NAME, PM_MESSAGE, JAVES_NAME, JAVES_MSG, ORI_MSG
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)
FULL_SUDO = os.environ.get("FULL_SUDO", None)
import inspect
running_processes: dict = {}
import os
import re
import urllib
from math import ceil
from ub import tebot as tgbot
from ub import bot as borg
import requests
from telethon import Button, custom, events, functions
#MADE BY SH1VAM USED CODES OF ORIGINAL JAVES 
# DONOT KANG
#HEHE I SECURED HARMFUL CMDS TOO 
#BY SHIVAM 




@tgbot.on(events.InlineQuery(pattern=r"exec (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):

    builder = event.builder
    code = event.pattern_match.group(1)
    urllib.parse.quote_plus(code)
    me = await client.get_me()
    if event.query.user_id == me.id:
        if not code:
                resultm = builder.article(title="No Results.",description="hmm",text=f"`{JAVES_NNAME}:` **At least a variable is required toexecute. Use !help script for an example.**",buttons=[[Button.switch_inline("Search Again", query="exec ", same_peer=True)],],)
                await event.answer([resultm])
                return
        if code in ("ub.session", "env", "printenv"):
                resultm = builder.article(title="Privacy Issue.",description="hmmm",text=f"`{JAVES_NNAME}:` **Privacy Error, This command not permitted**",buttons=[[Button.switch_inline("Search Again", query="exec ", same_peer=True)],], )
                await event.answer([resultm])
                return
        if len(code.splitlines()) <= 5:
                codepre = code
        else:
                clines = code.splitlines()
                codepre = clines[0] + "\n" + clines[1] + "\n" + clines[2] + \
		    "\n" + clines[3] + "..."
        command = "".join(f"\n {l}" for l in code.split("\n.strip()"))
        process = await asyncio.create_subprocess_exec(
		executable,
		'-c',
		command.strip(),
		stdout=asyncio.subprocess.PIPE,
		stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()
        result = str(stdout.decode().strip()) \
		+ str(stderr.decode().strip())
        if result:
            if len(result) > 4096:
                    file = open("exec.txt", "w+")
                    file.write(result)
                    file.close()
                    resultm = builder.document("exec.txt",title="text too long",description="click me",text=f"`{JAVES_NNAME}:` **Output too large sended as file,U Can Use !exec**",buttons=[[Button.switch_inline("Search Again", query="exec ", same_peer=True)],], )
                    await event.answer([resultm])
                    remove("exec.txt")
                    return
            resultm = builder.article(title=f"{codepre}",description=f"{result}",text=f"**Query: **`\n{codepre}`\n**Result: **\n`{result}`",buttons=[[Button.switch_inline("Search Again", query="exec ", same_peer=True)],], )
            await event.answer([resultm])
            return
    else:
                resultm = builder.article(title=f"{codepre}",description="No Result Returned",text=f"**Query: **\n{codepre}\n**Result: **\n`No Result Returned/False`",buttons=[[Button.switch_inline("Search Again", query="exec ", same_peer=True)],], )
                await event.answer([resultm])
                return
    if not event.query.user_id == me.id:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/Sh1vam/javes-3.0  ",buttons=[[Button.switch_inline("Search Again", query="exec ", same_peer=True)],], )
        await event.answer([resultm])
        return

@tgbot.on(events.InlineQuery(pattern=r"eval (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    me = await client.get_me()
    if event.query.user_id == me.id:
        if event.pattern_match.group(1):
                expression = event.pattern_match.group(1)
                urllib.parse.quote_plus(expression)
        else:
                resultm = builder.article(title="hey man",description="uuf",text=f"`{JAVES_NNAME}:` **At least a variable is required to execute. Use !help script for an example.**",buttons=[[Button.switch_inline("Search Again", query="eval ", same_peer=True)],], )
                await event.answer([resultm])
                return
        if expression in ("ub.session", "env", "printenv"):
                resultm = builder.article(title="Privacy Issue....",description="Bruh",text=f"`{JAVES_NNAME}:` **Privacy Error, This command not permitted**",buttons=[[Button.switch_inline("Search Again", query="eval ", same_peer=True)],], )
                await event.answer([resultm])
                return
        try:
                evaluation = str(eval(expression))
                if evaluation:
                    if isinstance(evaluation, str):
                        if len(evaluation) >= 4096:
                            file = open("eval.txt", "w+")
                            file.write(evaluation)
                            file.close()
                            resultm = builder.document("eval.txt",title="hehe text too long",description="Doc",text=f"`{JAVES_NNAME}:` **Output too large Snded as file, Can also use !eval**",buttons=[[Button.switch_inline("Search Again", query="eval ", same_peer=True)],], )
                            await event.answer([resultm])
                            remove("eval.txt")
                            return
                        else:
                            resultm = builder.article(title=f"{expression}",description=f"{evaluation}",text=f"**Query: **\n{expression}\n**Result: **\n`{evaluation}`",buttons=[[Button.switch_inline("Search Again", query="eval ", same_peer=True)],], )
                            await event.answer([resultm])
                            return
                else:
                    resultm = builder.article(title=f"{expression}",description="No Result Returned",text=f"**Query: **\n{expression}\n**Result: **\n`No Result Returned/False`",buttons=[[Button.switch_inline("Search Again", query="eval ", same_peer=True)],], )
                    await event.answer([resultm])
                    return
        except Exception as err:
                resultm = builder.article(title=f"{expression}",description=f"{err}",text=f"**Query: **\n{expression}`\n**Result: **\n`{err}",buttons=[[Button.switch_inline("Search Again", query="eval ", same_peer=True)],], )
                await event.answer([resultm])
                return
    if not event.query.user_id == me.id:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/Sh1vam/javes-3.0  ",buttons=[[Button.switch_inline("Search Again", query="eval ", same_peer=True)],], )
        await event.answer([resultm])
        return
@tgbot.on(events.InlineQuery(pattern=r"hash (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    me = await client.get_me()
    if event.query.user_id == me.id:
        hashtxt_ = event.pattern_match.group(1)
        urllib.parse.quote_plus(hashtxt_)
        hashtxt = open("hashdis.txt", "w+")
        hashtxt.write(hashtxt_)
        hashtxt.close()
        md5 = runapp(["md5sum", "hashdis.txt"], stdout=PIPE)
        md5 = md5.stdout.decode()
        sha1 = runapp(["sha1sum", "hashdis.txt"], stdout=PIPE)
        sha1 = sha1.stdout.decode()
        sha256 = runapp(["sha256sum", "hashdis.txt"], stdout=PIPE)
        sha256 = sha256.stdout.decode()
        sha512 = runapp(["sha512sum", "hashdis.txt"], stdout=PIPE)
        runapp(["rm", "hashdis.txt"], stdout=PIPE)
        sha512 = sha512.stdout.decode()
        ans = ("Text: `" + hashtxt_ + "`\nMD5: `" + md5 + "`SHA1: `" + sha1 +
               "`SHA256: `" + sha256 + "`SHA512: `" + sha512[:-1] + "`")
        if len(ans) > 4096:
            hashfile = open("hashes.txt", "w+")
            hashfile.write(ans)
            hashfile.close()
            resultm = builder.document("hashes.txt",title="Really",description="A FILE",text=f"`{JAVES_NNAME}:` **Output too large sended as doc ,can also use !hash**",buttons=[[Button.switch_inline("Search Again", query="hash ", same_peer=True)],], )
            await event.answer([resultm])
            runapp(["rm", "hashes.txt"], stdout=PIPE)
            return
        else:
            resultm = builder.article(title="Haha",description="Click Me",text=ans,buttons=[[Button.switch_inline("Search Again", query="hash ", same_peer=True)],], )
            await event.answer([resultm])
            return
    if not event.query.user_id == me.id:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/Sh1vam/javes-3.0  ",buttons=[[Button.switch_inline("Search Again", query="hash ", same_peer=True)],], )
        await event.answer([resultm])
        return
@tgbot.on(events.InlineQuery(pattern=r"base64 (en|de) (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):

    builder = event.builder
    me = await client.get_me()
    if event.query.user_id == me.id:
        if event.pattern_match.group(1) == "en":
            lething = str(
                pybase64.b64encode(bytes(event.pattern_match.group(2),
                                         "utf-8")))[2:]

            resultm = builder.article(title="Encoded",description=lething[:-1],text="Encoded: `" + lething[:-1] + "`",buttons=[[Button.switch_inline("Search Again", query="base64 ", same_peer=True)],], )
            await event.answer([resultm])
            return

        else:
            lething = str(
                pybase64.b64decode(bytes(event.pattern_match.group(2), "utf-8"),
                                   validate=True))[2:]
            resultm = builder.article(title="Decoded",description=lething[:-1],text="Decoded: `" + lething[:-1] + "`",buttons=[[Button.switch_inline("Search Again", query="base64 ", same_peer=True)],], )
            await event.answer([resultm])
            return
    if not event.query.user_id == me.id:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/Sh1vam/javes-3.0  ",buttons=[[Button.switch_inline("Search Again", query="base64 ", same_peer=True)],], )
        await event.answer([resultm])
        return
