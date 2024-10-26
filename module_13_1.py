from asyncio import run, sleep, create_task  # имортируем нужные функции


async def start_strongman(name, power):
	print(f'Силач {name} начал соревнования.')
	for approach in range(5):  # цикл подходов к подьему камней
		await sleep(1/power)
		print(f'Силач {name} поднял {approach + 1} шар')
	print(f'Силач {name} закончил соревнования')


# функцию соревнований зададим через генераторные списки				
async def start_tournament(list_participants_):
	print("Начало соревнований")
	task = [create_task(start_strongman(*participant)) for participant in list_participants_]
	[await task[i] for i in range(len(task))]		
	print("Соревнования окончены")
	
	
list_participants = [['Pasha', 3], ['Denis', 4], ['Apollon', 5]]  # т.к. участников много, зададим через список

run(start_tournament(list_participants))
