import asyncio
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageFilter
import os
from io import BytesIO
from functools import wraps
import time

# Funciones puras para el procesamiento de imágenes
def convert_to_grayscale(image):
    """Convierte la imagen a escala de grises."""
    return image.convert('L')

def apply_edge_detection(image):
    """Aplica detección de bordes a la imagen."""
    return image.filter(ImageFilter.FIND_EDGES)

def classify_image(image):
    """Clasifica la imagen, simulación de clasificación."""
    return "antelope"  # Simulación de resultado de clasificación

# Decorador para medir el tiempo de ejecución
def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds to run.")
        return result
    return wrapper

# Función para procesar una imagen individualmente, sincronizada para usar en ThreadPoolExecutor
def process_single_image(image_path):
    """Procesa una imagen leyéndola, convirtiéndola a escala de grises, aplicando detección de bordes y clasificándola."""
    with open(image_path, 'rb') as file:
        image_data = file.read()
    img = Image.open(BytesIO(image_data))
    gray_img = convert_to_grayscale(img)
    processed_img = apply_edge_detection(gray_img)
    class_label = classify_image(processed_img)
    return processed_img, class_label

@time_it
async def process_images(image_paths):
    """Procesa imágenes en paralelo utilizando ThreadPoolExecutor."""
    with ThreadPoolExecutor(max_workers=4) as executor:
        loop = asyncio.get_running_loop()
        tasks = [loop.run_in_executor(executor, process_single_image, path) for path in image_paths]
        results = await asyncio.gather(*tasks)
    return results

async def main():
    """Función principal para ejecutar el procesamiento asincrónico de imágenes."""
    images_dir = 'D:/Tareas de cursos/Evaluacion5_C8286/Antelope'
    image_paths = [os.path.join(images_dir, f) for f in os.listdir(images_dir) if f.endswith('.jpg')]
    
    processed_images = await process_images(image_paths)
    
    output_dir = 'D:/Tareas de cursos/Evaluacion5_C8286/processed_antelope_images'
    os.makedirs(output_dir, exist_ok=True)
    
    for i, (img, label) in enumerate(processed_images):
        img.save(os.path.join(output_dir, f'processed_{i}_{label}.jpg'))
        print(f"Saved {os.path.join(output_dir, f'processed_{i}_{label}.jpg')}")

if __name__ == "__main__":
    asyncio.run(main())
