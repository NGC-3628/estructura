from collections import deque


def opcionesColas():
    while True:
        
        print("Selecciona el tipo de cola que quieres probar\n1. normal\n2.normal con deque() function\n3. customized\n4. el juego xd")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            cola_lista()
        elif opcion == "2":
            cola_deque()
        elif opcion == "3":
            cola_personalizada()
        elif opcion == "4":
            juego_clientes()
        elif opcion == "5":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")



def cola_lista():
    q = []

    q.append(1)
    q.append(10)
    q.append(100)
    q.append(1000)
    q.append(10000)

    out = q.pop(0)

    print(f"El elemento {out} fue eliminado.")
    print(q)

def cola_deque():
    q = deque()

    q.append(1)
    q.append(10)
    q.append(100)
    q.append(1000)
    q.append(10000)

    print(q)

    q.popleft()

    print(q)



class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return None

    def seeElements(self):
        if not self.isEmpty():
            return self.items[0]
        return None

    def size(self):
        return len(self.items)


def cola_personalizada():
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print("Primer elemento:", q.seeElements())

    q.enqueue(6)

    print(q.items)



def juego_clientes():
    cola = deque()

    while True:
        nombre = input("Nombre del cliente (escribe 'fin' para terminar): ")

        if nombre.lower() == "fin":
            break

        cola.append(nombre)

    print("\nAtendiendo clientes...")

    while cola:
        cliente = cola.popleft()
        print(f"Se está atendiendo a {cliente}")

    print("Todos los clientes han sido atendidos.")
