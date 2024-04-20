` `![](Aspose.Words.76263f85-51e4-469a-9743-8ef3a29a4cc9.001.png)![ref1]

**Evaluación: Código Limpio, principio de código**

**limpio , refactorización**

.

Nombre: Josue Eduardo Huarauya Fabian

**Objetivos**

- Hacer que el código sea autoexplicativo y minimizar la necesidad de documentación extensa para entender flujos de ejecución complejos.
- Simplificar la adición de nuevas características o la modificación de comportamientos existentes sin introducir errores.
- Permitir una evolución fluida del código en proyectos que suelen ser más complejos debido a la naturaleza de la concurrencia y la distribución.
- Reducir la duplicidad de código y fomentar la modularidad a través de abstracciones claras y bien definidas.
- Implementar patrones de diseño y prácticas de programación que reduzcan los errores comunes en la programación paralela y distribuida.
- Identificar y refactorizar cuellos de botella o ineficiencias en el uso de recursos, como el uso excesivo de sincronización o la serialización innecesaria de operaciones que podrían ser paralelas.
- Estructurar el código de manera que pueda escalar de manera eficiente con el aumento de la carga de trabajo o los recursos disponibles.
- Permitir que el sistema gestione de manera efectiva un mayor número de usuarios, datos o tareas simultáneas sin degradar significativamente el rendimiento.
- Diseñar el código para que sea testeable, especialmente importante en

  entornos concurrentes y distribuidos donde los errores pueden ser difíciles de reproducir.

- Permitir una localización y corrección más rápidas de los errores, mejorando así

  la calidad del software.

**Código Limpio**

El código limpio no es un conjunto de reglas estrictas. Es un conjunto de principios para escribir código que es fácil de entender y modificar. En este caso, "comprensible" significa que cualquier desarrollador experimentado puede entender inmediatamente el código. Las siguientes características del código limpio son las que lo hacen fácil de leer:

- El orden de ejecución de toda la aplicación es lógico y está claramente estructurado.
- La conexión entre las diferentes partes del código es bastante obvia.
- La tarea o rol de cada clase, función, método y variable es

  inmediatamente comprensible.

El código es fácil de modificar si se puede adaptar y ampliar. Esto también facilita la corrección de errores en el código. El código limpio es, por lo tanto, muy fácil de mantener. El código fácilmente modificable tiene las siguientes características:

- Las clases y los métodos son pequeños y solo tienen una única tarea.
- Las clases y los métodos son predecibles, funcionan como se espera y están disponibles públicamente a través de API (interfaces) bien documentadas.
- El código utiliza pruebas unitarias.

Las ventajas de este tipo de programación son obvias. El código limpio no depende del desarrollador original. En principio, cualquier programador puede trabajar con el código. Esto evita problemas que pueden ocurrir cuando se trabaja con código heredado, por ejemplo. También es más fácil mantener el código porque los errores se pueden identificar y corregir más fácilmente.

**Características**

- El código se puede medir con "bueno" o "malo" en la revisión del código o por cuántos minutos te toma hablar sobre él.
- Un código limpio debe ser elegante, eficiente, legible, simple, sin duplicaciones y bien escrito.
- Debes agregar valor al negocio con su código.
- El código limpio ofrece calidad y comprensión cuando abrimos una clase. Es necesario que su código sea limpio y legible para que cualquier persona

  pueda encontrarlo y comprenderlo fácilmente. Evite perder el tiempo de los demás.

**Nombres significativos**

- Los nombres de las clases, variables y métodos deben ser significativos e

  indicar claramente qué hace un método o qué es un atributo.

- Crea nombres pronunciables para facilitar la comunicación.
- Evita las siglas y nombres confusos, que pueden llevar a conclusiones equivocadas a cualquiera que lea el código.
- Usa nombres que reflejen el dominio del sistema, el contexto y los problemas

  que deben resolverse.

**Funciones**

