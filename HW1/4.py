def number_input():
    number = 0
    try:
        number = int(input('Введите положительное целое число: '))
    except ValueError:
        number_input()

    if number <= 0:
        print('Неположительнео число!')
        number_input()

    return number


def find_big_digit():

    list_number = []
    biggest_digit = 0

    for digit in str(number_input()):
        list_number.append(int(digit))

    for digit in list_number:
        if digit > biggest_digit:
            biggest_digit = digit

    print(biggest_digit)


find_big_digit()
