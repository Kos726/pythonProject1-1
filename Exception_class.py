class ProZero(Exception):
    def __init__(self, message):
        self.message = message


class F:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.f_solve(a, b)

    def f_solve(self, a, b):
        if b == 0:
            raise ProZero('Ошибка')
        return print(a / b)


try:
    result = F(10, 5)
except ProZero as e:
    print(f'словили ошибку {e.message}')
