import re
with open('Dostoevsky.txt', encoding='utf-8')as file:
    inf = file.read()
fio = re.findall(r'[А-Я]\.\s+[А-Я]\.\s+[А-Я][а-я]+', inf)
print(fio)
