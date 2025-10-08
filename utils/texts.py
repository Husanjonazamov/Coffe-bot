# texts.py
prompt_text = (
        "🇺🇿 Iltimos, tilni tanlang:\n"
        "🇷🇺 Пожалуйста, выберите язык:\n"
        "🇬🇧 Please select your language:"
    )
# Boshlang'ich xabarlar
START = {
    "uz": (
        "☕️ <b>Assalomu alaykum!</b>\n"
        "Qahva dunyosiga xush kelibsiz!\n\n"
        "Sevimli qahvangizni tanlang va buyurtma bering — "
        "biz siz uchun mehr bilan tayyorlaymiz."
    ),
    "ru": (
        "☕️ <b>Здравствуйте!</b>\n"
        "Добро пожаловать в мир кофе!\n\n"
        "Выберите свой любимый кофе и сделайте заказ — "
        "мы приготовим его с любовью для вас."
    ),
    "en": (
        "☕️ <b>Hello!</b>\n"
        "Welcome to the world of coffee!\n\n"
        "Choose your favorite coffee and place an order — "
        "we will prepare it with love for you."
    )
}

CATEGORY = {
    "uz": "<b>Iltimos, qahvangiz turini tanlang:</b>",
    "ru": "<b>Пожалуйста, выберите тип кофе:</b>",
    "en": "<b>Please select your coffee type:</b>"
}

ADMIN = {
    "uz": "✅ Xabar yuborildi",
    "ru": "✅ Сообщение отправлено",
    "en": "✅ Message sent"
}

PAYMENT = {
    "uz": "To‘lov turini tanlang:",
    "ru": "Выберите способ оплаты:",
    "en": "Select payment method:"
}

ADMIN_CONFIRM = {
    "uz": "Sizning buyurtmangiz qabul qilindi. Tez orada tayyor bo‘ladi! ✅",
    "ru": "Ваш заказ принят. Скоро будет готов! ✅",
    "en": "Your order has been accepted. It will be ready soon! ✅"
}

PAYMENT_INFO = {
    "uz": (
        "Iltimos, quyidagi karta raqamiga to‘lovni amalga oshiring:\n\n"
        "<b><code>8600 4929 8667 8353</code></b>\n\n"
        "Sirojiddin Haydarov\n\n"
        "💡 To‘lovni amalga oshirgandan so‘ng, iltimos, "
        "chekni yoki screenshotni rasm sifatida menga yuboring."
    ),
    "ru": (
        "Пожалуйста, совершите оплату на следующую карту:\n\n"
        "<b><code>8600 4929 8667 8353</code></b>\n\n"
        "Sirojiddin Haydarov\n\n"
        "💡 После оплаты, пожалуйста, отправьте мне чек или скриншот в виде изображения."
    ),
    "en": (
        "Please make the payment to the following card:\n\n"
        "<b><code>8600 4929 8667 8353</code></b>\n\n"
        "Sirojiddin Haydarov\n\n"
        "💡 After making the payment, please send me the receipt or screenshot as a photo."
    )
}




def product_detail(detail: dict, categories_text: str, lang: str = "uz") -> str:
    data = detail.get("data", {})
    
    # Title va description ni tilga moslash
    title = (
        data.get("title", {"uz": "Noma'lum"}).get(lang, "Noma'lum")
        if isinstance(data.get("title"), dict) else data.get("title", "Noma'lum")
    )
    description = (
        data.get("description", {"uz": "Izoh yo‘q"}).get(lang, "Izoh yo‘q")
        if isinstance(data.get("description"), dict) else data.get("description", "Izoh yo‘q")
    )
    price = data.get("price", "0")

    # F-string ichida to'g'ri chaqirish
    text = (
        f"☕ <b>{title}</b>\n\n"
        f"📂 <b>{ {'uz':'Turi','ru':'Категория','en':'Category'}[lang] }:</b> {categories_text}\n\n"
        f"📖 <b>{ {'uz':'Tavsif','ru':'Описание','en':'Description'}[lang] }:</b> {description}\n\n"
        f"💰 <b>{ {'uz':'Narxi','ru':'Цена','en':'Price'}[lang] }:</b> {price} so'm"
    )
    return text


# Buyurtma tugmasi matni
ORDER = {
    "uz": "🛒 Buyurtma berish uchun quyidagi tugmani bosing 👇",
    "ru": "🛒 Нажмите на кнопку ниже, чтобы сделать заказ 👇",
    "en": "🛒 Click the button below to place an order 👇"
}

NAME = {
    "uz": "👤 Iltimos, ismingizni kiriting:",
    "ru": "👤 Пожалуйста, введите ваше имя:",
    "en": "👤 Please enter your name:"
}

PHONE = {
    "uz": "📱 Iltimos, telefon raqamingizni yuboring:",
    "ru": "📱 Пожалуйста, отправьте свой номер телефона:",
    "en": "📱 Please send your phone number:"
}

COMMENT = {
    "uz": "✏️ Agar qo‘shimcha izoh bo‘lsa, yozing:",
    "ru": "✏️ Если есть дополнительные комментарии, напишите:",
    "en": "✏️ If you have additional comments, write:"
}

def confirm(lang="uz", **kwargs) -> str:
    """
    kwargs:
        coffe, category, quantity, name, phone, comment, payment
    returns:
        str: faqat tanlangan til uchun matn
    """
    labels = {
        "uz": {
            "category": "Kategoriya",
            "quantity": "Miqdor",
            "name": "Ism",
            "phone": "Telefon",
            "comment": "Izoh",
            "payment": "To‘lov",
        },
        "ru": {
            "category": "Категория",
            "quantity": "Количество",
            "name": "Имя",
            "phone": "Телефон",
            "comment": "Комментарий",
            "payment": "Оплата",
        },
        "en": {
            "category": "Category",
            "quantity": "Quantity",
            "name": "Name",
            "phone": "Phone",
            "comment": "Comment",
            "payment": "Payment",
        },
    }

    return (
        f"📝 Buyurtma ma'lumotlari:\n\n"
        f"☕ Coffee: {kwargs.get('coffe', '-')}\n"
        f"📂 {labels[lang]['category']}: {kwargs.get('category', '-')}\n"
        f"🔢 {labels[lang]['quantity']}: {kwargs.get('quantity', '-')}\n"
        f"👤 {labels[lang]['name']}: {kwargs.get('name', '-')}\n"
        f"📞 {labels[lang]['phone']}: {kwargs.get('phone', '-')}\n"
        f"💬 {labels[lang]['comment']}: {kwargs.get('comment', '-')}\n"
        f"💵 {labels[lang]['payment']}: {kwargs.get('payment', '-')}\n"
    )

