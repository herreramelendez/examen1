import tkinter as tk

def buscar_elemento():
    elemento = int(entry_elemento.get())
    if elemento == 0:
        return
    if elemento in arreglo:
        resultado.set(f"El elemento {elemento} se encuentra en el arreglo.")
    else:
        resultado.set(f"El elemento {elemento} no se encuentra en el arreglo.")

def agregar_elemento():
    elemento = int(entry_elemento.get())
    if elemento == 0:
        return
    arreglo.append(elemento)
    entry_elemento.delete(0, tk.END)

# Crear ventana
ventana = tk.Tk()
ventana.title("Búsqueda Lineal")
ventana.geometry("300x200")

# Variables
arreglo = []
resultado = tk.StringVar()

# Etiqueta y entrada para el elemento
label_elemento = tk.Label(ventana, text="Elemento:")
label_elemento.pack()

entry_elemento = tk.Entry(ventana)
entry_elemento.pack()

# Botón para agregar elemento
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento)
btn_agregar.pack()

# Botón para buscar elemento
btn_buscar = tk.Button(ventana, text="Buscar", command=buscar_elemento)
btn_buscar.pack()

# Etiqueta para el resultado
label_resultado = tk.Label(ventana, textvariable=resultado)
label_resultado.pack()

# Iniciar bucle de la ventana
ventana.mainloop()
