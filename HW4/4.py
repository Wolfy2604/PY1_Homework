# Очень трудно решалась задача, наверное, есть более практичное решение

some_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def create_no_repeat_list(list):
    repeat_set = []
    main_list = []
    for num in list:
        if num in main_list:
            repeat_set.append(num)
            main_list.append(num)
        else:
            main_list.append(num)
    main_list = [x for x in main_list if repeat_set.count(x) == 0]

    return main_list


print(create_no_repeat_list(some_list))
