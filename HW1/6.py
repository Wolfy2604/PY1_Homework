a = int(input('Введите 1 результат: '))
b = int(input('Введите требуемый результат: '))
day_counter = 1

while a < b:
    a *= 1.1
    day_counter += 1

print(day_counter)
