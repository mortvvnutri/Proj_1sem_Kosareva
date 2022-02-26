# В последовательности на n целых чисел найти и вывести:
#   1. максимальный среди отрицательных
#   2. элементы кратные двум
#   3. их сумму

from random import randint
n = [randint(-9, 9) for i in range(int(input('Введите количество чисел в последовательности: ')))]
print(max([i for i in n if i < 0]), '\n' + str([i for i in n if i % 2 == 0]), '\n' + str(sum(n)))
