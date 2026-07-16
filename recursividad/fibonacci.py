import time
from recursividad.nombre import limpiar, pausa, separador

def fibonacciIterativo(n):
    
    contadorCiclos = 0
    inicio = time.perf_counter()

    if n == 0:
        fin = time.perf_counter()
        return 0, 0, (fin - inicio) * 1000
    elif n == 1:
        fin = time.perf_counter()
        return 1, 0, (fin - inicio) * 1000

    penultimo = 0
    ultimo = 1
    resultado = 0

    for _ in range(2, n + 1):
        resultado = penultimo + ultimo
        penultimo = ultimo
        ultimo = resultado
        contadorCiclos += 1 



    fin = time.perf_counter()
    tiempo_ms = (fin - inicio) * 1000


    return resultado, contadorCiclos, tiempo_ms









def fibonacciRecursivo(n):
    
    fibonacciRecursivo.contador += 1  

    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacciRecursivo(n - 1) + fibonacciRecursivo(n - 2)


def ejecutarFibonacciRecursivo(n):
    
    fibonacciRecursivo.contador = 0  
    
    inicio = time.perf_counter()
    resultado = fibonacciRecursivo(n)
    fin = time.perf_counter()
    
    tiempo_ms = (fin - inicio) * 1000
    totalLlamadas = fibonacciRecursivo.contador
    
    return resultado, totalLlamadas, tiempo_ms



def optFibonacci():
    limpiar()
    print("--- comparacion en Fibonacci ---")
    separador()
    
    try:
        n = int(input("Ingresa un numero positivo"))
        if n < 0:
            print("\nError: El numero debe ser entero y positivo.")
            pausa()
            return
    except ValueError:
        print("\nError.")
        pausa()
        return


    if n > 35:
        confirmar = input("Este numero puede tardar bastante. Deseas continuar anyways? \ns/n").lower()
        if confirmar != 's':
            return

    res_it, ciclos_it, tiempo_it = fibonacciIterativo(n)
    res_rec, llamadas_rec, tiempo_rec = ejecutarFibonacciRecursivo(n)

    separador()
    print("ITERATIVO:")
    print(f"  - Termino F({n}):          {res_it}")
    print(f"  - Vueltas al ciclo:      {ciclos_it}")
    print(f"  - Tiempo de ejecucion:   {tiempo_it:.4f} ms")
    
    separador()
    print("RECURSIVO:")
    print(f"  - Termino F({n}):          {res_rec}")
    print(f"  - Llamadas recursivas:   {llamadas_rec}")
    print(f"  - Tiempo de ejecucion:   {tiempo_rec:.4f} ms")
    separador()
    
    pausa()