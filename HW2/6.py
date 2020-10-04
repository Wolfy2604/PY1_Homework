goods = [
    (1, {
        'name': 'компьютер', 'price': 20000, 'count': 5, 'unit': 'шт.'
    }),
    (2, {
        'name': 'принтер', 'price': 6000, 'count': 2, 'unit': 'шт.'
    }),
    (3, {
        'name': 'сканер', 'price': 2000, 'count': 7, 'unit': 'шт.'
    })
]
goods_count = 3


def confirm_add_product():

    confirmation = input('Добавляем продукт (add)? Или exit? ')
    if confirmation == 'exit':
        return False
    else:
        return True


def add_item():
    if confirm_add_product():

        input_name = input('Введите название: ')
        input_price = int(input('Введите цену: '))
        input_count = int(input('Введите количество: '))
        input_unit = input('Введите ед. измерения: ')

        goods.append((goods_count, {
            'name': f'{input_name}', 'price': f'{input_price}', \
            'count': f'{input_count}', 'unit': f'{input_unit}'
        }))

    else:
        get_analyse()

    add_item()


def get_analyse():

    custom_list = []
    user_choice = input('Какой список нужен? Введите name/price/count/unit')

    if user_choice == 'name':
        for item in goods:
            custom_list.append(item[1]['name'])
        print(custom_list)

    elif user_choice == 'price':
        for item in goods:
            custom_list.append(item[1]['price'])
        print(custom_list)

    elif user_choice == 'count':
        for item in goods:
            custom_list.append(item[1]['count'])
        print(custom_list)

    elif user_choice == 'unit':
        for item in goods:
            custom_list.append(item[1]['unit'])
        print(list(set(custom_list)))


add_item()