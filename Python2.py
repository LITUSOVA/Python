import random
list_1 = [i for i in range(20)]
random.shuffle(list_1)
list_2 = [el for j, el in enumerate(list_1) if list_1[j - 1] < list_1[j]]
print(list_1)
print(list_2)
