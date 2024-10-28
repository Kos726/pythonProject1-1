from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

API_TOKEN_ = "..."

bot_ = Bot(token=API_TOKEN_)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(CommandStart())  # базовая функция команды старта
async def start_message(message: types.Message):
	print("Приветствие")
	await message.answer('Рады Вас видеть в нашем тестовом боте. '
						 'Бот может реагировать на команду /info, '
						 'отвечать на текст ff и Urban в любом регистре, '
						 'повторять сообщения пользователя')  # обычное сообщение


@dp.message(Command('info'))  # программируемая функция
async def info_message(message: types.Message):
	print("Info message")
	await message.answer('Это тестовый бот')  # обычное сообщение


@dp.message(F.text.lower().in_({"Urban", "ff"}))  # применяем фильтр по тексту с понижением регистра
async def urban_message(message: types.Message):
	print("Urban message")
	await message.reply(f'Мы получили сообщение {message.text}')  # сообщение в ответ


@dp.message()
async def all_message(message: types.Message):  # обработка любых сообщений их же возвратом
	print('эхо сообщение')
	await message.answer(message.text)


async def main():
	await bot_.delete_webhook(drop_pending_updates=True)  # аналог skip_updates=True версии aiogram 2
	await dp.start_polling(bot_)  # skip_updates=True используется выше

if __name__ == '__main__':
	asyncio.run(main())
