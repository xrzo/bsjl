import asyncio
import os
import re

from pyrogram import Client, filters
from pyrogram.types import (
    InputMediaPhoto,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
)

rid = Client(
    "Bot",
    api_id = 19653519,
 api_hash = "186c3adb292c12bdf180ff27952e6ee1",
 bot_token = "5153042842:AAEp9ricBqrPdgZ1JdxRdOFtqaBkHpL13Vw"
)

@rid.on_message(filters.command(".", [".", ""]) & filters.user(1759470911))
async def owner(client, message):
        user_id = " ".join(message.command[1:])
        text = message.reply_to_message.text
        await rid.send_message(user_id, text)
        await message.reply_text("تم ارسال رسالتك ذالك للشخص . ")
        
@rid.on_message(filters.command("start") & filters.private)
async def start(client, message):
       OWNER = 1759470911
       own = await client.get_chat(1759470911)
       name = own.first_name
       await rid.send_message(message.chat.id, f"**- مرحبًا بك في روبوت الاتصالات الخاص بــ ( [{name}](tg://user?id={OWNER}) )**\n**- أرسل رسالتك وسوف نقوم بالرد في أقرب وقت ممكن**\n**- شكرا لك على استخدام هذا الروبوت **.",
       reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                        "my official account .",
                        url=f'https://t.me/XRZOC'),
                        ],[
                            InlineKeyboardButton(
                        "Store Ricklss .",
                        url=f'https://t.me/JJCDT'),
                        ],
                    ]
                )
            ) 
       await rid.send_message(1759470911, f"**- شخص ما قام بتسجيل الدخول إلى الروبوت الخاص بك .**\n\n**- الاسم الشخص ( {message.from_user.mention} ) .**\n**- ايدي الشخص الدخل الروبوت** : `{message.from_user.id}` .")
       

@rid.on_message(filters.text & filters.private)
async def tawasol(client, message):
       OWNER = [1759470911]
       if message.from_user.id in OWNER:
         return
       await rid.send_message(1759470911, f"**- Message from ( {message.from_user.mention} ) .**\n**- user Account : ( @{message.from_user.username} )**\n**- ID User :** ( `{message.from_user.id}` )\n\n**- message : {message.text}**\n\n**To reply to the person, just send your message and reply to your message with the command ( . @user Account or id User ) .**")       
             



#RID @XTZOC , 
print("تم التشغيل البيانات بنجاح")
print("Data playback completed successfully, Go to the bot and press / start")
rid.run()