- El método debe ser fácil de leer y comprender.
- El método debe transmitir su intención.
- Los métodos deben ser pequeños.
- Otra regla para los métodos pequeños es que deben ser aún más pequeños. Deben tener hasta 20 líneas. (Creo que deberían tener hasta 10 líneas).
- Los métodos solo deben hacer una cosa: deben hacerlo de la manera correcta y simplemente hacerlo.
- Debes usar nombres con palabras que digan lo que realmente hace.
- El número óptimo de parámetros de un método es cero, después de uno y dos. Se deben evitar tres, pero si crees que se debe usar, ten una buena justificación.
- Los parámetros de tipo booleano como parámetro ya dice claramente que hace más de una cosa.
- Los métodos deben hacer algo y devolver algo.
- Evita la duplicación.

**Comentarios**

- Una de las razones más comunes de los comentarios es porque el código es malo.
- Si estás pensando en escribir un comentario, debes refactorizar el código.
- Los comentarios no guardan un código incorrecto.
- Trata de explicar lo que el código hace que suceda.
- Los comentarios pueden ser útiles cuando se colocan en ciertos lugares.
- Crea nombres de métodos y variables informativas en lugar de explicar el código con comentarios.
- Los comentarios se pueden utilizar para expresar la importancia de ciertos puntos en el código.
- El mejor comentario es el que debe escribirse porque tu código ya se explicó.
- No escribas comentarios con información redundante, inútil o falsa.
- No deben usarse para indicar quién cambió o por qué, porque eso ya existe en el control de versiones.
- No comentes el código que no se utilizará, elimínelo, solo contamina el código y

  no deja dudas en cualquiera que lea.

**Formateo**

- El formato debe indicar cosas de importancia ya que es una forma desarrolladora de comunicación.
- Un código desordenado es difícil de leer.
- La legibilidad del código tendrá efecto en todos los cambios que se realicen.
- Intenta escribir una clase con un máximo de 500 líneas. Las clases más pequeñas son más fáciles de entender.
- Establece un límite de caracteres por línea de código. Un buen límite de caracteres en una línea es 120.
- Intenta mantener verticalmente más conceptos relacionados a continuación para crear un flujo de código.
- Utiliza espacios entre operadores, parámetros y comas.

**Objetos y estructura de datos**

- Sigue la Ley de Deméter, que dice que un método M de un objeto O solo puede consumir servicios de los siguientes tipos de objetos:
- El objeto mismo, O.
- Los parámetros M.
- Cualquier objeto creado o instanciado por M.
- Componentes directos de O.
- Realiza una buena abstracción y encapsulación. No hagas objetos tontos. Los objetos ocultan la abstracción de datos y exponen métodos que operan los datos. Las estructuras de datos exponen sus datos y no tienen métodos significativos.

**Manejo de errores**

- Todos los programadores deben planificar cuidadosamente el manejo de errores.
- Cuando ocurren cosas malas, tenemos que conseguir que haga las cosas correctas.
- Deberíamos dar preferencia a lanzar una excepción que tratarla solo para ocultarla.
- Crea mensajes con información sobre el error.
- Menciona que falló. ¿Dónde estuvo este fracaso? Si es posible, menciona por qué falló.
- Mira reglas comerciales separadas para errores y manejo de errores.
- Evita devolver un NULL en los métodos, preferiblemente para devolver un objeto vacío.
- Evita pasar NULL a los métodos; esto puede generar NullPointerExceptions.

**Límites**

- En el código de terceros, para evitar pasar objetos, las API esperan mantener las cosas en la misma clase.
- Realiza pruebas en el tercero de la API.
- Estudia la documentación y prueba la API antes de empezar a usarla.
- Revisa bien las características que utilizarás.
- Estos pasos pueden ayudar a aumentar el rendimiento cuando hay nuevas actualizaciones de la API y solo puede ejecutar tus pruebas para verificar esta actualización.
- Crea pruebas de la funcionalidad de la API.

**Pruebas unitarias**

- Asegúrate de que cada pieza de código esté haciendo lo que espera que haga.
- Sigue la ley de TDD:
- No creas código antes de tener una prueba fallida.
- No creas más pruebas de las necesarias para fallar.
- No puedes escribir más código del suficiente para pasar la prueba que está fallando.
- Mantén tu prueba limpia.
- Las pruebas deben sufrir cambios de la misma manera que el código.
- Cuanto más sucio sea el código, más difícil será mantener la prueba.
- Usa la regla F.I.R.S.T para probar:
  - La prueba es rápida.
  - Las pruebas son independientes de otras.
  - La prueba es repetible en varios entornos.
  - La prueba es autovalidante.
  - La prueba es oportuna.
