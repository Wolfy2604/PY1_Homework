def my_func(arg1, arg2, arg3):
    booster = [arg1, arg2, arg3]
    sum1 = booster.pop(booster.index(max(booster)))
    sum2 = booster.pop(booster.index(max(booster)))
    result = sum1 + sum2

    return result


user_input = []
count = 0
while count < 3:
    try:
        user_number = int(input('Введите число: '))
        user_input.append(user_number)
    except ValueError:
        print('нужно ввести число!')
        break
    count += 1


print(my_func(*user_input))