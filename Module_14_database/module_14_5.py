from aiogram import Bot, Dispatcher, F  # Router
from aiogram.filters import CommandStart  # Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import FSInputFile
import asyncio
from crud_functions import *

API_TOKEN_ = "7944026758:AAFNyNXL3XXwK30MR8M8Kc7bg5cFmZd-o2k"

bot_ = Bot(token=API_TOKEN_)
dp = Dispatcher(storage=MemoryStorage())


# создание списка продуктов
# list_products_name = ['Наполеон', 'Шоколадный фондан', 'Медовик', 'Красный бархат']
# list_products_pictures = ['napoleon.png', 'shokoladniy_fondan.png', 'medovik.png', 'krasniy_barkhat.png']
# list_products_description = ['Кремово-Утончающий (735 кКал)', 'Шоколадно-Питающий (673 кКал)',
#                             'Медовый-Оздоровляющий (524 кКал)', 'Бисквитно-Успокаивающий (459 кКал)']

total_products = get_all_products(False)
list_products_name = [get_all_products(i, True)[0] for i in range(get_all_products(False))]
list_products_description = [get_all_products(i, True)[1] for i in range(get_all_products(False))]
list_products_price = [get_all_products(i, True)[2] for i in range(get_all_products(False))]
list_products_pictures = [get_all_products(i, True)[3] for i in range(get_all_products(False))]

print(total_products)
print(list_products_name)
print(list_products_description)
print(list_products_price)
print(list_products_pictures)


# настройка основного меню
button_solve = KeyboardButton(text="Рассчитать")
button_info = KeyboardButton(text="Информация")
button_buy = KeyboardButton(text="Купить")
button_registration = KeyboardButton(text="Регистрация")
list_button = [
    [button_solve, button_info], [button_buy], [button_registration]
]
kb = ReplyKeyboardMarkup(keyboard=list_button, resize_keyboard=True)

# настройка инлайн меню по расчету калорий
button_inline_calculation_calories = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calories')
button_inline_formulas_show = InlineKeyboardButton(text="Формулы расчёта", callback_data='formulas')
list_inline_buttons_calories = [
    [button_inline_calculation_calories],
    [button_inline_formulas_show]
]
kb_inline_calculation_calories = InlineKeyboardMarkup(inline_keyboard=list_inline_buttons_calories, row_width=2)


# меню выбора продуктов для покупки
"""
@dp.message(Command("inline"))
async def cmd_inline_buying(message: Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
"""
button_select_product_1 = InlineKeyboardButton(text=list_products_name[0], callback_data='product_buying_1')
button_select_product_2 = InlineKeyboardButton(text=list_products_name[1], callback_data='product_buying_2')
button_select_product_3 = InlineKeyboardButton(text=list_products_name[2], callback_data='product_buying_3')
button_select_product_4 = InlineKeyboardButton(text=list_products_name[3], callback_data='product_buying_4')

list_inline_buttons_buying = [
    [button_select_product_1, button_select_product_2], [button_select_product_3, button_select_product_4]
]

inline_keyboard_select_products = InlineKeyboardMarkup(inline_keyboard=list_inline_buttons_buying)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()


@dp.message(CommandStart())  # запрограммированная функция команды старта
async def start_message(message: Message):
    print("Приветствие")
    await message.answer('Добро пожаловать! '
                         'В этом боте вы можете ознакомиться, выбрать и преобретси продукты, '
                         'которые помогут сохранить стройность Вашей фигуры, '
                         'остроту ума и энергию в теле! '
                         '\n Для подбора подходящего Вам продукта, '
                         'Вы можете использовать встроеный калькулятор калорий.',
                         reply_markup=kb)


@dp.message(F.text.lower().in_({"рассчитать", "расчет"}))  # применяем фильтр по тексту с понижением регистра
async def main_menu(message: Message):
    print("Выбор опции расчета")
    await message.answer(f'Выберите опцию', reply_markup=kb_inline_calculation_calories)


@dp.callback_query(F.data == 'calories')
async def set_age(call: CallbackQuery, state: FSMContext):
    print("Запрос возраста")
    await call.message.answer(f'Введите свой возраст')  # сообщение в ответ
    print("ожидаем ввод - возраст")
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.update_data()
    await message.answer(f'Введите свой рост')  # сообщение в ответ
    print("ожидаем ввод - рост")
    await state.set_state(UserState.growth)


@dp.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await state.update_data()
    await message.answer(f'Введите свой вес')  # сообщение в ответ
    print("ожидаем ввод - вес")
    await state.set_state(UserState.weight)


@dp.message(UserState.weight)
async def set_gender(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    await state.update_data()
    await message.answer(f'укажите свой пол (муж, мужской, жен, женский)')
    print("ожидаем ввод - пол")
    await state.set_state(UserState.gender)

"""
Формула Миффлина-Сан Жеора
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
async def get_formulas(call: CallbackQuery):
    await call.message.answer(
        f'Сокращенная формула Миффлина-Сан Жеора для подсчета рекомендуемого количества калорий:'
        f'\n для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5'
        f'\n для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161'
        )  # сообщение в ответ
    print("ввод формул")


@dp.message(F.text.lower().in_({"купить", "покупка"}))  # применяем фильтр по тексту с понижением регистра
async def get_buying_list(message: Message):
    print("Выбор продукта")
    for i in range(len(list_products_name)):
        subject = (f'\nНазвание: {list_products_name[i]} | Цена: {list_products_price[i]}'
                   f'\nОписание: {list_products_description[i]}')
        # print(subject)
        await message.answer(subject)
        file_path = './Pictures/' + list_products_pictures[i]
        # print(file_path)
        await message.answer_photo(photo=FSInputFile(file_path))
    await message.answer(text="Выберете продукт для покупки", reply_markup=inline_keyboard_select_products)


@dp.callback_query(F.data.startswith('product_buying'))
async def send_confirm_message(call: CallbackQuery):
    code = call.data[-1]
    print(code, list_products_name[int(code) - 1])
    await call.message.answer(text=f'Вы приобрели продукт: '
                                   f'{list_products_name[int(code) - 1]}')  # сообщение в ответ
    print("Успешная покупка")


async def main():
    await bot_.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot_)


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000


@dp.message(F.text.lower().in_({"регистрация", "registration"}))
async def sing_up(message: Message, state: FSMContext):
    print("Запрос имени")
    initiate_db()
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await state.set_state(RegistrationState.username)


@dp.message(RegistrationState.username)
async def set_username(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
    if is_included(username=message.text) is True:
        await message.answer(f'Пользователь {message.text} существует, введите другое имя')
        await state.set_state(RegistrationState.username)
        print('Пользователь существует')
    else:
        date = await state.update_data()
        await message.answer(f'Введите email')  # сообщение в ответ
        print("ожидаем ввод - email")
        await state.set_state(RegistrationState.email)


@dp.message(RegistrationState.email)
async def set_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    date = await state.update_data()
    await message.answer(f'Введите свой возраст')  # сообщение в ответ
    print("ожидаем ввод - возраст")
    await state.set_state(RegistrationState.age)


@dp.message(RegistrationState.age)
async def set_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    date = await state.update_data()
    add_users(date["username"], date["email"], date["age"])
    await message.answer(f'Пользователь {date["username"]} зарегистрирован')
    print("Конец регистрации. Данные пользователя внесены в базу")
    await state.clear()

if __name__ == '__main__':
    asyncio.run(main())
