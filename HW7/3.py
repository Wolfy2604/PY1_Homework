from math import floor


class Cells:

    def __init__(self, cells_count):
        self.cells_count = int(cells_count)

    def __add__(self, other):
        return self.cells_count + other.cells_count

    def __sub__(self, other):
        if (self.cells_count - other.cells_count) > 0:
            return self.cells_count - other.cells_count
        else:
            print('Вычитаемое больше уменьшаемого!')

    def __mul__(self, other):
        return self.cells_count * other.cells_count

    def __truediv__(self, other):
        try:
            result = floor(self.cells_count / other.cells_count)
            return result

        except ZeroDivisionError:
            print('Деление на ноль!')

    def make_order(self, col_count):
        result = []
        for idx, letter in enumerate('*' * self.cells_count):
            if idx != 0 and (idx + 1) % col_count == 0:
                result.append('*\n')
            else:
                result.append('*')
        return ''.join(result)


cell1 = Cells(17)
cell2 = Cells(5)

print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)

print(cell1.make_order(6))


