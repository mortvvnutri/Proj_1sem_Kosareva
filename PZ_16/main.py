import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):

    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='blue', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="11.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить работника', command=self.open_dialog, bg='blue', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="12.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='blue',
                                    bd=0, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="13.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='blue',
                                    bd=0, compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="14.gif")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='blue',
                               bd=0, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="15.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='blue',
                               bd=0, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('user_id', 'name', 'adress', 'office', 'personal', 'eqipment', 'products', 'date'), height=15, show='headings')

        self.tree.column('user_id', width=50, anchor=tk.CENTER)
        self.tree.column('name', width=180, anchor=tk.CENTER)
        self.tree.column('adress', width=140, anchor=tk.CENTER)
        self.tree.column('office', width=140, anchor=tk.CENTER)
        self.tree.column('personal', width=140, anchor=tk.CENTER)
        self.tree.column('eqipment', width=140, anchor=tk.CENTER)
        self.tree.column('products', width=140, anchor=tk.CENTER)
        self.tree.column('date', width=140, anchor=tk.CENTER)



        self.tree.heading('user_id', text='Код')
        self.tree.heading('name', text='Наименование')
        self.tree.heading('adress', text='Адрес')
        self.tree.heading('office', text='Филиалы')
        self.tree.heading('personal', text='Персонал(чел)')
        self.tree.heading('eqipment', text='Стоимость(руб)')
        self.tree.heading('products', text='Объём(т)')
        self.tree.heading('date', text='Дата регистрации')

        self.tree.pack()

    def records(self, user_id, name, adress, office, personal, eqipment, products, date):
        self.db.insert_data(user_id, name, adress, office, personal, eqipment, products, date)
        self.view_records()

    def update_record(self, user_id, name, adress, office, personal, eqipment, products, date):
        self.db.cur.execute("""UPDATE users_v2 SET user_id=?, name=?, adress=?, office=?, personal=?, eqipment=?, products=?, date=? WHERE user_id=?""",
                            (user_id, name, adress, office, personal, eqipment, products, date, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users_v2""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM users_v2 WHERE user_id=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    # def search_records(self, user_id):
    #     user_id = ("%" + user_id + "%",)
    #     self.db.cur.execute("""SELECT * FROM users WHERE name LIKE ?""", user_id)
    #     [self.tree.delete(i) for i in self.tree.get_children()]
    #     [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def search_records(self, name):
        name = ('%' + name + '%',)
        self.db.cur.execute("""SELECT * FROM users_v2 WHERE name LIKE ?""", name)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]


    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()

class Child(tk.Toplevel):

    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить работника')
        self.geometry('400x420+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Код')
        label_description.place(x=40, y=25)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=110, y=25)

        label_name = tk.Label(self, text='Наименование')
        label_name.place(x=20, y=50)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=110, y=50)

        label_adress = tk.Label(self, text='Адрес')
        label_adress.place(x=30, y=75)
        self.entry_adress = ttk.Entry(self)
        self.entry_adress.place(x=110, y=75)

        label_office = tk.Label(self, text='Филиалы')
        label_office.place(x=30, y=100)
        self.entry_office = ttk.Entry(self)
        self.entry_office.place(x=110, y=100)

        label_personal = tk.Label(self, text='Персонал(чел)')
        label_personal.place(x=20, y=125)
        self.entry_personal = ttk.Entry(self)
        self.entry_personal.place(x=110, y=125)

        label_eqipment = tk.Label(self, text='Оборудование(руб)')
        label_eqipment.place(x=0, y=150)
        self.entry_eqipment = ttk.Entry(self)
        self.entry_eqipment.place(x=110, y=150)

        label_products = tk.Label(self, text='Объём(т)')
        label_products.place(x=30, y=175)
        self.entry_products = ttk.Entry(self)
        self.entry_products.place(x=110, y=175)

        label_date = tk.Label(self, text='Дата')
        label_date.place(x=40, y=200)
        self.entry_date = ttk.Entry(self)
        self.entry_date.place(x=110, y=200)


        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=230)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=230)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_name.get(),
                                                                       self.entry_adress.get(),
                                                                       self.entry_office.get(),
                                                                       self.entry_personal.get(),
                                                                       self.entry_eqipment.get(),
                                                                       self.entry_products.get(),
                                                                       self.entry_date.get()))


        self.grab_set()
        self.focus_set()

class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=210, y=230)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.entry_name.get(),
                                                                          self.entry_adress.get(),
                                                                          self.entry_office.get(),
                                                                          self.entry_personal.get(),
                                                                          self.entry_eqipment.get(),
                                                                          self.entry_products.get(),
                                                                          self.entry_date.get()))
        self.btn_ok.destroy()

class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

class DB:
    def __init__(self):
        self.con = sq.connect('notus')
        self.cur = self.con.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS users_v2 (
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        adress TEXT,
                        office TEXT,
                        personal INTEGER,
                        eqipment INTEGER,
                        products INTEGER,
                        date INTEGER
                        )""")
        self.con.commit()

    def insert_data(self, user_id, name, adress, office, personal, eqipment, products, date):
        self.cur.execute("""INSERT INTO users_v2( user_id, name, adress, office, personal, eqipment, products, date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                             ( user_id, name, adress, office, personal, eqipment, products, date))
        self.con.commit()

if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Промышленность")
    root.geometry("1150x450+300+200")
    root.resizable(False, False)
    root.mainloop()
