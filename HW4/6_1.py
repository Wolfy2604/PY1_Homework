from itertools import count


def iterator(start, stop):
    for i in count(start):
        if i < stop:
            print(i)
        else:
            break


iterator(10, 20)
