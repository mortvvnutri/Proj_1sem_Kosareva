#  В матрице найти среднее арифметическое положительных элементов.
from random import randint

m, n, y, z = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ", "От = ", "До = ")]
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
h = []
print('Матрица:')
for i in matrix:
    print(*i)
for i in matrix:
    for o in i:
        if o > 0:
            h.append(o)
print('Среднее арифметическое положительных элементов:', sum(h) / len(h))