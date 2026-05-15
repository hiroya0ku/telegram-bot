from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import asyncio

TOKEN = '8681119853:AAHhklnOOFlafsCT6rQ9mjbpG8_TGmFD-g8'
bot = Bot(token=TOKEN)
dp = Dispatcher()
@dp.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Привет я твой первый бот')

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('я умею отвечать на /start и /help')

async def main():
    await dp.start_polling(bot)
asyncio.run(main())