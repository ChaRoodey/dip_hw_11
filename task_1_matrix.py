class Matrix:
    def __init__(self, matrix) -> None:
        self.matrix = matrix

    def __add__(self, other):
        rezult = [[] for _ in range(len(self.matrix))]
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError('Сложение можно проводить только с равными матрицами.')

        for row in range(len(self.matrix)):
            for column in range(len(self.matrix[row])):
                rezult[row].append(self.matrix[row][column] + other.matrix[row][column])

        return rezult

    def __sub__(self, other):
        rezult = [[] for _ in range(len(self.matrix))]
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError('Вычитание можно проводить только с равными матрицами.')

        for row in range(len(self.matrix)):
            for column in range(len(self.matrix[row])):
                rezult[row].append(self.matrix[row][column] - other.matrix[row][column])

        return rezult

    def __matmul__(self, other):
        rezult = [[] for _ in range(len(self.matrix))]
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError('Число столбцов не равно числу строк.')

        for row in range(len(self.matrix)):
            for column in range(len(other.matrix[0])):
                cell = (self.matrix[row][i] * other.matrix[i][column] for i in range(len(self.matrix[0])))
                rezult[row].append(sum(cell))

        return rezult

    def transp(self):
        rezult = [[] for _ in range(len(self.matrix[0]))]
        for row in range(len(self.matrix)):
            for column in range(len(self.matrix[row])):
                rezult[column].append(self.matrix[row][column])
        return rezult


if __name__ == '__main__':
    matrix_1 = Matrix([[12],
                       [13]])

    matrix_2 = Matrix([[18, 11],
                       [12, 10]])

    '''for i in matrix_1 + matrix_2:
        print(i)

    for i in matrix_1 - matrix_2:
        print(i)

    rez = matrix_1 @ matrix_2
    for i in rez:
        print(i)'''

    rez = matrix_2.transp()
    for i in rez:
        print(i)
