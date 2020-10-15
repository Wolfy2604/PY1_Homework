

with open('test_4.txt', 'r', encoding='utf-8') as test:
    rus_text = []
    for line in test:
        line = line.split('—')
        if line[1].find('1') == 1:
            line[0] = 'Один'
        elif line[1].find('2') == 1:
            line[0] = 'Два'
        elif line[1].find('3') == 1:
            line[0] = 'Три'
        else:
            line[0] = 'Четыре'
        line = line[0] + line[1]
        rus_text.append(line)
    with open('test_4_2.txt', 'w', encoding='utf-8') as test2:
        print(rus_text)
        test2.writelines(rus_text)

