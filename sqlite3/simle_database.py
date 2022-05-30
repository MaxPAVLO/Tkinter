from tkinter import *
import sqlite3

#Присоединение базы данных
db = sqlite3.connect('server_num2.db')
sql = db.cursor()

#Создание базы данных, если она не существует
sql.execute("""CREATE TABLE IF NOT EXISTS addresses_num2(
	first_name TEXT,
	last_name TEXT,
	adress TEXT,
	city TEXT,
	state TEXT,
	zipcode INTEGER
	)""")


#Создание графического окна
root = Tk()

#Сохранения изменений
def save():

	db = sqlite3.connect('server_num2.db')
	sql = db.cursor()

	sql.execute("""UPDATE addresses_num2 SET
		first_name = :first,
		last_name = :last,
		adress = :adress,
		city = :city,
		state = :state,
		zipcode = :zipcode

		WHERE oid = :oid""",
		{
			'first': data_name_changer.get(),
			'last': data_surname_changer.get(),
			'adress': data_adress_changer.get(),
			'city': data_city_changer.get(),
			'state': data_state_changer.get(),
			'zipcode': data_zipcode_changer.get(),
			'oid': delete_box.get()
		})

	data_name_changer.delete(0, END)
	data_surname_changer.delete(0, END)
	data_adress_changer.delete(0, END)
	data_city_changer.delete(0, END)
	data_state_changer.delete(0, END)
	data_zipcode_changer.delete(0, END)

	editor.destroy()

	db.commit()
	db.close()

#Изменение записей
def update():
	
	db = sqlite3.connect('server_num2.db')
	sql = db.cursor()

	global editor
	editor = Tk()

	sql.execute("SELECT * from addresses_num2 WHERE oid = " + delete_box.get())
	records = sql.fetchall()

	global data_name_changer
	global data_surname_changer
	global data_adress_changer
	global data_city_changer
	global data_state_changer
	global data_zipcode_changer

	your_name_changer = Label(editor, text = "Name").grid(row = 0, column = 0)
	your_surname_changer = Label(editor, text = "Surname").grid(row = 1, column = 0)
	your_adress_changer = Label(editor, text = "Adress").grid(row = 2, column = 0)
	your_city_changer = Label(editor, text = "City").grid(row = 3, column = 0)
	your_state_changer = Label(editor, text = "State").grid(row = 4, column = 0)
	your_zipcode_changer = Label(editor, text = "Zipcode").grid(row = 5, column = 0)

	data_name_changer = Entry(editor, width = 30)
	data_surname_changer = Entry(editor, width = 30)
	data_adress_changer = Entry(editor, width = 30)
	data_city_changer = Entry(editor, width = 30)
	data_state_changer = Entry(editor, width = 30)
	data_zipcode_changer = Entry(editor, width = 30)

	data_name_changer.grid(row = 0, column = 1)
	data_surname_changer.grid(row = 1, column = 1)
	data_adress_changer.grid(row = 2, column = 1)
	data_city_changer.grid(row = 3, column = 1)
	data_state_changer.grid(row = 4, column = 1)
	data_zipcode_changer.grid(row = 5, column = 1)

	save_btn = Button(editor, text = "Save Records", command = save)
	save_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 137)

	for record in records:
		data_name_changer.insert(0, record[0])
		data_surname_changer.insert(0, record[1])
		data_adress_changer.insert(0, record[2])
		data_city_changer.insert(0, record[3])
		data_state_changer.insert(0, record[4])
		data_zipcode_changer.insert(0, record[5])

	root.mainloop()

	db.commit()
	db.close()

#Функция удаления
def delete():
	
	db = sqlite3.connect('server_num2.db')
	sql = db.cursor()

	sql.execute("DELETE from addresses_num2 WHERE oid = " + delete_box.get())

	delete_box.delete(0, END)

	db.commit()
	db.close()


#Вывод записей из базы данных
def query():
	
	db = sqlite3.connect('server_num2.db')
	sql = db.cursor()

	sql.execute("SELECT *, oid FROM addresses_num2")
	records = sql.fetchall()

	print_records = ''
	for record in records[-1]:
		print_records += str(record) + "\n"

	Label(root, text = print_records).grid(row = 8, columnspan = 2)

	db.commit()
	db.close()

#Добавление записей в базу данных
def submit():

	db = sqlite3.connect('server_num2.db')
	sql = db.cursor()

	sql.execute("""CREATE TABLE IF NOT EXISTS addresses_num2(
	first_name TEXT,
	last_name TEXT,
	adress TEXT,
	city TEXT,
	state TEXT,
	zipcode INTEGER
	)""")
	
	
	#Даем значения переменным
	sql.execute("INSERT INTO addresses_num2 VALUES(:data_name, :data_surname, :data_adress, :data_city, :data_state, :data_zipcode)",
			{
				'data_name': data_name.get(),
				'data_surname': data_surname.get(),
				'data_adress': data_adress.get(),
				'data_city': data_city.get(),
				'data_state': data_state.get(),
				'data_zipcode': data_zipcode.get()
			})

	data_name.delete(0, "end")
	data_surname.delete(0, "end")
	data_adress.delete(0, "end")
	data_city.delete(0, "end")
	data_state.delete(0, "end")
	data_zipcode.delete(0, "end")

	db.commit()
	db.close()

#Записи и поля ввода
your_name = Label(root, text = "Name").grid(row = 0, column = 0)
your_surname = Label(root, text = "Surname").grid(row = 1, column = 0)
your_adress = Label(root, text = "Adress").grid(row = 2, column = 0)
your_city = Label(root, text = "City").grid(row = 3, column = 0)
your_state = Label(root, text = "State").grid(row = 4, column = 0)
your_zipcode = Label(root, text = "Zipcode").grid(row = 5, column = 0)

data_name = Entry(root, width = 30)
data_surname = Entry(root, width = 30)
data_adress = Entry(root, width = 30)
data_city = Entry(root, width = 30)
data_state = Entry(root, width = 30)
data_zipcode = Entry(root, width = 30)

data_name.grid(row = 0, column = 1)
data_surname.grid(row = 1, column = 1)
data_adress.grid(row = 2, column = 1)
data_city.grid(row = 3, column = 1)
data_state.grid(row = 4, column = 1)
data_zipcode.grid(row = 5, column = 1)

#Кнопочки
submit_button = Button(root, text = "Add Record To Database", command = submit)
submit_button.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 110)

query_button = Button(root, text = "Show Records", command = query)
query_button.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 137)

delete_btn = Button(root, text = "Delete Records", command = delete)
delete_btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 135)

update_btn = Button(root, text = "Update Records", command = update)
update_btn.grid(row = 11, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 132)

delete_box = Entry(root, width = 30)
delete_box.grid(row = 9, column = 1)

delete_box_label = Label(root, text = "ID")
delete_box_label.grid(row = 9, column = 0)

root.mainloop()

db.commit()
db.close()
