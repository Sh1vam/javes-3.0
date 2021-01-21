"""
Created by @mrconfused and @sandy1709
memify plugin
"""
import asyncio
import os
import random

from userbot.helpers import (
    add_frame,
    asciiart,
    convert_toimage,
    convert_tosticker,
    crop,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    runcmd,
    solarize,
    take_screen_shot,
)
import asyncio
import os
import shlex
from os import getcwd
from os.path import basename, join
from textwrap import wrap
from typing import Optional, Tuple

import numpy as np


from PIL import Image, ImageDraw, ImageFont
from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image as catimage

MARGINS = [50, 150, 250, 350, 450]
CNG_FONTS = "userbot/helpers/styles/impact.ttf"
font_list = os.system("ls userbot/helpers/styles")
FONTS = list(font_list)
from userbot.utils import admin_cmd
from userbot import bot , CMD_HELP
async def cat_meme(CNG_FONTS, topString, bottomString, filename, endname):
    img = Image.open(filename)
    imageSize = img.size
    # find biggest font size that works
    fontSize = int(imageSize[1] / 5)
    font = ImageFont.truetype(CNG_FONTS, fontSize)
    topTextSize = font.getsize(topString)
    bottomTextSize = font.getsize(bottomString)
    while topTextSize[0] > imageSize[0] - 20 or bottomTextSize[0] > imageSize[0] - 20:
        fontSize -= 1
        font = ImageFont.truetype(CNG_FONTS, fontSize)
        topTextSize = font.getsize(topString)
        bottomTextSize = font.getsize(bottomString)

    # find top centered position for top text
    topTextPositionX = (imageSize[0] / 2) - (topTextSize[0] / 2)
    topTextPositionY = 0
    topTextPosition = (topTextPositionX, topTextPositionY)

    # find bottom centered position for bottom text
    bottomTextPositionX = (imageSize[0] / 2) - (bottomTextSize[0] / 2)
    bottomTextPositionY = imageSize[1] - bottomTextSize[1]
    bottomTextPosition = (bottomTextPositionX, bottomTextPositionY)
    draw = ImageDraw.Draw(img)
    # draw outlines
    # there may be a better way
    outlineRange = int(fontSize / 15)
    for x in range(-outlineRange, outlineRange + 1):
        for y in range(-outlineRange, outlineRange + 1):
            draw.text(
                (topTextPosition[0] + x, topTextPosition[1] + y),
                topString,
                (0, 0, 0),
                font=font,
            )
            draw.text(
                (bottomTextPosition[0] + x, bottomTextPosition[1] + y),
                bottomString,
                (0, 0, 0),
                font=font,
            )
    draw.text(topTextPosition, topString, (255, 255, 255), font=font)
    draw.text(bottomTextPosition, bottomString, (255, 255, 255), font=font)
    img.save(endname)


