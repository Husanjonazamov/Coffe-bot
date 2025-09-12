# handlers/order/confirm.py
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from utils import texts
from state.state import CoffeState
from utils.env import ADMIN
from services.services import getProductDetail



@dp.message_handler(lambda msg: msg.text == "✅ Tasdiqlash", state=CoffeState.confirm)
async def confirm_order(message: types.Message, state: FSMContext):
    data = await state.get_data()

    text = texts.confirm(**data)
    print(text)
    
    detail = getProductDetail(data.get("coffe")) 

    image_file_id = detail["data"]["image"]
    print(image_file_id)

    detail = data.get("detail")
    if image_file_id:
        await bot.send_photo(
            chat_id=ADMIN,
            photo=image_file_id,
            caption=f"📩 Yangi buyurtma keldi!\n\n{text}"
        )
    else:
        await bot.send_message(
            chat_id=ADMIN,
            text=f"📩 Yangi buyurtma keldi!\n\n{text}"
        )

    await message.answer("✅ Buyurtmangiz adminimizga yuborildi. Tez orada siz bilan bog'lanamiz!")

    await state.finish()
