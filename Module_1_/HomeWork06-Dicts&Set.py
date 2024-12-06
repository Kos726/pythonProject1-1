# Словарь
my_dict = {'Katia' : 1985, 'Masha': 1995, 'Sveta': 1987}
print(my_dict)
print(my_dict['Katia'])
sub_1 = 'Такого ключа нет' # собщение для случае отсутсвия ключа. в виде переменной чтоб хранить-изменять отдельно
print(my_dict.get('Tanya', sub_1)) # Тани нет, с выводом сообщения
my_dict.update({'Olga':1984,
                'Kira':1986})
a = my_dict.pop('Sveta')
print(a)
print(my_dict)

# Множество
my_set = {5,3,1,2,4,1,2,8,3,'Ау!',True,(726,621)}
print(my_set) #Булево значение True не выводится, вопрос преподавателю
my_set.update({'Кто здесь?', "O_o"})
my_set.discard(8)
print(my_set)

