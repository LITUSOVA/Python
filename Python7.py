import json
my_dict = {}
profit = {}
income = 0
average = 0
i = 0
with open('my_file_7.txt', 'r') as file:
    for line in file:
        firm, ownership, revenue, costs = line.split()
        my_dict[firm] = int(revenue) - int(costs)
        if my_dict.setdefault(firm) >= 0:
            income = income + my_dict.setdefault(firm)
            i += 1
    if i != 0:
        average = income / i
        print(f'Средняя прибыль: {average:.2f}')
    else:
        print(f'Все фирмы работают в убыток!')
    profit = {'Средняя прибыль': round(average)}
    my_dict.update(profit)
    print(f'Прибыль каждой компании - {my_dict}')
with open('my_file_7.json', 'w') as file_7_js:
    json.dump(my_dict, file_7_js)
    my_js = json.dumps(my_dict)
    print(f'Создан файл с расширением json со следующим содержимым: \n ' f' {my_js}')
