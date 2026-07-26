from recursividad.nombre import mostrarNombres
from recursividad.factorial import optFactorial
from recursividad.euclides import optEuclides
from recursividad.fibonacci import optFibonacci
from main import main
from recursividad.nombre import limpiar



def main2():

    print("Selecciona una opcion")
    option = input(
        "\n1. Factorial"\
        "\n2. Euclides"\
        "\n3. Fibonacci"\
        "\n4. Creditos\n\n"\
        "\n5. Primer menu"\
        "\n6. Salir de todo"
    )

    while True:
        if option == "1":
            optFactorial()
            main2()
        elif option == "2":
            optEuclides()
            main2()
        elif option == "3":
            optFibonacci()
            main2()
        elif option == "4":
            mostrarNombres()
            main2()
        elif option == "5":
            main()
        elif option == "6":
            print("Vaya con Dios, hdsptm")
            limpiar()
            break
        else:
            print("opcion no valida")
            main2()
    
    

    