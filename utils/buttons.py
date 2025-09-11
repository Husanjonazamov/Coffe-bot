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


def get_category(categories):
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True
    )

    buttons = []
    for cat in categories:
        buttons.append(KeyboardButton(text=f"☕ {cat['title']}"))

    keyboard.row(*buttons)

    keyboard.add(KeyboardButton(text="⬅️ Orqaga"))

    return keyboard



def quantity():
    keyboard = ReplyKeyboardMarkup(
        row_width=3,  
        resize_keyboard=True
    )

    buttons = [KeyboardButton(text=str(i)) for i in range(1, 10)]
    keyboard.add(*buttons)

    keyboard.add(KeyboardButton(text="⬅️ Orqaga"))

    return keyboard