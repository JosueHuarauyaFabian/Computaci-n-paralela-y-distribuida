# SPRINT 3 REPORT

## Introducción
**Objetivos del Sprint:**
- Desarrollar un panel de control para monitorear y gestionar la red P2P.
- Preparar documentación completa del sistema y los algoritmos implementados.
- Preparar y realizar una presentación sobre la implementación y los resultados obtenidos.

## Planificación
**Tareas planificadas:**
- Crear la interfaz gráfica para el panel de control.
- Implementar funcionalidades de gestión de nodos.
- Documentar la arquitectura del sistema y los algoritmos.
- Realizar pruebas de rendimiento y documentarlas.

**Asignación de tareas:**
- Desarrollo del panel de control: Josue Huarauya
- Implementación de algoritmos: Equipo
- Documentación y pruebas: Equipo

**Cronograma:**
- Inicio del sprint: 24/06/2024
- Fin del sprint: 01/07/2024
- Hitos importantes: Finalización del panel de control, pruebas de rendimiento, documentación completa.

## Implementación
**Descripción del trabajo realizado:**
Durante este sprint, se desarrolló un panel de control para monitorear en tiempo real la latencia y el ancho de banda de la red P2P. Se implementaron funcionalidades para la gestión de nodos, permitiendo agregar nodos desde la interfaz.

**Algoritmos y métodos:**
- **Compresión de datos:** Se utilizó zlib para comprimir los datos enviados entre nodos.
- **Replicación de datos:** Implementada para asegurar la integridad y disponibilidad de la información.

**Desafíos encontrados:**
- Integración de datos en tiempo real en el panel de control.
- Manejo de concurrencia en la replicación de datos.

**Pruebas realizadas:**
- Pruebas de latencia y ancho de banda en diferentes condiciones de red.
- Verificación de la replicación de datos.
- **Pruebas unitarias y de integración:**
    - **Pruebas unitarias:** Se realizaron pruebas unitarias para verificar la compresión de datos y la estructura de datos. Estas pruebas aseguraron que los datos comprimidos se descomprimen correctamente y que la estructura de datos contiene los campos necesarios.
    - **Pruebas de integración:** Se realizaron pruebas de integración para verificar la funcionalidad de agregar nodos y obtener métricas a través de la API. Estas pruebas aseguraron que la API responde correctamente y que los nodos se agregan exitosamente.

**Demostración de funcionalidades:**
- Capturas de pantalla del panel de control funcionando en tiempo real.
![Panel de control](https://imgur.com/TV6Ze1S.png)

## Análisis y evaluación
**Comparación con los objetivos del Sprint:**
Se lograron todos los objetivos establecidos para este sprint, con la implementación del panel de control y la documentación completa del sistema.

**Lecciones aprendidas:**
- La importancia de una planificación detallada para la integración de múltiples componentes.
- La necesidad de realizar pruebas exhaustivas para asegurar la robustez del sistema.

**Retroalimentación recibida:**
- Feedback positivo sobre la interfaz gráfica del panel de control.
- Sugerencias para mejorar la visualización de datos y la gestión de nodos.

## Plan para el próximo Sprint
**Objetivos del próximo Sprint:**
- Este es el último sprint del proyecto, por lo tanto, no hay un próximo sprint planificado.

**Tareas planificadas:**
- Realizar una revisión final del proyecto.
- Preparar la presentación final.

**Ajustes necesarios:**
- Incorporar mejoras sugeridas en la presentación y documentación del sistema.
- Realizar más pruebas de rendimiento en diferentes escenarios de red.

## Instrucciones de Ejecución del Entorno

### Requisitos
- Python 3.7 o superior
- ZeroMQ
- Flask
- Requests (para pruebas)

### Instalación de Dependencias
Para instalar las dependencias necesarias, ejecuta:
```bash
pip install flask zmq requests
```

### Ejecución del Entorno
Para ejecutar el entorno, incluyendo el servidor y los clientes, utiliza el siguiente comando:
```bash
./src/scripts/run_servers.sh
```
Este script mata cualquier proceso anterior en los puertos utilizados y ejecuta tanto el servidor gather como varios clientes gather.

Para ejecutar solo el panel de control, usa el siguiente comando:
```bash
flask run
```

### Pruebas
Para ejecutar las pruebas unitarias y de integración, usa los siguientes comandos:
```bash
# Pruebas unitarias
python tests/test_unit.py

# Pruebas de integración
python tests/test_integration.py
```

**Estructura del Sprint3:**
```
.
├── reports
│   └── integration_report.md
├── SPRINT3_REPORT.md
├── src
│   ├── app.py
│   ├── scripts
│   │   ├── gather_client_with_replication.py
│   │   ├── gather_server_with_replication.py
│   │   └── run_servers.sh
│   ├── static
│   │   ├── main.js
│   │   └── styles.css
│   └── templates
│       └── index.html
└── tests
    ├── test_integration.py
    └── test_unit.py
```
