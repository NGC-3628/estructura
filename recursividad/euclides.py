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
    print("--- comparacion de teorema de euclides.  ---")
    
    try:
        a = int(input("Ingresa el primer numero entero positivo: "))
        b = int(input("Ingresa el segundo numero entero positivo: "))
        
        if a < 0 or b < 0:
            print("\nError: Debes ingresar numeros mayores o iguales a cero.")
            pausa()
            return
    except ValueError:
        print("\nError: Debes ingresar numeros enteros válidos.")
        pausa()
        return



    # iterative
    mcd_it, tiempo_it, ciclos_it = euclidesIterativo(a, b)




    # recusrive
    mcd_rec, llamadas_rec, tiempo_rec = ejecutarEuclides(a, b)




    # results
    separador()
    print(f"\nResultados para MCD({a}, {b}):")
    print(f"-> Maximo Común Divisor: {mcd_it}\n")
    
    print("--- Version Iterativa ---")
    print(f"Ciclos ejecutados: {ciclos_it}")
    print(f"Tiempo de ejecucion: {tiempo_it:.6f} ms\n")
    
    print("--- Version Recursiva ---")
    print(f"Llamadas recursivas: {llamadas_rec}")
    print(f"Tiempo de ejecucion: {tiempo_rec:.6f} ms")
    separador()

    pausa()