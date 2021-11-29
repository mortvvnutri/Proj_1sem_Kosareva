# Дан список размера N.
# Найти количество его промежутков монотонности.
a = list(map(int, input('Введите значение чисел через пробел: ').split()))  # ввод списка с клавиатуры
N = len(a)  # узнавание длины списка

x = 0
y = True
for i in range(1, N):
    if a[i-1] > a[i]:
        if y:
            x += 1
            y = False
    else:
        y = True
print("Монотонные промежутки убывания:", x)

z = 0
k = True
for i in range(1, N):
    if a[i-1] < a[i]:
        if k:
            z += 1
            k = False
    else:
        k = True
print("Монотонные промежутки возрастания:", z)

print("Всего промежутков монотонности", z+x)
