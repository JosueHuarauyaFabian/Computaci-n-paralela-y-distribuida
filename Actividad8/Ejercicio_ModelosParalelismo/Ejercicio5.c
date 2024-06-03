#include <stdio.h>      // Biblioteca estándar de entrada/salida para printf
#include <stdlib.h>     // Biblioteca estándar para funciones de utilidad como rand y malloc
#include <pthread.h>    // Biblioteca para manejar hilos POSIX

#define NUM_THREADS 4    // Número de hilos
#define VECTOR_SIZE 1000000 // Tamaño del vector

// Estructura para almacenar datos del hilo
typedef struct {
    int start;         // Índice de inicio del segmento del vector
    int end;           // Índice de fin del segmento del vector
    double *vector;    // Puntero al vector
    double sum;        // Suma parcial calculada por el hilo
} ThreadData;

// Función que calcula la suma parcial de un segmento del vector
void *partial_sum(void *arg) {
    ThreadData *data = (ThreadData *)arg; // Convertir el argumento a tipo ThreadData
    data->sum = 0.0;                      // Inicializar la suma parcial a 0
    for (int i = data->start; i < data->end; i++) {
        data->sum += data->vector[i];     // Calcular la suma parcial
    }
    pthread_exit(NULL);                   // Terminar el hilo
}

int main() {
    // Crear e inicializar el vector
    double *vector = (double *)malloc(VECTOR_SIZE * sizeof(double));
    for (int i = 0; i < VECTOR_SIZE; i++) {
        vector[i] = rand() % 100; // Llenar el vector con valores aleatorios
    }

    // Declarar hilos y sus datos
    pthread_t threads[NUM_THREADS];
    ThreadData thread_data[NUM_THREADS];
    int segment_size = VECTOR_SIZE / NUM_THREADS; // Tamaño de cada segmento

    // Crear hilos y asignarles segmentos del vector
    for (int i = 0; i < NUM_THREADS; i++) {
        thread_data[i].start = i * segment_size; // Índice de inicio del segmento
        thread_data[i].end = (i == NUM_THREADS - 1) ? VECTOR_SIZE : (i + 1) * segment_size; // Índice de fin del segmento
        thread_data[i].vector = vector; // Asignar el vector al hilo
        pthread_create(&threads[i], NULL, partial_sum, (void *)&thread_data[i]); // Crear el hilo
    }

    double total_sum = 0.0;
    // Esperar a que los hilos terminen y combinar los resultados
    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL); // Esperar a que el hilo termine
        total_sum += thread_data[i].sum; // Sumar la suma parcial del hilo al total
    }

    // Imprimir la suma total
    printf("Total sum: %f\n", total_sum);

    // Liberar memoria
    free(vector);
    return 0;
}
