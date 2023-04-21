import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from tkinter import*
import numpy as np
from tkinter import ttk
from sympy import*

root=Tk()
fig, ax= plt.subplots()
root.geometry("850x950")

grado=StringVar()
selgrados=StringVar()
A=IntVar()
B=IntVar()
C=IntVar()
D=IntVar()
Lineal=StringVar()
Cuadratica=StringVar()
Cubica=StringVar()
liminferior=IntVar()
limsuperior=IntVar()
inicial=IntVar()
vlA=IntVar()
vlE=IntVar()

def graficar():
    ax.clear()
    ax.grid(axis="both",linestyle="dotted")
    x=np.arange(liminferior.get(),limsuperior.get(),0.1)
    ax.set_xlim([liminferior.get(),limsuperior.get()])
    ax.set_ylim([-35,35])
    y=A.get()*x*x*x+B.get()*x**2+C.get()*x+float(D.get())
    ax.plot(x,y)
    canvas.draw()

def exponencial():
    ax.clear()
    ax.grid(axis="both",linestyle="dotted")
    x=np.arange(liminferior.get(),limsuperior.get(),0.1)
    ax.set_xlim([liminferior.get(),limsuperior.get()])
    #ax.set_ylim(-50,50 )
    y=(vlA.get()*np.exp(vlE.get()*x))
    ax.plot(x,y)
    canvas.draw()

def raices():
    x=Symbol('x')
    y=A.get()*x*x*x+B.get()*x**2+C.get()*x+D.get()
    yderivada=y.diff(x)
    x=inicial.get()

    for i in range(0,12):
        yeval=eval(str(y))
        yderval=eval(str(yderivada))
        funcion=x-(yeval/yderval)
        x=funcion
    
    mostrarraiz.config(text=funcion)
    plt.axvline(funcion,-50,50,color="green",linestyle="dashed") 
    canvas.draw()

frame=Frame(root)
titulo=Label(frame,text="Funciones")
titulo.config(font=("Roboto",25))
titulo.grid(row=1,column=1,columnspan=4,padx=5,pady=5)
frame.pack()
canvas=FigureCanvasTkAgg(fig,master=frame)
canvas.get_tk_widget().grid(row=3,column=1,columnspan=4,padx=5,pady=5)

# Labels \\\\\\\

Ax=Label(frame,text="ax**3")
Ax.grid(row=8,column=1,padx=5,pady=5)
Bx=Label(frame,text="+ bx**2")
Bx.grid(row=8,column=2,padx=5,pady=5)
Cx=Label(frame,text="+ cx")
Cx.grid(row=8,column=3,padx=5,pady=5)
Dx=Label(frame,text="+ d")
Dx.grid(row=8,column=4,padx=5,pady=5)


# Entrys de coeficientes \\\\\\\

gradoslabel=Label(frame, text="////// COEFICIENTES DEL POLINOMIO //////")
gradoslabel.grid(row=7,column=1,columnspan=4,pady=10)

coeficienteA=Entry(frame,textvariable=A)
coeficienteA.grid(row=9,column=1,padx=5,pady=5)

coeficienteB=Entry(frame,textvariable=B)
coeficienteB.grid(row=9,column=2,padx=5,pady=5)   

coeficienteC=Entry(frame,textvariable=C)
coeficienteC.grid(row=9,column=3,padx=5,pady=5)

coeficienteD=Entry(frame,textvariable=D)
coeficienteD.grid(row=9,column=4,padx=5,pady=5)

expo=Label(frame, text="////// FUNCION EXPONENCIAL //////")
expo.grid(row=10,column=1,columnspan=4,pady=10)

CoeExpoA=Entry(frame,textvariable=vlA)
CoeExpoA.grid(row=11,column=1,padx=5,pady=5)

CoeExpoB=Entry(frame,textvariable=vlE)
CoeExpoB.grid(row=11,column=2,padx=5,pady=5)

# limites \\\\
    
labellimite=Label(frame,text="///// LIMITES /////")
labellimite.grid(row=12,column=1,columnspan=2,padx=5,pady=5)
    
inf=Label(frame,text="Limite Inferior:")
inf.grid(row=13,column=1,padx=5,pady=5)

datoinferior=Entry(frame,textvariable=liminferior)
datoinferior.grid(row=13,column=2,padx=5,pady=5)

sup=Label(frame,text="Limite Superior:")
sup.grid(row=14,column=1,padx=5,pady=5)

datosuperior=Entry(frame,textvariable=limsuperior)
datosuperior.grid(row=14,column=2,padx=5,pady=5)

#botones \\\\\\

botongraficas=Button(frame,text="Graficar",command=graficar)
botongraficas.grid(row=13,column=3,columnspan=2,pady=15,padx=5)

BoExpo=Button(frame,text="Graficar EXP",command=exponencial)
BoExpo.grid(row=11,column=3,columnspan=2,pady=15,padx=5)

    
# raices \\\\\

inraiz=Label(frame,text="///// RAIZ DE LA FUNCIÓN /////")
inraiz.grid(row=15,column=2,columnspan=2,padx=5,pady=5)

rz=Label(frame,text="VALOR INICIAL")
rz.grid(row=15,column=1,padx=5,pady=5)

raiz=Button(frame,text="Buscar Raiz",command=raices)
raiz.grid(row=16,column=2,padx=5,pady=5)

valin=Entry(frame,textvariable=inicial)
valin.grid(row=16,column=1,padx=5,pady=5)

mostrarraiz2=Label(frame,text="La Raiz Es:")
mostrarraiz2.grid(row=16,column=3,padx=5,pady=5)

mostrarraiz=Label(frame,text="")
mostrarraiz.grid(row=16,column=4,padx=5,pady=5)

#///

root.mainloop()