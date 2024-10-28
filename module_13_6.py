from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

API_TOKEN_ = "..."

bot_ = Bot(token=API_TOKEN_)
dp = Dispatcher(storage=MemoryStorage())

button_solve = KeyboardButton(text="Рассчитать")
button_info = KeyboardButton(text="Информация")
list_button = [
    [button_solve, button_info]
]
kb = ReplyKeyboardMarkup(keyboard=list_button, resize_keyboard=True)

button_inline_result = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calories')
button_inline_formulas_show = InlineKeyboardButton(text="Формулы расчёта", callback_data='formulas')
list_inline_buttons = [
    [button_inline_result],
    [button_inline_formulas_show]
]
kb_inline = InlineKeyboardMarkup(inline_keyboard=list_inline_buttons, row_width=2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()


@dp.message(CommandStart())  # запрограммированная функция команды старта
async def start_message(message: Message):
    print("Приветствие")
    await message.answer('Рады Вас видеть в нашем тестовом боте', reply_markup=kb)


@dp.message(F.text.lower().in_({"рассчитать", "расчет"}))  # применяем фильтр по тексту с понижением регистра
async def main_menu(message: Message):
    print("Выбор опции")
    await message.answer(f'Выберите опцию', reply_markup=kb_inline)


@dp.callback_query(F.data == 'calories')
async def set_age(call: CallbackQuery, state: FSMContext):
    print("Запрос возраста")
    await call.message.answer(f'Введите свой возраст')  # сообщение в ответ
    print("ожидаем ввод - возраст")
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    date = await state.update_data()
    await message.answer(f'Введите свой рост')  # сообщение в ответ
    print("ожидаем ввод - рост")
    await state.set_state(UserState.growth)


@dp.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    date = await state.update_data()
    await message.answer(f'Введите свой вес')  # сообщение в ответ
    print("ожидаем ввод - вес")
    await state.set_state(UserState.weight)


@dp.message(UserState.weight)
async def set_gender(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    date = await state.update_data()
    await message.answer(f'укажите свой пол (муж, мужской, жен, женский)')
    print("ожидаем ввод - пол")
    await state.set_state(UserState.gender)

"""
для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5
для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161
"""


@dp.message(UserState.gender)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(gender=message.text.lower())  # понижаем регистр перед сохранением
    date = await state.update_data()
    print('введенные значения:', date['gender'], date['age'], date['growth'], date['weight'])
    if date["gender"] == "муж" or date["gender"] == "мужской":
        print('калории для муж')
        result_male = 10 * int(date["weight"]) + 6.25 * int(date["growth"]) - 5 * int(date["age"]) + 5
        await message.answer(f'Рекомендуемая норма калорий: {result_male}')
    elif date['gender'] == "жeн" or date['gender'] == "женский":
        print('калории для жен')
        result_femail = 10 * int(date["weight"]) + 6.25 * int(date["growth"]) - 5 * int(date["age"]) - 161
        await message.answer(f'Рекомендуемая норма калорий: {result_femail}')
    await state.clear()  # вместо finish aiogram v.2


@dp.callback_query(F.data == "formulas")
async def get_formulas(call: CallbackQuery, state: FSMContext):
    await call.message.answer(
        f'Сокращенная формула Миффлина-Сан Жеора для подсчета рекомендуемого количества калорий:'
        f'\n для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5'
        f'\n для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161'
        )  # сообщение в ответ
    print("ввод формул")



async def main():
    await bot_.delete_webhook(drop_pending_updates=True)  # аналог skip_updates=True версии aiogram 2
    await dp.start_polling(bot_)  # skip_updates=True используется выше


if __name__ == '__main__':
    asyncio.run(main())