- La prueba es tan importante como el código de producción.

**Clases**

- De forma predeterminada, las clases de Java deben comenzar con las variables:
- Estático y constantemente público
- Privado estático y variable
- Instancias y variables privadas
- Poco después vienen las funciones
- El nombre de la clase debe representar su responsabilidad.
- La clase debe tener una sola responsabilidad.
- Saber el tamaño de la clase es ideal o no debemos medir su responsabilidad.
- Debes intentar hacer una breve descripción de la clase.
- Los métodos deben ser:
- Pequeños. e incluso más pequeños.
- Deben tener una sola responsabilidad.

**Sistemas**

- Es importante reconocer y separar las responsabilidades de un sistema.
- Debes estar separado y modularizar la ejecución lógica, permitiendo una estrategia independiente para resolver la dependencia de la aplicación.
- Es importante cuidar las inyecciones de dependencia y permitir que solo los objetos se ocupen del negocio de la lógica.
- Es muy difícil crear un sistema correctamente primero. Debes estar disponible para la historia, luego refactorizar y luego expandirse para continuar implementando nuevas historias.
- Para llegar al punto en que TDD es necesario, necesitas refactorizar y limpiar el código.
- Debemos construir una lógica a través de pruebas y evolucionar desde lo

  simple hasta interconectar los diversos aspectos necesarios.

Aquí están las reglas dadas por Kent Beck para crear buenos diseños:

- Ejecuta todas las pruebas. Verifica que el sistema se comporta como se esperaba.
- Elimina la duplicación porque el código duplicado trae trabajo adicional.
- Para expresar la intención del programador, usa un código más expresivo para facilitar el mantenimiento.
- Escoge buenos nombres para funciones, clases y pruebas que no deben ser pequeños y estar bien escritos.
- Minimiza el número de clases y métodos. Siguiendo este patrón se puede ignorar si las clases son muy pequeñas.
- Aplica todos los conocimientos para mejorar el diseño durante la refactorización. Aumenta la cohesión, reduce el acoplamiento, separa las responsabilidades, reduce las clases y los métodos, escoge los mejores nombres.

Incluso aplicándolo una vez, no podrás tener un buen software. Necesitas hacer esto una y otra vez para lograr una mejora continua.

**Concurrencia**

- La concurrencia es un aspecto que puede estar presente en los códigos.
- La concurrencia puede mejorar los tiempos de respuesta y la eficiencia de las aplicaciones.
- Debes considerar las siguientes ideas sobre la concurrencia:
- Inyecta cierta sobrecarga.
- Puede ser complejo de operar.
- Los errores causados pueden ser difíciles de reproducir.
- Por lo general, requiere cambios de diseño.
- El problema de concurrencia es que diferentes segmentos de una aplicación pueden estar siguiendo subprocesos múltiples enredados, lo que puede causar problemas inesperados en situaciones normales.
- Por razones de concurrencia, es importante que cada clase tenga una responsabilidad única.
- Crea secciones que estén sincronizadas y minimizadas. Ejecutar pruebas a menudo es la mejor manera de encontrar errores en el código. Sin embargo, es difícil de hacer cuando hay pruebas de concurrencia.
- Una buena forma de probar es insertar códigos para probar en medio del

  código implementado.

**Refinamiento Sucesivo**

- El trabajo de solo código no es suficiente para tener un buen código.
- **Los profesionales que solo se preocupan por el código que funciona no pueden ser considerados profesionales**.
- Debemos ignorar que no tenemos tiempo para refactorizar un código. El código que no se atendió hoy puede convertirse en un problema después de convertirse en un problema para el equipo porque nadie querrá meterse con él.
- Trata de no dejar que el código se deteriore. Es mucho más económico crear un código limpio que limpiar un código deteriorado, ya que moverse en una maraña puede ser una tarea ardua.
- La solución, entonces, se reduce a mantener el código lo más limpio posible y lo más simple posible sin dejar que comience a deteriorarse.

**Refactorización**

- Antes de realizar cualquier tipo de refactorización, es importante realizar buenas pruebas de cobertura.
- Después de aumentar o crear una cobertura de prueba, puedes comenzar a dejar el código más claro y corregir algunos errores.
- Ahora, después de dejar el código más claro, alguien más probablemente

  pueda limpiarlo aún más.

