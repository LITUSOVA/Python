with open('my_file_3.txt', 'r') as file_3:
    salary = []
    surname = []
    my_sum = 0
    my_list = file_3.read().split('\n')
    for el in my_list:
        el = el.split()
        if float(el[1]) < 20000:
            surname.append(el[0])
        salary.append(el[1])
        my_sum = my_sum + float(el[1])
print(f'Оклад меньше 20000 у: {surname}')
print(f'Средний оклад сотрудников: {my_sum / len(salary):.2f}')

