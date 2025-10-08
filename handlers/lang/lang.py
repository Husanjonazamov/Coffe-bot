# start.py
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from asyncio.tasks import create_task

from loader import dp, bot
from utils import texts, buttons
from services.services import getProduct, patchUser, getUser
from state.state import LangUpdate, CoffeState
from handlers.start import start_handler


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

    resoult = patchUser(tg_id=user_id,lang=lang)

    await start_handler(message, state)

@dp.message_handler(content_types=['text'], state=LangUpdate.lang)
async def lang_handler(message: Message, state: FSMContext):
    await create_task(_task(message, state))
