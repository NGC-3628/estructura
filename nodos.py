def opcionesListas():
    while True:
        print("Selecciona una opcion\n1. mi primer recursion xd\n2. suma casi iterativa\n3. Hanoi towwers\n4. suma de multiplicacion")
        
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            single()
        elif opcion == "2":
            segundo()
        elif opcion == "3":
            tercero()
        elif opcion == "4":
            cuarto()
        else:
            print("opcion no validad")
            break

"""
there are 4 types of lists:
    1. single 
    2. double single 
    3. circular single
    4. double circular

    

"""

#class 

class Nodo:   # Molde de vagon
    def __init__(self, valor):  
        # self es una referencia de memoria, ademas esta variable indica que le pertenece a Nodo

        self.valor = valor      # Este vagon guarda su propio dato (su carga)
        self.next = None        # Este vagon define su propio gancho trasero (apunta a la nada al principio).
                                # la referencia de memoria 

class LinkedList:   # El centro de control o la estacion que maneja el tren
    def __init__(self):  
        # Aqui self representa a la estación especifica que estamos creando. Ademas, indico que me pertenece.
        
        self.head = None        # La estacion coloca su propio letrero de "INICIO".
                                # Al nacer, este letrero apunta a None porque no hay vagones amarrados todavía.

    def addFinal(self, valor):  #hay dos variables. la de self, que le recuerda a la maquina, esta esto, y la de valor que sera agregado.
        new = Nodo(valor)       # la variable new llama al modle del vagon. y le dice que habra un vagon con "producto" que se pondra desde afuera. 
        if self.head is None:   # Y si el apuntador apunta a la nada... Osea, y si no hay ningun vagon anclado a la estacion, 
            self.head = new     #la cabeza que me pertenece, apunta al nuevo vagon creado. 
            return              # termina de "conectar el vagon nuevo que llego".

        current = self.head                 #la variable current, recorre desde el princio y empieza a caminar hasta el final(?)

        while current.next is not None:     # mientras el "inspector de trenes" va al final del vagon y este no es el ultimo, 
            current = current.next          # va recorriendo vagones. Ademas, el inspector se detiene cuando el pauntador apunta a nada.(end While)

        current.next = new                  #el "inspector" engancgha ese next al nuevo vagon.

    def mostrar(self):                                  # la funciona recibe una variable que indica que eso le pertenece
        current = self.head                            #el "inspector" va hacia el ancla en la estacion y al primer vagon
        elementos = []                                  # los elementos estaran en un arreglo
        while current is not None:                      #mientras el "inspector" no este en el ultimo...
            elementos.append(str(current.valor))        # se agregan valores en este caso String con append.
            current = current.next                      #y el "inspector va recorriendo" de vagon en vagon
        
        print(" -> ".join(elementos) + "-> None")       # finalmente, se imprimen los elementos de cada vagon con el vagon en si.

lista = LinkedList()                                    # se llama a la clase.
#ista.addFinal("EH")                                      # se van agregando valores llamando a la funcion que agrega (pero como agrega si los agrega en mostrar?)
#lista.addFinal("Puto")
#lista.addFinal("Putote")
lista.mostrar()                                         # se llama a la funcion mostrar y los imprime.





class NodoDoble:   # Molde del vagón doble
    def __init__(self, valor):  
        # self es el vagón específico que está naciendo en la memoria RAM
        
        self.valor = valor      # Este vagón guarda su propio dato o producto (su carga)
        self.next = None        # Gancho delantero: apunta a la nada al principio (siguiente vagón)
        self.prev = None        # Gancho trasero: apunta a la nada al principio (vagón anterior)
                                # Ambos ganchos guardarán referencias de memoria automáticamente.

class DoublyLinkedList:   # El centro de control o la estación que maneja el tren doble
    def __init__(self):  
        # Aquí self representa a la estación específica que estamos creando.
        
        self.head = None        # La estación coloca su propio letrero de "INICIO".
                                # Al nacer, este letrero apunta a None porque no hay vagones amarrados todavía.

    def addFinal(self, valor):  
        new = NodoDoble(valor)   # Fabricamos el vagón doble en memoria y le metemos su "producto".
        
        if self.head is None:   # Si no hay ningún vagón anclado a la estación...
            self.head = new     # ...el letrero de INICIO apunta directamente al nuevo vagón.
            return              # Termina la función aquí porque ya quedó asegurado.

        # Si ya hay un tren, mandamos al inspector "current" a pararse en el primer vagón
        current = self.head                 

        # El inspector camina de vagón en vagón buscando el final
        while current.next is not None:     
            current = current.next          # Se detiene exactamente cuando está parado sobre el ÚLTIMO vagón.

        # --- AQUÍ OCURRE EL DOBLE ENLACE ---
        current.next = new                  # 1. El viejo último vagón estira su gancho 'next' y se conecta al nuevo.
        new.prev = current                  # 2. ¡EL PASO EXTRA! El nuevo vagón estira su gancho 'prev' hacia atrás y se conecta al viejo último.

    def mostrarAdelante(self):                                  
        current = self.head                             # El inspector va al primer vagón (head)
        elementos = []                                  
        while current is not None:                      # Mientras esté pisando un vagón real...
            elementos.append(str(current.valor))        # Copia el valor en su libreta temporal de Python
            current = current.next                      # Camina hacia ADELANTE usando el gancho '.next'
        
        print("Hacia adelante: " + " -> ".join(elementos) + " -> None")

    def mostrarAlReves(self):
        # Esta función SOLO se puede hacer gracias al superpoder de la lista doble
        if self.head is None:
            print("Lista vacía")
            return

        current = self.head
        # Primero, llevamos al inspector hasta el último vagón del tren
        while current.next is not None:
            current = current.next

        # Ahora que está en el final, el inspector camina HACIA ATRÁS
        elementos = []
        while current is not None:                      # Mientras esté pisando un vagón real...
            elementos.append(str(current.valor))        # Copia el valor en su libreta
            current = current.prev                      # ¡Camina hacia ATRÁS usando el gancho '.prev'!
        
        print("Hacia atrás:    " + " -> ".join(elementos) + " -> None")


# --- PRUEBA DEL TREN DOBLE ---
lista = DoublyLinkedList()                                    
lista.addFinal(10)                                      
lista.addFinal(20)
lista.addFinal(30)

# Probamos ambos recorridos
lista.mostrarAdelante()  # Imprime: Hacia adelante: 10 -> 20 -> 30 -> None
lista.mostrarAlReves()   # Imprime: Hacia atrás:    30 -> 20 -> 10 -> None