team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score1 + score2
time_avg = (team1_time + team2_time) / tasks_total

if score1 > score2 or score1 == score2 and team1_time > team2_time:
    challenge_result = 'победа команды Мастера кода!'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    challenge_result = 'победа команды Волшебники Данных!'
else:
    challenge_result = 'ничья!'

#Использование %:
print('В команде Мастера кода участников: %s!' % (team1_num))
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

#Использование format():
print('Команда Волшебники данных решила задач: {} !'.format(score2))
print('Волшебники данных решили задачи за {} c!'.format(team2_time))

#Использование f-строк:
print(f'Команды решили {score1} и {score2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 1)} секунды на задачу!')

