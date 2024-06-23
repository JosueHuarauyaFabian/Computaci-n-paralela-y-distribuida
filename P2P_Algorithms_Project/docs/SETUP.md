# Instrucciones para configurar el entorno

## 1. Requisitos previos

Antes de comenzar, asegúrate de tener instaladas las siguientes herramientas y bibliotecas:

- Python 3.8 o superior
- `pip` - el gestor de paquetes de Python
- `virtualenv` - para crear entornos virtuales
- Git

## 2. Clonar el repositorio

Primero, clona el repositorio del proyecto desde GitHub:

```bash
git clone https://github.com/JosueHuarauyaFabian/Proyecto_P2P_Algorithms.git
cd Proyecto_P2P_Algorithms
```

## 3. Crear y activar un entorno virtual

Crea un entorno virtual para aislar las dependencias del proyecto:

```bash
python -m venv p2p_env
source p2p_env/bin/activate  # En Windows usa `p2p_env\Scripts\activate`
```

## 4. Instalar dependencias

Instala todas las dependencias necesarias utilizando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` debería contener las siguientes dependencias:

```plaintext
pyzmq
python-dateutil
```

## 5. Configuración del entorno de red P2P

### 5.1. Configuración de ZeroMQ

ZeroMQ se utiliza para la comunicación entre nodos en la red P2P. No se necesita configuración adicional más allá de la instalación de la biblioteca.

## 6. Estructura del proyecto

A continuación se muestra la estructura del proyecto:

```plaintext
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
```

## 7. Ejecución de pruebas

### 7.1. Pruebas Unitarias e Integradas

Para ejecutar las pruebas unitarias e integradas:

```bash
python -m unittest sprint1/tests/unit_tests.py
python -m unittest sprint1/tests/integration_tests.py
```

### 7.2. Pruebas de Estrés

Para ejecutar las pruebas de estrés:

```bash
cd sprint2/tests
chmod +x run_stress_tests.sh
./run_stress_tests.sh
```

## 8. Documentación

Toda la documentación del proyecto, incluyendo guías de instalación, configuración y uso del sistema, se encuentra en la carpeta `docs`.

## 9. Panel de control (Sprint 3)

El desarrollo del panel de control y la documentación correspondiente se completará en el Sprint 3. Mantente atento a las actualizaciones en el repositorio.

## 10. Soporte

Si tienes alguna pregunta o necesitas asistencia, por favor contacta a Josue Huarauya a través del repositorio de GitHub.