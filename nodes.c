#include <stdio.h>
#include <stdlib.h> // Necesaria para usar malloc() (pedir memoria física)

// --- MOLDE DEL VAGÓN ---
struct Nodo {
    int valor;           // La carga del vagón (el dato)
    struct Nodo* next;   // El asterisco (*) significa: "Este gancho guarda un número HEXADECIMAL de memoria"
};

// --- LA ESTACIÓN ---
struct LinkedList {
    struct Nodo* head;   // El letrero de INICIO (guarda el hexadecimal del primer vagón)
};

// Función para agregar al final
void addFinal(struct LinkedList* lista, int valor) {
    // malloc pide una dirección de memoria libre al sistema operativo para fabricar el vagón
    struct Nodo* new_node = (struct Nodo*)malloc(sizeof(struct Nodo));
    new_node->valor = valor; // Le metemos el producto
    new_node->next = NULL;   // Nace soltero, apunta a NULL

    // Si la estación está vacía (head apunta a la nada)
    if (lista->head == NULL) {
        lista->head = new_node; // Anclamos el primer vagón directamente a la estación
        return;
    }

    // El inspector "current" se para en el primer vagón
    struct Nodo* current = lista->head;

    // Mientras el gancho del vagón actual no apunte a la nada, camina...
    while (current->next != NULL) {
        current = current->next; // El inspector salta de hexadecimal en hexadecimal
    }

    // Al salir del while, el inspector está parado en el último vagón y amarra el nuevo
    current->next = new_node;
}

// Función para mostrar el tren
void mostrar(struct LinkedList* lista) {
    struct Nodo* current = lista->head; // El inspector va al primer vagón

    // Mientras el inspector esté pisando un vagón real (que no sea NULL)
    while (current != NULL) {
        printf("%d -> ", current->valor); // Imprime la carga en la pantalla
        current = current->next;          // Camina al siguiente
    }
    printf("NULL\n"); // Terminó el tren
}

int main() {
    // Creamos la estación e inicializamos el letrero de INICIO en NULL
    struct LinkedList lista;
    lista.head = NULL;

    addFinal(&lista, 10); // El símbolo & le pasa la ubicación de la estación a la función
    addFinal(&lista, 20);
    addFinal(&lista, 30);

    mostrar(&lista); // Imprime: 10 -> 20 -> 30 -> NULL

    return 0;
}




#include <stdio.h>
#include <stdlib.h>

// --- MOLDE DEL VAGÓN DOBLE ---
struct NodoDoble {
    int valor;
    struct NodoDoble* next; // Gancho hacia adelante (Hexadecimal del siguiente)
    struct NodoDoble* prev; // Gancho hacia atrás (Hexadecimal del anterior)
};

// --- LA ESTACIÓN ---
struct DoublyLinkedList {
    struct NodoDoble* head; // Letrero de INICIO
};

// Función para agregar al final en lista doble
void addFinalDoble(struct DoublyLinkedList* lista, int valor) {
    // Fabricamos el vagón doble en la memoria RAM
    struct NodoDoble* new_node = (struct NodoDoble*)malloc(sizeof(struct NodoDoble));
    new_node->valor = valor;
    new_node->next = NULL; // No hay nadie adelante
    new_node->prev = NULL; // No hay nadie atrás

    // Si la estación está vacía
    if (lista->head == NULL) {
        lista->head = new_node; // Anclamos el vagón al inicio
        return;
    }

    // El inspector camina buscando el último vagón
    struct NodoDoble* current = lista->head;
    while (current->next != NULL) {
        current = current->next;
    }

    // --- AQUÍ OCURRE EL DOBLE ENLACE ---
    current->next = new_node; // 1. El viejo último vagón se conecta hacia adelante con el nuevo
    new_node->prev = current; // 2. EL PASO EXTRA: El nuevo vagón se conecta hacia atrás con el viejo último
}

void mostrarAdelante(struct DoublyLinkedList* lista) {
    struct NodoDoble* current = lista->head;
    printf("Hacia adelante: ");
    while (current != NULL) {
        printf("%d -> ", current->valor);
        current = current->next;
    }
    printf("NULL\n");
}

int main() {
    struct DoublyLinkedList lista;
    lista.head = NULL;

    addFinalDoble(&lista, 10);
    addFinalDoble(&lista, 20);
    addFinalDoble(&lista, 30);

    mostrarAdelante(&lista); // Imprime: Hacia adelante: 10 -> 20 -> 30 -> NULL

    return 0;
}