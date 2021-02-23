import os
#MADE BY SHIVAM DONT KANG
import cv2
from ub import CMD_HELP
#MADE BY SHIVAM DONT KANG
#MADE BY SHIVAM DONT KANG
from telegraph import upload_file
from telethon.tl.types import MessageMediaPhoto
from ub.utils import admin_cmd
from ub import bot 
from ub import bot as borg
import os , shutil
sedpath = "./s_h_i_v_a_m/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)
@borg.on(admin_cmd(pattern=r"tpic"))
async def hmm(event):

    await event.delete()
    sed = await event.get_reply_message()
    linc = event.text
    links=linc[6:]
    text,colors,thicknes,orgs,fontsize=links.split("|")
    a,b,c=colors.split(";")
    c,d=orgs.split(";")

    img = await borg.download_media(sed.media, sedpath)
    miraculous=cv2.VideoCapture(img)
    ladybug,catnoar = miraculous.read()
    cv2.imwrite("shivammememe.png", catnoar)
    img = "shivammememe.png"
    window_name = 'Made By Shivam'
    image = cv2.imread(img) 
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (int(c),int(d))
    color = (int(a),int(b),int(c))
    thickness=int(thicknes)
    fontScale=int(fontsize)
    image = cv2.putText(image, text, org, font, fontScale,  
                 color, thickness, cv2.LINE_AA, False)
    image = cv2.putText(image, text, org, font, fontScale, 
                  color, thickness, cv2.LINE_AA, True)
    #image=cv2.imshow(window_name, image)
    cv2.imwrite("s_h_i_v_a_m.jpg", image)
    #await borg.send_file(event.chat_id,"s_h_i_v_a_m.png")
    #await event.client.send_file(event.chat_id, "s_h_i_v_a_m.png", force_document=True, reply_to=event.reply_to_msg_id)
    await event.client.send_file(event.chat_id, "s_h_i_v_a_m.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    shutil.rmtree(sedpath)
    os.remove("s_h_i_v_a_m.jpg")
@borg.on(admin_cmd(pattern=r"ipic"))
async def hmm(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    await event.delete()
    sed = await event.get_reply_message()
    linc = event.text
    links=linc[6:]
    text,colors,thicknes,orgs,fontsize=links.split("|")
    a,b,c=colors.split(";")
    c,d=orgs.split(";")
    img = await borg.download_media(sed.media, sedpath)
    miraculous=cv2.VideoCapture(img)
    ladybug,catnoar = miraculous.read()
    cv2.imwrite("shivammememe.png", catnoar)
    img = "shivammememe.png"
    window_name = 'Made By Shivam'
    image = cv2.imread(img) 
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (int(c),int(d))
    color = (int(a),int(b),int(c))
    thickness=int(thicknes)
    fontScale=int(fontsize)
    image = cv2.putText(image, text, org, font, fontScale,  
                 color, thickness, cv2.LINE_AA)
    #image=cv2.imshow(window_name, image)
    cv2.imwrite("s_h_i_v_a_m.jpg", image)
    #await borg.send_file(event.chat_id,"s_h_i_v_a_m.png")
    #await event.client.send_file(event.chat_id, "s_h_i_v_a_m.png", force_document=True, reply_to=event.reply_to_msg_id)
    await event.client.send_file(event.chat_id, "s_h_i_v_a_m.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    shutil.rmtree(sedpath)
    os.remove("s_h_i_v_a_m.jpg")
CMD_HELP.update({
    "CustomMemefy":"\n\n.tpic text|no1;no2;no3|thickness|coordinate x;coordinate y|fontsize\
    \n\n.ipic text|no1;no2;no3|thickness|coordinate x;coordinate y|fontsize"})
#MADE BY SHIVAM DONT KANG#MADE BY SHIVAM DONT KANG#MADE BY SHIVAM DONT KANG#MADE BY SHIVAM DONT KANG#MADE BY SHIVAM DONT KANG
