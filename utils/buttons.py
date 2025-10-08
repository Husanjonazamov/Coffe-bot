from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
BUTTON_TEXTS = {
    "uz": {
        "back": "⬅️ Orqaga",
        "order": "✅ Buyurtma berish",
        "phone": "📱 Telefon raqamni yuborish",
        "confirm": "✅ Tasdiqlash",
        "cancel": "❌ Bekor qilish",
        "card": "💳 Karta orqali",
        "cash": "💵 Naqd pul",
        "accepted": "✅ Qabul qilindi",
        "change_lang": "🌐 Tilni o‘zgartirish"   # 🔥 qo‘shildi
    },
    "ru": {
        "back": "⬅️ Назад",
        "order": "✅ Сделать заказ",
        "phone": "📱 Отправить номер телефона",
        "confirm": "✅ Подтвердить",
        "cancel": "❌ Отменить",
        "card": "💳 По карте",
        "cash": "💵 Наличные",
        "accepted": "✅ Принято",
        "change_lang": "🌐 Сменить язык"         # 🔥 qo‘shildi
    },
    "en": {
        "back": "⬅️ Back",
        "order": "✅ Place Order",
        "phone": "📱 Send phone number",
        "confirm": "✅ Confirm",
        "cancel": "❌ Cancel",
        "card": "💳 By card",
        "cash": "💵 Cash",
        "accepted": "✅ Accepted",
        "change_lang": "🌐 Change language"      # 🔥 qo‘shildi
    }
}

# Universal BACK tugmasi
def back_keyboard(lang="uz"):
    texts = BUTTON_TEXTS.get(lang, BUTTON_TEXTS["uz"])
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=texts["back"])]],
        resize_keyboard=True
    )
    return keyboard




def get_product(products, lang="uz"):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    change_lang_text = BUTTON_TEXTS.get(lang, BUTTON_TEXTS["uz"])["change_lang"]
    keyboard.add(KeyboardButton(text=change_lang_text))

    for product in products:
        if isinstance(product, dict):
            title = product.get("title") or "Noma'lum"
        else:
            title = str(product)
        keyboard.insert(KeyboardButton(text=title))

    back_text = BUTTON_TEXTS.get(lang, BUTTON_TEXTS["uz"])["back"]
    keyboard.add(KeyboardButton(text=back_text))

    return keyboard


# Kategoriyalar uchun
def get_category(categories, lang="uz"):
    texts = BUTTON_TEXTS.get(lang, BUTTON_TEXTS["uz"])
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = [KeyboardButton(text=f"☕ {cat['title']}") for cat in categories]
    keyboard.row(*buttons)
    keyboard.add(KeyboardButton(text=texts["back"]))
    return keyboard

# Miqdor tanlash
def quantity(lang="uz"):
    texts = BUTTON_TEXTS.get(lang, BUTTON_TEXTS["uz"])
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    buttons = [KeyboardButton(text=str(i)) for i in range(1, 10)]
    keyboard.add(*buttons)
    keyboard.add(KeyboardButton(text=texts["back"]))
    return keyboard

# Buyurtma berish
def order_keyboard(lang="uz"):
    texts = BUTTON_TEXTS.get(lang, BUTTON_TEXTS["uz"])
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton(text=texts["order"]))
    keyboard.add(KeyboardButton(text=texts["back"]))
    return keyboard

# Telefon raqam
def phone_keyboard(lang="uz"):
    texts = BUTTON_TEXTS.get(lang, BUTTON_TEXTS["uz"])
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton(text=texts["phone"], request_contact=True))
    keyboard.add(KeyboardButton(text=texts["back"]))
    return keyboard

# Tasdiqlash / bekor qilish
def confirm_keyboard(lang="uz"):
    texts = BUTTON_TEXTS.get(lang, BUTTON_TEXTS["uz"])
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
    keyboard.add(KeyboardButton(text=texts["confirm"]))
    keyboard.add(KeyboardButton(text=texts["cancel"]))
    return keyboard

def payment_type_keyboard(lang="uz"):
    texts = BUTTON_TEXTS.get(lang, BUTTON_TEXTS["uz"])
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        KeyboardButton(text=texts["card"]),
        KeyboardButton(text=texts["cash"]),
    )
    keyboard.add(KeyboardButton(text=texts["back"]))
    return keyboard

def confirm_admin(lang, user_id):
    texts = BUTTON_TEXTS.get(lang, BUTTON_TEXTS["uz"])
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text=texts["confirm"],
            callback_data=f"confirm_{user_id}"
        )
    )
    return keyboard

# Oddiy inline confirm button
def confirm_button(lang="uz"):
    texts = BUTTON_TEXTS.get(lang, BUTTON_TEXTS["uz"])
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=texts["accepted"], callback_data="accepted")]]
    )
    return keyboard


LANGUAGES_UZ = "🇺🇿 O'zbekcha"
LANGUAGES_RU = "🇷🇺 Русский"
LANGUAGES_EN = "🇺🇸 English"

LANGUAGES = ReplyKeyboardMarkup(
    keyboard=[
        [LANGUAGES_RU],
        [LANGUAGES_UZ],
        [LANGUAGES_EN],
    ],
    resize_keyboard=True,
)
