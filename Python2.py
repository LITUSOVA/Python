my_str = input('Введите значения для списка через пробел: ')
my_list = list(my_str.split())

for i in range(0, len(my_list) - 1, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)

