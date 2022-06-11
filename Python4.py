my_str = input('Введите строку: ')
my_list = list(my_str.split())
n = 0
for el in my_list:
    n += 1
    if len(el) <= 10:
        print(n, el)
    else:
        print(n, el[0: 10])




