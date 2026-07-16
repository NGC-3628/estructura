import time 
from recursividad.nombre import limpiar, pausa, separador  

########################    ITERATIVO    #####################    
def iterativo(n):
    resultado = 1
    contador_ciclos = 0
    
     
    inicio = time.perf_counter()
    
    for i in range(1, n + 1):
        resultado *= i
        contador_ciclos += 1  
        
    
    fin = time.perf_counter()
    
    
    tiempo_ms = (fin - inicio) * 1000
    
    return resultado, contador_ciclos, tiempo_ms



#####################    RECSURIVO    #####################    
def recursivo(n, contador = 0):
    
    contador += 1
    
    
    if n == 0 or n == 1:
        return 1, contador
    
   
    sub_resultado, contador_actualizado = recursivo(n - 1, contador)
    
    return n * sub_resultado, contador_actualizado


def ejecutarRecursivo(n):
    inicio = time.perf_counter()
    
    resultado, total_llamadas = recursivo(n)
    
    fin = time.perf_counter()
    tiempo_ms = (fin - inicio) * 1000
    
    return resultado, total_llamadas, tiempo_ms



def optFactorial():
    limpiar()
    print("--- comparacion de factorial ---")
    try:
        n = int(input("Ingresa un numero entero positivo: "))
        if n < 0:
            print("Intenat otra cvez. Ingresa un numero positivo.")
            pausa()
            return
    except ValueError:
        print("Ingresa un numero entero")
        pausa()
        return

    
    res_it, ciclos_it, tiempo_it = iterativo(n)
    res_rec, llamadas_rec, tiempo_rec = ejecutarRecursivo(n)

    
    separador()
    print(f"RESULTADO ITERATIVO:")
    print(f"  - Resultado: {res_it}")
    print(f"  - Veces que entró al ciclo: {ciclos_it}")
    print(f"  - Tiempo de ejecución: {tiempo_it:.4f} ms")
    
    separador()
    print(f"RESULTADO RECURSIVO:")
    print(f"  - Resultado: {res_rec}")
    print(f"  - Llamadas a la función: {llamadas_rec}")
    print(f"  - Tiempo de ejecución: {tiempo_rec:.4f} ms")
    separador()
    
    pausa()