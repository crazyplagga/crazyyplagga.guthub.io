import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    MenuButtonWebApp,
    Message,
    WebAppInfo,
)

TOKEN = os.environ.get("BOT_TOKEN")  # токен от @BotFather
WEBAPP_URL = os.environ.get("WEBAPP_URL")  # публичный https-адрес webapp/index.html

if not TOKEN:
    raise RuntimeError("Не задан BOT_TOKEN. Запусти бота через 2_start_bot.command и введи токен от BotFather.")
if not WEBAPP_URL or not WEBAPP_URL.startswith("https://"):
    raise RuntimeError("WEBAPP_URL должен быть публичным HTTPS-адресом, например https://....trycloudflare.com")

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text="🍭 Играть", web_app=WebAppInfo(url=WEBAPP_URL))
        ]]
    )
    await message.answer(
        "Secret Drops: слот на игровые монеты.\n"
        "Собирай 8+ одинаковых сладостей, лови множители и фриспины.",
        reply_markup=kb,
    )


async def main():
    # кнопка «Играть» рядом с полем ввода
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(text="Играть", web_app=WebAppInfo(url=WEBAPP_URL))
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
