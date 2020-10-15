from itertools import cycle
import time

some_list = []
while len(some_list) < 3:
    some_list.append(
        input('Введите элементы списка: ')
    )


def iterator(some_list):
    count = 0
    for i in cycle(some_list):
        if count < 100:
            time.sleep(1)
            print(i)
            count += 1
        else:
            break


iterator(some_list)