numbers_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []                                                     # пустое множество простых чисел
not_primes = []                                                 # пустое множество составных чисел
for i in range(int(len(numbers_))):                             # перебираем главный список (ГС)
    if int(numbers_[i]) != 1:                                   # исключаем единицу
        primes.append(numbers_[i])                              # добвляем элемент в список простых чисел
                                                # начинаем проверку элемента на "простоту"
        for j in range(0, int(len(primes))):                    # перебор элементов в списке простых чисел (ПЧ)
                                                # два условия "простоты" числа
            if (int(numbers_[i]) % int(primes[j]) == 0          # 1 услов: деление без остатка
                    and int(primes[j]) <= int(numbers_[i])-1):  # 2 услов: значен из списка ПЧ меньше чем значен ГС
                not_primes.append(numbers_[i])
                primes.remove(numbers_[i])
                break
print(f'Primes: {primes}')
print(f'Not primes: {not_primes}')
