def is_prime(func):
	def wrapper(*args):
		if func(*args) % 2 != 0:
			print(f'Простое')
			return func(*args)
		else:
			print(f'Составное')
			return func(*args)
	return wrapper


@is_prime	
def sum_three(*args): # решил сделать универсальную запись, нежели для трех значений (a, b, c)
	return sum(args)

		
result = sum_three(2, 3, 6)
print(result)
	