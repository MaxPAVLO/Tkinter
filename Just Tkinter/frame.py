from tkinter import *

root = Tk()

my_frame = LabelFrame(root, text = "This is my first frame-label", padx = 50, pady = 50)
my_frame.pack(padx = 10, pady = 10)

b = Button(my_frame, text =  "Don't click here")
b2 = Button(my_frame, text = "Or here")

b2.grid(row = 0, column = 1)
b.grid(row = 0, column = 0)

root.mainloop()