import time
from recursividad.nombre import limpiar, pausa, separador



def euclidesIterativo(a, b):
    
    contadorCiclos = 0
    inicio = time.perf_counter()

    while b != 0:
        residuo = a % b
        a = b          
        b = residuo    
        contadorCiclos += 1
    
    fin = time.perf_counter()
    tiempo_ms = (fin - inicio) * 1000

    return a, tiempo_ms, contadorCiclos







def euclidesRecursivo(a, b):

    euclidesRecursivo.contador += 1

    if b == 0:
        return a
    return euclidesRecursivo(b, a % b)


def ejecutarEuclides(a, b):

    euclidesRecursivo.contador = 0  
    
    inicio = time.perf_counter()
    resultado = euclidesRecursivo(a, b)
    fin = time.perf_counter()
    
    tiempo_ms = (fin - inicio) * 1000
    totalLlamadas = euclidesRecursivo.contador
    
    return resultado, totalLlamadas, tiempo_ms








def optEuclides():
    limpiar()
    print("--- comparacion entre iterativo y recursivo ---")
    
    try:
        a = int(input("Ingresa el primer numero entero positivo: "))
        b = int(input("Ingresa el segundo numero entero positivo: "))
        
        if a < 0 or b < 0:
            print("\nError. Ambos numeros son negativos")
            pausa()
            return
    except ValueError:
        print("\nError 404 not found xd.")
        pausa()
        return
    
    