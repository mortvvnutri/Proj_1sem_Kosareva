# Практическая №10 №1
# Средствами языка Python сформировать текстовый файл (.txt), содержайщий последовательность из целых положительных и
# отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов: Исхдные данные: Количество элементов: Элементы в обратном порядке:
# Сумма элементов последней половины:
print('5, 4, 3, 2, 1, -1, -2, -3, -4, -5', file=open('file10_1.txt', 'w'))
d = [int(i) for i in open('file10_1.txt').read().split(', ')]   # Перебор файла запись целочисленных в список
u = open('file_new10_1.txt', 'w')  # Создаём новый .txt файл
print('Исходные данные:', open('file10_1.txt').read(), file=u)
print('Количество элементов:', len(open('file10_1.txt').read().split(', ')), '\n', file=u)
print('Элементы в обратном порядке:', d[::-1], '\n', file=u)
print('Сумма элементов последней половины:', sum(d[5:]), file=u)
u.close()  # Закрываем .txt файл
