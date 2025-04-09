from aiogram import Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from utils.texts import get_start_text

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="/register"), KeyboardButton(text="/balance")],
            [KeyboardButton(text="/catalog"), KeyboardButton(text="/cart")],
            [KeyboardButton(text="/topup"), KeyboardButton(text="/clearcart")]
        ],
        resize_keyboard=True
    )
    await message.answer(get_start_text(message.from_user.full_name), reply_markup=kb)
