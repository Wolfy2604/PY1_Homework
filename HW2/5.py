rating = [7, 5, 3, 3, 2]


def add_user_value():
    user_value = input('Введите число или exit: ')
    if user_value == 'exit':
        print(rating)
    else:
        user_value = int(user_value)
        temp_list = []
        user_value_index = 0

        # Заполняем список разностями начальных чисел и пользовательского числа
        for digit in rating:
            temp_list.append(digit - user_value)
        print(temp_list)

        # Проходим временный список, чтобы найти место для пользовательского числа
        for idx, value in enumerate(temp_list):
            # Разное поведение для положительной, отрицательной разницы, нуля
            if value > 0:
                if value == min(temp_list):
                    user_value_index = idx + 1
                    print(user_value_index)
                    break
                else:
                    continue
            elif value < 0:
                if value == max(temp_list):
                    user_value_index = idx
                    print(user_value_index)
                    break
                else:
                    continue
            else:
                if value == 0:
                    user_value_index = idx
                    print(user_value_index)
                    break
                else:
                    continue

        rating.insert(user_value_index, user_value)

        add_user_value()


add_user_value()
