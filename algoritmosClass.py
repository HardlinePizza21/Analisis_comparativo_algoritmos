import numpy as np
import time

class algoritmos:

    def __init__(self):
        self.operacionesSamuelSort = 0 


    # n es un arreglo con todos los tamaños de arreglo que va a a tener nuestro arreglo inventado.
    #tipoOrden es uns strin "random"/"sorted"/"reversed" que indica el tipo de orden que va a tener el arreglo
    # algoritmos es un arreglo que es ve asi [0,0,0,0,0] donde cada posicion representa un algoritmo
    # Y dependiendo del valor que tenga en esa posicion se va a realizar el analisis de ese algoritmo
    # TipoAnlisis es un string "tiempo"/"operaciones" que indica los datos que va a retornar la funcion
    #La funcion retorna un arreglo bidimensional con los datos de la forma
    # [ blublesort, bubbleSortImproved, insertionSort, samuelSort, timsort]
    #En caso de que el algoritmo no se haya seleccionado se retorna un arreglo vacio
    #

    def generarData(self, n, algoritmos, tipoAnalisis, tipoOrden):
        data = [[],[],[],[],[]] 
        for size in n:
            arr = self.generar_lista(size, tipoOrden)

            if algoritmos[0] == 1:
                data[0].append(self.bubble_sort(arr.copy(), tipoAnalisis))

            if algoritmos[1] == 1:
                data[1].append(self.bubble_sort_improved(arr.copy(), tipoAnalisis))
            
            if algoritmos[2] == 1:
                data[2].append(self.insertion_sort(arr.copy(), tipoAnalisis))

            if algoritmos[3] == 1:
                data[3].append(self.samuel_sort(arr.copy(), tipoAnalisis))
            
            if algoritmos[4] == 1:
                data[4].append(self.tim_sort(arr.copy(), tipoAnalisis))

        return data
    
    def generar_lista(self, size, type = "random"):
        if type == "random":
            return np.random.randint(0, 100, size)
        elif type == "sorted":
            return list(range(1,size+1))
        elif type == "reversed":
            lista = list(range(size, 0, -1))
            return lista
        else: 
            print("Tipo de lista no soportado: random, sorted, reversed")       
    
    #Recibe un numero entero > 10 que representa la cantidad maxima de datos que va a tener el arreglo
    #Retorna la cantidad de operaciones que se realizaron para organizar cada tamaño diferente de arreglo
    #Y retorna el tamaño de los diferentes arreglos oragnizados

    def tim_sort(self, arr, dataType):

        operations = 0
        inicio = time.time()
        n = len(arr)

        operations = n * np.log(n)

        sorted(arr) 

        tiempo =  time.time() - inicio;

        data = tiempo if dataType == "time" else operations

        return data       

    def bubble_sort(self, arr, dataType):
        n = len(arr)
        operations = 0
        inicio = time.time()
        
        for i in range(n):
            operations += 1
            for j in range(0, n-i-1):
                operations += 1
                if arr[j] > arr[j+1]:
                    self.swap(arr, j)
                    operations += 1

        tiempo =  time.time() - inicio;

        data = tiempo if dataType == "time" else operations

        return data
    
    def bubble_sort_improved(self, arr, dataType):
        n = len(arr)
        operations = 0
        inicio = time.time()
        swapped = False
        
        for i in range(n):
            operations += 1
            for j in range(0, n-i-1):
                operations += 1
                if arr[j] > arr[j+1]:
                    self.swap(arr, j)
                    swapped = True
                    operations += 1
            if swapped == False:
                break
            else:
                swapped = False

        tiempo =  time.time() - inicio;

        data = tiempo if dataType == "time" else operations

        return data

    def insertion_sort(self, arr,dataType):
        operations = 1
        inicio = time.time()
        for i in range(1, len(arr)):
            operations += 1
            key = arr[i]  

            j = i - 1
            while j >= 0 and key < arr[j]:
                operations += 1
                arr[j + 1] = arr[j]

                operations += 1
                j -= 1

            arr[j + 1] = key
    
        tiempo = time.time() - inicio

        data = tiempo if dataType == "time" else operations

        return data 

    def swap(self, arr, j):
        arr[j], arr[j+1] = arr[j+1], arr[j]

    def samuel_sort(self, arr, dataType):
        self.operacionesSamuelSort = 0
        size = len(arr)
        run = 32
        arrInsertions = []
        arrFinal = []
        inicio = time.time()    

        for i in range(0,size,run):
            self.operacionesSamuelSort += 1
            left = i 
            right = left + run
            if right > size:
                right = size
            
            arrInsertions = self.fusionar(arrInsertions, self.insertion_sort_samuelsort(arr, left, right))

        for i in range(len(arrInsertions)-1, -1,-1):
            self.operacionesSamuelSort += 1
            arrFinal = self.merge(arrFinal, arrInsertions[i])

    

        tiempo = time.time() - inicio

        data = tiempo if dataType == "time" else self.operacionesSamuelSort


        return data 

    def fusionar(self, arrBi, arrUni):
        for arr in arrBi:
            self.operacionesSamuelSort += 1
            if len(arr) == len(arrUni):
                nuevoArr = self.merge(arr, arrUni)
                arrBi = [elemento for elemento in arrBi if len(elemento) != len(arr)]
                return self.fusionar(arrBi, nuevoArr)
        arrBi.append(arrUni)
        return arrBi

    def insertion_sort_samuelsort(self, arr, left, right):
        fragmentoArr = []
        for i in range(left + 1, right):
            self.operacionesSamuelSort += 1
            key = arr[i]  

            j = i - 1
            while j >= left and key < arr[j]:
                self.operacionesSamuelSort += 1
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key
        fragmentoArr = arr[left:right]
        return fragmentoArr

    def merge(self, arrLeft, arrRight):
        result = []
        left_idx, right_idx = 0, 0

        while left_idx < len(arrLeft) and right_idx < len(arrRight):
            self.operacionesSamuelSort += 1
            if arrLeft[left_idx] < arrRight[right_idx]:
                result.append(arrLeft[left_idx])
                left_idx += 1
            else:
                result.append(arrRight[right_idx])
                right_idx += 1
        
        result.extend(arrLeft[left_idx:])
        result.extend(arrRight[right_idx:])
        
        return list(result)

    # Esta funcion esta aqui por si quiere comprobar que los arreglos si esten oredenados
    # def esta_ordenado(self, arr):
    #     # Iteramos sobre el arreglo desde el segundo elemento hasta el final
    #     for i in range(1, len(arr)):
    #         # Si el elemento actual es menor que el anterior, el arreglo no está ordenado
    #         if arr[i] < arr[i - 1]:
    #             return False
    #     # Si no se encontraron elementos desordenados, el arreglo está ordenado
    #     return True







