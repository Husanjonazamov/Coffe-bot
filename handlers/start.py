# start.py
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from asyncio.tasks import create_task

from loader import dp, bot
from utils import texts, buttons
from services.services import getProduct, createUser
from state.state import CoffeState


async def _task(message: Message, state: FSMContext):
    """
    Botning asosiy /start handleri
    """
    result = createUser(message.from_user.id, message.from_user.first_name)

    product = getProduct()
    
    await message.answer(
        texts.START,
        reply_markup=buttons.get_product(product)    
    )

    await CoffeState.coffe.set()

@dp.message_handler(commands=['start'], state="*")
async def start_handler(message: Message, state: FSMContext):
    await create_task(_task(message, state))