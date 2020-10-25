from random import randint, sample


class Card:

    def __init__(self, name):
        self.name = name
        self.counters = []

    def __str__(self):
        result = ''
        result_line = ''
        i = 0
        for val in self.counters:
            if i == 9 or i == 18:
                result += f'{result_line}\n'
                result_line = ''
            if 0 < val < 10:
                result_line += f' {val} '
            elif val == 0:
                result_line += '   '
            elif val == -1:
                result_line += ' - '
            else:
                result_line += f'{val} '
            i += 1
        result += f'{result_line}'
        return result

    @staticmethod
    def create_cards(counters, user, comp):
        i = 30
        while i > 0:
            while i > 15:
                user.counters.append(counters._main_list.pop \
                                         (randint(0, len(counters._main_list) - 1)))
                i -= 1
            comp.counters.append(counters._main_list.pop \
                                     (randint(0, len(counters._main_list) - 1)))
            i -= 1

        user.counters = [sorted(user.counters[0:5]), sorted(user.counters[5:10]), \
                         sorted(user.counters[10:15])]
        comp.counters = [sorted(comp.counters[0:5]), sorted(comp.counters[5:10]), \
                         sorted(comp.counters[10:15])]

        def create_cards_line(counters):
            result = []
            for line in counters:
                num_indexes = sample(list(range(0, 9)), k=5)
                for idx in range(9):
                    if idx in num_indexes:
                        try:
                            result.append(line.pop(0))
                        except IndexError:
                            result.append(0)
                    else:
                        result.append(0)
            return result

        user.counters = create_cards_line(user.counters)
        comp.counters = create_cards_line(comp.counters)

        # print(user.counters)
        # print(comp.counters)


class Counters:

    def __init__(self):
        self._full_list = list(range(1, 91))
        self._main_list = list(range(1, 91))

    def take_current(self):
        return self._full_list.pop(randint(0, len(self._full_list) - 1))


class Manager:

    def __init__(self):
        pass

    def start_game(self):
        Card.create_cards(counters, user, comp)
        self.dialog()

    def dialog(self):
        current_num = counters.take_current()
        print(f'Новый бочонок: {current_num}'
              f'\nВаша карточка:\n{user}\n\nКарточка компьютера:\n{comp}')
        decision = True if (input('Зачеркнуть число? (y/n) ') == 'y') else False

        def check_counter(decision):
            if decision:
                for idx, num in enumerate(user.counters):
                    if num == current_num:
                        user.counters.pop(idx)
                        user.counters.insert(idx, -1)
                        if user.counters.count(-1) == 15:
                            manager.end_game('win')
                        else:
                            manager.dialog()
                    else:
                        continue
                else:
                    manager.end_game('wrong')
            else:
                for idx, num in enumerate(comp.counters):
                    if num == current_num:
                        comp.counters.pop(idx)
                        comp.counters.insert(idx, -1)
                        if comp.counters.count(-1) == 15:
                            manager.end_game('comp')
                        else:
                            manager.dialog()
                    else:
                        continue
                else:
                    manager.dialog()

        check_counter(decision)

    def end_game(self, reason):
        if reason == 'wrong':
            print('Вы поторопились! Нет такого значения!')
        elif reason == 'comp':
            print('Компьютер набрал все очки!')
        else:
            print('Вы собрали все очки!')


counters = Counters()
user = Card('Игрок')
comp = Card('Бот')
manager = Manager()

manager.start_game()
print(user)
print(comp)
