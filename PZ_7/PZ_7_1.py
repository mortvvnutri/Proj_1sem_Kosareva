#  Дана строка. Вывести строку, содержащую те же символы, но расположенные в обратном порядке
a = input('Введите строку, после нажмите Enter: ')
b = ''.join(reversed(a))
print(b)