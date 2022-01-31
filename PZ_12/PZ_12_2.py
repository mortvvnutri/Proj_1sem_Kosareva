# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 3 – 8.
from tkinter import *


def various_elements(vvod):
    c['text'] = 'Перевёрнутая строка:', n.get()[::-1]


root = Tk()
root.title('Переворот строки')
root.geometry("500x120")
Label(text='Ввод:').grid(row=1, column=0)
n = Entry(width=50)
n.grid(row=1, column=1)
button1 = Button(text="Переворот")
button1.grid(row=4, column=1)
c = Label(font='arial 12')
c.grid(row=5, column=1)
button1.bind('<Button-1>', various_elements)
root.mainloop()
