from itertools import count
from math import factorial

a = 0


def my_factorial():
    for el in count(1):
        yield factorial(el)


result = my_factorial()
for i in result:
    if a < 15:
        print(i)
        a += 1
    else:
        break
