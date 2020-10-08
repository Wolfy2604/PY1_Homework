def take_input():

    number1 = int(input('Введите 1 число: '))
    number2 = int(input('Введите 2 число: '))

    divide_func(number1, number2)


def divide_func(num_1, num_2):

    try:
        result = num_1 / num_2
    except ZeroDivisionError:
        take_input()
    print(result)


take_input()
