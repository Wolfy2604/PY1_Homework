user_input = ' '
all_lines = []
while user_input != '':
    user_input = input('Введите строку: ')
    all_lines.append(user_input + '\n')

with open('test_1.txt', 'w') as test:
    test.writelines(all_lines)