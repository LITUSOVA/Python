def my_func_1(x, y):
    exp_1 = x ** y
    return exp_1


def my_func_2(x, y):
    while y > 1:
        x = x * x
        y = y - 1
    return 1 / x


a = float(input('Введите действительное положительное число: '))
b = int(input('Введите отрицательное целое число: '))
z = abs(b)

print(my_func_1(a, b))

print(my_func_2(a, z))
