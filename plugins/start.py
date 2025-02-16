#Coded by KA18 the @legend580 💛❤️

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os, time
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, CallbackQuery
from bot import Bot
from config import *
from Script import script

@Bot.on_message(filters.command('start') & filters.private)
async def start_command(client: Client, message: Message):

    id = message.from_user.id
    # if not db.is_user_exist(id):
    #     try:
    #       await db.add_user(id)
    #       await client.send_message(
    #       Config.LOG_CHANNEL,
    #          f"<b>#𝐍𝐞𝐰𝐔𝐬𝐞𝐫: \n\n᚛› 𝐈𝐃 - {message.from_user.id} \n᚛› 𝐍𝐚𝐦𝐞 - [{message.from_user.first_name}](tg://user?id={message.from_user.id})</b>"
    #       )
    #     except:
    #       pass    

    a = await message.reply_text("Processing....")
    time.sleep(2)
    await a.delete()
    await client.send_message(
        	chat_id=message.chat.id,
            text = script.START_MSG.format(message.from_user.mention if message.from_user else message.chat.title),
            disable_web_page_preview = True,
            reply_markup=script.START_BUTTONS)
