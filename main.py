from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from environs import Env
from parser import get_random_quote

env = Env()
env.read_env()

BOT_TOKEN: str = env('BOT_TOKEN')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer(
        text='Это бот с рандомными цитатами. Напишите /quote, чтобы получить случайную цитату',
    )


@dp.message(Command(commands=['quote']))
async def process_quote_command(message: Message):
    await message.answer(
        text=get_random_quote(),
    )


if __name__ == '__main__':
    dp.run_polling(bot)
