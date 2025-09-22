# start.py
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from asyncio.tasks import create_task

from loader import dp, bot
from utils import texts, buttons
from services.services import getProduct, createUser, getUser
from state.state import UserState, CoffeState


async def _task(message: Message, state: FSMContext):
    user_id = message.from_user.id
    lang_text = message.text
    lang_codes = {
        buttons.LANGUAGES_UZ: 'uz',
        buttons.LANGUAGES_RU: 'ru',
        buttons.LANGUAGES_EN: 'en'
    }

    if not lang_text in lang_codes:
        """
        Agar user xato til kiritsa
        """
        await message.delete()
        return

    lang = lang_codes[lang_text]

    first_name = message.from_user.first_name
    resoult = createUser(user_id=user_id, first_name=first_name, lang=lang)
    
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['lang']

    product = getProduct(lang)
    
    await message.answer(
        texts.START[lang],
        reply_markup=buttons.get_product(product, lang)    
    )

    await CoffeState.coffe.set()

@dp.message_handler(content_types=['text'], state=UserState.lang)
async def lang_handler(message: Message, state: FSMContext):
    await create_task(_task(message, state))
