# Documento de Diseño de Pruebas

## Resumen
Este documento describe el diseño de las pruebas para el Proyecto de Algoritmos P2P. El objetivo es verificar la funcionalidad, rendimiento y fiabilidad de los algoritmos Gather y Broadcast implementados.

## Objetivos de Prueba
- Verificar la correcta transmisión de mensajes entre nodos y servidor.
- Medir y registrar métricas de rendimiento como latencia y uso de ancho de banda.
- Asegurar que el sistema maneja efectivamente un gran número de nodos y volúmenes de datos.

## Escenarios de Prueba

### Algoritmo Gather
1. **Prueba de Funcionalidad**
   - Verificar que los nodos pueden enviar datos al servidor exitosamente.
   - Verificar que el servidor reconoce la recepción de datos de los nodos.

2. **Prueba de Rendimiento**
   - Medir la latencia de transmisión de datos desde los nodos hasta el servidor.
   - Medir el uso de ancho de banda durante la transmisión de datos.

### Algoritmo Broadcast
1. **Prueba de Funcionalidad**
   - Verificar que el servidor puede difundir mensajes a todos los nodos exitosamente.
   - Verificar que los nodos reciben correctamente los mensajes difundidos.

2. **Prueba de Rendimiento**
   - Medir la latencia para la recepción de mensajes en los nodos.
   - Medir el uso de ancho de banda durante la difusión de mensajes.

## Entorno de Prueba
- Red simulada con múltiples nodos.
- ZeroMQ para la comunicación.
- Scripts de Python para la automatización de pruebas.

## Herramientas de Prueba
- Python para la automatización de pruebas.
- ZeroMQ para la comunicación en red.
- Scripts personalizados para la recolección y análisis de métricas.

## Resultados Esperados
- Todos los nodos deben comunicarse exitosamente con el servidor.
- Las métricas de rendimiento deben estar dentro de límites aceptables para latencia y ancho de banda.
- El sistema debe manejar una carga aumentada sin una degradación significativa en el rendimiento.