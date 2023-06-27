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
    for i in range(n):
        max_index = i
        for j in range(i+1, n):
            if arreglo[j] > arreglo[max_index]:
                max_index = j
        arreglo[i], arreglo[max_index] = arreglo[max_index], arreglo[i]
    actualizar_informacion()

def actualizar_informacion():
    tamano.set(f"Tamaño del arreglo: {len(arreglo)}")
    promedio.set(f"Promedio del arreglo: {sum(arreglo)/len(arreglo):.2f}")
    suma.set(f"Suma de los elementos: {sum(arreglo)}")

# Crear ventana
ventana = tk.Tk()
ventana.title("Operaciones con Arreglos")
ventana.geometry("300x200")

# Variables
tamano = tk.StringVar()
promedio = tk.StringVar()
suma = tk.StringVar()

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

# Etiqueta para el promedio del arreglo
label_promedio = tk.Label(ventana, textvariable=promedio)
label_promedio.pack()

# Etiqueta para la suma de los elementos del arreglo
label_suma = tk.Label(ventana, textvariable=suma)
label_suma.pack()

# Iniciar bucle de la ventana
ventana.mainloop()
