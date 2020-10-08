def start():
    try:
        num1 = float(input('Введите действительное положительное число: '))
        num2 = int(input('Введите целое отрицательное число: '))
    except ValueError:
        print('Ошибка ввода!')
        start()

    return user_input_check(num1, num2)


def user_input_check(num1, num2):
    if num1 < 0 or num2 > 0:
        print('Неверные числа!')
        start()
    else:
        return elevate(num1, num2)


def elevate(x, y):
    i = 1
    elev_value = x
    while i < abs(y):
        i += 1
        elev_value *= x
        print(elev_value)
    result = 1 / elev_value

    return result


print(start())
