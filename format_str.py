format_color_1 = '\u001b[38;5;40m'
format_color_2 = '\033[0m'

# Использование %:
print(f'{format_color_1}\n__ Использование % __{format_color_2}')

team1_num = 5
team2_num = 6
print('В команде Мастера кода участников: %s !' % team1_num)
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

#Использование format
print(f'{format_color_1}\n__ Использование format __{format_color_2}')

team2_name = 'Волшебники данных'
score_2 = 42
team2_time = 18015.2
print('Команда {} решила задач: {} !'.format(team2_name, score_2))
print('{team_name} решили задачи за {team_time} с !'.format(team_name = team2_name, team_time = team2_time))

# Использование f-строки:
print(f'{format_color_1}\n__ Использование f-строки __{format_color_2}')

score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач.')

challenge_result = 'Мастера кода'
tasks_total = 82
time_avg = 350.4
print(f'Результат битвы: победа команды {challenge_result}!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
