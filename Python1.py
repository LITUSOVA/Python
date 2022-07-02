from time import sleep

t = int(input('Сколько секунд горит зеленый сигнал светофора? '))


class TrafficLight:
    __color = ['Красный', 'Жёлтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            if i == 0:
                print(TrafficLight.__color[i])
                sleep(7)
            elif i == 1:
                print(TrafficLight.__color[i])
                sleep(2)
            else:
                print(TrafficLight.__color[i])
                sleep(t)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()

# Не смогла сообразить как осуществить проверку порядка режимов
