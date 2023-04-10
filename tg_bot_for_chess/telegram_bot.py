import logging


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



@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    hel=str(__version__)
    print(__version__)
    await message.reply("sdfsdfsdsd       "+hel)

# Обработчик текстовых сообщений
@dp.message_handler()
async def echo_message(message: types.Message):

    await message.reply(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
