def devi (argun_1, argun_2):
    return argun_1 / argun_2


arg1 = int(input('Введите первое число: '))
arg2 = int(input('Введите второе число: '))

if arg2 != 0:
    print(devi(arg1, arg2))
else:
    print('На ноль делить нельзя!')
