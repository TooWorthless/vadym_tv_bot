from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import os

API_TOKEN = os.getenv("BOT_TOKEN", "token")

BOT_PROPERTIES = DefaultBotProperties(parse_mode=ParseMode.HTML)
