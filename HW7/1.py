import itertools


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix if self.matrix_check(matrix) else None
        self.col_num = len(self.matrix[0])

    def __add__(self, other):
        # Переводим в простые списки и суммируем
        list1 = sum(self.matrix, [])
        list2 = sum(other.matrix, [])
        sum_list = [num1 + num2 for num1, num2 in zip(list1, list2)]
        # Перевод списка в матрицу
        result = []
        while sum_list:
            temp_list = []
            i = self.col_num
            while i:
                try:
                    temp_list.append(sum_list.pop(0))
                except IndexError:
                    break
                i -= 1
            result.append(temp_list)
        # Визуализация матрицы
        visualize = ''
        for col in result:
            visualize += f'{col}\n'
        else:
            return visualize

    def __str__(self):
        visualize = ''
        for col in self.matrix:
            visualize += f'{col}\n'

        return visualize

    # Проверка матрицы
    def matrix_check(self, matrix):
        col_num = len(matrix[0])
        for col in matrix:
            if isinstance(matrix, list):
                if isinstance(col, list):
                    if len(col) == col_num:
                        try:
                            if [int(num) for num in col]:
                                continue
                        except ValueError:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return True


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[7, 8, 9], [4, 5, 6], [1, 4, 3]]
my_matrix = Matrix(matrix)
my_matrix2 = Matrix(matrix2)

print(my_matrix)
print(my_matrix2)
print(my_matrix + my_matrix2)
