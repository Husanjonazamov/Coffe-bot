# handlers/order/confirm.py
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from utils import texts
from state.state import CoffeState
from utils.env import ADMIN
from services.services import getProductDetail
from handlers.start import start_handler



@dp.message_handler(lambda msg: msg.text == "❌ Bekor qilish", state=CoffeState.confirm)
async def cencel_order(message: types.Message, state: FSMContext):

    await start_handler(message, state)

