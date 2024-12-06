# Вариант 1
calls = 0
def counts_calls_1():
    global calls                                    # задаем глобальную функцию
    calls += 1                                      # подсчет количества обращений

# Вариант 2
def counts_calls_2():
    counts_calls_2.counter += 1                     # используем оператор подсчета
counts_calls_2.counter = 0                          # стартовое значение подсчета

def string_info(string):
    counts_calls_1()                                # вызываем функцию подсчета обращений варианта 1
    counts_calls_2()                                # вызываем функцию подсчета обращений варианта 2
    string_len = len(string)                        # подсчет символов
    string_up = string.upper()                      # повышение регистра
    string_low = string.lower()                     # понижение регистра
    tuple_ = (string_len, string_up, string_low)    # сборка кортежа. Перечень эл. определен, указываем "как есть"
    return tuple_

def is_contains(string, list_to_search):
    counts_calls_1()                                # вызываем функцию подсчета обращений варианта 1
    counts_calls_2()                                # вызываем функцию подсчета обращений варианта 2
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
print(f' Ответ по варианту подсчета 1: {calls}')
print(f' Ответ по варианту подсчета 2: {counts_calls_2.counter}')

