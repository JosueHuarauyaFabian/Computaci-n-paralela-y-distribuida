#include <stdio.h>       // Biblioteca estándar de entrada/salida para printf
#include <stdlib.h>      // Biblioteca estándar para funciones de utilidad como rand
#include <pthread.h>     // Biblioteca de hilos POSIX
#include <unistd.h>      // Biblioteca para funciones de dormir (sleep)

#define BUFFER_SIZE 10   // Define el tamaño del búfer

int buffer[BUFFER_SIZE]; // Búfer compartido
int count = 0;           // Contador de elementos en el búfer
pthread_mutex_t mutex;   // Mutex para sincronizar el acceso al búfer
pthread_cond_t cond_producer, cond_consumer; // Variables de condición para productores y consumidores

// Función del productor
void* producer(void* arg) {
    for (int i = 0; i < 20; i++) { // Produce 20 elementos
        pthread_mutex_lock(&mutex); // Adquiere el mutex

        while (count == BUFFER_SIZE) { // Espera si el búfer está lleno
            pthread_cond_wait(&cond_producer, &mutex); // Espera la señal de consumidor
        }

        buffer[count++] = i; // Añade un elemento al búfer
        printf("Produced: %d\n", i);

        pthread_cond_signal(&cond_consumer); // Señala a los consumidores
        pthread_mutex_unlock(&mutex); // Libera el mutex

        sleep(rand() % 2); // Duerme un tiempo aleatorio (0-1 segundos)
    }
    pthread_exit(NULL); // Termina el hilo
}

// Función del consumidor
void* consumer(void* arg) {
    for (int i = 0; i < 20; i++) { // Consume 20 elementos
        pthread_mutex_lock(&mutex); // Adquiere el mutex

        while (count == 0) { // Espera si el búfer está vacío
            pthread_cond_wait(&cond_consumer, &mutex); // Espera la señal de productor
        }
        int item = buffer[--count]; // Consume un elemento del búfer
        printf("Consumed: %d\n", item);

        pthread_cond_signal(&cond_producer); // Señala a los productores
        pthread_mutex_unlock(&mutex); // Libera el mutex

        sleep(rand() % 3); // Duerme un tiempo aleatorio (0-2 segundos)
    }
    pthread_exit(NULL); // Termina el hilo
}
https://upch.zoom.us/j/94683123956


int main() {
    pthread_t prod_thread, cons_thread; // Declarar hilos para el productor y el consumidor
    pthread_mutex_init(&mutex, NULL); // Inicializar el mutex
    pthread_cond_init(&cond_producer, NULL); // Inicializar la condición del productor
    pthread_cond_init(&cond_consumer, NULL); // Inicializar la condición del consumidor

    pthread_create(&prod_thread, NULL, producer, NULL); // Crear el hilo del productor
    pthread_create(&cons_thread, NULL, consumer, NULL); // Crear el hilo del consumidor

    pthread_join(prod_thread, NULL); // Esperar a que el hilo del productor termine
    pthread_join(cons_thread, NULL); // Esperar a que el hilo del consumidor termine

    pthread_mutex_destroy(&mutex); // Destruir el mutex
    pthread_cond_destroy(&cond_producer); // Destruir la condición del productor
    pthread_cond_destroy(&cond_consumer); // Destruir la condición del consumidor

    return 0; // Terminar el programa
}

// Compilar el código con soporte para OpenMP
// gcc -o Ejercicio15_producer_consumer -pthread Ejercicio15_producer_consumer.c

//Ejecutar el programa
// ./Ejercicio15_producer_consumer