import tkinter as tk 
from pyowm import OWM
from pyowm.utils.config import get_default_config

def getting():

	try:

		value = city.get()
		value2 = answer.get()
		if value:

			answer.delete(0, "end")
			owm = OWM('c2a7abaeee27d5b6bc639039d38d3ab2')
			mgr = owm.weather_manager()
			config_dict = get_default_config()
			config_dict['language'] = 'ru'
			observation = mgr.weather_at_place(value)
			w = observation.weather
			temp = w.temperature("celsius")['temp']
			toch = w.detailed_status

			amswer = "Температура в районе: " +  str(temp) + ", " + toch
			answer.insert(0, amswer)
			city.delete(0, "end")

		elif value2:
			answer.delete(0, "end")
			answer.insert(0, "Вводите только в верхнюю строчку")

		else:
			answer.insert(0, "Введите что нибудь")

	except:
		city.delete(0, "end")
		answer.insert(0, "Чего?")

win = tk.Tk()
win.geometry("400x300+290+300")
win.resizable(False, False)
win.config(bg = "orange")
win.title("Weather")
photo = tk.PhotoImage(file = "cloud.png")
win.iconphoto(True, photo)

label_num1 = tk.Label(win, text = "Введите ниже название города:", font = ("skia", 12), 
																bg = "orange",
																fg = "white",
																width = 30,
																height = 5).pack()
city = tk.Entry(win, width = 37)
city.pack()

label_num2 = tk.Label(win, text = "Введите ниже название города:", font = ("skia", 12), bg = "orange", fg = "orange").pack()

tk.Button(win, text = "Посмотреть погоду", width = 20, command = getting).pack()

label_num3 = tk.Label(win, text = "Введите ниже название города:", font = ("skia", 12), bg = "orange", fg = "orange").pack()

answer = tk.Entry(win, width = 37)
answer.pack()

win.mainloop()