print("\n________этап 1_______")
print(int.__mro__)
print(object)

class User:
    def __init__(self):
        print('Я в ините')

user1 = User()
print(User.__mro__)

print("\n________этап 2_______")
class User2:
    def __new__(cls, *args, **kwargs):
        print("Я в new")
    def __init__(self):
        print('Я в ините')

user2 = User2()
print(User2.__mro__)
print(user1)
print(user2)

print("\n________этап 3_______")
class User3:
    def __new__(cls, *args, **kwargs):
        print("Я в new")
        return super().__new__(cls)
    def __init__(self):
        print('Я в ините')

user3_1 = User3()
user3_2 = User3()
print(User3.__mro__)
print(user3_1)
print(user3_2)
print(user3_1 is user3_2)
print(id(user3_1), id(user3_2)) # две записи занимат разные места в памяти

print("\n________этап 4_______")
class User4:
    __instance = None
    def __new__(cls, *args, **kwargs):
        print("Я в new")
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self):
        print('Я в ините')

user4_1 = User4()
user4_2 = User4()
print(User4.__mro__)
print(user4_1)
print(user4_2)
print(user4_1 is user4_2)
print(id(user4_1), id(user4_2)) # две записи занимат ОДНО место в памяти

print("\n________этап 5_______")
class User5:
    __instance = None
    def __new__(cls, *args, **kwargs):
        print("Я в new")
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self, *args, **kwargs):
        print('Я в ините')
        self.args = args
        self.kwargs = kwargs

other = [1, 2, 3]
user5_1 = {'name': 'Kos', 'age': 40}
user5_2 = {'name': 'Kat', 'age': 40}
user_5_1 = User5(other, user5_1)
print(user_5_1.args)
print(user_5_1.kwargs)
user_5_2 = User5(other, user5_2, name = 'Katia')
print(user_5_2.args)
print(user_5_2.kwargs)

print("\n________этап 6_______")
class User6:
    __instance = None
    def __new__(cls, *args, **kwargs):
        print("Я в new")
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self, *args, **kwargs):
        print('Я в ините')
        self.args = args
        #self.kwargs = kwargs
        self.name = kwargs.get('name')
        self.age = kwargs.get('age')

other = [1, 2, 3]
user6_1 = {'name': 'Kos', 'age': 40}
user6_2 = {'name': 'Kat', 'age': 40}
user_6_1 = User6(*other, **user6_1)
print(user_6_1.args)
#print(user_6_1.kwargs)
print(user_6_1.name)
print(user_6_1.age)
user_6_2 = User6(*other, **user6_2)
print(user_6_2.args)
#print(user_6_2.kwargs)
print(user_6_2.name)
print(user_6_2.age)

print("\n________этап 7_______")
class User7:
    __instance = None
    def __new__(cls, *args, **kwargs):
        print("Я в new")
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self, *args, **kwargs):
        print('Я в ините')
        self.args = args
        for key, values in kwargs.items():
            setattr(self, key, values)

other = [1, 2, 3]
user7_1 = {'name': 'Kos', 'age': 40, 'gender': 'male'}
user7_2 = {'name': 'Kat', 'age': 40, 'gender': 'female'}
user_7_1 = User7(*other, **user7_1)
print(user_7_1.args)
print(user_7_1.name)
print(user_7_1.age)
print(user_7_1.gender)
user_7_2 = User7(*other, **user7_2)
print(user_7_2.args)
print(user_7_2.name)
print(user_7_2.age)
print(user_7_2.gender)