**Nombres**

- Escoge nombres descriptivos.
- Escoge nombres en el nivel apropiado de abstracción.
- Utiliza la nomenclatura estándar cuando sea posible.
- Utiliza nombres largos para ámbitos largos.
- Evita las codificaciones.
- Los nombres deben describir los efectos secundarios.

**Algunos principios del código limpio**

El código incorrecto es difícil de entender, es más complejo de lo que debería ser, no es fácil de probar y hace que otros desarrolladores se llenen de frustración. Si bien puede llevar más tiempo escribir código limpio a corto plazo, está más que establecido que escribir código limpio les ahorrará a todos tiempo, esfuerzo y, en última instancia, dinero.

Pero siempre hay lugar para aprender. Nadie escribe código limpio desde el principio.

El código limpio no se basa en reglas específicas del lenguaje. En su lugar, se basa en principios independientes del lenguaje acordados por la comunidad de desarrolladores:

KISS <https://en.wikipedia.org/wiki/KISS_principle> : Keep It Simple Stupid Mantenlo Simple Estúpido. Un principio de diseño originario de la Marina de los EE. UU. que ya se remonta a 1960. Establece que la mayoría de los sistemas deben mantenerse lo más simple posible (pero no más simple, como habría dicho Einstein). **Debe evitarse la complejidad innecesaria. La pregunta que debe hacerse cuando está escribiendo código es "¿se puede escribir esto de una manera más simple?"**

DRY <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself> : Don't Repeat Yourself No te repitas. Muy relacionado con KISS y la filosofía del diseño minimalista. Establece que cada pieza de conocimiento (código, en este caso) debe tener una representación única,

inequívoca y autorizada dentro de un sistema (código base). Las violaciones de DRY se denominan WET: disfrutamos escribir, escribir todo dos veces, perder el tiempo de todos. We Enjoy Typing, Write Everything Twice, Waste Everyone 's Time.

YAGNI <https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it> : No lo vas a necesitar. You Aren't Gonna Need It

Un desarrollador no debe agregar funcionalidad a menos que lo considere necesario. YAGNI es parte de la metodología Extreme Programming (XP), que busca mejorar la calidad del software y aumentar la capacidad de respuesta a los requisitos del cliente. YAGNI debe usarse junto con la refactorización continua, las pruebas unitarias y la integración.

Composición sobre herencia <https://en.wikipedia.org/wiki/Composition_over_inheritance> : Lamentablemente, no es un acrónimo. Es un principio en el que diseñas tus tipos sobre lo que hacen en lugar de sobre lo que son. Muchos desarrolladores prefieren la composición a la herencia, porque la herencia les obliga a construir una taxonomía de objetos al principio de un proyecto, lo que hace que su código sea inflexible para los cambios posteriores.

**Refactorización**

Hoy en día, el desarrollo de software ágil es literalmente imprescindible y los equipos ágiles mantienen y amplían mucho su código de iteración en iteración, y sin una refactorización continua, esto es difícil de lograr. Esto se debe a que el código no refactorizado tiende a degradarse: dependencias poco saludables entre clases o paquetes, mala asignación de responsabilidades de clase, demasiadas responsabilidades por método o clase, código duplicado y muchas otras variedades de confusión y desorden. Por lo tanto, las ventajas incluyen una mejor legibilidad del código y una menor complejidad capacidades que pueden mejorar la capacidad de mantenimiento del código fuente y crear una arquitectura interna más expresiva.

La refactorización del código se debe realizar como una serie de pequeños cambios, cada uno de los cuales mejora un poco el código existente y deja el programa en condiciones de funcionamiento. No mezcles un montón de refactorizaciones en un gran cambio.

Cuando refactorices, definitivamente debe hacerlo usando TDD y CI. Si no puedes ejecutar esas pruebas después de cada pequeño paso en una refactorización, creas el riesgo de introducir errores. El código debería volverse más limpio.

No se debe crear una nueva funcionalidad durante la refactorización. No mezcles la refactorización y el desarrollo directo de nuevas características. Intenta separar estos procesos al menos dentro de los límites de las confirmaciones individuales.

**Beneficios de la refactorización de código**

1. Ver la imágen completa

