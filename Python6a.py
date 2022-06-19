from itertools import count
for el in count(int(input('Стартовое число: '))):
    if el == 100:
        break
    else:
        print(el)
