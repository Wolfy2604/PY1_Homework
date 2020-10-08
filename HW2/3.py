# Решение через list

season_list = ['Зима', 'Весна', 'Лето', 'Осень']

user_number = int(input('Введите номер месяца 1-12: '))

if user_number <= 2 or user_number == 12:
    print(f'Время года - {season_list[0]}')
elif 3 <= user_number <= 5:
    print(f'Время года - {season_list[1]}')
elif 6 <= user_number <= 8:
    print(f'Время года - {season_list[2]}')
elif 9 <= user_number <= 11:
    print(f'Время года - {season_list[3]}')

# Решение через dict

season_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}

user_number = int(input('Введите номер месяца 1-12: '))

if user_number <= 2 or user_number == 12:
    print(f'Время года - {season_dict[1]}')
elif 3 <= user_number <= 5:
    print(f'Время года - {season_dict[2]}')
elif 6 <= user_number <= 8:
    print(f'Время года - {season_dict[3]}')
elif 9 <= user_number <= 11:
    print(f'Время года - {season_dict[4]}')


