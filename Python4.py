my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('my_file_4.txt', 'r') as file_4:
    for el in file_4:
        el = el.split(' ', 1)
        new_file.append(my_dict[el[0]] + ' ' + el[1])
    print(new_file)
with open('new_my_file_4.txt', 'w') as new_file_4:
    new_file_4.writelines(new_file)
