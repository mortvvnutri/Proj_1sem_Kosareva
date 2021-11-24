def minmax(x, y):
    if y < x:
        y, x = x, y
    return x, y

a = float(input('Введите данные для переменной А '))
b = float(input('Введите данные для переменной B '))
c = float(input('Введите данные для переменной C '))
d = float(input('Введите данные для переменной D '))

min1, max1 = minmax(a, b)  # поиск максимума и минимума из а и b
min2, max2 = minmax(c, d)  # поиск максимума и минимума из с и d
min_minimal, max_minimal = minmax(min1, min2)  # поиск наименьшего из минимов
min_maximal, max_maximal = minmax(max1, max2)  # поиск наибольшего из максимов

print('Миниамльное число', min_minimal)
print('Максимальное число', max_maximal)