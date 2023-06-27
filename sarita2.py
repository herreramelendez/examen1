import tkinter as tk
from queue import Queue

cola = Queue()

def encolar_elemento():
    elemento = int(entry_elemento.get())
    if elemento == 0:
        return
    cola.put(elemento)
    entry_elemento.delete(0, tk.END)
    actualizar_tamano()

def descolar_elemento():
    if not cola.empty():
        cola.get()
        actualizar_tamano()
    else:
        resultado.set("La cola está vacía.")

def actualizar_tamano():
    tamano.set(f"Tamaño de la cola: {cola.qsize()}")

def verificar_vacia():
    if cola.empty():
        resultado.set("La cola está vacía.")
    else:
        resultado.set("La cola no está vacía.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Operaciones con Colas")
ventana.geometry("300x200")

# Variables
tamano = tk.StringVar()
resultado = tk.StringVar()

# Etiqueta y entrada para el elemento
label_elemento = tk.Label(ventana, text="Elemento:")
label_elemento.pack()

entry_elemento = tk.Entry(ventana)
entry_elemento.pack()

# Botón para encolar elemento
btn_encolar = tk.Button(ventana, text="Encolar", command=encolar_elemento)
btn_encolar.pack()

# Botón para descolar elemento
btn_descolar = tk.Button(ventana, text="Descolar", command=descolar_elemento)
btn_descolar.pack()

# Etiqueta para el tamaño de la cola
label_tamano = tk.Label(ventana, textvariable=tamano)
label_tamano.pack()

# Botón para verificar si la cola está vacía
btn_vacia = tk.Button(ventana, text="Verificar Vacía", command=verificar_vacia)
btn_vacia.pack()

# Etiqueta para el resultado
label_resultado = tk.Label(ventana, textvariable=resultado)
label_resultado.pack()

# Iniciar bucle de la ventana
ventana.mainloop()
