#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

#define ARRAY_SIZE 100
#define ROOT 0

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int local_size = ARRAY_SIZE / size;
    int* array = NULL;
    int* local_array = (int*)malloc(local_size * sizeof(int));

    if (rank == ROOT) {
        array = (int*)malloc(ARRAY_SIZE * sizeof(int));
        for (int i = 0; i < ARRAY_SIZE; i++) {
            array[i] = i + 1;
        }
    }

    // Distribuir el array a todos los procesos
    MPI_Scatter(array, local_size, MPI_INT, local_array, local_size, MPI_INT, ROOT, MPI_COMM_WORLD);

    // Cada proceso calcula la suma parcial de su porción del array
    int local_sum = 0;
    for (int i = 0; i < local_size; i++) {
        local_sum += local_array[i];
    }

    // Reducir todas las sumas parciales al proceso raíz
    int global_sum;
    MPI_Reduce(&local_sum, &global_sum, 1, MPI_INT, MPI_SUM, ROOT, MPI_COMM_WORLD);

    // El proceso raíz imprime la suma total
    if (rank == ROOT) {
        printf("Total sum: %d\n", global_sum);
        free(array);
    }

    free(local_array);
    MPI_Finalize();

    return 0;
}
