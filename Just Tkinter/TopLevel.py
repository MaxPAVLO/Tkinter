from tkinter import *

root = Tk()
root.geometry("300x250+350+350")
root.resizable(False, False)
root.title("My first window")

def top():
	top = Toplevel() 
	top.geometry("300x250+350+350")
	top.resizable(False, False)
	top.title("Second window")
	Button(top, text = "Close window", command = top.destroy).pack()

Button(root, text = "New window", command = top).pack()

root.mainloop()