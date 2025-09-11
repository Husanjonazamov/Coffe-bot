# bot.py fayli
# bot.py fayli
# aiogram import
from aiogram import executor

# kode import
from loader import dp, bot
from utils.env import ADMIN

import handlers

async def on_startup(dp):
    """
    botni asosiy ishga tushiradigan file
    """
    
    await bot.send_message(ADMIN, "bot ishga tushdi /start")
    
executor.start_polling(dp, on_startup=on_startup, skip_updates=True)