def opcionesRecursion():
    while True:
        print("Selecciona una opcion\n1. mi primer recursion xd\n2. suma casi iterativa\n3. Hanoi towwers\n4. suma de multiplicacion")
        
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            ejecutarFactorial()
        elif opcion == "2":
            suma()
        elif opcion == "3":
            ejecutar_hanoi()
        elif opcion == "4":
            ejecutarMultiplicacionSinOperand()
        else:
            print("opcion no validad")
            break



def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def ejecutarFactorial():
    n = int(input("Ingresa un número: "))
    print(f"El factorial es {factorial(n)}")








def suma(n, acumulado):
    if n > 15:
        return acumulado

    return suma(n + 1, n + acumulado)

resultado = suma(1, 2)
print(resultado)







def hanoi_recursive(n):
    if n == 1: 
        return 1
    else:
        return (hanoi_recursive(n - 1)* 2) + 1

def ejecutar_hanoi():
    n = int(input("¿Cuantas piezas tendra la torre? "))
    resultado = hanoi_recursive(n)
    print(f"Los movimientos a lograr son {resultado} para completar esta torre.")






def multiplicacionSinOperador(a, b):
    if b == 1:
        return a
    
    return (a + multiplicacionSinOperador(a, b - 1))

def ejecutarMultiplicacionSinOperand():
    a = int(input("Ingresa el numero a multiplicar: "))
    b = int(input("Ingresa por cuantas veces sera \"sumado\": "))
    
    resultado = multiplicacionSinOperador(a, b)
    
    print(f"El resultado de {a} x {b} es: {resultado}\n")





def euclidesIterativo(n, m):
    while n!= 0:
        b = m % n
        m = n
        n = b
    
    return m

def euclidesRecursivo(a, b):
    if b == 0:
        return a
    return euclides_recursivo(b, a % b)


def ejecutarEuclides():
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))

    print("Iterativo:", euclidesIterativo(a, b))
    print("Recursivo:", euclidesRecursivo(a, b))
