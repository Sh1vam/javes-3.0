#ported from catub 
#by Sh1vam
import asyncio
import os
import subprocess
import time
from datetime import datetime
from pathlib import Path
from shutil import copyfile 
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pymediainfo import MediaInfo
import lottie
from ub import bot
from ub.utils import admin_cmd
from telethon.tl.types import DocumentAttributeVideo
import asyncio
import functools
import difflib
import shlex
from typing import Tuple
from ub import bot
from ub.utils import admin_cmd
from ub.helpers import progress
PATH = os.path.join("./temp", "temp_vid.mp4")
thumb_image_path = Config.TMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"
def run_sync(func, *args, **kwargs):
    return asyncio.get_event_loop().run_in_executor(
        None, functools.partial(func, *args, **kwargs)
    )
async def catlst_of_files(path):
    files = []
    for dirname, dirnames, filenames in os.walk(path):
        # print path to all filenames.
        for filename in filenames:
            files.append(os.path.join(dirname, filename))
    return files


def get_video_thumb(file, output=None, width=320):
    output = file + ".jpg"
    metadata = extractMetadata(createParser(file))
    p = subprocess.Popen(
        [
            "ffmpeg",
            "-i",
            file,
            "-ss",
            str(
                int((0, metadata.get("duration").seconds)[metadata.has("duration")] / 2)
            ),
            # '-filter:v', 'scale={}:-1'.format(width),
            "-vframes",
            "1",
            output,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    p.communicate()
    if not p.returncode and os.path.lexists(file):
        return output


def sortthings(contents, path):
    catsort = []
    contents.sort()
    for file in contents:
        catpath = os.path.join(path, file)
        if os.path.isfile(catpath):
            catsort.append(file)
    for file in contents:
        catpath = os.path.join(path, file)
        if os.path.isdir(catpath):
            catsort.append(file)
    return catsort
async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )
async def thumb_from_audio(audio_path, output):
    await runcmd(f"ffmpeg -i {audio_path} -filter:v scale=500:500 -an {output}")
async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id
async def make_gif(event, reply, quality=None, fps=None):
    fps = fps or 1
    quality = quality or 256
    result_p = os.path.join("temp", "animation.gif")
    animation = lottie.parsers.tgs.parse_tgs(reply)
    with open(result_p, "wb") as result:
        await run_sync(lottie.exporters.gif.export_gif, animation, result, quality, fps)
    return result_p
@bot.on(admin_cmd(pattern="roundv ?(.*)", outgoing=True))

async def video_catfile(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    if input_str:
        path = Path(input_str)
        if not os.path.exists(path):
            await event.edit(
                f"`there is no such directory/file with the name {path} to upload`",
            )
            return
        catevent = await event.edit( "`Converting to video note..........`")
        filename = os.path.basename(path)
        catfile = os.path.join("./temp", filename)
        copyfile(path, catfile)
    else:
        if not reply:
            await event.edit( "`Reply to supported media`")
            return
        if not (reply and (reply.media)):
            await event.edit( "`Reply to supported Media...`")
            return
        catevent = await event.edit( "`Converting to video note..........`")
        catfile = await reply.download_media(file="./temp/")
    if not catfile.endswith((".mp4", ".tgs", ".mp3", ".mov", ".gif", ".opus")):
        os.remove(catfile)
        await event.edit( "```Supported Media not found...```")
        return
    if catfile.endswith((".mp4", ".tgs", ".mov", ".gif")):
        if catfile.endswith((".tgs")):
            hmm = await make_gif(catevent, catfile)
            if hmm.endswith(("@tgstogifbot")):
                os.remove(catfile)
                return await catevent.edit(hmm)
            os.rename(hmm, "./temp/circle.mp4")
            catfile = "./temp/circle.mp4"
        media_info = MediaInfo.parse(catfile)
        '''media_info = cv2.VideoCapture(catfile)
        height = media_info.get(cv2.CAP_PROP_FRAME_HEIGHT)
        width = media_info.get(cv2.CAP_PROP_FRAME_WIDTH)'''


        aspect_ratio = 1
        #aspect_ratio = width/height
        for track in media_info.tracks:
            if track.track_type == "Video":
                aspect_ratio = track.display_aspect_ratio
                height = track.height
                width = track.width
        if aspect_ratio != 1:
            crop_by = width if (height > width) else height
            await runcmd(f'ffmpeg -i {catfile} -vf "crop={crop_by}:{crop_by}" {PATH}')
        else:
            copyfile(catfile, PATH)
        if str(catfile) != str(PATH):
            os.remove(catfile)
    else:
        thumb_loc = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")
        catthumb = None
        try:
            catthumb = await reply.download_media(thumb=-1)
        except:
            catthumb = os.path.join("./temp", "thumb.jpg")
            await thumb_from_audio(catfile, catthumb)
        if catthumb is None:
            catthumb = os.path.join("./temp", "thumb.jpg")
            copyfile(thumb_loc, catthumb)
        if (
            catthumb is not None
            and not os.path.exists(catthumb)
            and os.path.exists(thumb_loc)
        ):
            catthumb = os.path.join("./temp", "thumb.jpg")
            copyfile(thumb_loc, catthumb)
        if catthumb is not None and os.path.exists(catthumb):
            await runcmd(
                f"ffmpeg -loop 1 -i {catthumb} -i {catfile} -c:v libx264 -tune stillimage -c:a aac -b:a 192k -vf \"scale='iw-mod (iw,2)':'ih-mod(ih,2)',format=yuv420p\" -shortest -movflags +faststart {PATH}"
            )
            os.remove(catfile)
        else:
            os.remove(catfile)
            return await catevent.edit( "`No thumb found to make it video note`",)
    if os.path.exists(PATH):
        catid = event.reply_to_msg_id
        c_time = time.time()
        await event.client.send_file(
            event.chat_id,
            PATH,
            allow_cache=False,
            reply_to=catid,
            video_note=True,
            attributes=[
                DocumentAttributeVideo(
                    duration=60,
                    w=1,
                    h=1,
                    round_message=True,
                    supports_streaming=True,
                )
            ],
          )

        os.remove(PATH)
    await catevent.delete()
#made by shivam bottom code
@bot.on(admin_cmd(pattern=r"space"))
async def space(e):
    await e.edit("ㅤ")
@bot.on(admin_cmd(pattern=r"blank"))
async def blank(e):
    await e.edit("­")



