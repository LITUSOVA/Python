class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} начал движение'

    def stop(self):
        return f'Автомобиль {self.name} остановился'

    def turn(self):
        return f'Автомобиль {self.name} изменил направление'

    def show_speed(self):
        return f'Автомобиль {self.name} движется со скоростью {self.speed}'

    def police(self):
        if self.is_police:
            return f'Автомобиль {self.name} является полицейским'
        else:
            return f'Автомобиль {self.name} не является полицейским'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Автомобиль {self.name} нарушает скоростной режим!')
        else:
            return f'Автомобиль {self.name} движется c разрешенной скоростью'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Автомобиль {self.name} нарушает скоростной режим!')
        else:
            return f'Автомобиль {self.name} движется c разрешенной скоростью'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car_1 = TownCar(50, 'gray', 'Audi A5', False)
car_2 = SportCar(100, 'purple', 'Aston Martin Vanquish', False)
car_3 = WorkCar(35, 'red', 'ГАЗ', False)
car_4 = PoliceCar(70, 'white', 'Volkswagen Polo', True)
print(car_1.go())
print(car_1.stop())
print(car_1.turn())
print(car_1.show_speed())
print(car_4.police())
print(car_1.police())
print(car_3.show_speed())
