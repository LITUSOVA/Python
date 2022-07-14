class Date:
    def __init__(self, b_day):
        self.b_day = b_day

    @classmethod
    def retrieve(cls, b_day):
        date = []

        for el in b_day.split():
            if el.isdigit():
                date.append(el)
        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def validation(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 1900:
                    return f'Возможная дата рождения'
                else:
                    return f'Ошибка! неправильно указан год!'
            else:
                return f'Ошибка! неправильно указан месяц!'
        else:
            return f'Ошибка! неправильно указан день!'


def __str__(self):
    return f'Текущая дата {Date.retrieve(self.day_month_year)}'


my_day = Date('20 - 10 - 1995')
print(Date.retrieve('20 - 10 - 1995'))
print(my_day.validation(11, 10, 2011))