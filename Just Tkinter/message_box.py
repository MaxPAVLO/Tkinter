from tkinter import *
from tkinter import messagebox

root = Tk()

def clicked():

# showinfo, showwarning, showerror, askquestion, askokcansel, askyesno	

	response = messagebox.askyesno("This is my Popup", "Hello wolrld!")
	if response == 1:
		my_label = Label(root, text = "You clicked yes!").pack()

	else:
		my_label = Label(root, text = "You clicked no!").pack()

my_btn1 = Button(root, text = "Popup", command = clicked).pack()

root.mainloop()