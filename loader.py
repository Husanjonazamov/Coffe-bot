# loader.py fayli
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils.env import BOT_TOKEN
import logging


logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")

dp = Dispatcher(bot, storage=storage)