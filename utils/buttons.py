# buttons.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_product(products):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    for product in products:
        if isinstance(product, dict):   
            title = product.get("title", "Noma'lum")
        else:                           
            title = str(product)

        keyboard.insert(KeyboardButton(title))

    return keyboard
