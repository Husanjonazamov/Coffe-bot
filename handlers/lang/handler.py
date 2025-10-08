from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils import buttons, texts
from state.state import LangUpdate


@dp.message_handler(lambda m: m.text in [
    buttons.BUTTON_TEXTS["uz"]["change_lang"],
    buttons.BUTTON_TEXTS["ru"]["change_lang"],
    buttons.BUTTON_TEXTS["en"]["change_lang"]
], state="*")

async def change_language(message: types.Message, state: FSMContext):
    await message.answer(
        texts.prompt_text,  
        reply_markup=buttons.LANGUAGES
    )
    await LangUpdate.lang.set()