Si tienes un método principal que maneja toda la funcionalidad, lo más probable es que sea demasiado largo e increíblemente complejo. Pero si se divide en partes, es fácil ver lo que realmente se está haciendo.

2. Legibilidad para tu equipo

Haz que sea fácil de entender para tus compañeros, no lo escribas para ti mismo, piensa a largo plazo.

3. Mantenibilidad

La integración de actualizaciones y actualizaciones es un proceso continuo que es inevitable y debe ser bienvenido. Cuando el código base no está organizado y se basa en una base débil, los desarrolladores a menudo dudan en realizar cambios. Pero con la refactorización de código, el código organizado, el producto se construirá sobre una base limpia y estará listo para futuras actualizaciones.

4. Eficiencia

La refactorización de código puede considerarse una inversión, pero obtienes buenos resultados. Reduce el esfuerzo requerido para futuros cambios en el código, ya sea por ti o por otros desarrolladores, mejorando así la eficiencia.

5. Reducir la complejidad

Haz que sea más fácil para ti y tu equipo trabajar en el proyecto.

**Ejercicios**

Hay muchas técnicas de refactorización de código.En <https://refactoring.guru/refactoring/techniques> presenta algunas de las más comunes y útiles. Tu trabajo es encontrar las soluciones y como se pueden refactorizar. Presenta código funcional en el lenguaje de programación favorito código antes de refactorizar y luego de refactorizar, de la siguientes técnicas.

1. **Extract Method**

Separar bloques de código en métodos con nombres descriptivos puede hacer el código más claro y modular, facilitando la identificación de secciones que pueden ejecutarse en paralelo o requieren sincronización.

**Antes de refactorizar (Python):** class Report:

def print\_owing(self, amount):

self.print\_banner()

- print details

print(f"name: {self.name}") print(f"amount: {amount}")

def print\_banner(self):

print("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*") print("\*\*\*\*\* Customer Owes \*\*\*\*\*") print("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*")

Este es un ejemplo de un método que realiza dos tareas principales: imprimir un encabezado (banner) y luego imprimir detalles.

**Después de refactorizar (Python):**

class Report:

def print\_owing(self, amount):

self.print\_banner() self.print\_details(amount)

def print\_banner(self):

print("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*") print("\*\*\*\*\* Customer Owes \*\*\*\*\*") print("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*")

def print\_details(self, amount):

print(f"name: {self.name}") print(f"amount: {amount}")

La refactorización ha movido la impresión de detalles a su propio método `print\_details`. Esto hace que `print\_owing` sea más conciso y mejora la organización del código al separar claramente las responsabilidades entre los métodos.

2. **Inline method**

Fusionar métodos que son demasiado granulares puede reducir la sobrecarga de llamadas a métodos en ambientes de alta concurrencia, mejorando el rendimiento.

**Antes de refactorizar (Python):** class PizzaDelivery:

def \_\_init\_\_(self, number\_of\_late\_deliveries):

self.number\_of\_late\_deliveries = number\_of\_late\_deliveries

def get\_rating(self):

if self.more\_than\_five\_late\_deliveries():

return 2

else:

return 1

def more\_than\_five\_late\_deliveries(self):

return self.number\_of\_late\_deliveries >5

**Después de refactorizar (Python):** class PizzaDelivery:

def \_\_init\_\_(self, number\_of\_late\_deliveries):

self.number\_of\_late\_deliveries = number\_of\_late\_deliveries

def get\_rating(self):

return 2 if self.number\_of\_late\_deliveries >5 else 1

Hemos refactorizado el código de Python para que la comprobación se realice directamente dentro del método **get\_rating,** lo que elimina la necesidad del método **more than five late deliveries.**

3. **Extract variable**

Extraer expresiones en variables puede ayudar a identificar datos compartidos entre threads, lo cual es crucial para evitar condiciones de carrera.

**Antes de refactorizar (Python):**

class BannerRenderer:

def \_\_init\_\_(self, platform, browser,resize):

self.platform = platform

self.browser = browser

self.resize = resize

def render\_banner(self):

if (self.platform.upper().find('MAC') >-1 and

self.browser.upper().find('IE') > -1 and self.was\_initialized() and self.resize >0):

- do something

pass

def was\_initialized(self):

- Some initialization check pass

