from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
from services.catalog_service import load_catalog, get_product
from services.cart_service import add_to_cart
from services.user_service import get_user_balance

router = Router()

@router.message(Command("catalog"))
async def show_catalog(message: Message):
    catalog = load_catalog()
    for item in catalog:
        text = f"📺 <b>{item['brand']} {item['model']}</b>\n💰 <b>{item['price']} грн</b>"
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="➕ Додати в кошик", callback_data=f"add_{item['id']}")]
        ])
        await message.answer(text, reply_markup=kb)

@router.callback_query(lambda c: c.data and c.data.startswith("add_"))
async def handle_add_callback(callback: CallbackQuery):
    product_id = int(callback.data.replace("add_", ""))
    user_id = callback.from_user.id

    product = get_product(product_id)
    if not product:
        return await callback.answer("❌ Товар не знайдено", show_alert=True)

    balance = get_user_balance(user_id)
    if balance is None:
        return await callback.answer("⚠️ Спочатку зареєструйтесь: /register", show_alert=True)

    if balance < product["price"]:
        return await callback.answer(f"❌ Недостатньо коштів. Потрібно {product['price']} грн", show_alert=True)

    add_to_cart(user_id, product_id)
    await callback.answer("✅ Товар додано до кошика", show_alert=False)
