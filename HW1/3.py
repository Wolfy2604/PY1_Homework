n = int(input('Введите число: '))
numbers = []


def n_calc(arg):
    numbers.append(n)
    numbers.append(int(str(n) + str(n)))
    numbers.append(int(str(n) + str(n) + str(n)))
    numbers_sum = 0

    for number in numbers:
        numbers_sum += number
    return numbers_sum


print(n_calc(n))
