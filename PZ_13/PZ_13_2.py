# Из заданной строки отобразить только цифры. Использовать библиотеку string.
# Строка - The Great Pyramid of Khufu at Giza was built about 2700 BC, 755 feet (230 metres)
# long and 481 feet (147 metres) high.
import string

print(''.join([i for i in 'The Great Pyramid of Khufu at Giza was built about 2700 BC, 755 feet (230 metres) long and 481 feet (147 metres) high' if i in string.digits]))
