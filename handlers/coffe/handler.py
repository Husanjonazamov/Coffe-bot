# start.py
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from asyncio.tasks import create_task

from loader import dp, bot
from utils import texts, buttons
from services.services import getProduct, getProductDetail, getUser
from state.state import CoffeState
from handlers.start import start_handler


async def _task(message: Message, state: FSMContext):
    
    user_text = message.text.strip()
    user_id=message.from_user.id
    user = getUser(user_id)
    lang = user['lang']
    

    detail = getProductDetail(user_text)
    if not detail or not detail.get("status"):
        await start_handler(message, state)
        return

    detail = getProductDetail(user_text)
    
    categories = detail["data"]["category"]
    category_text = texts.CATEGORY[lang]
    
    for cat in categories:
        category_text += f"- {cat['title']}\n"
    
    await message.answer(
        category_text,
        reply_markup=buttons.get_category(categories, lang)
    )
    
    await state.update_data({"coffe": user_text})
    
    
    await CoffeState.category.set()


@dp.message_handler(content_types=['text'], state=CoffeState.coffe)
async def coffe_handler(message: Message, state: FSMContext):
    await create_task(_task(message, state))
