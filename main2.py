from recursividad.nombre import mostrarNombres
from recursividad.factorial import optFactorial
from recursividad.euclides import optEuclides
from recursividad.fibonacci import optFibonacci



def main2():

    print("Selecciona una opcion")
    option = input(
        "\n1. Factorial"\
        "\n2. Euclides"\
        "\n3. Fibonacci"\
        "\n4. Creditos"
    )

    if option == "1":
        optFactorial
    elif option == "2":
        optEuclides
    elif option == "3":
        optFibonacci
    elif option == "4":
        mostrarNombres
    else:
        print("opcion no valida")
    
    

    