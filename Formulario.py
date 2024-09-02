#importa la biblioteca tkinter para crear interfaces graficas
import tkinter as tk
#importa el modulo messagebox para mostrar mensajes emergentes
from tkinter import messagebox

#limpia los campos de entrada
def lc():
    tbN.delete(0,tk.END)
    tbA.delete(0,tk.END)
    tbE.delete(0,tk.END)
    tbS.delete(0,tk.END)
    tbT.delete(0,tk.END)
    gen.set(0)

def bf():
    lc()
    
#guarda los datos ingresados
def gv():
    nom=tbN.get()
    ape=tbA.get()
    eda=tbE.get()
    est=tbS.get()
    tel=tbT.get()

    Gen=""
    if gen.get()==1:
        Gen="Hombre"
    elif gen.get==2:
        Gen="Mujer"        
#crea una cadena con todos los datos
    d="Nombre: "+nom+"\n"+"Apellido: "+ape+"\n"+"Edad: "+eda+"\n"+"Estatura: "+est+"\n"+"Telefono: "+tel+"\n"+"Genero: "+Gen+"\n"
#abre el archivo en modo de edicion y escribe los datos
    with open("C:/Users/perez/OneDrive/Documentos/tareas semestre 3/Programacion Avanzada/FormuPython/datosformulario.txt","a") as arc:
        arc.write(d+"\n\n")
#muestra un mensaje de exito al usuario
    messagebox.showinfo("Informacion", "Datos guardados con exito: \n\n"+d)
#limpia los campos de entrada despues de guardar
    tbN.delete(0,tk.END)
    tbA.delete(0,tk.END)
    tbE.delete(0,tk.END)
    tbS.delete(0,tk.END)
    tbT.delete(0,tk.END)
    gen.set(0)
#configuracion de la ventana principal
raiz=tk.Tk()
raiz.geometry("520x500")
raiz.title("Formulario Vr.01")
gen=tk.IntVar()
#creacion de etiquetas y campos de entrada
lbN=tk.Label(raiz, text="Nombre: ")
lbN.pack()
tbN=tk.Entry()
tbN.pack()
lbA=tk.Label(raiz, text="Apellido: ")
lbA.pack()
tbA=tk.Entry()
tbA.pack()
lbE=tk.Label(raiz, text="Edad: ")
lbE.pack()
tbE=tk.Entry()
tbE.pack()
lbS=tk.Label(raiz, text="Estatura: ")
lbS.pack()
tbS=tk.Entry()
tbS.pack()
lbT=tk.Label(raiz, text="Telefono: ")
lbT.pack()
tbT=tk.Entry()
tbT.pack()
lbG=tk.Label(raiz, text="Genero")
lbG.pack()
rbH=tk.Radiobutton(raiz, text="Hombre", variable=gen, value=1)
rbH.pack()
rbM=tk.Radiobutton(raiz, text="Mujer", variable=gen, value=2)
rbM.pack()
#botones para borrar y guardar
btnb=tk.Button(raiz, text="Borrar valores", command=bf)
btnb.pack()
btng=tk.Button(raiz, text="Guardar", command=gv)
btng.pack()

raiz.mainloop()
