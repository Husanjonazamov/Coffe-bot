# start.py
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from asyncio.tasks import create_task

from loader import dp, bot
from utils import texts, buttons


async def _task(message: Message, state: FSMContext):
    """
    Botning asosiy /start handleri
    """
    
    await message.answer()

@dp.message_handler(commands=['start'], state="*")
async def start_handler(message: Message, state: FSMContext):
    await create_task(_task(message, state))