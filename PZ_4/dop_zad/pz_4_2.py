while True:  # Проверка на тип данных переменной P
    try:
        P = int(input('P = '))
        if 0 < P < 25:  # Проверка на натуральность переменной и соответствие условию
            break  # Прерывание цикла
        else:
            print("Неверные данные")

    except ValueError:
        print("Неправильно ввели!")
k = 0
s = 1000
while s < 1100:
    k += 1
    s += s * (P/100)
print('через', k, 'месяцев')
print('итоговый размер вклада =', s)
