# start.py
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from asyncio.tasks import create_task

from loader import dp, bot
from utils import texts, buttons
from services.services import getProduct, createUser, getUser
from state.state import CoffeState, UserState


async def _task(message: Message, state: FSMContext):
    """
    Botning asosiy /start handleri
    """
    user_id = message.from_user.id
    user = getUser(user_id)
    print(user)
    if user and user.get("status") is False:
        await message.answer(
            texts.prompt_text,
            reply_markup=buttons.LANGUAGES
        )
        await UserState.lang.set()
    else:
       
        user_id = message.from_user.id
        user = getUser(user_id)
        lang = user['lang']

        product = getProduct(lang)
        print(product)
        await message.answer(
            texts.START[lang],
            reply_markup=buttons.get_product(product, lang)    
        )

        await CoffeState.coffe.set()


@dp.message_handler(commands=['start'], state="*")
async def start_handler(message: Message, state: FSMContext):
    await create_task(_task(message, state))