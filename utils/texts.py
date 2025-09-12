START = \
"""
☕️ <b>Assalomu alaykum!</b>  
Qahva dunyosiga xush kelibsiz!  

Sevimli qahvangizni tanlang va buyurtma bering — biz siz uchun mehr bilan tayyorlaymiz.  
"""


CATEGORY = \
"""
<b>Iltimos, qahvangiz turini tanlang:</b>
"""



def product_detail(detail: dict, categories_text) -> str:

    data = detail["data"]

    title = data.get("title", "Noma'lum")
    description = data.get("description", "Izoh yo‘q")
    price = data.get("price", "0")


    text = (
        f"☕ <b>{title}</b>\n\n"
        f"📂 <b>Turi:</b> {categories_text}\n\n"
        f"📖 <b>Tavsif:</b> {description}\n\n"
        f"💰 <b>Narxi:</b> {price} so'm"
    )

    return text


order = "🛒 Buyurtma berish uchun quyidagi tugmani bosing 👇"



NAME = "👤 Iltimos, ismingizni kiriting:"
PHONE = "📱 Iltimos, telefon raqamingizni yuboring:"
COMMENT = "✏️ Agar qo‘shimcha izoh bo‘lsa, yozing:"



def confirm(**kwargs) -> str:
    return (
        "📝 Buyurtma ma'lumotlari:\n\n"
        f"☕ Coffee: {kwargs.get('coffe', '-')}\n"
        f"📂 Kategoriya: {kwargs.get('category', '-')}\n"
        f"🔢 Miqdor: {kwargs.get('quantity', '-')}\n"
        f"👤 Ism: {kwargs.get('name', '-')}\n"
        f"📞 Telefon: {kwargs.get('phone', '-')}\n"
        f"💬 Izoh: {kwargs.get('comment', '-')}\n"
    )