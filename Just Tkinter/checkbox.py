from tkinter import *

root = Tk()
root.geometry("400x400")

var = StringVar()
var.set("On")

c = Checkbutton(root, text = "Check it!", variable = var, onvalue = 'On', offvalue = 'Off')
c.pack()

def penis():
	Label(root, text = var.get()).pack()

my_button = Button(root, text = "Penis", command = penis).pack()

root.mainloop()