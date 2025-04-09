from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from payments.liqpay_mock import MockLiqPay
from services.user_service import update_user_balance

router = Router()

@router.message(Command("topup"))
async def topup_menu(message: Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="50 грн"), KeyboardButton(text="100 грн")],
            [KeyboardButton(text="200 грн"), KeyboardButton(text="❌ Скасувати")]
        ],
        resize_keyboard=True
    )
    await message.answer("💸 Виберіть суму для поповнення:", reply_markup=kb)

@router.message(F.text.in_(["50 грн", "100 грн", "200 грн"]))
async def process_payment(message: Message):
    amount = int(message.text.replace(" грн", ""))
    payment_url = MockLiqPay.create_payment(message.from_user.id, amount)

    await message.answer(f"🔗 Ось ваше мокове посилання для оплати:\n{payment_url}")
    await message.answer("⏳ Обробка платежу...")

    status = MockLiqPay.check_payment_status()

    if status == "success":
        update_user_balance(message.from_user.id, amount)
        await message.answer(
            f"✅ Платіж на <b>{amount} грн</b> успішно завершено!",
            reply_markup=ReplyKeyboardRemove()
        )
    else:
        await message.answer(
            "❌ Платіж не пройшов. Спробуйте ще раз.",
            reply_markup=ReplyKeyboardRemove()
        )

@router.message(F.text == "❌ Скасувати")
async def cancel_topup(message: Message):
    await message.answer("❌ Поповнення скасовано.", reply_markup=ReplyKeyboardRemove())
