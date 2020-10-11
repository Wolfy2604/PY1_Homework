from functools import reduce

list_1 = list(range(100, 1001, 2))

print(reduce(lambda num1, num2: num1 * num2, list_1))