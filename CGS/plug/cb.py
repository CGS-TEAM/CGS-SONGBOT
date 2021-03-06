import os
from CGS.exe import exe
from pyrogram import Client
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from CGS import CGS as app

# Call backs @CGSUPDATES 

@app.on_callback_query()
async def cb_data(client, message):
    if message.data == "jsjsjp":
        await message.message.edit_text(
            text=exe.HELP_TEXT.format(message.from_user.mention),
            reply_markup=exe.btns,
            disable_web_page_preview=True,
        )
    elif message.data == "helpback":
        await message.message.edit_text(
            text=exe.START_TEXT.format(message.from_user.mention),
            reply_markup=exe.btn,
            disable_web_page_preview=True
        )
    elif message.data == "help":
        await message.message.edit_text(
            text=exe.HELP_TEXT.format(message.from_user.mention),
            reply_markup=exe.btns,
            disable_web_page_preview=True
        )
