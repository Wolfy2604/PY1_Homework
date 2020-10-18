class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        result = f'{self.name} {self.surname}'
        return result

    def get_total_income(self):
        result = sum(self._income.values())
        return result


director = Position('Ivan', 'Petrov', 'director', 30000, 40000)
print(director.get_full_name())
print(director.get_total_income())