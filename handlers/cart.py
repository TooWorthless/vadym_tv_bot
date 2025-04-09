from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from services.cart_service import get_cart, clear_cart, calculate_total
from services.user_service import get_user_balance, update_user_balance

router = Router()

@router.message(Command("cart"))
async def view_cart(message: Message):
    items = get_cart(message.from_user.id)
    if not items:
        return await message.answer("🧺 Ваш кошик порожній.")
    
    text = "🧺 <b>Ваш кошик:</b>\n"
    for item in items:
        p = item["product"]
        q = item["quantity"]
        text += f"- {p['brand']} {p['model']} x{q} = <b>{p['price'] * q} грн</b>\n"
    total = calculate_total(items)
    text += f"\n💰 Всього: <b>{total} грн</b>\n\nНапиши /checkout щоб оформити замовлення."
    await message.answer(text)

@router.message(Command("clearcart"))
async def clear_cart_cmd(message: Message):
    clear_cart(message.from_user.id)
    await message.answer("🧹 Кошик очищено.")

@router.message(Command("checkout"))
async def checkout_cmd(message: Message):
    user_id = message.from_user.id
    items = get_cart(user_id)
    if not items:
        return await message.answer("🧺 Ваш кошик порожній.")
    
    total = calculate_total(items)
    balance = get_user_balance(user_id)

    if balance is None:
        return await message.answer("⚠️ Спочатку зареєструйтеся: /register")

    if balance < total:
        return await message.answer(f"❌ Недостатньо коштів. Вам потрібно <b>{total - balance:.2f} грн</b>.\nПоповніть баланс: /topup")
    
    update_user_balance(user_id, -total)
    clear_cart(user_id)
    await message.answer(f"✅ Замовлення успішно оформлено!\n💸 З вас списано <b>{total} грн</b>.")
