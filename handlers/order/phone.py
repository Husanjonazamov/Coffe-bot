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
    user_text = message.text
    user_id=message.from_user.id
    user = getUser(user_id)
    lang = user['lang']
    
    if user_text:
        phone = user_text
    else:
        phone = message.contact.phone_number
    
    await state.update_data({"phone": phone})
    
    
    await message.answer(
        texts.COMMENT[lang],
        reply_markup=buttons.back_keyboard(lang)
    )    
    
    await CoffeState.comment.set()

@dp.message_handler(content_types=['contact', 'text'], state=CoffeState.phone)
async def phone_handler(message: Message, state: FSMContext):
    user_id=message.from_user.id
    user = getUser(user_id)
    lang = user['lang']
    
    if message.text == buttons.BUTTON_TEXTS[lang]["back"]:
        await message.answer(
            texts.NAME,
            reply_markup=buttons.BACK
        )    
        
        await CoffeState.name.set()
    else:
        await create_task(_task(message, state))
