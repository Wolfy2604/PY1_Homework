with open('test_2.txt', 'r', encoding='utf-8') as test:
    file_text = test.readlines()

print(f'Количество строк - {len(file_text)}')
for idx, line in enumerate(file_text):
    print(f'Количество слов в {idx + 1} строке- {len(line.split())}')


