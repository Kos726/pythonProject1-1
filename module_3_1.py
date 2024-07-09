calls = 0

# В задании написано создать отдельную функцию counts_calls.
# Зачем она нужна я так и не разобрался.
# Потомучто счетчик работает и без нее - см. ответ по Варианту 1. Или я чего-то не понимаю.
# Однако, я сделал также вариант и с ней - см. ответ по Варинату 2.
# Но чтоб отделить глобальную переменную варианта 1 от варианта 2,
# ввожу новую "локальную" переменную calls_, и считаю по ней отдельно.

def counts_calls():
    global calls                                    # импортируем глобальную функцию
    calls_ = 0                                      # новая переменная для подсчета обращений варианта 2
    calls_ = calls_ + calls                         # подсчет количества обращений
    return calls_

def string_info(string):
    global calls                                    # импортируем глобальную функцию
    calls += 1                                      # прибавляем к calls единицу при работе функции
    string_len = len(string)                        # подсчет символов
    string_up = string.upper()                      # повышение регистра
    string_low = string.lower()                     # понижение регистра
    tuple_ = (string_len, string_up, string_low)    # сборка кортежа. Перечень эл. определен, указываем "как есть"
    return tuple_

def is_contains(string, list_to_search):
    global calls                                    # импортируем глобальную переменную
    calls += 1                                      # прибавляем к calls единицу при работе функции
    string = string.lower()                         # приводим к нижнему регистру строку в string
    i = 0                                           # начальное условие для количества элементов в list_to_search
    list_ = []                                      # создаем пустой список
    for i in range(len(list_to_search)):            # цикл для понижения регистра каждого эл. списка list_to_search
        list_i_low = list_to_search[i].lower()      # понижение регистра i-го элемента списка
        list_.append(list_i_low)                    # набор нового списка с элементами в нижнем регистре
    sub_ = string in list_                          # анализ наличия string в списке list_to_search
    return sub_

print()                                             # для отступа строки
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(f' Вариант 1 : {calls}')                                  # вывод варианта 1
print(f' Вариант 2 : {counts_calls()}')                         # вывод варианта 2
