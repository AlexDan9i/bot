import asyncio
import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import logging
import random

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаем объект бота
bot=Bot(token=config.token) 

# Диспетчер

dp = Dispatcher()

 # Хендлер на команду /start
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    print(message)
    await message.answer(f'Привет, {name}')

 # Асинхронная функция 
async def main():
    await dp.start_polling(bot)

 # Зацикливание для того что бы бот ждал коиманды 
if __name__ == '__main__':
    asyncio.run(main())

       


