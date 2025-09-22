# start.py
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from asyncio.tasks import create_task

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser, getProductDetail
from state.state import CoffeState
from handlers.start import start_handler
from .handler import _task as category_task


async def _task(message: Message, state: FSMContext):
    user_id=message.from_user.id
    user = getUser(user_id)
    lang = user['lang']
    user_text = message.text.strip()
    
    
    await state.update_data({"quantity": user_text})

    await message.answer(
        texts.ORDER[lang],
        reply_markup=buttons.order_keyboard(lang)
        
    )    
    
    await CoffeState.order.set()
    

@dp.message_handler(content_types=['text'], state=CoffeState.quantity)
async def quantity_handler(message: Message, state: FSMContext):
    print(message.text)
    user_id=message.from_user.id
    user = getUser(user_id)
    lang = user['lang']
    
    if message.text == buttons.BUTTON_TEXTS[lang]["back"]:
        data = await state.get_data()
        
        coffe = data.get("coffe")

        detail = getProductDetail(coffe)
        
        categories = detail["data"]["category"]
        category_text = texts.CATEGORY[lang]
        print(categories)
        for cat in categories:
            category_text += f"- {cat['title']}\n"
        
        await message.answer(
            category_text,
            reply_markup=buttons.get_category(categories)
        )
        
        await CoffeState.category.set()
    else:
        await create_task(_task(message, state))
