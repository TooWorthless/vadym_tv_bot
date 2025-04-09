from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from utils.texts import get_start_text

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(get_start_text(message.from_user.first_name))
