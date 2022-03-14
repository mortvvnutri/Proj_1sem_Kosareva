#  В матрице элементы третьей строки заменить элементами из одномерного
#  динамического массива соответствующей размерности.

from random import randint

m, n, y, z = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ", "От = ", "До = ")]
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
print('Исходная матрица:')
for i in matrix:
    print(*i)
matrix[2] = [randint(-100, 100) for o in range(n)]
print('Полученная матрица:')
for i in matrix:
    print(*i)