**Después de refactorizar (Python):**

class BannerRenderer:

def \_\_init\_\_(self, platform, browser,resize):

self.platform = platform

self.browser = browser

self.resize = resize

def render\_banner(self):

is\_mac\_os = 'MAC' in self.platform.upper() is\_ie = 'IE'in self.browser.upper() was\_resized = self.resize >0

if is\_mac\_os and is\_ie and self.was\_initialized() and was\_resized:

- do something

pass

def was\_initialized(self):

- Some initialization check pass

En la versión refactorizada en Python, hemos extraído las comprobaciones complejas del if en tres variables separadas: is\_mac\_os, is\_ie, y was\_resized. Esto hace que cada condición sea autoexplicativa y mejora significativamente la legibilidad del código.

4. **Replace temp with Query**

Fomenta el uso de métodos para calcular valores en lugar de variables temporales, lo cual puede simplificar la sincronización de acceso a datos entre múltiples threads.

**Antes de refactorizar (Python):**

class Order:

def \_\_init\_\_(self, quantity,item\_price):

self.quantity = quantity self.item\_price = item\_price

def base\_price(self):

return self.quantity \*self.item\_price

def has\_discount(self):

base\_price = self.base\_price() return base\_price >1000

**Después de refactorizar (Python):** class Order:

def \_\_init\_\_(self, quantity,item\_price):

self.quantity = quantity self.item\_price = item\_price

def base\_price(self):

return self.quantity \*self.item\_price

def has\_discount(self):

return self.base\_price() >1000

En la versión refactorizada, la llamada al método base\_price() reemplaza a la variable temporal base\_price directamente en la condición. Esto hace que el código sea más conciso y directo, evitando la necesidad de una variable temporal que solo se usa una vez.

5. **Remove assignments to parameters**

Modificar parámetros dentro de una función puede llevar a efectos secundarios inesperados en un entorno concurrente; evitarlo hace que el código sea más seguro en términos de concurrencia.

**Antes de refactorizar (Python):** def calculate\_total(base\_price):

if base\_price >1000:

base\_price \*=0.95

else:

base\_price \*=0.98

return base\_price

**Después de refactorizar (Python):** def calculate\_total(base\_price):

if base\_price >1000:

return base\_price \*0.95

else:

return base\_price \*0.98

En este ejemplo refactorizado, en lugar de modificar base\_price directamente, simplemente devolvemos el resultado de la expresión, lo cual es una práctica más segura y clara. Si base\_price necesitara ser calculado dentro de la función, podríamos introducir una nueva variable local para eso.

6. **Replace method with method object**

Convierte métodos en objetos que pueden ser ejecutados en paralelo, facilitando la división del trabajo y la gestión del estado local de cada tarea.

**Antes de refactorizar (Python):** class Order:

- ...

def price(self):

primary\_base\_price = 0 secondary\_base\_price = 0 tertiary\_base\_price = 0

- Perform long computation.
- ...
- return the computed price

**Después de refactorizar (Python):** class Order:

- ...

def price(self):

return PriceCalculator(self).compute()

class PriceCalculator:

def \_\_init\_\_(self, order):

self.order = order

self.primary\_base\_price = 0 self.secondary\_base\_price = 0 self.tertiary\_base\_price = 0

- Copy relevant information from the order object.
- ...

def compute(self):

- Perform long computation.
- ...
- return the computed price

En este ejemplo refactorizado, la lógica de cálculo del precio se ha trasladado a una clase PriceCalculator. Cada uno de los precios base se convierte en un campo de la nueva clase, lo que permite un manejo más claro y modular del estado durante el cálculo. Además, separar la lógica de cálculo en su propia clase facilita la ejecución en paralelo de múltiples cálculos y ayuda a gestionar el estado local de cada tarea.

7. **Split Temporary Variable**

Evita la reutilización de variables temporales en contextos donde múltiples threads pueden modificarlas, reduciendo así el riesgo de condiciones de carrera.

**Antes de refactorizar (Python):**

def calculate\_geometry(height, width):

temp = 2 \* (height + width)

print(temp) # Supuestamente imprime el perímetro temp = height \* width

print(temp) # Supuestamente imprime el área

**Después de refactorizar (Python):**

def calculate\_geometry(height, width):

