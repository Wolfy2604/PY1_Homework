# Реализовал не через именованные аргументы, подумал, что так аккуратнее

user_data = []
requests = ['Введите свое имя: ', 'Введите свою фамилию: ', \
            'Введите свой год рождения: ', 'Введите свой город: ', \
            'Введите свой email: ', 'Введите свой телефон: ']


def take_params():
    for index, phrase in enumerate(requests):
        try:
            current_phrase = input(phrase)
            if current_phrase == '':
                user_data.append('no_data')
            elif index == 2 or index == 5:
                user_data.append(int(current_phrase))
            else:
                user_data.append(current_phrase)

        except ValueError:
            print('Год рождения и номер телефона - числа')
            take_params()

    print(*user_data)


take_params()


