some_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []


def generate_list(list):
    previous_num = 0
    for num in list:
        if num > previous_num:
            yield num
        previous_num = num


print(list(generate_list(some_list)))