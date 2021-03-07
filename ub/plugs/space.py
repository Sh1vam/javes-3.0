from ub import bot
from ub.utils import admin_cmd

@bot.on(admin_cmd(pattern=r"space"))
async def space(e):
    await e.edit("ㅤㅤㅤㅤㅤㅤ")
