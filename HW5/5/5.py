with open('test-5.txt', 'w', encoding='utf-8') as test:
    test.write(input('Введите числа через пробел: '))

with open('test-5.txt', 'r', encoding='utf-8') as test_read:
    user_input = test_read.read().split()
    user_input = list(map(lambda item: int(item), user_input))
    print(sum(user_input))
