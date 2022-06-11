my_list1 = [3, 'geek', 26.5, True, None, [3, 2.4]]
my_list2 = [2, "brains", 23.4]

print('Типы элементов списка my_list1 ')
for i in range(len(my_list1)):
    print(type(my_list1[i]))
    if type(my_list1[i]) is list:
        print('Типы элементов списка в списке my_list1: ')
        for j in range(len(my_list1[i])):
            print(type(my_list1[i][j]))

print('Типы элементов списка my_list2 ')
for el in my_list2:
    print(type(el))







