# Tests

Esta carpeta contiene scripts de prueba para los algoritmos distribuidos implementados en el proyecto.

## Contenido

- `unit_tests.py`: Contiene pruebas unitarias para verificar la funcionalidad de los algoritmos de difusión (`Broadcast`).
- `integration_tests.py`: Contiene pruebas de integración para verificar la funcionalidad del algoritmo de recolección de datos (`Gather`).

## Cómo ejecutar las pruebas

1. Asegúrese de tener el entorno virtual activado.
2. Ejecute las pruebas unitarias con el siguiente comando:
   ```bash
   python -m unittest tests/unit_tests.py
