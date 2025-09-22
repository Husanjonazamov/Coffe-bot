# comment.py
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from asyncio.tasks import create_task

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser
from state.state import CoffeState


async def _task(message: Message, state: FSMContext):
    user_text = message.text.strip()
    await state.update_data({"comment": user_text})
    user_id=message.from_user.id
    user = getUser(user_id)
    lang = user['lang']
    
    
    await message.answer(
        texts.PAYMENT[lang],
        reply_markup=buttons.payment_type_keyboard(lang)
    )

    await CoffeState.payment.set()
    


@dp.message_handler(content_types=['contact', 'text'], state=CoffeState.comment)
async def phone_handler(message: Message, state: FSMContext):
    user_id=message.from_user.id
    user = getUser(user_id)
    lang = user['lang']
    
    if message.text == buttons.BUTTON_TEXTS[lang]["back"]:
        await message.answer(
            texts.PHONE,
            reply_markup=buttons.PHONE
        )    
        
        await CoffeState.phone.set()
    else:
        await create_task(_task(message, state))
