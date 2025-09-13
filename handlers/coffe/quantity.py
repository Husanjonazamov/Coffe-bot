# start.py
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from asyncio.tasks import create_task

from loader import dp, bot
from utils import texts, buttons
from services.services import getProduct, getProductDetail
from state.state import CoffeState
from handlers.start import start_handler
from .handler import _task as category_task

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
    print(message.text)
    if message.text == buttons.BACK_TEXT:
        data = await state.get_data()
        
        coffe = data.get("coffe")

        detail = getProductDetail(coffe)
        
        categories = detail["data"]["category"]
        category_text = texts.CATEGORY
        
        for cat in categories:
            category_text += f"- {cat['title']}\n"
        
        await message.answer(
            category_text,
            reply_markup=buttons.get_category(categories)
        )
        
        await CoffeState.category.set()
    else:
        await create_task(_task(message, state))
