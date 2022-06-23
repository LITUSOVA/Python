file_2 = open('my_file_2.txt', 'r')
content = file_2.readlines()
print(f'Всего строк в файле - {len(content)}')
for i in range(len(content)):
    print(f'Всего слов в {i + 1} строке {len(content[1].split())}')
file_2.close()



