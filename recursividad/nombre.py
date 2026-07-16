import os

# ------ utilidades de pantalla ------------

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")
def pausa():
    input("\nClick enter to continue...")

def separador():
    print("alv " * 20)



def mostrarNombres():
    limpiar()
    print("--- CREDITOS ---")
    separador()
    print("Materia: Estructira de Datos")
    print("Practica Personal: Recursividad")
    separador()
    print("Author : Isaac Iturralde Puente.  |  Matricula: \"24170079\"")
    separador()
    pausa()

    

