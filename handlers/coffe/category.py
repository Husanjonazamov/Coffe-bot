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
    data = await state.get_data()
    coffe = data.get("coffe")
    detail = getProductDetail(coffe)
    
    
    await state.update_data({"category": user_text})
    
    image = detail["data"].get("image")


    if image:
        await message.answer_photo(
            photo=image,   
            caption=texts.product_detail(detail=detail, categories_text=user_text),
            reply_markup=buttons.quantity()
        )
        
    else:
        await message.answer(
            text=texts.product_detail(detail=detail, categories_text=user_text),
            reply_markup=buttons.quantity()
        )
  
    await CoffeState.quantity.set()


@dp.message_handler(content_types=['text'], state=CoffeState.category)
async def category_handler(message: Message, state: FSMContext):
    
    if message.text == buttons.BACK_TEXT:
        await start_handler(message, state)
    else:
        await create_task(_task(message, state))
