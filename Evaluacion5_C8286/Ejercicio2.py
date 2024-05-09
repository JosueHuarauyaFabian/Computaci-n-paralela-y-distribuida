import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import random
import time

# Funciones puras para manipular el estado de las reservas
def add_reservation(reservations, reservation):
    """Agrega una nueva reserva a la lista de reservas de manera inmutable."""
    return reservations + [reservation]

def cancel_reservation(reservations, reservation_id):
    """Cancela una reserva por ID, inmutablemente."""
    return [res for res in reservations if res['id'] != reservation_id]

def update_reservation(reservations, reservation_id, new_details):
    """Actualiza una reserva por ID, inmutablemente."""
    return [res if res['id'] != reservation_id else {**res, **new_details} for res in reservations]

# Simulación del procesamiento de solicitudes usando ThreadPoolExecutor
def handle_request(request):
    """Maneja una solicitud individual simulando cierta lógica y tiempo de procesamiento."""
    time.sleep(random.uniform(0.1, 0.5))  # Simular tiempo de procesamiento
    return f"Processed request {request['id']} with status: {request['status']}"

# Integración de multiprocessing para manejar la carga en múltiples procesos
def process_booking_requests(requests):
    """Procesa una lista de solicitudes de reserva concurrentemente usando multiprocessing."""
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(handle_request, requests))
    return results

# Manejo asincrónico de reservas
async def manage_reservations(requests):
    """Gestiona reservas asincrónicamente usando asyncio y concurrent.futures."""
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, process_booking_requests, requests)
    result = await future
    print(result)

# Simulación de un escenario de alta demanda
async def simulate_high_demand_scenario():
    """Simula la llegada de múltiples solicitudes durante un evento de alta demanda."""
    requests = [{'id': i, 'status': 'new'} for i in range(100)]  # Simular 100 solicitudes para "Black Friday"
    await manage_reservations(requests)

if __name__ == "__main__":
    asyncio.run(simulate_high_demand_scenario())
