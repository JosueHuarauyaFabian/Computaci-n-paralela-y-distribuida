# Actividad 0: Verificación del funcionamiento de Docker, Docker, Desktop, Minikube, Kind

**Pruba de docker**
 - Para la version de docker ejecutamos en la terminal el comando *docker version*
![Texto alternativo](https://i.imgur.com/iIq4foe.png)
 - Para ver si puede ejecutar contenedores ejecutamos el siguiente comando *docker container run hello-world*
![Texto alternativo](https://imgur.com/kz7ttqP.png) <div style="text-align: justify;"> El resultado anterior, habrá notado que Docker no encontró una imagen llamada hello-world:latest y, por lo tanto, decidió descargarla desde un registro de imágenes de Docker. Una vez descargado, Docker Engine creó un contenedor a partir de la imagen y lo ejecutó. La aplicación se ejecuta dentro del contenedor y luego genera todo el texto, comenzando con Hello from Docker! Esta es una prueba de que Docker está instalado y funcionando correctamente en su máquina. </div>
