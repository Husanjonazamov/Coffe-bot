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
