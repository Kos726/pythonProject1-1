class Example:
    houses_history = []
    def __new__(cls, *args, **kwargs):
      cls.houses_history = args
      print("1", args)
      print(kwargs)
      return object.__new__(cls)
    def __init__(self, first, second, third):
      print(first)
      print(second)
      print(third)

    def add_sub(self):
        pass



ex1 = Example('data 1', second=25, third=3.14)
ex2 = Example('data 2', second=25, third=3.14)