from matplotlib.pyplot import figure
from graph import *
from test_graph1 import G, F
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def show_plot(grafica):
    fig, ax = plt.subplots()
    Plot(grafica)

    canvas = FigureCanvasTkAgg(fig, master=consola_frame)
    canvas.draw()
    canvas_picture = canvas.get_tk_widget()
    canvas_picture.config(width=600, height=400)
    canvas_picture.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)


ventana = tk.Tk()
ventana.geometry('1000x600')
ventana.title('Versión 1')
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=10)
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)

#gráfica ejemplo step 3
graficaejemplo_frame = tk.LabelFrame(ventana, text='Gráfica Ejemplo')
graficaejemplo_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
graficaejemplo_frame.rowconfigure(0, weight=1)
graficaejemplo_frame.columnconfigure(0, weight=1)

boton1 = tk.Button(graficaejemplo_frame, text='Mostrar gráfica inventada', command=lambda: show_plot(G))
boton1.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#gráfica inventada step 3
graficainventada_frame = tk.LabelFrame(ventana, text='Gráfica inventada')
graficainventada_frame.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
graficainventada_frame.rowconfigure(0, weight=1)
graficainventada_frame.columnconfigure(0, weight=1)

boton2 = tk.Button(graficainventada_frame, text='Mostrar gráfica de ejemplo', command=lambda: show_plot(F))
boton2.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#consola
consola_frame = tk.LabelFrame(ventana, text='Gráficos')
consola_frame.grid(row=0, column=1, rowspan=2, padx=5, pady=5, sticky='nsew')
consola_frame.rowconfigure(0, weight=1)
consola_frame.columnconfigure(0, weight=1)


ventana.mainloop()