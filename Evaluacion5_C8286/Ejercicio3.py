import asyncio
from concurrent.futures import ProcessPoolExecutor
import random
import time

# Funciones puras para el cálculo de métricas de tráfico
def calculate_average_speed(data):
    """Calcula la velocidad promedio a partir de datos de velocidad recogidos."""
    total_speed = sum(data['speed'])
    count = len(data['speed'])
    return total_speed / count if count else 0

def calculate_traffic_volume(data):
    """Calcula el volumen de tráfico a partir de datos de conteo de vehículos."""
    return sum(data['vehicles'])

# Función para procesar datos de una ubicación usando multiprocessing
def process_single_location(data):
    """Procesa los datos de tráfico de una única ubicación."""
    average_speed = calculate_average_speed(data)
    traffic_volume = calculate_traffic_volume(data)
    return {'location': data['location'], 'average_speed': average_speed, 'traffic_volume': traffic_volume}

# Función para procesar datos de múltiples ubicaciones en paralelo
def process_traffic_data(locations_data):
    """Procesa datos de múltiples ubicaciones utilizando procesamiento en paralelo."""
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(process_single_location, locations_data))
    return results

# Función asincrónica para actualizar los datos de tráfico
async def update_traffic_data():
    """Actualiza periódicamente los datos de tráfico y la visualización."""
    while True:
        locations_data = fetch_traffic_data()  # Recolecta datos de tráfico
        processed_data = await asyncio.get_event_loop().run_in_executor(None, process_traffic_data, locations_data)
        update_visualization(processed_data)  # Actualiza la visualización
        await asyncio.sleep(10)  # Actualiza cada 10 segundos

# Simulación de recolección de datos de tráfico
def fetch_traffic_data():
    """Simula la recolección de datos de tráfico de múltiples sensores."""
    return [
        {'location': 'Location A', 'speed': [random.randint(30, 70) for _ in range(10)], 'vehicles': [random.randint(80, 120) for _ in range(10)]},
        {'location': 'Location B', 'speed': [random.randint(20, 50) for _ in range(10)], 'vehicles': [random.randint(60, 90) for _ in range(10)]}
    ]

# Simulación de actualización de la visualización
def update_visualization(data):
    """Actualiza una interfaz de usuario o un dashboard con los últimos datos procesados."""
    print("Updated visualization with:", data)

if __name__ == "__main__":
    asyncio.run(update_traffic_data())
