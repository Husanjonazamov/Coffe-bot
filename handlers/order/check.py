# handlers/order/confirm.py
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from utils import texts
from state.state import CoffeState
from utils.env import CHANNEL
from services.services import getProductDetail
from handlers.start import start_handler
from utils import buttons


@dp.message_handler(content_types=['photo'], state=CoffeState.check)
async def check_order(message: types.Message, state: FSMContext):
    
    lang = 'uz'
    user_id = message.from_user.id
    data = await state.get_data()

    text = texts.confirm(**data)
    check = message.photo[-1].file_id
    await state.update_data({"check": check})
    detail = getProductDetail(data.get("coffe")) 
    image_file_id = detail["data"]["image"]
    detail = data.get("detail")
    
    
    if image_file_id:
        await bot.send_photo(
            chat_id=CHANNEL,
            photo=image_file_id,
            caption=f"📩 Yangi buyurtma keldi!\n\n{text}",
            reply_markup=buttons.confirm_admin(lang, user_id)
        )
        await bot.send_photo(
            chat_id=CHANNEL,
            photo=check
        )

    else:
        await bot.send_message(
            chat_id=CHANNEL,
            text=f"📩 Yangi buyurtma keldi!\n\n{text}"
        )

    await start_handler(message, state)

    await state.finish()
