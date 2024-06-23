# Sprint 1 Report

## 1. Introducción
### Objetivos del Sprint:
El objetivo del Sprint 1 fue implementar y probar algoritmos distribuidos básicos en una red P2P usando ZeroMQ. Se enfocó en dos algoritmos: Gather y Broadcast. Además, se realizaron mediciones de latencia y otros parámetros de rendimiento.

## 2. Planificación
### Tareas planificadas:
- Implementación del algoritmo Gather.
- Implementación del algoritmo Broadcast.
- Configuración del entorno de desarrollo con ZeroMQ.
- Pruebas iniciales sin métricas.
- Pruebas con medición de métricas de rendimiento.

### Asignación de tareas:
Todas las tareas fueron realizadas por Josue Huarauya.

### Cronograma:
- **Inicio:** 1 de junio
- **Fin:** 12 de junio

### Hitos importantes:
- Configuración del entorno de desarrollo.
- Implementación de Gather.
- Implementación de Broadcast.
- Pruebas iniciales.
- Pruebas con métricas.

## 3. Implementación

### Descripción del trabajo realizado:
- Se configuró un entorno virtual con ZeroMQ.
- Se implementaron los algoritmos Gather y Broadcast en scripts de Python.
- Se realizaron pruebas iniciales para asegurar la correcta transmisión de mensajes.
- Se añadieron funcionalidades para medir la latencia y otros parámetros de rendimiento.

### Algoritmos y métodos:
- **Gather:** Los nodos envían datos al servidor, que responde con una confirmación.
- **Broadcast:** El servidor envía mensajes a todos los nodos.

### Pseudocódigo:

#### Gather:
```plaintext
Inicio del Nodo:
    Configurar ZeroMQ
    Conectar al servidor
    Mientras haya datos por enviar:
        Enviar datos al servidor
        Esperar confirmación
        Registrar confirmación
    Fin

Inicio del Servidor:
    Configurar ZeroMQ
    Enlazar a un puerto
    Mientras el servidor esté activo:
        Recibir datos del nodo
        Enviar confirmación al nodo
    Fin 
```

#### Broadcast:
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

#### Broadcast:
![Diagrama de flujo Broadcast](https://imgur.com/8upukKK.png)

#### Gather:
![Diagrama de flujo Gather](https://imgur.com/Tm3FRNt.png)

### Desafíos encontrados:
- Inicialmente, se encontraron problemas con el formato de tiempo en las mediciones de latencia.
  - **Solución:** Se instaló la librería `dateutil` y se modificó el código para usar `parser.parse` para manejar los formatos de tiempo correctamente.

## 4. Resultados

### Funcionalidades desarrolladas:
- Envío y recepción de mensajes en algoritmos Gather y Broadcast.
- Medición de métricas de latencia en ambos algoritmos.

### Pruebas realizadas:
- **Pruebas sin métricas:** Asegurar la transmisión correcta de mensajes.
- **Pruebas con métricas:** Medición de latencia en milisegundos.

### Demostración de funcionalidades:
A continuación se muestran capturas de pantalla de las ejecuciones de los algoritmos:

### Ejecuciones sin métricas:
- **Broadcast Server:**
  ![Broadcast Server](https://imgur.com/1Y4BRSs.png)

- **Broadcast Client:**
  ![Broadcast Client](https://imgur.com/gRPXtCX.png)
  ![Broadcast Client](https://imgur.com/2wff29v.png)
  ![Broadcast Client](https://imgur.com/dEYowOw.png)

- **Gather Server:**
  ![Gather Server](https://imgur.com/aN62fzZ.png)

- **Gather Client:**
  ![Gather Client](https://imgur.com/jXqjH87.png)
  ![Gather Client](https://imgur.com/nZwBx3p.png)
  ![Gather Client](https://imgur.com/5pQtDWm.png)

### Ejecuciones con métricas:
- **Broadcast Server with Metrics:**
  ![Broadcast Server with Metrics](https://imgur.com/aTUMw8c.png)

- **Broadcast Client with Metrics:**
  ![Broadcast Client with Metrics](https://imgur.com/XcMts3B.png)
  ![Broadcast Client with Metrics](https://imgur.com/nvR2IDn.png)
  ![Broadcast Client with Metrics](https://imgur.com/twYSS51.png)

- **Gather Server with Metrics:**
  ![Gather Server with Metrics](https://imgur.com/34vOFPk.png)

- **Gather Client with Metrics:**
  ![Gather Client with Metrics](https://imgur.com/aUke8Wm.png)
  ![Gather Client with Metrics](https://imgur.com/1m7pncH.png)
  ![Gather Client with Metrics](https://imgur.com/r1fTgMJ.png)

### Comentarios a los resultados:
- Las pruebas sin métricas confirmaron que los mensajes se transmitían correctamente entre los nodos y el servidor.
- Las pruebas con métricas mostraron latencias bajas y consistentes en la transmisión de mensajes, lo que indica una comunicación eficiente en la red P2P.

### Librerías utilizadas:

-   **ZeroMQ:** Utilizada para la comunicación en red P2P.
-   **Python Dateutil:** Utilizada para manejar los formatos de tiempo en las mediciones de rendimiento.

## 5. Análisis y evaluación

### Comparación con los objetivos del Sprint:
- Se cumplieron todos los objetivos iniciales del sprint, con la implementación y prueba exitosa de los algoritmos Gather y Broadcast, y la correcta medición de métricas de rendimiento.

### Lecciones aprendidas:
- La importancia de manejar correctamente los formatos de tiempo en las mediciones de rendimiento.
- La utilidad de `dateutil.parser` para manejar formatos de tiempo diversos.

### Retroalimentación recibida:
- No se recibió retroalimentación externa específica durante este sprint.

## 6. Plan para el próximo Sprint

### Objetivos del próximo Sprint (Sprint 2):
- Implementación de algoritmos más complejos en la red P2P.
- Mejorar la robustez y eficiencia del código actual.
- Realizar pruebas de estrés para evaluar el rendimiento bajo carga.

### Tareas planificadas:
- Implementar algoritmos adicionales.
- Optimizar el código actual.
- Configurar pruebas de estrés y analizar los resultados.

### Ajustes necesarios:
- Ajustar la planificación en función del rendimiento observado y las mejoras necesarias en el código.
