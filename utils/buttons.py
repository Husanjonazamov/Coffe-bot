from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Universal BACK tugmasi
BACK_TEXT = "⬅️ Orqaga"

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

    # Universal BACK tugmasi
    keyboard.add(KeyboardButton(text=BACK_TEXT))

    return keyboard



def quantity():
    keyboard = ReplyKeyboardMarkup(
        row_width=3,  
        resize_keyboard=True
    )

    buttons = [KeyboardButton(text=str(i)) for i in range(1, 10)]
    keyboard.add(*buttons)

    # Universal BACK tugmasi
    keyboard.add(KeyboardButton(text=BACK_TEXT))

    return keyboard



order = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✅ Buyurtma berish")],
        [KeyboardButton(text=BACK_TEXT)]
    ],
    resize_keyboard=True
)


BACK = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=BACK_TEXT)]
    ],
    resize_keyboard=True
)


PHONE = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 Telefon raqamni yuborish", request_contact=True)],
        [KeyboardButton(text=BACK_TEXT)]
    ],
    resize_keyboard=True
)


CONFIRM = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Tasdiqlash"),
        ],
        [
            KeyboardButton(text="❌ Bekor qilish"),
        ]
    ],
    resize_keyboard=True,   
    one_time_keyboard=True  
)
