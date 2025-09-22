# comment.py
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from asyncio.tasks import create_task

from loader import dp, bot
from utils import texts, buttons
from services.services import getProductDetail, getUser
from state.state import CoffeState


async def _task(message: Message, state: FSMContext):
    user_text = message.text.strip()
    await state.update_data({"payment": user_text})

    data = await state.get_data()
    user_id=message.from_user.id
    user = getUser(user_id)
    lang = user['lang']

    detail = getProductDetail(data.get("coffe")) 
    print(detail)


    image_file_id = detail["data"]["image"]
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=image_file_id,
        caption=texts.confirm(
            coffe=data.get("coffe"),
            category=data.get("category"),
            quantity=data.get("quantity"),
            name=data.get("name"),
            phone=data.get("phone"),
            comment=data.get("comment"),
            payment=data.get("payment"),
            lang=lang
        ),
        reply_markup=buttons.confirm_keyboard(lang)
    )

    await CoffeState.confirm.set()


@dp.message_handler(content_types=['contact', 'text'], state=CoffeState.payment)
async def phone_handler(message: Message, state: FSMContext):
    user_id=message.from_user.id
    user = getUser(user_id)
    lang = user['lang']
    
    if message.text == buttons.BUTTON_TEXTS[lang]["back"]:
        await message.answer(
            texts.PHONE,
            reply_markup=buttons.PHONE
        )    
        
        await CoffeState.phone.set()
    else:
        await create_task(_task(message, state))
