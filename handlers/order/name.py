# start.py
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from asyncio.tasks import create_task

from loader import dp, bot
from utils import texts, buttons
from services.services import getProduct, getUser
from state.state import CoffeState
from handlers.start import start_handler


async def _task(message: Message, state: FSMContext):
    user_id=message.from_user.id
    user = getUser(user_id)
    lang = user['lang']
    user_text = message.text.strip()
    
    await state.update_data({"name": user_text})
    
    
    await message.answer(
        texts.PHONE[lang],
        reply_markup=buttons.phone_keyboard(lang)
    )    
    
    await CoffeState.phone.set()
    
    

@dp.message_handler(content_types=['text'], state=CoffeState.name)
async def name_handler(message: Message, state: FSMContext):
    user_id=message.from_user.id
    user = getUser(user_id)
    lang = user['lang']
    
    if message.text == buttons.BUTTON_TEXTS[lang]["back"]:
        user_text = message.text.strip()
        await state.update_data({"quantity": user_text})

        await message.answer(
            texts.order,
            reply_markup=buttons.order
        )    
        
        await CoffeState.order.set()
    else:
        await create_task(_task(message, state))
