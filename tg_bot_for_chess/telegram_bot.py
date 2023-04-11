import logging
import requests
import aiohttp
#python tg_bot_for_chess/telegram_bot.py
from aiogram import Bot, Dispatcher, executor, types,__version__

# Установка уровня логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token='5343231561:AAGB0nKpggD61U7t83sNgW_a0baKCQk2Deo')
dp = Dispatcher(bot)

async def start():
    await dp.start_polling()

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    hel=str(__version__)
    print(__version__)
    await message.reply("Привет! Я бот sdfasdfsfsdfasdffdsfsadfTelegram."+hel)

async def handle_error(message, error, count):
    if isinstance(error, IndexError):
        await message.answer("/command int from 0 to {}".format(count))
    elif isinstance(error, ValueError):
        await message.answer(f"Invalid id. Please provide a number from 0 to {count}")
    elif isinstance(error, aiohttp.client_exceptions.ClientResponseError) and error.status == 404:
        await message.answer("Article not found")
    else:
        await message.answer("Unknown error occurred")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8000/api/v1/Chess/') as resp:
            data = await resp.json()
            count = int(data['count'])
            try:
                symbol = int(message.text.split()[1])
                if symbol < 0 or symbol >= count:
                    raise ValueError
            except (IndexError, ValueError, aiohttp.client_exceptions.ClientResponseError) as e:
                await handle_error(message, e, count)
                return
            url = f"http://127.0.0.1:8000/api/v1/Chess/{symbol}/"
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    await message.reply(data)
                else:
                    await message.answer(f"Ошибка {resp.status}: {resp.text}")


# Обработчик текстовых сообщений
@dp.message_handler()
async def echo_message(message: types.Message):

    await message.reply(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
