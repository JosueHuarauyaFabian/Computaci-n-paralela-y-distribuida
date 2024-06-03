import cv2  #Importa la biblioteca OpenCV para procesamiento de imágenes.
import numpy as np
from multiprocessing import Pool  #Importa Pool para crear un grupo de procesos y ejecutar tareas en paralelo.


# Función para aplicar el desenfoque gaussiano a un segmento de la imagen
def apply_blur(segment):
    return cv2.GaussianBlur(segment, (15, 15), 0)

# Función para procesar una imagen en paralelo
def parallel_image_processing(image_path):
    # Leer la imagen desde el archivo
    image = cv2.imread(image_path)
    # Obtener las dimensiones de la imagen
    height, width, _ = image.shape
    # Dividir la imagen en 4 segmentos a lo largo del eje horizontal
    segments = np.array_split(image, 4, axis=1)

    # Crear un pool de procesos con 4 procesos
    with Pool(processes=4) as pool:
        # Aplicar la función de desenfoque a cada segmento en paralelo
        blurred_segments = pool.map(apply_blur, segments)

    # Concatenar los segmentos desenfocados a lo largo del eje horizontal
    blurred_image = np.hstack(blurred_segments)
    # Guardar la imagen desenfocada en un archivo
    cv2.imwrite('/home/josue-huarauya/Imágenes/imagenes de prueba.jpeg', blurred_image)

# Llamar a la función de procesamiento de imagen en paralelo con la ruta de la imagen de entrada
parallel_image_processing('/home/josue-huarauya/Imágenes/imagenes de prueba/messi.jpeg')
