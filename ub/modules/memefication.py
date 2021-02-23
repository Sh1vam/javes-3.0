from ub import bot 
from ub import bot as borg
global Miraaculousladybug
from ub.utils import admin_cmd
from PIL import Image, ImageDraw, ImageFont
import os
from ub import CMD_HELP
sedpath = "./s_h_i_v_a_m_j_a_v_e_s_3/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)
import cv2
@borg.on(admin_cmd(pattern=r"pictext"))
async def hmm(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    await event.delete()
    sed = await event.get_reply_message()
    linc = event.text
    links=linc[9:]
    text, font,size,color,align= links.split('|')
    x,y=align.split(";")
    img = await borg.download_media(sed.media, sedpath)
    miraculous=cv2.VideoCapture(img)
    ladybug,catnoar = miraculous.read()
    cv2.imwrite("shivammememe.png", catnoar)
    img = "shivammememe.png"
    size=int(size)
    img = Image.open(img)
    fonts = ImageFont.truetype(r"ub/helpers/styles/{}".format(font),size)
    draw = ImageDraw.Draw(img)
    draw.text(((int(x), int(y))), text,fill=(color),font=fonts )
    img.save('catnoiar.png')
    await borg.send_file(event.chat_id, 'catnoiar.png')
    shutil.rmtree(sedpath)
    os.remove("shivammememe.png")
    os.remove("catnoiar.png")
