from tkinter import *

root  = Tk()
root.geometry("400x400")

days = [
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday"
]

clicked = StringVar()
clicked.set(days[0])

my_menu = OptionMenu(root, clicked, *days)
my_menu.pack()

def click():
	my_label = Label(root, text = clicked.get())
	my_label.pack()

my_button = Button(root, text = "Click!", command = click).pack()

root.mainloop()