import tkinter as tk

arreglo = []

def agregar_elemento():
    elemento = int(entry_elemento.get())
    if elemento == 0:
        return
    arreglo.append(elemento)
    entry_elemento.delete(0, tk.END)
    actualizar_informacion()

def ordenar_arreglo():
    n = len(arreglo)
    for i in range(n-1):
        for j in range(n-1-i):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
    actualizar_informacion()

def actualizar_informacion():
    tamano.set(f"Tamaño del arreglo: {len(arreglo)}")
    maximo.set(f"Elemento de mayor valor: {max(arreglo)}")
    minimo.set(f"Elemento de menor valor: {min(arreglo)}")

# Crear ventana
ventana = tk.Tk()
ventana.title("Operaciones con Arreglos")
ventana.geometry("300x200")

# Variables
tamano = tk.StringVar()
maximo = tk.StringVar()
minimo = tk.StringVar()

# Etiqueta y entrada para el elemento
label_elemento = tk.Label(ventana, text="Elemento:")
label_elemento.pack()

entry_elemento = tk.Entry(ventana)
entry_elemento.pack()

# Botón para agregar elemento
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento)
btn_agregar.pack()

# Botón para ordenar el arreglo
btn_ordenar = tk.Button(ventana, text="Ordenar", command=ordenar_arreglo)
btn_ordenar.pack()

# Etiqueta para el tamaño del arreglo
label_tamano = tk.Label(ventana, textvariable=tamano)
label_tamano.pack()

# Etiqueta para el elemento de mayor valor
label_maximo = tk.Label(ventana, textvariable=maximo)
label_maximo.pack()

# Etiqueta para el elemento de menor valor
label_minimo = tk.Label(ventana, textvariable=minimo)
label_minimo.pack()

# Iniciar bucle de la ventana
ventana.mainloop()
