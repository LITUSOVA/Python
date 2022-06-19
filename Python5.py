from functools import reduce


def my_fun(prev_el, el):
    return prev_el * el


print(f'Список из четных значений: {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Произведение всех элементов списка: {reduce(my_fun, [el for el in range(99, 1001) if el % 2 == 0])}')
