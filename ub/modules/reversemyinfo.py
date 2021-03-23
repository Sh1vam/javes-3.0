from ub.events import javes05
from ub import bot
from telethon.tl.types import User
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl import functions
l=[]
@javes05(pattern="^\!savemyinfo", outgoing=True)
async def fetch_info(event):

    shivam=await bot.get_entity('me')
    ruser=await event.client(GetFullUserRequest(shivam.id))
    
    first_name = ruser.user.first_name
    
    if first_name == None:
        first_name=" "
        l.append(first_name)
    else :
        first_name=first_name
        l.append(first_name)
        
    last_name = ruser.user.last_name
    
    if last_name== None:
        last_name=" "
        l.append(last_name)
    else :
        last_name=last_name
        l.append(last_name)
        
    user_bio = ruser.about

    if user_bio == None:
        user_bio=" "
        l.append(user_bio)
    else:
        user_bio=user_bio
        l.append(user_bio)
    await event.edit("Saved Info For !mereverse command used to reverse after cloning")
   
@javes05(pattern="^\!mereverse", outgoing=True)
async def reverse(event):
    await bot(functions.account.UpdateProfileRequest(
        first_name=l[0]
    ))
    await bot(functions.account.UpdateProfileRequest(
        last_name=l[1]
    ))
    await bot(functions.account.UpdateProfileRequest(
        about=l[2]
    ))
    await event.edit("Done Delete pfp using !delpfp 1 if u want to delete it")
