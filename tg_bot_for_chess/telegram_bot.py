import logging
import yaml
import aiohttp
# python tg_bot_for_chess/telegram_bot.py
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from aiogram.dispatcher import FSMContext

# Установка уровня логирования
logging.basicConfig(level=logging.INFO)


# Инициализация бота и диспетчера
bot = Bot(token='5343231561:AAGB0nKpggD61U7t83sNgW_a0baKCQk2Deo',parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


async def start():
    await dp.start_polling()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('<b>Добро пожаловать!</b>\n\nЯ бот, который готов помочь вам с нашей системой.'
                        ' Если вы хотите узнать больше о моих командах, введите <code>/help</code>.',
                        parse_mode=types.ParseMode.HTML)


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    help_text = "<b>Доступные команды:</b>\n\n"
    help_text += "<code>/post id</code> - показать определенную статью\n"
    help_text += "<code>/show</code> - показать все статьи\n"
    help_text += "<code>/help</code> - показать список доступных команд\n"
    await message.reply(help_text, parse_mode=types.ParseMode.HTML)


async def handle_error(message, error, count):
    if isinstance(error, IndexError):
        await message.answer("/command int from 0 to {}".format(count))
    elif isinstance(error, ValueError):
        await message.answer(f"Invalid id. Please provide a number from 0 to {count}")
    elif isinstance(error, aiohttp.client_exceptions.ClientResponseError) and error.status == 404:
        await message.answer("Article not found")
    else:
        await message.answer("Unknown error occurred")


@dp.message_handler(commands=['show'])
async def send_show(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8000/api/v1/Chess/') as resp:
            data = await resp.json()
            count = int(data['count'])
            for i in range(1, count + 1):
                url = f"http://127.0.0.1:8000/api/v1/Chess/{i}/"
                async with session.get(url) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        formatted_data = f"<b>ID:</b> <i>{data['id']}</i>\n<b>Title:</b><i> {data['title']}</i>\n<b>Content:</b> <i>{data['content']}</i>\n"
                        await message.reply(formatted_data, parse_mode=types.ParseMode.HTML)
                    else:
                        await message.answer(f"Ошибка {resp.status}")


@dp.message_handler(commands=['post'])
async def send_post(message: types.Message):
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
                    formatted_data = f"<b>ID:</b> <i>{data['id']}</i>\n<b>Title:</b><i> {data['title']}</i>\n<b>Content:</b> <i>{data['content']}</i>\n"
                    await message.reply(formatted_data, parse_mode=types.ParseMode.HTML)
                else:
                    await message.answer(f"Ошибка {resp.status}: {resp.text}")


@dp.message_handler(commands=['id'])
async def get_my_id(message: types.Message):
    user_id = message.from_user.id
    await message.answer(user_id)





from functools import wraps

def is_admin(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        message = args[0]  # message будет всегда первым аргументом
        with open('tg_bot_for_chess/ADMIN.YAML') as f:
            templates = yaml.safe_load(f)
        for i in range(len(templates)):
            if int(message.from_user.id) == int(templates[i]["id"]):
                return await func(*args, **kwargs)
        await message.answer("У вас недостаточно прав для выполнения этой команды")
    return wrapper

# Команда для вывода списка доступных команд админ-панели
@dp.message_handler(commands=['ahelp'])
@is_admin
async def admin_help(message: Message, state: FSMContext):
    help_text = ("<b>Список доступных команд:</b>\n\n"
                 "<code>/broadcast</code> - отправить сообщение всем пользователям бота\n"
                 "<code>/set_welcome</code> - установить приветственное сообщение для новых пользователей\n"
                 "<code>/set_admin</code> - добавить пользователя в администраторы\n"
                 
                 "<code>/cancel</code> - отменить текущее действие\n")

    await message.answer(help_text)










# Обработчик текстовых сообщений
@dp.message_handler()
async def echo_message(message: types.Message):

    await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
