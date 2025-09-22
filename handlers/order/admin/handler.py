# comment.py
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from asyncio.tasks import create_task
from services.services import getUser

from loader import dp, bot
from utils import texts, buttons



@dp.callback_query_handler(lambda c: c.data.startswith("confirm_"), state="*")
async def admin_task(call: CallbackQuery, state: FSMContext):
    user_id = int(call.data.split("_")[1])
    
    user = getUser(user_id)
    lang = user['lang']
    
    
    await call.answer(
        texts.ADMIN[lang]
    )
    
    await bot.send_message(
        chat_id=user_id,
        text=texts.ADMIN_CONFIRM[lang],
    )
    await call.message.edit_reply_markup(reply_markup=buttons.confirm_button)


    await state.finish()
    



