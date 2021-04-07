from ub.utils import register
import lyricsgenius
import os
GENIUS_API_TOKEN=os.environ.get("GENIUS_API_TOKEN",None)
@register(outgoing=True, pattern=r"^!artist ?(.*)")
async def artist(event):
    artist=event.pattern_match.group(1)
    genius = lyricsgenius.Genius(GENIUS_API_TOKEN)
    sh=genius.search_artist(artist)
    await event.edit(sh)
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
