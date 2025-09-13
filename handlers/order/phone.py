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
    user_text = message.text
    
    if user_text:
        phone = user_text
    else:
        phone = message.contact.phone_number
    
    await state.update_data({"phone": phone})
    
    
    await message.answer(
        texts.COMMENT,
        reply_markup=buttons.BACK
    )    
    
    await CoffeState.comment.set()

@dp.message_handler(content_types=['contact', 'text'], state=CoffeState.phone)
async def phone_handler(message: Message, state: FSMContext):
    if message.text == buttons.BACK_TEXT:
        await message.answer(
            texts.NAME,
            reply_markup=buttons.BACK
        )    
        
        await CoffeState.name.set()
    else:
        await create_task(_task(message, state))
