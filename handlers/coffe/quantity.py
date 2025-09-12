# start.py
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from asyncio.tasks import create_task

from loader import dp, bot
from utils import texts, buttons
from services.services import getProduct, getProductDetail
from state.state import CoffeState
from handlers.start import start_handler


async def _task(message: Message, state: FSMContext):
    
    user_text = message.text.strip()
    
    
    await state.update_data({"quantity": user_text})

    await message.answer(
        texts.order,
        reply_markup=buttons.order
    )    
    
    await CoffeState.order.set()
    

@dp.message_handler(content_types=['text'], state=CoffeState.quantity)
async def quantity_handler(message: Message, state: FSMContext):
    await create_task(_task(message, state))
