from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from services.user_service import create_user

router = Router()

@router.message(Command("register"))
async def register_user(message: Message):
    create_user(message.from_user)
    await message.answer("✅ Ви успішно зареєстровані!")
