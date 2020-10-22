class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return 'Запуск отрисовки ручкой'


class Pencil(Stationery):
    def draw(self):
        return 'Запуск отрисовки карандашом'


class Handle(Stationery):
    def draw(self):
        return 'Запуск отрисовки маркером'


pencil = Pencil('Карандашик')
parker = Pen('Ручка')
handle = Handle('Красный маркер')

print(pencil.draw())
print(parker.draw())
print(handle.draw())