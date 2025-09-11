# start.py
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from asyncio.tasks import create_task

from loader import dp, bot
from utils import texts, buttons
from services.services import getProduct


async def _task(message: Message, state: FSMContext):
    """
    Botning asosiy /start handleri
    """
    
    product = getProduct()
    
    await message.answer(
        texts.START,
        reply_markup=buttons.get_product(product)    
    )

@dp.message_handler(commands=['start'], state="*")
async def start_handler(message: Message, state: FSMContext):
    await create_task(_task(message, state))