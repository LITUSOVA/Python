class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            length = len(self.matrix[0])
            numbers = []
        for i in range(len(self.matrix)):
            for j in range(length):
                sum_matrix = other.matrix[i][j] + self.matrix[i][j]
                numbers.append(sum_matrix)
            return f'matrix {sum_matrix}'


matrix_1 = Matrix([[1, 1], [2, 2]])
matrix_2 = Matrix([[1, 1], [2, 2]])

print(matrix_1 + matrix_2)

# В общем, с матрицами у меня совсем не срослось