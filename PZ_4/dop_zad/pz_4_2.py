#  Начальный вклад в банке равен 1000 руб. Через каждый месяц размер вклада увеличивается
#  на P процентов от имеющейся суммы (P — вещественное число, 0< P <25). По данному P
#  определить, через сколько месяцев размер вклада превысит 1100 руб., и вывести найденное
#  количество месяцев K (целое число) и итоговый размер вклада S (вещественное число).
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
