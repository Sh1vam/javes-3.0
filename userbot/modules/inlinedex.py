from pokedex import pokedex as badhiya
import os
import shutil
from re import findall
from telethon import Button, custom, events
from userbot import client
from userbot import tebot as tgbot
from userbot import tebot
from userbot.utils import admin_cmd
import requests
#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG
@tgbot.on(events.InlineQuery(pattern=r"pokedex (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):

    builder = event.builder
    query = event.text
    me = await client.get_me()
    if event.query.user_id == me.id:
        pokemon = event.pattern_match.group(1)

        rw = f"https://some-random-api.ml/pokedex?pokemon={pokemon}"
        w=requests.get(f"https://api.pokemontcg.io/v1/cards?name={pokemon}")
        lol=w.json()
        weaknesses=lol['cards'][0]['weaknesses'][0]['type']
        r = requests.get(rw)
        a=r.json()
        name=a['name']
        typ=a['type']
        species=a['species']
        abilities=a['abilities']
        height=a['height']
        weight=a['weight']
        esatge=r.json()['family']['evolutionStage']
        l=r.json()['family']['evolutionLine']
        line='\n'.join(map(str, l))
        gen=a['generation']
        description=a['description']
        typ=', '.join(map(str, typ))
        Stats=a['stats']
        species=','.join(map(str, species))
        abilities=','.join(map(str, abilities))
        poli = badhiya.Pokedex()
        pname = poli.get_pokemon_by_name(pokemon)
        pokemon = pname[0]
        lst=pokemon.get("sprite")
        cap=f'''

**NAME** : `{name}`
**TYPE** : `{typ}`
**SPECIES** : `{species}`
**Evolution Line : `{line}`
**Evolution Stage** : `{esatge}`
**Generation** : `{gen}`
**ABILITIES** : `{abilities}`
**WEAKNESSES** :`{weaknesses}` 
**HEIGHT** : `{height}`
**WEIGHT** : `{weight}`

**Stats**
\n

**Hp** : `{Stats['hp']}`
**Attack** : `{Stats['attack']}`
**Defense** : `{Stats['defense']}`
**Sp_atk** : `{Stats['sp_atk']}`
**Sp_def** : `{Stats['sp_def']}`
**Speed** : `{Stats['speed']}`
**Total** : `{Stats['total']}`

**DESCRIPTION** : `{description}`
  
    '''
        result = builder.photo(lst,text=cap,buttons=[[Button.switch_inline("Search Again", query="pokedex ", same_peer=True)],], )
        await event.answer([result])
    if not event.query.user_id == me.id:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/Sh1vam/javes-3.0  ",buttons=[[Button.switch_inline("Search Again", query="pokedex ", same_peer=True)],], )
        await event.answer([resultm])
        return
#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG
@tgbot.on(events.InlineQuery(pattern=r"pokecard(.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    query = event.text
    me = await client.get_me()
    if event.query.user_id == me.id:
        pokename=event.pattern_match.group(1)
        rw = f"https://api.pokemontcg.io/v1/cards?name={pokename}"
        r = requests.get(rw)
        a=r.json()
        o=a['cards'][0]['imageUrlHiRes']
        result = builder.photo(o,buttons=[[Button.switch_inline("Search Again", query="pokecard ", same_peer=True)],], )
        await event.answer([result])
    if not event.query.user_id == me.id:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/Sh1vam/javes-3.0  ",buttons=[[Button.switch_inline("Search Again", query="pokecard ", same_peer=True)],], )
        await event.answer([resultm])
        return
#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG#made by cyberkiller@kali~# AND SH1vam DONOT KANG