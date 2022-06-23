file_1 = open('my_file_1.txt', 'w')
line = input('Введите строку: ')

while line:
    line += '\n'
    file_1.writelines(line)
    line = input('Введите строку: ')

file_1.close()
file_1 = open('my_file_1.txt', 'r')
content = file_1.readlines()
print(content)
file_1.close()
