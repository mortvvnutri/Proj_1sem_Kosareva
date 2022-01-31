# В соответствии с номером варианта перейти по ссылке на прототип.
# Реализовать его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу (см. таблицу 1).

from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import Combobox
root = Tk()
root.geometry('700x656')
root['bg'] = '#acacac'
Canvas(root, bg='#cbcbcb', height=600, width=475,  highlightthickness=6, highlightbackground='white').place(x=100, y=25)
Label(text='Contact Form', width=11, bg='#cbcbcb', fg='black', font=('arial', '18', BOLD)).place(x=150, y=60)
Label(text='Please fill all entries', width=16, bg='#cbcbcb', fg='black', font=('arial', '10', BOLD)).place(x=159, y=110)
Label(text='Name:', width=7, bg='#cbcbcb', fg='black', font='arial 12').place(x=170, y=175)
Entry(width=20, font='arial 17').place(x=230, y=174)
Label(text='Email:', width=7, bg='#cbcbcb', fg='black', font='arial 12').place(x=170, y=235)
Entry(width=20, font='arial 17').place(x=230, y=234)
Label(text='Message:', width=7, bg='#cbcbcb', fg='black', font='arial 12').place(x=159, y=295)
Entry(width=6, font='arial 58').place(x=230, y=294)
Label(text='Subject:', width=7, bg='#cbcbcb', fg='black', font='arial 12').place(x=162, y=415)
combo = Combobox(root, width=40, values=['Product Inquiry'])
combo.current(0)
combo.place(x=230, y=417)
Button(root, text='Send', width=10, height=2, bg='#999', fg='white', font='arial 8').place(x=230, y=475)
root.mainloop()
