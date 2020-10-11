def general_func(total = 0, end = False):
    total
    is_end = end
    if not is_end:
        calc_sum(total)
    else:
        print(f'Итоговая сумма - {total}')


def calc_sum(total):
    print(total)
    current_list = input('Введите числа через пробел: ').split(' ')
    for index, item in enumerate(current_list):
        if item.isdigit():
            total += int(item)
            print(total)
            end = False
        else:
            end = True
            current_list = current_list[0:index - 1]
            total += sum(current_list)
            brea

    general_func(total, end)


general_func()
