from sys import argv


def my_salary(hour, rate, premium):
    return float(hour) * float(rate) + float(premium)


print(my_salary(argv[1], argv[2], argv[3]))
