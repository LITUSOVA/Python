ans = 0
with open('my_file_5.txt', 'w') as file_5:
    line = input('Введите числа через пробел: \n')
    file_5.writelines(line)

file_5 = open('my_file_5.txt', 'r')
content = file_5.read().split()
try:
    for el in content:
        ans = ans + int(el)
    print(ans)
except ValueError:
    print('Ошибка ввода/вывода!')
file_5.close()






