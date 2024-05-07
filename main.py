import tkinter as tk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from algoritmosClass import algoritmos

class dataViewer:
    
    def __init__(self):
        #Obejtos logicos
        self.alg = algoritmos()
        self.ventana = tk.Tk()
        self.opcionFuncion = tk.IntVar()
        self.opcionDataType = tk.IntVar()
        self.alg1 = tk.IntVar()    
        self.alg2 = tk.IntVar()    
        self.alg3 = tk.IntVar()    
        self.alg4 = tk.IntVar()    
        self.alg5 = tk.IntVar()    
        
        #Elementos de la interfaz

        #Elementos para decidir el tipo de datos a mostrar
        self.functionLayout = tk.Frame(self.ventana)
        self.labelFunction = tk.Label(self.functionLayout, text="Selecciona los datos a extraer: ")
        self.timeButton = tk.Radiobutton(self.functionLayout, text="Tiempo(n)", variable=self.opcionFuncion, value=1, command=lambda: self.seleccionar_boton(1))
        self.opertationsButton = tk.Radiobutton(self.functionLayout, text="Operacione(n)", variable=self.opcionFuncion, value=2, command=lambda: self.seleccionar_boton(2))

        #Elementos para seleccionar los algoritmos a los que se les realizara la prueba
        self.algoritmoLayout = tk.Frame(self.ventana)
        self.labelAlgChoice = tk.Label(self.algoritmoLayout, text="Selecciona los algoritmos a comparar: ")
        self.bubbleSortButton = tk.Checkbutton(self.algoritmoLayout, text="Bubble Sort", variable=self.alg1)
        self.bubbleSortImprovedButton = tk.Checkbutton(self.algoritmoLayout, text="Bubble Sort Mejorado", variable=self.alg2)
        self.insertionSortButton = tk.Checkbutton(self.algoritmoLayout, text="Insertion Sort", variable=self.alg3)
        self.samuelSortButton = tk.Checkbutton(self.algoritmoLayout, text="SamuelSort", variable=self.alg4)
        self.timSortButton = tk.Checkbutton(self.algoritmoLayout, text="TimSort", variable=self.alg5)

        #Elementos para decidir el orden de las listas que se van a evaluar
        self.dataTypeLayotu = tk.Frame(self.ventana)
        self.labelType = tk.Label(self.dataTypeLayotu, text="Selecciona el tipo de listas a organizar: ")
        self.sortedButton = tk.Radiobutton(self.dataTypeLayotu, text="Sorted", variable=self.opcionDataType, value=1, command=lambda: self.seleccionar_boton_dataType(1))
        self.reversedButton = tk.Radiobutton(self.dataTypeLayotu, text="Reversed", variable=self.opcionDataType, value=2, command=lambda: self.seleccionar_boton_dataType(2))
        self.randomButton = tk.Radiobutton(self.dataTypeLayotu, text="Random", variable=self.opcionDataType, value=3, command=lambda: self.seleccionar_boton_dataType(3))

        #Seleccion del n mas grande
        self.deslizador = tk.Scale(self.ventana, from_=10, to=1000, orient=tk.HORIZONTAL, resolution=10, command=self.seleccionar_numero)
        self.etiqueta_numero = tk.Label(self.ventana, text="Seleccione la cantidad de datos a comparar: 0")

        #Opciones
        self.optLayout = tk.Frame(self.ventana)
        self.limpiarGrafico = tk.Button(self.optLayout, text="Limpiar Gráfico", command=self.clear_graph)
        self.limpiarGrafico.config(state="disabled")
        self.crearGraficoButton = tk.Button(self.optLayout, text="Mostrar Grafica", command=self.crear_grafico)
        self.configurarVentana()

    def seleccionar_boton(self, boton):
        self.opcionFuncion.set(boton)

    def seleccionar_boton_dataType(self,boton):
        self.opcionDataType.set(boton)
    
    def seleccionar_boton_alg(self):
        seleccionados = [self.alg1.get(), self.alg2.get(), self.alg3.get(), self.alg4.get(), self.alg5.get()]
        print("Seleccione la cantidad de datos a comparar: ", seleccionados)


    #Crea una funcion que manda a llamar el metodo de algortimos que retorna los datos, a este metodo hay que pasarle
    #El tamaño de los datos maximos, un arreglo el arreglo de las opciones de la forma:
    # [BubbleSort, BubbleSortMejorado, InsertionSort, samuelSort], y el tipo de analisis que se quiere hacer tiempo/operaciones
    #Tambien como se quieren los datos, reversed,sorted o random
    # def generarGrafico(self):



    def configurarVentana(self):
        #Elementos generales
        self.ventana.geometry("1000x1000")
        self.ventana.title("trabajo de estructura de datos")   

        #Primer formulario
        self.labelFunction.pack()
        self.timeButton.pack(side=tk.LEFT)  
        self.opertationsButton.pack(side=tk.LEFT)
        self.functionLayout.pack()

        #Segundo formulario
        self.algoritmoLayout.pack()
        self.labelAlgChoice.pack()
        self.bubbleSortButton.pack(side=tk.LEFT)
        self.bubbleSortImprovedButton.pack(side=tk.LEFT)
        self.insertionSortButton.pack(side=tk.LEFT)
        self.samuelSortButton.pack(side=tk.LEFT)
        self.timSortButton.pack(side=tk.LEFT)

        #tercer formulario
        self.dataTypeLayotu.pack()
        self.labelType.pack()
        self.sortedButton.pack(side=tk.LEFT)
        self.reversedButton.pack(side=tk.LEFT)
        self.randomButton.pack(side=tk.LEFT)

        self.deslizador.pack()
        self.etiqueta_numero.pack()


        self.optLayout.pack()
        self.limpiarGrafico.pack(side=tk.LEFT)
        self.crearGraficoButton.pack(side=tk.LEFT)
        self.ventana.mainloop() 

    def seleccionar_numero(self, event):
        valor = self.deslizador.get()
        self.etiqueta_numero.config(text=f"Seleccione la cantidad de datos a comparar: {valor}")

    def crear_grafico(self):
        #Pulir toda informacion para mandarla a alg.generarData()
        #Recibir lo que retorna esa funcion y mostrarlos en un grafico dependiendo de lo que se reciba 

        self.crearGraficoButton.config(state="disabled")
        self.limpiarGrafico.config(state="normal")


        ArregloDeNs = list(range(10,self.deslizador.get() + 1,10))
        AlgortimosElegidos = [self.alg1.get(), self.alg2.get(), self.alg3.get(), self.alg4.get(), self.alg5.get()]
        tipoDeAnalisis = "time" if self.opcionFuncion.get() == 1 else "operations"
        tipoDeOrden = "sorted" if self.opcionDataType.get() == 1 else("reversed" if self.opcionDataType.get() == 2 else("random"))

        data = self.alg.generarData(ArregloDeNs, AlgortimosElegidos, tipoDeAnalisis, tipoDeOrden)

        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        
        if len(data[0]) > 0:
            self.ax.plot(ArregloDeNs, data[0], color='blue', label="Bubble Sort")
        if len(data[1]) > 0:
            self.ax.plot(ArregloDeNs, data[1], color='red', label="Bubble Sort Mejorado")
        if len(data[2]) > 0:
            self.ax.plot(ArregloDeNs, data[2], color='green', label="Insertion Sort")
        if len(data[3]) > 0:
            self.ax.plot(ArregloDeNs, data[3], color='yellow', label="SamuelSort")
        if len(data[4]) > 0:
            self.ax.plot(ArregloDeNs, data[4], color='black', label="TimSort")

        self.ax.legend()
        self.ax.set(xlabel='Tamaño del arreglo', ylabel=tipoDeAnalisis)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.ventana)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    def clear_graph(self):
        self.canvas.get_tk_widget().destroy()
        self.crearGraficoButton.config(state="normal")
        self.limpiarGrafico.config(state="disabled")



     

    



obj1 = dataViewer()        



