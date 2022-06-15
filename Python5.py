def my_func():
    my_sum = 0
    ex = False
    while not ex:
        num = input('Введите значения для суммирования или S для остановки - ').split()
        res = 0
        for i in range(len(num)):
            if num[i] == 'S':
                ex = True
                break
            else:
                res = res + int(num[i])
        my_sum = my_sum + res
        print(f'Текущая сумма {my_sum}')
    print(f'Итоговая сумма {my_sum}')


my_func()
