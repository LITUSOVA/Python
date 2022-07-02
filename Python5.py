class Stationary:
    def __init__(self, title):
        self.title = title

    def draw():
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки для инструмента: {self.title} '


class Pencil(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки для инструмента: {self.title}'


class Handle(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки для инструмента: {self.title}'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())

