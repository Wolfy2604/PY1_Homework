with open('test_3.txt', 'r', encoding='utf-8') as test:
    file_text = test.readlines()

salary_dict = {}
low_salary_workers = []
for pair in file_text:
    pair = pair.split()
    temp_dict = {pair[0]: int(pair[1])}
    salary_dict.update(temp_dict)

    if int(pair[1]) < 20000:
        low_salary_workers.append(pair[0])

average_salary = sum(list(salary_dict.values())) / len(salary_dict.values())

print(f'Работники с зп меньше 20000: {low_salary_workers}')
print(f'Средняя зп: {average_salary}')



