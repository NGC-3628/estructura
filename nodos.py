def opcionesListas():
    while True:
        print("Selecciona una opcion\n1. mi primer recursion xd\n2. suma casi iterativa\n3. Hanoi towwers\n4. suma de multiplicacion")
        
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            primero()
        elif opcion == "2":
            segundo()
        elif opcion == "3":
            tercero()
        elif opcion == "4":
            cuarto()
        else:
            print("opcion no validad")
            break


def primero():
    