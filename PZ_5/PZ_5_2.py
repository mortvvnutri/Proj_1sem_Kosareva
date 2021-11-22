def minmax(v, x, y, z):
    vNum = int
    xNum = int
    yNum = int
    zNum = int

    if v < x and v < y and v < z:
        vNum = 1
    elif (v < x and v < y) or (v < y and v < z) or (v < x and v < z):
        vNum = 2
    elif v < x or v < y or v < z:
        vNum = 3
    else:
        vNum = 4

    if x < v:
        xNum = vNum - 1
    else:
        xNum = vNum + 1

    if y < x:
        yNum = xNum
        xNum += 1
    else:
        yNum = xNum + 1

    if z < y:
        zNum = yNum
        yNum += 1
    else:
        zNum = yNum + 1

    print(xNum, yNum, zNum, vNum)

    if xNum == 1:
        A = x
    elif yNum == 1:
        A = y
    elif zNum == 1:
        A = z
    elif vNum == 1:
        A = v
    if xNum == 4:
        D = x
    elif yNum == 4:
        D = y
    elif zNum == 4:
        D = z
    elif vNum == 4:
        D = v



A = float(input('А = '))
B = float(input('B = '))
C = float(input('C = '))
D = float(input('D = '))

minmax(A, B, C, D)

print(A, '- минимальное значение')
print(D, '- максимальное значение')
