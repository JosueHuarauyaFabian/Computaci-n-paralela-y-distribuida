# Sprint 2 Report

## 1. Introducción
### Objetivos del Sprint:
El objetivo del Sprint 2 fue optimizar los algoritmos Gather y Broadcast, implementar técnicas de replicación y recuperación, y realizar pruebas de estrés en una red simulada.

## 2. Planificación
### Tareas planificadas:
- Optimización de algoritmos.
- Implementación de técnicas de replicación y recuperación.
- Pruebas de estrés en una red simulada.

### Asignación de tareas:
Todas las tareas fueron realizadas por Josue Huarauya.

### Cronograma:
- **Inicio:** 13 de junio
- **Fin:** 22 de junio

### Hitos importantes:
- Implementación de replicación en el algoritmo Gather.
- Optimización del algoritmo Broadcast.
- Realización de pruebas de estrés.

## 3. Implementación

### Descripción del trabajo realizado:

- Se implementaron las optimizaciones para los algoritmos Gather y Broadcast.
- Se añadieron técnicas de replicación para mejorar la tolerancia a fallos.
- Se realizaron pruebas de estrés con una gran cantidad de nodos y volúmenes de datos elevados.

### Algoritmos y métodos:

- **Gather con Replicación:** Los nodos envían datos al servidor, que responde con una confirmación y replica los datos a otros servidores.
- **Broadcast Optimizado:** El servidor envía mensajes a todos los nodos de manera eficiente, minimizando la latencia.

### Pseudocódigo:

#### Gather con Replicación:
```plaintext
Inicio del Nodo:
    Configurar ZeroMQ
    Conectar al servidor principal y de replicación
    Mientras haya datos por enviar:
        Enviar datos al servidor principal
        Esperar confirmación
        Enviar datos al servidor de replicación
        Registrar confirmación
    Fin

Inicio del Servidor:
    Configurar ZeroMQ
    Enlazar a un puerto
    Mientras el servidor esté activo:
        Recibir datos del nodo
        Enviar confirmación al nodo
        Replicar datos a otros servidores
    Fin 
```

#### Broadcast Optimizado:
```plaintext
Inicio del Servidor:
    Configurar ZeroMQ
    Enlazar a un puerto
    Mientras el servidor esté activo:
        Crear mensaje de difusión
        Enviar mensaje a todos los nodos
        Esperar un intervalo de tiempo
    Fin

Inicio del Nodo:
    Configurar ZeroMQ
    Conectar al servidor
    Mientras el nodo esté activo:
        Recibir mensaje del servidor
        Registrar mensaje
    Fin
```

### Diagramas de flujo:

#### Gather con Replicación:
![Diagrama de flujo Gather con Replicación](https://imgur.com/YVcbQpw.png)

#### Broadcast Optimizado:
![Diagrama de flujo Broadcast Optimizado](https://imgur.com/4T6sKyq.png)

### Desafíos encontrados:

- **Problemas con las importaciones en los scripts de prueba.**
  - **Solución:** Ajustar las rutas de importación y verificar la estructura del proyecto.

## 4. Resultados

### Funcionalidades desarrolladas:
- Implementación de algoritmos Gather y Broadcast optimizados.
- Técnicas de replicación y recuperación para mejorar la tolerancia a fallos.

### Pruebas realizadas:
- **Pruebas de replicación:** Confirmación de recepción de datos y replicación exitosa.
- **Pruebas de estrés:** Evaluación de la latencia y el rendimiento bajo carga.

### Demostración de funcionalidades:
- A continuación se muestran capturas de pantalla de las ejecuciones de los algoritmos:

#### Gather Server with Replication:
![Gather Server with Replication](https://imgur.com/i4OJDfh.png)

#### Broadcast Server Optimizado:
![Broadcast Server Optimizado](https://imgur.com/d9qImtf.png)

### Comentarios a los resultados:
- Las pruebas mostraron que los algoritmos optimizados manejan eficientemente grandes volúmenes de datos y nodos.
- Las técnicas de replicación implementadas mejoraron la tolerancia a fallos sin afectar significativamente el rendimiento.


### Librerías utilizadas:

-   **ZeroMQ:** Utilizada para la comunicación en red P2P.
-   **Python Dateutil:** Utilizada para manejar los formatos de tiempo en las mediciones de rendimiento.
-   **Zlib:** Utilizada para la compresión de datos en las técnicas de replicación.
-   **Threading:** Utilizada para manejar la concurrencia en la replicación de datos.
-   **Sys:** Utilizada para manejar argumentos y la configuración del entorno.

## 5. Análisis y evaluación

### Comparación con los objetivos del Sprint:
- Se cumplieron todos los objetivos iniciales del sprint, con la optimización de algoritmos, implementación de replicación, y realización de pruebas de estrés exitosas.

### Lecciones aprendidas:
- La importancia de la replicación para mejorar la robustez del sistema.
- La necesidad de realizar pruebas de estrés para evaluar la escalabilidad del sistema.

## 6. Plan para el próximo Sprint

### Objetivos del próximo Sprint (Sprint 3):
- Desarrollar un panel de control para monitorear y gestionar la red P2P.
- Preparar documentación completa del sistema y los algoritmos implementados.
- Preparar y realizar una presentación sobre la implementación y los resultados obtenidos.

### Actividades planificadas:
**Desarrollo de un panel de control:**
- Crear una interfaz gráfica o web para monitorear el estado de la red P2P en tiempo real.
- Implementar funcionalidades para gestionar los nodos, visualizar métricas de rendimiento y detectar fallos.

**Documentación completa del sistema:**
- Documentar detalladamente la arquitectura del sistema, los algoritmos implementados y las técnicas de optimización utilizadas.
- Incluir guías de instalación, configuración y uso del sistema.
- Preparar informes técnicos sobre los resultados de las pruebas de rendimiento y estrés.

**Preparación y presentación:**
- Crear una presentación que detalle los objetivos, metodología, resultados y conclusiones del proyecto.
- Incluir demostraciones en vivo del sistema funcionando y análisis de casos de uso específicos.
- Documentar todo el proceso de desarrollo en el repositorio de GitHub, incluyendo código, informes y resultados de pruebas.

### Entregables:
- Panel de control desarrollado para monitorear y gestionar la red P2P.
- Documentación completa del sistema y los algoritmos implementados.
- Presentación detallada con demostraciones en vivo y análisis de casos de uso.
- Repositorio de GitHub con toda la documentación, código y resultados del proyecto.