async def cat_meeme(upper_text, lower_text, CNG_FONTS, picture_name, endname):
    main_image = catimage(filename=picture_name)
    main_image.resize(
        1024, int(((main_image.height * 1.0) / (main_image.width * 1.0)) * 1024.0)
    )
    upper_text = "\n".join(wrap(upper_text, get_warp_length(main_image.width))).upper()
    lower_text = "\n".join(wrap(lower_text, get_warp_length(main_image.width))).upper()
    lower_margin = MARGINS[lower_text.count("\n")]
    text_draw = Drawing()
    text_draw.font = join(getcwd(), CNG_FONTS)
    text_draw.font_size = 100
    text_draw.text_alignment = "center"
    text_draw.stroke_color = Color("black")
    text_draw.stroke_width = 3
    text_draw.fill_color = Color("white")
    if upper_text:
        text_draw.text((main_image.width) // 2, 80, upper_text)
    if lower_text:
        text_draw.text(
            (main_image.width) // 2, main_image.height - lower_margin, lower_text
        )
    text_draw(main_image)
    main_image.save(filename=endname)
def random_color():
    number_of_colors = 2
    return [
        "#" + "".join(random.choice("0123456789ABCDEF") for j in range(6))
        for i in range(number_of_colors)
    ]


CNG_FONTS = "userbot/helpers/styles/impact.ttf"



@bot.on(admin_cmd(outgoing=True, pattern="(mm3f|mm3s) ?(.*)"))

async def memes(cat):
    if cat.fwd_from:
        return
    cmd = cat.pattern_match.group(1)
    catinput = cat.pattern_match.group(2)
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await cat.edit( "`Reply to supported Media...`")
        return
    catid = cat.reply_to_msg_id
    if catinput:
        if ";" in catinput:
            top, bottom = catinput.split(";", 1)
        else:
            top = catinput
            bottom = ""
    else:
        await cat.edit( "```what should i write on that u idiot give some text```"
        )
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await cat.edit( "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await cat.edit( "```Supported Media not found...```")
        return
    import base64

    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha memifying this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")

        meme_file = catfile
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha memifying this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found... `")
            return
        meme_file = catfile
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Mwahaha memifying this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found...```")
            return
        meme_file = catfile
    else:
        await cat.edit(
            "```Transfiguration Time! Mwahaha memifying this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker
    '''try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await cat.client(san)
    except BaseException:
        pass'''
    meme_file = convert_toimage(meme_file)
    meme = "catmeme.jpg"
    if max(len(top), len(bottom)) < 21:
        await cat_meme(CNG_FONTS, top, bottom, meme_file, meme)
    else:
        await cat_meeme(top, bottom, CNG_FONTS, meme_file, meme)
    if cmd != "mm3f":
        meme = await convert_tosticker(meme)
    await cat.client.send_file(cat.chat_id, meme, reply_to=catid)
    await cat.delete()
    os.remove(meme)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(pattern="cfont(?: |$)(.*)"))

async def lang(event):
    if event.fwd_from:
        return
    global CNG_FONTS
    input_str = event.pattern_match.group(1)
    if not input_str:
        await event.edit(f"**Available Fonts names are here:-**\n\n{FONTS}")
        return
    if input_str not in font_list:
        catevent = await event.edit( "`Give me a correct font name...`")
        await asyncio.sleep(1)
        await catevent.edit(f"**Available Fonts names are here:-**\n\n{font_list}")
    else:
        arg = f"userbot/helpers/styles/{input_str}"
        CNG_FONTS = arg
        await event.edit( f"**Fonts for Memify changed to :-** `{input_str}`")


@bot.on(admin_cmd(outgoing=True, pattern="asi ?(.*)"))

async def memes(cat):
    if cat.fwd_from:
        return
    catinput = cat.pattern_match.group(1)
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await cat.edit( "`Reply to supported Media...`")
        return
    catid =reply.id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await cat.edit( "`Downloading media......`")
    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await cat.edit( "```Supported Media not found...```")
        return
    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha converting to ascii image of this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")

        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha converting to ascii image of this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found... `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Mwahaha converting to ascii image of this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found...```")
            return
        meme_file = catfile
        jisanidea = True
    else:
        await cat.edit(
            "```Transfiguration Time! Mwahaha converting to asci image of this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker
    meme_file = convert_toimage(meme_file)
    outputfile = "ascii_file.webp" if jisanidea else "ascii_file.jpg"
    c_list = random_color()
    color1 = c_list[0]
    color2 = c_list[1]
    bgcolor = "#080808" if not catinput else catinput
    asciiart(meme_file, 0.3, 1.9, outputfile, color1, color2, bgcolor)
    await cat.client.send_file(cat.chat_id, outputfile, reply_to=catid)
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(pattern="envert$", outgoing=True))

async def memes(cat):
    if cat.fwd_from:
        return
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await cat.edit( "`Reply to supported Media...`")
        return
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await cat.edit( "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await cat.edit( "```Supported Media not found...```")
        return
    import base64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")

        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found... `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found...```")
            return
        meme_file = catfile
        jisanidea = True
    else:
        await cat.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker

    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if jisanidea else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await cat.client.send_file(
        cat.chat_id, outputfile, force_document=False, reply_to=catid
    )
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="solr$"))

async def memes(cat):
    if cat.fwd_from:
        return
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await cat.edit( "`Reply to supported Media...`")
        return
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await cat.edit( "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await cat.edit( "```Supported Media not found...```")
        return
    import base64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha solarizeing this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")
            
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha solarizeing this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found... `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Mwahaha solarizeing this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found...```")
            return
        meme_file = catfile
        jisanidea = True
    else:
        await cat.edit(
            "```Transfiguration Time! Mwahaha solarizeing this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if jisanidea else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await cat.client.send_file(
        cat.chat_id, outputfile, force_document=False, reply_to=catid
    )
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="mirror$"))

async def memes(cat):
    if cat.fwd_from:
        return
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await cat.edit( "`Reply to supported Media...`")
        return
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await cat.edit( "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await cat.edit( "```Supported Media not found...```")
        return
    import base64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")
            
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found... `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found...```")
            return
        meme_file = catfile
        jisanidea = True
    else:
        await cat.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker

    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if jisanidea else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await cat.client.send_file(
        cat.chat_id, outputfile, force_document=False, reply_to=catid
    )
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="flip$"))

