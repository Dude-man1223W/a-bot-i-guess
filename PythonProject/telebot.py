import asyncio
import logging
import sympy as sp

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

TOKEN = "8549122435:AAEIhcJUF9SSwRLGFnBgrBMA_gMDEa_usjQ"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Приветствую, я проекная работа в сфере телеграм технологий и обучения студентов. Я калькулятор 🤖\nНапиши выражение, например:\n2+2*3")


@dp.message()
async def calculate(message: Message):
    try:
        expression = message.text.replace(",", ".")
        result = sp.sympify(expression).evalf()
        await message.answer(f"Ответ: {result}")
    except Exception:
        await message.answer("Ошибка! Введите корректное математическое выражение.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())