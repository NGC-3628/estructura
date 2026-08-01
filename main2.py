from recursividad.nombre import mostrarNombres, limpiar, separador
from recursividad.factorial import optFactorial
from recursividad.euclides import optEuclides
from recursividad.fibonacci import optFibonacci

def main2():
    while True:
        print("Selecciona una opción:")
        option = input(
            "\n1. Factorial"\
            "\n2. Euclides"\
            "\n3. Fibonacci"\
            "\n4. Créditos"\
            "\n5. Volver al primer menú"\
            "\n6. Salir de todo\n\n"
        )

        if option == "1":
            optFactorial()
        elif option == "2":
            optEuclides()
        elif option == "3":
            optFibonacci()
        elif option == "4":
            mostrarNombres()
        elif option == "5":
            return  
        elif option == "6":
            print("Vaya con Dios, hdsptm")
            limpiar()
            exit() 
        else:
            print("Opción no válida.\n")