import tkinter as tk

word = input("")

count = 0
def counter():
	global count
	count += 1
	btn['text'] = f"Счетчик: {count}"

def clicked():
    label2 = tk.Label(win, text="Я же просил...",
    						bg = "#8442D6",
    						font = ("Arial", 25, "bold"))
    label2.grid(row = 15, column = 5)

win = tk.Tk()
win.title("Мое первое графическое окно")
win.resizable(True, True)

photo = tk.PhotoImage(file = "fun.png")
win.iconphoto(True, photo)

win.minsize(200, 300)
win.maxsize(450, 350)

win.config(bg = "#8442D6")

label = tk.Label(win, text = word, 
						font = ("Arial", 20, "bold"),
						bg = "#8442D6")

btn = tk.Button(win, text = f"Счетчик: {count}",
							command = counter,
							bg = "black",
							fg = "red")

btn2 = tk.Button(win, text = "Не нажимать",
							command = clicked)

btn2.grid(row = 15, column = 4)
btn.grid(row = 0, column = 1)
label.grid(row = 0, column = 0)

win.geometry("300x200+650+290")
win.mainloop()