async def memes(cat):
    if cat.fwd_from:
        return
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await cat.edit( "`Reply to supported Media...`")
        return
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await cat.edit( "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await cat.edit( "```Supported Media not found...```")
        return
    import base64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha fliping this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")
            
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha fliping this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found... `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Mwahaha fliping this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found...```")
            return
        meme_file = catfile
        jisanidea = True
    else:
        await cat.edit(
            "```Transfiguration Time! Mwahaha fliping this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker

    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if jisanidea else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await cat.client.send_file(
        cat.chat_id, outputfile, force_document=False, reply_to=catid
    )
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="gray$"))

async def memes(cat):
    if cat.fwd_from:
        return
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await cat.edit( "`Reply to supported Media...`")
        return
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await cat.edit( "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await cat.edit( "```Supported Media not found...```")
        return
    import base64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")
            
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found... `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found...```")
            return
        meme_file = catfile
        jisanidea = True
    else:
        await cat.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker

    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if jisanidea else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await cat.client.send_file(
        cat.chat_id, outputfile, force_document=False, reply_to=catid
    )
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))

async def memes(cat):
    if cat.fwd_from:
        return
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await cat.edit( "`Reply to supported Media...`")
        return
    catinput = cat.pattern_match.group(1)
    catinput = 50 if not catinput else int(catinput)
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await cat.edit( "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await cat.edit( "```Supported Media not found...```")
        return
    import base64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha zooming this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")

        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha zooming this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found... `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Mwahaha zooming this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found...```")
            return
        meme_file = catfile
    else:
        await cat.edit(
            "```Transfiguration Time! Mwahaha zooming this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker

    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if jisanidea else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, catinput)
    except Exception as e:
        return await cat.edit(f"`{e}`")
    try:
        await cat.client.send_file(
            cat.chat_id, outputfile, force_document=False, reply_to=catid
        )
    except Exception as e:
        return await cat.edit(f"`{e}`")
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))

async def memes(cat):
    if cat.fwd_from:
        return
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await cat.edit( "`Reply to supported Media...`")
        return
    catinput = cat.pattern_match.group(1)
    if not catinput:
        catinput = 50
    if ";" in str(catinput):
        catinput, colr = catinput.split(";", 1)
    else:
        colr = 0
    catinput = int(catinput)
    colr = int(colr)
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await cat.edit( "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await cat.edit( "```Supported Media not found...```")
        return
    import base64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha framing this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")

        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```Transfiguration Time! Mwahaha framing this sticker! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found... `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Transfiguration Time! Mwahaha framing this video! (」ﾟﾛﾟ)｣```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found...```")
            return
        meme_file = catfile
    else:
        await cat.edit(
            "```Transfiguration Time! Mwahaha framing this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = catsticker

    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if jisanidea else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, catinput, colr)
    except Exception as e:
        return await cat.edit(f"`{e}`")
    try:
        await cat.client.send_file(
            cat.chat_id, outputfile, force_document=False, reply_to=catid
        )
    except Exception as e:
        return await cat.edit(f"`{e}`")
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


CMD_HELP.update(
    {
        "memify0": "**Plugin : **`memify0`\
    \n\n  • **Syntax :** `.mm3f toptext ; bottomtext`\
    \n  • **Function : **Creates a image meme with give text at specific locations and sends\
    \n\n  • **Syntax : **`.mm3s toptext ; bottomtext`\
    \n  • **Function : **Creates a sticker meme with give text at specific locations and sends\
    \n\n  • **Syntax : **`.cfont` <Font Name>\
    \n  • **Function : **Change the font style use for memify,\nTo get fonts name use this cmd (`!term ls userbot/helpers/styles`)\
    \n\n  • **Syntax : **`.asci`\
    \n  • **Function : **reply to media file to get ascii image of that media\
    \n\n  • **Syntax : **`.envert`\
    \n  • **Function : **Inverts the colors in media file\
    \n\n  • **Syntax : **`.solr`\
    \n  • **Function : **Watch sun buring ur media file\
    \n\n  • **Syntax : **`.mirror`\
    \n  • **Function : **shows you the reflection of the media file\
    \n\n  • **Syntax : **`.flip`\
    \n  • **Function : **shows you the upside down image of the given media file\
    \n\n  • **Syntax : **`.gray`\
    \n  • **Function : **makes your media file to black and white\
    \n\n  • **Syntax : **`.zoom` or `.zoom range`\
    \n  • **Function : **zooms your media file\
    \n\n  • **Syntax : **`.frame` or `.frame range` or `.frame range ; fill`\
    \n  • **Function : **make a frame for your media file\
    \n  • **fill:** This defines the pixel fill value or color value to be applied. The default value is 0 which means the color is black.\
    "
    }
)
