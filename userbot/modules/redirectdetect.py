#Don't even try to come here. 
from userbot.utils import admin_cmd
from userbot import bot 
from userbot import bot as borg
import requests

#made by @THE_B_LACK_HAT & Sh1vam
@bot.on(admin_cmd(pattern=r"detect"))
async def scan(event):

	lin = event.text
	link = lin[8:]

	r = requests.get(link)


	for x in r.history:
		y=str(x.url)+" ; "
		y+=str(y)
		await event.edit(y)
	    
