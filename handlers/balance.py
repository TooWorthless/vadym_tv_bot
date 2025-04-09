from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from services.user_service import get_user_balance

router = Router()

@router.message(Command("balance"))
async def show_balance(message: Message):
    balance = get_user_balance(message.from_user.id)

    if balance is None:
        await message.answer("⚠️ Ви ще не зареєстровані. Напишіть /register")
    else:
        await message.answer(f"💰 Ваш баланс: <b>{balance:.2f} грн</b>")
