# кортеж - неизменяемый набор
immutable_var = 726, True, 'create', ['tuple_', 'lol']
print(immutable_var)
# immutable_var[0] = 627  # невозможная команда, т.к. кортеж содержит неизменяемые объекты
# за исключеним случая, когда элементом кортежа выступает список, внутри которого можно производить изменения:
immutable_var[3][0] = 'lists'
print(immutable_var)

# список - изменяемый набор
mutable_var = [627, False, 'add']
print(mutable_var)
mutable_var[0] = 726
mutable_var[1] = True
mutable_var.extend(['21:40'])
print(mutable_var)
