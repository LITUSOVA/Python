s = int(input('Введите количество секунд, которое не превышает общее количество секунд в сутках: '))

if s < 86400:
    h = s // 3600
    s = s % 3600
    m = s // 60
    s = s % 60
    print("%02d:%02d:%02d" % (h, m, s))
else:
    print('Введенное количество секунд превышает общее количество секунд в сутках')





