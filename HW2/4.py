user_input = input('Введите предложение: ')

input_list = enumerate(list(user_input.split(' ')))

for index, word in input_list:

    if len(word) > 10:
        print(f'{index + 1}. {word[ :9 ]}...')
    else:
        print(f'{index + 1}. {word}')