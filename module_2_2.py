first=float(input('Введите любое первое число: ')) # float для ввода целых и дробных чисел
print(f"{'Отлично!':>40}")
second=float(input('Введите любое второе число: '))
print(f"{'Замечательно!':>40}")
third=float(input('Введите любое третье число: '))
print(f"{'Incredeble!':>40}")
if first == second and second == third:
    print(3, 'Да, это три, почему именно эта цифра, даже не спрашивайте!')
elif first == second or first == third or second == third:
    print(2, 'Да, два. Нет это не оценка, это просто значение...')
else:
    print(0, 'Ноль, он и в Африке ноль. Почему именно тут ноль? Почем я знаю!!!')