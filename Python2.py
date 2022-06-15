name = input('Имя: ')
surname = input('Фамилия: ')
b_year = input('Год рождения: ')
e_mail = input('e-mail: ')
tel = input('Телефон: ')


def my_func(name1="", surname1="", b_year1="", e_mail1="", tel1=""):
    return ' '.join([name1, surname1, b_year1, e_mail1, tel1])


print(my_func(name1=name, surname1=surname, b_year1=b_year, e_mail1=e_mail, tel1=tel))
