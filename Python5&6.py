profit = int(input('Выручка (руб): '))
attrition = int(input('Издержки (руб): '))

if profit == attrition:
    print('Выручка покрывает издержки, чистая прибыль равна: 0.00 руб')

if profit < attrition:
    n = attrition - profit
    print('Выручка не покрывает издержки, убыль составляет: ' "{:.2f}".format(n), 'руб')

if profit > attrition:
    n = profit - attrition
    profitability = (n / profit) * 100
    wokers = int(input('Введите количество сотрудников: '))
    prof_for_one_w = n / wokers
    print('Выручка покрывает издержки, чистая прибыль равна: ' "{:.2f}".format(n), 'руб')
    print('Рентабельность выручки составила:' "{:.2f}".format(profitability), '%')
    print('Чистая прибыль в расчете на одного сотрудника равна: ' "{:.2f}".format(prof_for_one_w), 'руб')



