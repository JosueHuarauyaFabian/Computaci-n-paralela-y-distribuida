import numpy as np
from joblib import Parallel, delayed

# Función para multiplicar sub-matrices
def multiply_sub_matrices(A, B):
    return np.dot(A, B)

# Función para realizar la multiplicación de matrices en paralelo
def parallel_matrix_multiplication():
    # Crear dos matrices grandes de 1000x1000 con valores aleatorios
    A = np.random.rand(1000, 1000)
    B = np.random.rand(1000, 1000)
    
    # Dividir la matriz A en 4 sub-matrices a lo largo del eje 0 (filas)
    A_subs = np.array_split(A, 4, axis=0)
    # Dividir la matriz B en 4 sub-matrices a lo largo del eje 1 (columnas)
    B_subs = np.array_split(B, 4, axis=1)

    # Utilizar joblib.Parallel y joblib.delayed para multiplicar las sub-matrices en paralelo
    results = Parallel(n_jobs=4)(delayed(multiply_sub_matrices)(A_sub, B_sub) for A_sub in A_subs for B_sub in B_subs)
    
    # Crear una matriz de ceros de 1000x1000 para almacenar el resultado final
    C = np.zeros((1000, 1000))
    
    # Reunir los resultados y formar la matriz resultante
    for i, res in enumerate(results):
        # Calcular las posiciones en las que se deben colocar las sub-matrices multiplicadas
        row_idx = i // 4
        col_idx = i % 4
        C[row_idx*250:(row_idx+1)*250, col_idx*250:(col_idx+1)*250] = res

    return C

# Ejecutar la función de multiplicación de matrices en paralelo
C = parallel_matrix_multiplication()