perimeter = 2 \* (height + width)

print(perimeter) # Ahora es claro que esto imprime el perímetro area = height \* width

print(area) # Y esto imprime el área, cada uno con su propia variable

En el código refactorizado, utilizamos perimeter y area como variables independientes para almacenar el perímetro y el área, respectivamente. Esto elimina la ambigüedad de qué valor se está imprimiendo y hace que el código sea más fácil de entender y mantener. Además, al tener variables separadas, se minimiza el riesgo de errores en entornos de programación concurrente.

8. **Encapsulate Collection**

Encapsular colecciones y proveer métodos para su acceso y modificación puede ayudar a controlar cómo y cuándo se accede a datos compartidos, facilitando la sincronización.

**Antes de refactorizar** class Order:

def \_\_init\_\_(self):

self.product\_ids = []

- ... otros métodos ...

**Después de refactorizar** class Order:

def \_\_init\_\_(self):

self.\_product\_ids = []

def add\_product\_id(self, product\_id):

self.\_product\_ids.append(product\_id)

def remove\_product\_id(self, product\_id): self.\_product\_ids.remove(product\_id)

def get\_product\_ids(self):

return list(self.\_product\_ids) # Retorna una copia para evitar modificaciones

externas

- ... otros métodos ...

En el código refactorizado, la colección \_product\_ids es privada (\_ es una convención para indicar que un atributo es de uso interno). Se proporcionan métodos para agregar y eliminar IDs de productos, y para obtener la lista de IDs. Importante notar que get\_product\_ids retorna una copia de la lista, lo que evita que el receptor de la lista pueda modificar la colección original dentro de la clase Order. Esto es un aspecto clave de la encapsulación que ayuda a mantener la integridad del estado interno de la clase.

9. **Replace Conditional with Polymorphism**

Utilizar polimorfismo en lugar de condicionales para manejar comportamientos basados en tipos puede simplificar el código y mejorar su extensibilidad, lo cual es útil cuando se diseñan sistemas distribuidos que deben ser flexibles y escalables.

**Antes de refactorizar**

class Shape:

def \_\_init\_\_(self, shape\_type, width=None, height=None, radius=None):

self.shape\_type = shape\_type

self.width = width

self.height = height

self.radius = radius

def calculate\_area(self):

if self.shape\_type == "square":

return self.width \* self.width elif self.shape\_type == "circle":

return 3.14 \* self.radius \* self.radius elif self.shape\_type == "triangle": return 0.5 \* self.width \* self.height

**Después de refactorizar**

class Shape:

def calculate\_area(self):

pass

class Square(Shape):

def \_\_init\_\_(self, width):

self.width = width

def calculate\_area(self):

return self.width \* self.width

class Circle(Shape):

def \_\_init\_\_(self, radius): self.radius = radius

def calculate\_area(self):

return 3.14 \* self.radius \* self.radius

class Triangle(Shape):

def \_\_init\_\_(self, width, height):

self.width = width

self.height = height

def calculate\_area(self):

return 0.5 \* self.width \* self.height

Esta refactorización hace que el código sea más legible, mantenible y extensible, ya

que cada clase se encarga de su propio comportamiento específico en lugar de tener un bloque de condicionales en la clase principal.

10. **Introduce Parameter Object**

Agrupar parámetros relacionados en objetos puede simplificar la firma de los métodos y mejorar la organización del código, lo que es especialmente útil en operaciones distribuidas que requieren múltiples datos de entrada.

**Antes de refactorizar**

class Calculator:

def calculate(self, num1, num2, operation):

- Implementación del método

pass

def save\_result(self, result, timestamp, user):

- Implementación del método

pass

- Llamadas a los métodos

calculator = Calculator()

calculator.calculate(10, 5, 'addition') calculator.save\_result(15, '2024-04-20', 'user123') **Después de refactorizar**

class Calculation:

def \_\_init\_\_(self, num1, num2, operation):

self.num1 = num1

self.num2 = num2

self.operation = operation

class Result:

def \_\_init\_\_(self, value, timestamp, user):

self.value = value

self.timestamp = timestamp

self.user = user

class Calculator:

def calculate(self, calculation):

- Implementación del método usando calculation.num1, calculation.num2, etc. pass

def save\_result(self, result):

