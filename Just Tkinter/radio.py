from tkinter import *

root = Tk()

MODES = [
	("Pepperoni", "Pepperoni"),
	("Cheese", "Cheese"),
	("Mushroom", "Mushroom"),
	("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")
for text, modes in MODES:
	Radiobutton(root, text = text, variable = pizza, value = modes).pack(anchor = W)

def clicked(value):
	my_label = Label(root, text = value).pack()

my_btn = Button(root, text = "Click me!", command = lambda: clicked(pizza.get())).pack()

root.mainloop()