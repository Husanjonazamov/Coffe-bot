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
    await message.answer(
        texts.NAME,
        reply_markup=buttons.BACK
    )    
    
    await CoffeState.name.set()

@dp.message_handler(lambda msg: msg.text == "✅ Buyurtma berish", state=CoffeState.order)
async def order_handler(message: Message, state: FSMContext):
    await create_task(_task(message, state))
