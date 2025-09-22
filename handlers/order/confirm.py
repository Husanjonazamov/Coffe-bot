# handlers/order/confirm.py
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from utils import texts
from state.state import CoffeState
from utils.env import CHANNEL
from services.services import getProductDetail, getUser
from handlers.start import start_handler
from utils import buttons



@dp.message_handler(content_types=['text'], state=CoffeState.confirm)
async def confirm_order(message: types.Message, state: FSMContext):
    
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['lang']
    user_id = message.from_user.id
    data = await state.get_data()

    text = texts.confirm(**data)
    
    payment_type = data.get("payment", "cash")  
    detail = getProductDetail(data.get("coffe")) 
    image_file_id = detail["data"]["image"]
    
    
    print(buttons.BUTTON_TEXTS[lang]['confirm'])
    if payment_type == buttons.BUTTON_TEXTS[lang]['card']:
        await message.answer(
            texts.PAYMENT_INFO[lang]
        )
        await CoffeState.check.set()
    elif message.text == buttons.BUTTON_TEXTS[lang]['confirm']:
        detail = data.get("detail")
        if image_file_id:
            await bot.send_photo(
                chat_id=CHANNEL,
                photo=image_file_id,
                caption=f"📩 Yangi buyurtma keldi!\n\n{text}",
                reply_markup=buttons.confirm_admin(lang, user_id)
            )
        else:
            await bot.send_message(
                chat_id=CHANNEL,
                text=f"📩 Yangi buyurtma keldi!\n\n{text}"
            )
            
        await state.finish()
        await start_handler(message, state)

