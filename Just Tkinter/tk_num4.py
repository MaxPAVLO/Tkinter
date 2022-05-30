import tkinter as tk 
import random
from tkinter import messagebox

win = tk.Tk()
win.geometry("500x550+140+150")
win.resizable(False, False)
win.title("Опрос")

def yes():
	messagebox.showinfo('', "Так и знал")
	quit()

def motionMouse(event):
	btn1.place(x = random.randint(0, 500), y = random.randint(0, 500))

label = tk.Label(win, text = "Ты даун?", font = ("Arial", 20)).pack()
btn1 = tk.Button(win, text = "Нет", font = ("Arial", 20))
btn1.place(x = 130, y = 100)
btn1.bind('<Enter>', motionMouse)
btn2 = tk.Button(win, text = "Да", command = 'yes', font = ("Arial", 20)).place(x = 270, y = 100)

win.mainloop()