n = int(input('Введите количество товаров: '))
dictionary = []
all_products = []
list_prod = []
list_pr = []
list_am = []
list_un = []
new_dict = {}

for el in range(n):
    name = 'dic_' + str(el+1)
    dictionary.append(name)

for i in range(n):
    product = input('Введите название товара: ')
    price = float(input('Введите стоимость товара: '))
    amount = int(input('Введите количество: '))
    unit = input('Введите ед.: ')
    dictionary[i] = {}
    dictionary[i].update({'название': product})
    dictionary[i].update({'цена': price})
    dictionary[i].update({'количество': amount})
    dictionary[i].update({'ед.': unit})
    all_products.append((i+1, dictionary[i]))
    list_prod.append(product)
    list_pr.append(price)
    list_am.append(amount)
    list_un.append(unit)
    new_dict.update({'название': list_prod})
    new_dict.update({'цена': list_pr})
    new_dict.update({'количество': list_am})
    new_dict.update({'ед': list(set(list_un))})

print("Товары: ")
for element in all_products:
    print(element)

print("Аналитика:")
for key in new_dict:
    print(f"{key}:{new_dict[key]}")





