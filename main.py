from colas import opcionesColas
from recursion import opcionesRecursion


def main():
    print("seleccione una opcion")
    option = input(
        "\n1. COLAS " \
        "\n2. STAKS " \
        "\n3. ARBOLES BINARIOS " \
        "\n4. LISTAS ENLAZADAS " \
        "\n5. ARREGLOS " \
        "\n6. RECURSIVIDAD "
    )


    if option == "1":
        opcionesColas()
    elif option == "2":
        print("Stacks (pendiente)")
    elif option == "3":
        print("Árboles binarios (pendiente)")
    elif option == "4":
        print("Listas enlazadas (pendiente)")
    elif option == "5":
        print("Arreglos (pendiente)")
    elif option == "6":
        opcionesRecursion()
    else:
        print("Opción no válida.")



if __name__ == "__main__":
    main()


