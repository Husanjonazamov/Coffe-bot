# comment.py
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from asyncio.tasks import create_task

from loader import dp, bot
from utils import texts, buttons
from services.services import getProductDetail
from state.state import CoffeState


async def _task(message: Message, state: FSMContext):
    user_text = message.text.strip()
    await state.update_data({"comment": user_text})

    data = await state.get_data()

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
        ),
        reply_markup=buttons.CONFIRM
    )

    await CoffeState.confirm.set()


@dp.message_handler(content_types=['contact', 'text'], state=CoffeState.comment)
async def phone_handler(message: Message, state: FSMContext):
    await create_task(_task(message, state))
