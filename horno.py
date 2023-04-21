import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

root = Tk()
root.geometry("850x750")
root.title("Control de temperatura")
fig, ax = plt.subplots()

def graficar():
    ax.clear()
    x = np.arange(0, int(temp_act.get()))
    y = (x**2/4.5)
    ax.plot(x, y)
    max_y = np.max(y)
    min_y = np.min(y)
    ax.set_xlabel("Abertura de válvula")
    ax.set_ylabel("Temperatura Actual")

    if max_y > int(tempMax.get()):
        messagebox.showwarning("Alerta", f"La temperatura es muy elevada.")
    if min_y > int(tempMin.get()):
        messagebox.showwarning("Alerta",f'La temperatura es muy baja para fundir el hierro')

    valor_maximo.set(f"Temperatura actual: {max_y}")
    canvas.draw()

frame = Frame(root)
frame.pack()

ax.set_xlabel("Abertura de válvula")
ax.set_ylabel("Temperatura Actual")
titulo = Label(frame, text="Control de temperatura de Horno\nFundición de hierro", font=("Britannic",20,"bold"))
titulo.pack(padx=10, pady=10, side=TOP)

izq = Frame(frame)
izq.pack(side=LEFT)

temp_min = Label(izq, text="Temperatura Mínima", font=("Roboto",15,"bold"))
temp_min.pack(padx=3, pady=3)
tempMin = StringVar()
Ltempmin = ttk.Combobox(izq, width=10, values=["0", "5", "10", "15", "20", "25", "30"], textvariable=tempMin)
Ltempmin.pack(padx=3, pady=3)

temp_max = Label(izq, text="Temperatura Máxima", font=("Roboto",15,"bold"))
temp_max.pack(padx=3, pady=3)
tempMax = StringVar()
Ltempmax = ttk.Combobox(izq, width=10, values=["1000", "1100", "1200", "1300", "1400", "1500", "1600"], textvariable=tempMax)
Ltempmax.pack(padx=3, pady=3)

tempAct = Label(izq, text="% de Abertura.", font=("Roboto",15))
tempAct.pack(padx=4, pady=4)
temp_act = StringVar()
Etemp = Entry(izq, textvariable=temp_act)
Etemp.pack(padx=4, pady=4)

Bgrafica = Button(izq, text="Graficar", command=graficar)
Bgrafica.pack(padx=5, pady=5)

valor_maximo = StringVar()
etiqueta_valor_maximo = Label(frame, textvariable=valor_maximo, font=("Roboto", 15))
etiqueta_valor_maximo.pack(padx=5, pady=10, side=TOP)

barraProgreso = ttk.Progressbar(root, orient="horizontal", length=500)
barraProgreso.pack(padx=40, pady=40)

def progreso():
    temp_min = int(tempMin.get())
    temp_max = int(tempMax.get())
    stop_value = int(temp_act.get())

    for temp_actual in range(temp_min, temp_max+1):
            time.sleep(0.1)
            barraProgreso['value'] = temp_actual
            barraProgreso.update()
            if temp_actual >= stop_value:
             break

ETMIN = Label(root, text="Temp. Min")
ETMIN.place(relx=0.18, rely=0.91)

ETMAX = Label(root, text="Temp. Max")
ETMAX.place(relx=0.75, rely=0.91)

Bbarra = Button(root, text="Mostrar progreso", command=progreso)
Bbarra.place(relx=0.46, rely=0.915)

canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=True)

root.mainloop()