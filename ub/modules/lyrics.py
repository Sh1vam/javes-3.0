from ub.utils import register
import lyricsgenius
from telethon import events
import os
GENIUS_API_TOKEN=os.environ.get("GENIUS_API_TOKEN",None)
@register(outgoing=True, pattern=r"^!artist ?(.*)")
async def artist(event):
    l=[]
    artist=event.pattern_match.group(1)
    genius = lyricsgenius.Genius(GENIUS_API_TOKEN)
    shivam=genius.search_artist(artist)
    l.append(shivam)
    limits = 4096
    ladybug = [l[miracul:miracul+limits] for miracul in range(0, len(l), limits)]
    for miracul in ladybug:
            chatnoir = f"{miracul}"
            await event.client.send_message(event.chat_id, chatnoir)
@register(outgoing=True, pattern=r"^!lyrics ?(.*)")
async def lyrics(event):
    try :
        song,artist=event.pattern_match.group(1).split(";")
        genius = lyricsgenius.Genius(GENIUS_API_TOKEN)
        sh=genius.search_song(song,artist).lyrics
        await event.edit(sh)
    except:
        song=event.pattern_match.group(1)
        genius = lyricsgenius.Genius(GENIUS_API_TOKEN)
        sh=genius.search_song(song).lyrics
        await event.edit(sh)
