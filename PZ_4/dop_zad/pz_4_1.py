a = int(input('Число A = '))
while True:  # Проверка на тип данных переменной b
    try:
        b = int(input('Число B = '))
        if b <= a:  # Проверка на натуральность переменной
            print("Неверные данные, повторите ввод!")
        else:
            break  # Прерывание цикла
    except ValueError:
        print("Неправильно ввели, повторите ввод!")
k = 0
c = 0
while b > a - 1:
    c = b ** 2
    b -= 1
    k += c
    c = 0
print(k, end=' ')
