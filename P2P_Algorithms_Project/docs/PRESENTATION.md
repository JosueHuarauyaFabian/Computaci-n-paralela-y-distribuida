
# Presentación del Proyecto de Algoritmos P2P

## 1. Introducción

### Objetivo del Proyecto
El objetivo de este proyecto es diseñar e implementar algoritmos distribuidos en una red P2P utilizando ZeroMQ. Se centra en la implementación y optimización de los algoritmos Gather y Broadcast, y en la creación de un panel de control para monitorear el rendimiento de la red en tiempo real.

### Justificación
Los sistemas P2P son esenciales para aplicaciones distribuidas que requieren alta escalabilidad y robustez. Este proyecto aplica los conceptos y técnicas de la computación paralela y distribuida para resolver problemas comunes en redes P2P.

## 2. Descripción del Proyecto

### Algoritmos Implementados
- **Gather:** Algoritmo para recolectar datos de múltiples nodos hacia un nodo central.
- **Broadcast:** Algoritmo para difundir mensajes desde un nodo central a todos los nodos en la red.
- **Replicación:** Técnicas para replicar datos entre nodos, asegurando la integridad y disponibilidad de la información.

### Panel de Control
Se desarrolló un panel de control utilizando Flask y Chart.js para monitorear en tiempo real la latencia y el ancho de banda de la red P2P. Este panel permite la gestión de nodos y la visualización de métricas de rendimiento.

## 3. Implementación Técnica

### Herramientas y Tecnologías
- **ZeroMQ:** Para la comunicación en red P2P.
- **Flask:** Para el desarrollo del servidor web del panel de control.
- **Chart.js:** Para la visualización de gráficos en tiempo real.
- **Zlib:** Para la compresión de datos.
- **Threading en Python:** Para manejar la concurrencia en la replicación de datos.

### Estructura del Proyecto
```
Proyecto_P2P_Algorithms/
├── docs/
│   ├── PRESENTATION.md
│   ├── README.md
│   └── SETUP.md
├── final_presentation/
├── sprint1/
│   ├── reports/
│   │   └── metrics_report.txt
│   ├── src/
│   │   ├── broadcast_client.py
│   │   ├── broadcast_server.py
│   │   ├── gather_client.py
│   │   └── gather_server.py
│   ├── tests/
│   │   ├── integration_tests.py
│   │   └── unit_tests.py
│   └── SPRINT1_REPORT.md
├── sprint2/
│   ├── reports/
│   ├── src/
│   │   ├── broadcast_client_optimized.py
│   │   ├── broadcast_server_optimized.py
│   │   ├── gather_client_optimized.py
│   │   ├── gather_client_with_replication.py
│   │   ├── gather_server_optimized.py
│   │   └── gather_server_with_replication.py
│   ├── tests/
│   │   └── run_stress_tests.sh
│   └── SPRINT2_REPORT.md
└── sprint3/
    ├── reports/
    │   └── integration_report.md
    ├── src/
    │   ├── app.py
    │   ├── scripts/
    │   │   ├── gather_client_with_replication.py
    │   │   ├── gather_server_with_replication.py
    │   │   └── run_servers.sh
    │   ├── static/
    │   │   ├── main.js
    │   │   └── styles.css
    │   └── templates/
    │       └── index.html
    ├── tests/
    │   ├── test_integration.py
    │   └── test_unit.py
    └── SPRINT3_REPORT.md
```

## 4. Resultados

### Funcionalidades Desarrolladas
- Implementación de algoritmos Gather y Broadcast.
- Optimización de algoritmos para mejorar el rendimiento.
- Panel de control para monitorear y gestionar la red P2P en tiempo real.

### Pruebas Realizadas
- **Pruebas de latencia y ancho de banda:** Se midió el rendimiento del sistema bajo diferentes condiciones de red.
- **Pruebas de replicación:** Verificación de la replicación de datos entre nodos.
- **Pruebas de estrés:** Evaluación de la escalabilidad del sistema con múltiples nodos.

## 5. Análisis y Evaluación

### Comparación con los Objetivos
Se cumplieron todos los objetivos establecidos para el proyecto, con la implementación exitosa de los algoritmos y la creación del panel de control.

### Lecciones Aprendidas
- La importancia de una planificación detallada y pruebas exhaustivas.
- La necesidad de manejar correctamente la concurrencia y la replicación de datos en sistemas distribuidos.

### Retroalimentación
Se recibió feedback positivo sobre la interfaz gráfica del panel de control y sugerencias para futuras mejoras.

## 6. Conclusión y Futuro Trabajo

### Conclusión
El proyecto demostró la aplicación práctica de los conceptos de computación paralela y distribuida en la implementación y gestión de una red P2P eficiente y robusta.

### Futuro Trabajo
- Mejorar la visualización de datos y la gestión de nodos en el panel de control.
- Continuar optimizando los algoritmos para manejar una mayor escala de nodos y datos.

## 7. Referencias
- **ZeroMQ Documentation**: [ØMQ - The Guide](https://zguide.zeromq.org/docs/), [ZeroMQ API](https://zeromq.org/languages/python/)
- **Flask Documentation**: [Flask Documentation](https://flask.palletsprojects.com/), [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- **Chart.js Documentation**: [Chart.js Documentation](https://www.chartjs.org/docs/latest/), [Chart.js Getting Started](https://www.chartjs.org/docs/latest/getting-started/)