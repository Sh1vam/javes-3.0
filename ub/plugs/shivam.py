
#telegram javes05




from telethon import *
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from ub.events import javes05, rekcah05
from ub import CMD_HELP, ALIVE_NAME, PM_MESSAGE, JAVES_NAME, JAVES_MSG, ORI_MSG, bot, TEMP_DOWNLOAD_DIRECTORY, BOTLOG, BOTLOG_CHATID
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)
import subprocess, io, asyncio, time, glob, os, datetime, re, json, shutil, bs4, requests, json, io
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
javes = bot
try:
  import asyncurban
except:
   pass
from bs4 import BeautifulSoup
from html import unescape
from re import findall
from random import choice
from difflib import get_close_matches
from urllib.parse import quote_plus
from urllib.error import HTTPError
from wikipedia import summary
from ub import CMD_HELP, BOTLOG, BOTLOG_CHATID,client
from wikipedia.exceptions import DisambiguationError, PageError
from urbandict import define
from requests import get
from search_engine_parser import GoogleSearch
try:
  from googleapiclient.discovery import build
  from googleapiclient.errors import HttpError
  from googletrans import LANGUAGES, Translator
except:
   pass
from gtts import gTTS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from emoji import get_emoji_regexp
from asyncio import sleep
from ub.events import register
from telethon.tl.types import DocumentAttributeAudio
from ub.javes_main.commands import progress
from ub.javes_main.extra.google_images_download import googleimagesdownload
from datetime import datetime
from PIL import Image
import urllib
from telethon.tl.types import MessageMediaPhoto
from urllib.request import urlopen
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.tl.types import DocumentAttributeVideo
try:
   from ub.javes_main.commands import meaning
except:
   pass
from ub import tebot as tgbot
from ub import bot as borg
opener = urllib.request.build_opener() ; useragent = 'Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.70 Mobile Safari/537.36' ; opener.addheaders = [('User-agent', useragent)]

async def ParseSauce(googleurl):   
    source = opener.open(googleurl).read()
    soup = BeautifulSoup(source, 'html.parser')
    results = {'similar_images': '', 'best_guess': ''}
    try:
        for similar_image in soup.findAll('input', {'class': 'gLFyf'}):
            url = 'https://www.google.com/search?tbm=isch&q=' + \
                urllib.parse.quote_plus(similar_image.get('value'))
            results['similar_images'] = url
    except BaseException:
        pass
    for best_guess in soup.findAll('div', attrs={'class': 'r5a77d'}):
        results['best_guess'] = best_guess.get_text()
    return results

async def scam(results, lim):
    single = opener.open(results['similar_images']).read()
    decoded = single.decode('utf-8')
    imglinks = []
    counter = 0
    pattern = r'^,\[\"(.*[!png|!jpg|!jpeg])\",[0-9]+,[0-9]+\]$'
    oboi = re.findall(pattern, decoded, re.I | re.M)
    for imglink in oboi:
        counter += 1
        if not counter >= int(lim):
            imglinks.append(imglink)
        else:
            break
    return imglinks


  
async def chrome(chrome_options=None):
    if chrome_options is None:
        chrome_options = await options()
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.mkdir(TEMP_DOWNLOAD_DIRECTORY)
    prefs = {'download.default_directory': TEMP_DOWNLOAD_DIRECTORY}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER,
                              options=chrome_options)
    return driver
    
@javes05(outgoing=True, pattern="^!pic (.*)")
@javes.on(rekcah05(pattern=f"pic (.*)", allow_sudo=True))
async def img_sampler(event):
    me = await event.client.get_me()
    query,limit = event.pattern_match.group(1).split(";")    
    try:
        lim = limit
    except Exception as e:
        await event.edit(str(e))
    response = googleimagesdownload()
    arguments = {
        "keywords": query,
        "limit": int(lim),
        "format": "jpg",
        "no_directory": "no_directory"
    }
    paths = response.download(arguments)
    lst = paths[0][query]
    await event.client.send_file(await event.client.get_input_entity(event.chat_id), lst, reply_to=event.message.reply_to_msg_id)
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    return await event.delete()
@tgbot.on(events.InlineQuery(pattern=r"pic (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
  builder = event.builder
  me = await client.get_me()
  query,lim = event.pattern_match.group(1).split(";")
  #query = event.pattern_match.group(1)
  if event.query.user_id == me.id:
    result=[]
    response = googleimagesdownload()
    arguments = {
        "keywords": query,
        "limit": int(lim),
        "format": "jpg",
        "no_directory": "no_directory"
    }
    paths = response.download(arguments)
    lst = paths[0][query]
    #await event.client.send_file(await event.client.get_input_entity(event.chat_id), lst, reply_to=event.message.reply_to_msg_id)
    for pic in lst:
      result.append(builder.photo(
          pic,
          # title="Shivam",
          text=query,
          buttons=[[Button.switch_inline("Search Again", query="pic ", same_peer=True)],],
      ))
    await event.answer(result)
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
  if not event.query.user_id == me.id:
      resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/Sh1vam/javes-3.0  ",buttons=[[Button.switch_inline("Search Again", query="pic ", same_peer=True)],], )
      await event.answer([resultm])
      return
