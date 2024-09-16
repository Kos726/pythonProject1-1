first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x[0]) - len(x[1]) for x in zip(first, second) if not len(x[0]) == len(x[1]))

second_result = (len(first[x]) == len(second[x]) for x in list(range(len(second))))


print(list(first_result))
print(list(second_result))
