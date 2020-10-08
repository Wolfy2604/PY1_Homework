# Не предусмотрены случаи повторяющихся элементов списка

some_list = []


def form_list():

    while True:
        input_val = input('Введите значение в список (end для остановки): ')
        if input_val == 'end':
            break
        elif input_val == 'True' or input_val == 'False':
            some_list.append(bool(input_val))
        elif input_val.isdigit():
            some_list.append(int(input_val))
        elif input_val == 'None':
            some_list.append(None)
        else:
            some_list.append(input_val)
    print(some_list)


def change_items ():

    for index, item in enumerate(some_list):
        if index % 2 != 0 and index != 0:
            some_list.insert(index - 1, some_list.pop(index))
        else:
            continue

    print(some_list)


form_list()
change_items()