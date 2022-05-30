import tkinter as tk 
from PIL import ImageTk,Image

win  = tk.Tk()

def quit(): print("picture")

tk.Button(win, text = "Exit Program", command = quit).pack()
my_image = ImageTk.PhotoImage(Image.open("веселый дядя.jpg"))
my_label = tk.Label(image = my_image)
my_label.pack()

win.mainloop()