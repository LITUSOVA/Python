from itertools import cycle
a = 0
my_list = ['GeekBrains', 4, None]
for el in cycle(my_list):
    if a > 10:
        break
    else:
        print(el)
        a += 1
