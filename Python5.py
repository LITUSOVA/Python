my_list = [7, 5, 3, 3, 2]
my_number = int(input('Введите число: '))
if my_number in my_list:
    how_many = my_list.count(my_number)
    index = my_list.index(my_number)
    my_list.insert(index + how_many, my_number)
else:
    for el in my_list:
        if my_number < el:
            my_list.insert(my_list.index(el) + 1, my_number)
        else:
            my_list.insert(0, my_number)
            break
print(my_list)

