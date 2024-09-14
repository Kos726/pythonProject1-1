class ProZero(Exception):
    def __init__(self, message):
        self.message = message
        #F.f_solve(self)


class F(ProZero):
#class F:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def f_solve(self):
        if self.b == 0:
            raise ProZero(message='Ошибка')
        return self.a / self.b


try:
    result = F(10, 5)
except ProZero as e:
    print(f'словили ошибку e.message_')
    print(f'словили ошибку {e.message}')
