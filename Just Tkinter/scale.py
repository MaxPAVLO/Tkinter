from tkinter import *

root = Tk()
root.geometry("400x400")

vertical = Scale(root, from_ = 0, to = 400)
vertical_num2 = Scale(root, from_ = 0, to = 400)
vertical.grid(row = 0, column = 0)
vertical_num2.grid(row = 0, column = 1)

def clicked():
	root.geometry(str(vertical.get()) + "x" + str(vertical_num2.get()))

def dick():
	my_label = Label(root, text = horizontal.get())
	my_label.grid(row = 3, column = 0)

my_button = Button(root, text = "Click me!", command = clicked).grid(row = 0, column = 2, rowspan = 1, sticky = "NS")

horizontal = Scale(root, from_ = 0, to = 400, orient = HORIZONTAL)
horizontal.grid(row = 1, column = 0)

my_button_num2 = Button(root, text = "Me too!", command = dick).grid(row = 2, column = 0)

root.mainloop()