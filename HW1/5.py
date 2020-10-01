def get_values():
    income = 0
    costs = 0
    try:
        income = int(input('Введите выручку: '))
        costs = int(input('Введите расходы: '))
    except ValueError:
        get_values()
    return (income, costs)


def analyze():
    balance_data = get_values()
    if balance_data[0] < balance_data[1]:
        print(f'Вы работаете в минус!')

    elif balance_data[0] == balance_data[1]:
        print(f'Вы работаете в ноль!')

    else:
        state = int(input('Сколько у вас сотрудников: '))
        print(f'Вы заработали по {int((balance_data[0] - balance_data[1]) / state)} ен на сотрудника')


analyze()
