def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# вывод значений ппраметров, заданных по умолчанию
print_params()

# обычное присвоение знасенич именованному параметру
print_params(b = 25)
print_params(c = [1,2,3])

# появление новых списка и словаря с тремя параметрами, как в базовой функции
value_list = [7, 'string', False]
value_dikt = {'a': 8, 'b': 'int', 'c': 'True_'}

#распаковка списка и словоря для переприсвоения значений у параметров
print_params(*value_list)
print_params(**value_dikt)

# появление нового списка, имеющего только два параметра
values_list_2 = ['t', [4, 5]]

# исходная функция имеет три параметра, а лист 2 только два, изменения будут по порядку
print_params(*values_list_2)
print_params('@', *values_list_2)
print_params(*values_list_2, '@')

# проверка согласно заданию
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
