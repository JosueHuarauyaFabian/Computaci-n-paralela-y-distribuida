# Proyecto de Algoritmos Distribuidos en Redes P2P

## Descripción

Este proyecto implementa y prueba algoritmos distribuidos básicos en una red P2P utilizando ZeroMQ. Los algoritmos implementados son Gather y Broadcast. Se realizaron pruebas de rendimiento y medición de latencia.

## Requisitos

- Python 3.6+
- ZeroMQ
- Python-dateutil

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. Crea y activa un entorno virtual:
    ```bash
    python -m venv p2p_env
    source p2p_env/bin/activate  # En Windows usa `p2p_env\Scripts\activate`
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Ejecución

Para ejecutar los scripts de los algoritmos:

1. Inicia el servidor de Broadcast:
    ```bash
    python sprint1/src/broadcast_server_with_metrics.py
    ```

2. Inicia el cliente de Broadcast:
    ```bash
    python sprint1/src/broadcast_client_with_metrics.py
    ```

3. Inicia el servidor de Gather:
    ```bash
    python sprint1/src/gather_server_with_metrics.py
    ```

4. Inicia el cliente de Gather:
    ```bash
    python sprint1/src/gather_client_with_metrics.py
    ```

## Pruebas

Para ejecutar las pruebas unitarias y de integración:
```bash
python -m unittest discover -s sprint1/tests
