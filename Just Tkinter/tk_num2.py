import tkinter as tk

win = tk.Tk()
win.geometry("400x300+290+300")
win.resizable(False, False)
win.title("My second graрhic window")
photo = tk.PhotoImage(file = "fun.png")
win.iconphoto(True, photo)

def getting():
	value = name.get()
	value2 = password.get()
	
	if value and value2:
		
		print(value)
		print(value2)
		name.delete(0, "end")	
		password.delete(0, "end")

	else:
		print("Empty Value")

tk.Label(win, text = "Name: ", font = ('skia', 15)).grid(row = 0, column = 0, stick = "e")
name = tk.Entry(win)
name.grid(row = 0, column = 1, stick = "w")
tk.Button(win, text = "Submit", command = getting).grid(row = 0, column = 2, rowspan = 2, stick = 'ns')

tk.Label(win, text = "Password: ", font = ('skia', 15)).grid(row = 1, column = 0)
password = tk.Entry(win, show = "*")
password.grid(row = 1, column = 1, stick = "w")

win.mainloop()