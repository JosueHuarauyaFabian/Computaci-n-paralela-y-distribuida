#include <stdio.h>       // Biblioteca estándar de entrada/salida para printf
#include <stdlib.h>      // Biblioteca estándar para funciones de utilidad como rand
#include <omp.h>         // Biblioteca para usar OpenMP para paralelización

// Función para realizar la multiplicación de matrices en paralelo
void parallel_matrix_multiplication(int N) {
    int i, j, k;
    
    // Asignar memoria para las matrices A, B y C
    double **A = (double **)malloc(N * sizeof(double *));
    double **B = (double **)malloc(N * sizeof(double *));
    double **C = (double **)malloc(N * sizeof(double *));
    
    // Inicializar las matrices A y B con valores aleatorios y la matriz C con ceros
    for (i = 0; i < N; i++) {
        A[i] = (double *)malloc(N * sizeof(double));
        B[i] = (double *)malloc(N * sizeof(double));
        C[i] = (double *)malloc(N * sizeof(double));
        for (j = 0; j < N; j++) {
            A[i][j] = rand() % 100;  // Inicializa A con valores aleatorios
            B[i][j] = rand() % 100;  // Inicializa B con valores aleatorios
            C[i][j] = 0.0;           // Inicializa C con ceros
        }
    }

    // Paralelizar los bucles de multiplicación de matrices utilizando OpenMP
    #pragma omp parallel for private(i, j, k) shared(A, B, C)
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            for (k = 0; k < N; k++) {
                C[i][j] += A[i][k] * B[k][j];  // Multiplica las matrices A y B y guarda el resultado en C
            }
        }
    }

    // Imprimir una pequeña parte de la matriz resultado
    for (i = 0; i < 5; i++) {
        for (j = 0; j < 5; j++) {
            printf("%f ", C[i][j]);  // Imprime los primeros 5x5 elementos de la matriz resultante C
        }
        printf("\n");
    }

    // Liberar la memoria asignada para las matrices
    for (i = 0; i < N; i++) {
        free(A[i]);
        free(B[i]);
        free(C[i]);
    }
    free(A);
    free(B);
    free(C);
}

// Función principal
int main() {
    int N = 1000;  // Tamaño de las matrices
    parallel_matrix_multiplication(N);
    return 0;
}

// Compilar el código con soporte para OpenMP
// gcc -o Ejercicio4 -fopenmp Ejercicio4.c

//Ejecutar el programa
// ./Ejercicio4