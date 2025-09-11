# start.py fayli
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from asyncio.tasks import create_task



async def _task(message: Message, state: FSMContext):
    """
     botni assosiy /start file
    """
    print("dd")
    await message.answer(
        message.photo[-1].file_id
    )    
    
    
@dp.message_handler(content_types=['photo'], state="*")
async def start_handler(message: Message, state: FSMContext):
    await create_task(_task(message, state))