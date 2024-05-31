#include <stdio.h>
#include <omp.h>

#define NUM_THREADS 4
#define ARRAY_SIZE 16

int main() {
    int array[ARRAY_SIZE];
    for (int i = 0; i < ARRAY_SIZE; i++) {
        array[i] = i;
    }

    omp_set_num_threads(NUM_THREADS);

    #pragma omp parallel
    {
        int id = omp_get_thread_num();
        int nthreads = omp_get_num_threads();

        // Fase 1: Sumar 10 a cada elemento del array
        for (int i = id; i < ARRAY_SIZE; i += nthreads) {
            array[i] += 10;
        }

        // Sincronización de barrera
        #pragma omp barrier

        // Fase 2: Multiplicar cada elemento por 2
        for (int i = id; i < ARRAY_SIZE; i += nthreads) {
            array[i] *= 2;
        }
    }

    printf("Array final:\n");
    for (int i = 0; i < ARRAY_SIZE; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    return 0;
}