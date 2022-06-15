def my_fun(arg_1, arg_2, arg_3):
    if arg_1 >= arg_3 and arg_2 >= arg_3:
        return arg_1 + arg_2
    elif arg_1 >= arg_2 and arg_3 >= arg_2:
        return arg_1 + arg_3
    else:
        return arg_2 + arg_3


argum_1 = int(input('Введите первый аргумент: '))
argum_2 = int(input('Введите второй аргумент: '))
argum_3 = int(input('Введите третий аргумент: '))

print(my_fun(argum_1, argum_2, argum_3))