- Implementación del método usando result.value, result.timestamp, etc. pass
- Llamadas a los métodos

calculator = Calculator()

calculation = Calculation(10, 5, 'addition') result = Result(15, '2024-04-20', 'user123') calculator.calculate(calculation) calculator.save\_result(result)

En este ejemplo refactorizado, los parámetros relacionados para la operación de cálculo se agrupan en un objeto Calculation, y los parámetros relacionados para guardar el resultado se agrupan en un objeto Result. Esto simplifica la firma de los métodos y mejora la organización del código al proporcionar una estructura más clara y coherente. Además, facilita la gestión de múltiples datos de entrada en operaciones distribuidas.

Completa el código de refactorización dado en: [https://github.com/kapumota/Actividades- C8286/blob/main/Caso-Refactorizacion.ipynb](https://github.com/kapumota/Actividades-C8286/blob/main/Caso-Refactorizacion.ipynb)

**Uso básico de threads**

Implementar un programa que utilice threads para realizar múltiples tareas en paralelo. Utiliza un nombramiento significativo de threads y uso de funciones para separar lógica.

**Multiprocesamiento y pool de trabajadores**

Usa **multiprocessing.Pool** para paralelizar tareas intensivas en CPU. Aplica el principio DRY al dividir las tareas en funciones reutilizables.

**Asyncio básico**

Crea un programa que utilice **asyncio** para manejar operaciones de E/S de manera asincrónica. Utiliza una estructura clara de corutinas y manejo de excepciones.

**Uso de Futures en Concurrent**

Emplea **concurrent.futures** para ejecutar tareas de manera asincrónica. Utiliza context managers para gestionar correctamente los recursos.

**Programación distribuida con Dask**

Implementa un flujo de trabajo distribuido usando Dask. Usa la modularización del código y comentarios claros que expliquen la lógica.

**Procesamiento paralelo de datos con Pandas y Dask**

Usa Dask para paralelizar operaciones de datos pesados con Pandas. Organiza del código en pequeñas unidades lógicas.

**Sockets para comunicación en red**

Crea un sistema básico cliente-servidor usando sockets. Muestra una separación clara entre lógica de cliente y servidor y un manejo adecuado de excepciones.

**Uso avanzado de Asyncio**

Implementa un chat server utilizando **asyncio** para manejar múltiples conexiones de cliente. Aplica de KISS para mantener la simplicidad en el manejo de conexiones.

**Creación de un Sistema de Colas de Mensajes**

Desarrolla un sistema de colas de mensajes básico para procesamiento distribuido de tareas. Utiliza código modular y principio YAGNI para evitar sobreingeniería.

**Tareas en paralelo con Celery**

Configura un proyecto simple con Celery para ejecutar tareas en paralelo. La estructura del proyecto debe ser clara, uso de nombres de tareas descriptivos y documentación.


Para cada uno de estos ejercicios, es crucial aplicar las siguientes prácticas de código limpio y estándares:![](Aspose.Words.76263f85-51e4-469a-9743-8ef3a29a4cc9.003.png)![ref1]

- **PEP8:** Seguir las guías de estilo de PEP8 para la consistencia del código.
- **Refactorización:** Después de la primera implementación, revisar el código para simplificarlo y mejorarlo.
- **KISS:** Mantener cada solución lo más simple posible.
- **DRY:** No repetir código; usar funciones y módulos para reutilizar la lógica.
- **YAGNI:** No añadir funcionalidades hasta que sean estrictamente necesarias.

SOLUCION: <https://colab.research.google.com/drive/1WQq7vSKTiE0iTH3oiBiVnrX6eSvizJM9?usp=sharing>

**Entregable:**

Presenta el código completo desarrollado en tu repositorio personal hasta el dia 19 de abril (medianoche). Puedes utilizar el codigo de muestra para ayudarte a guiarte para estos ejercicios. Recuerda que debes interiorizar estas reglas, técnicas para futuras implementacione.

El código de muestra esta aquí: [https://github.com/kapumota/Actividades- C8286/blob/main/Evaluacion2/Ejercicios.py](https://github.com/kapumota/Actividades-C8286/blob/main/Evaluacion2/Ejercicios.py)

[ref1]: Aspose.Words.76263f85-51e4-469a-9743-8ef3a29a4cc9.002.png
