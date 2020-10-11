def int_func(word):
    # word = input('Введите слово из прописных букв на латинице: ')
    result = word.capitalize()

    return result


def phrase_func():
    phrase = input('Введите фразу на латинице: ')
    buffer = phrase.split(' ')
    total_phrase = ''
    for item in buffer:
        total_phrase += f'{int_func(item)} '

    return total_phrase


print(phrase_func())