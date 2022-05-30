from tkinter import *
from tkinter import messagebox
import psycopg2
import datetime as dt

root = Tk()

root.resizable(False, False)
root.title("NotePad From Maximka")

def Save():
    
    def Confirm():
        conn = None
        cur = None

        try:
            conn = psycopg2.connect(
                host = "localhost",
                dbname = "demo",
                user = "postgres",
                password = 256809,
                port = 5433)

            cur = conn.cursor()

            create_script = """CREATE TABLE IF NOT EXISTS files(
                    names varchar(255),
                    dates varchar(50))"""

            cur.execute(create_script)

            date = dt.datetime.now()
            str_date = str(date)
        
            getting = nameOfFile.get()
            file = open(getting + ".txt", "w+")
            file.write(fieldOfFile.get(1.0, END))
            messagebox.showinfo("INFO", "File has succsesfully saved")
            root2.destroy()
            fieldOfFile.delete(1.0, END)
            file.close()

            insert_script = "INSERT INTO files (names, dates) VALUES(%s, %s)"
            insert_value = (getting, str_date)

            cur.execute(insert_script, insert_value)  

            conn.commit()

        finally:
            if conn is not None:
                conn.close()

            if cur is not None:
                cur.close() 

    root2 = Tk()
    root2.resizable(False, False)

    File = Label(root2, text = "Name of File").pack()
    nameOfFile = Entry(root2)
    nameOfFile.pack()
    confirmButton = Button(root2, text = "Confirm", command = Confirm, width = 17).pack()

    root2.mainloop()

def Delete():
    fieldOfFile.delete(1.0, END)

def Open():
    conn = None
    cur = None

    try:

        conn = psycopg2.connect(
            host = "localhost",
            dbname = "demo",
            user = "postgres",
            password = 256809,
            port = 5433)

        root2 = Tk()
        root2.geometry("310x100")
        
        Label1 = Label(root2, text = "Write a File's Name").grid(row = 0, column = 0, pady = 10, padx = 10, columnspan = 2)   
        nameFile = Entry(root2, width = 20)
        nameFile.grid(row = 1, column = 0, padx = 15)

        OR = Label(root2, text = "Or").grid(row = 0, column = 1)

        Label2 = Label(root2, text = "Choose resent File").grid(row = 0, column = 2, pady = 10, padx = 10, columnspan = 2)

        cur = conn.cursor()

        select_script = """SELECT DISTINCT names FROM files 
        LIMIT 5"""

        cur.execute(select_script)
        files = []
        for i in cur.fetchall():
            for x in i:
                files.append(x + ".txt")

        clicked = StringVar()
        clicked.set(files[0])

        resent_files = OptionMenu(root2, clicked, *files)
        resent_files.grid(row = 1, column = 2)
        
        def ConfirmOpen():
            try:
                date = dt.datetime.now()
                str_date = str(date)
                getting = clicked.get()        

                insert_script = "INSERT INTO files VALUES(%s, %s)"
                insert_value = (getting[:-4], str_date)

                cur.execute(insert_script, insert_value)

                file = open(getting, "r+")
                fieldOfFile.insert(1.0, *file)
                root2.destroy()
                file.close()

            except:
                pass


        confirmButton = Button(root2, text = "OPEN", command = ConfirmOpen).grid(row = 2, column = 0, columnspan = 3, ipadx = 130)

        root2.mainloop()

        conn.commit()

    finally:
        if conn is not None:
            conn.close()

        if cur is not None:
            cur.close()

fieldOfFile = Text(root, width = 71, height = 12, font = (7))
fieldOfFile.grid(row = 0, column = 0, columnspan = 3)

SaveButton = Button(root, text = "SAVE", command = Save).grid(row = 1, column = 0, ipadx = 82, ipady = 10)
DeleteButton = Button(root, text = "DELETE ALL", command = Delete).grid(row = 1, column = 1, ipadx = 79, ipady = 10)
OpenButton = Button(root, text = "OPEN", command = Open).grid(row = 1, column = 2, ipadx = 88, ipady = 10)

root.mainloop()