import math

n = int(input('Введите число n: '))


def gen_factorial(num):
    for el in range(1, num + 1):
        yield math.factorial(el)


print(list(gen_factorial(n)))

