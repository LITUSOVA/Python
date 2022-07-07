class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return str(f'Количество ячеек в клетке - {self.cell}')

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if (self.cell - other.cell) > 0:
            return Cell(abs(self.cell - other.cell))
        else:
            return f'Разность количества ячеек меньше 0!'

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def make_order(self, integer):
        my_cell = self.cell
        while my_cell > 0:
            for i in range(0, integer):
                print('*', end='')
                my_cell -= 1
                if my_cell <= 0:
                    break
            print('\n', end='')


cell_1 = Cell(5)
cell_2 = Cell(10)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

cell_1.make_order(3)
cell_2.make_order(5)