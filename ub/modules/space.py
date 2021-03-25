from ub import bot
from ub.utils import admin_cmd

@bot.on(admin_cmd(pattern=r"space"))
async def space(e):
    await e.edit("ㅤ")
@bot.on(admin_cmd(pattern=r"blank"))
async def blank(e):
    await e.edit("­")
