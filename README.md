### **🌀 Dominando la Lógica en Python: Katas y Retos Programáticos**

### **Descripción del Proyecto**

El proyecto **"Katas de Python"** consiste en la implementación de funciones y programas que abordan conceptos fundamentales de programación en Python. Este conjunto de ejercicios tiene como objetivo aplicar y reforzar conocimientos en:

1. Manejo de tipos de datos básicos y funciones incorporadas.  
2. Uso de estructuras de datos en Python y sus métodos.  
3. Implementación de condicionales, estructuras de iteración y funciones personalizadas.  
4. Programación Orientada a Objetos (POO).  
5. Uso de funciones integradas como map, filter y reduce.  
6. Manejo de excepciones y buenas prácticas en programación.

El enfoque principal del proyecto es resolver problemas prácticos que permitan entender cómo trabajar con datos y estructuras comunes en Python, a través de ejercicios diversos y realistas.

### **Estructura del Proyecto**

El proyecto está organizado de la siguiente manera:

├── funciones/ \# Código de las funciones organizadas por temática  
├── pruebas/ \# Comentarios dentro del código para probar el funcionamiento  
de las funciones  
├── README.md \# Documentación del proyecto

### **Instalación y Requisitos**

Para ejecutar este proyecto, necesitarás:

* **Python 3.8 o superior**: Se recomienda un entorno virtual para gestionar las dependencias.  
* Un editor de código como **VSCode**.

### **Ejercicios Implementados**

A continuación, se enumeran algunos de los ejercicios desarrollados con una breve descripción:

1. **Cálculo de frecuencias de letras:** Función que devuelve un diccionario con la frecuencia de letras en un texto.  
2. **Doblar valores:** Usa map() para duplicar los valores en una lista.  
3. **Filtrar palabras objetivo:** Devuelve palabras de una lista que contengan un texto específico.  
4. **Diferencia entre listas:** Calcula la diferencia elemento a elemento entre dos listas.  
5. **Media y estado de notas:** Calcula el promedio de una lista y determina si está aprobada.  
6. **Factorial recursivo:** Implementación del cálculo factorial mediante recursión.  
7. **Lista de tuplas a strings:** Convierte una lista de tuplas en una lista de cadenas usando map().  
8. **División con manejo de excepciones:** Programa que divide dos números y maneja entradas inválidas o divisiones por cero.  
9. **Filtro de mascotas prohibidas:** Excluye mascotas específicas de una lista usando filter().  
10. **Cálculo de promedio con excepción:** Calcula la media y lanza un error si la lista está vacía.  
11. **Validación de edades:** Solicita una edad y maneja valores fuera del rango o no numéricos.

### **Resultados del Proyecto**

#### **Resultados Destacados**

* **Uso de map, filter y reduce:** Los ejercicios destacan el uso práctico de estas funciones para manipular listas y secuencias de manera eficiente.  
* **Programación Orientada a Objetos:** Se implementaron clases como Arbol y UsuarioBanco, que ejemplifican el uso de métodos, atributos y casos de uso específicos.  
* **Manejo de Excepciones:** Se abordaron problemas relacionados con entradas inválidas y cómo manejar errores de manera clara para el usuario final.

#### **Patrones de Código**

1. Se priorizó la legibilidad y modularidad de las funciones.  
2. Se implementaron pruebas directas dentro de cada script para verificar su funcionamiento.  
3. Se incluyeron comentarios sobre dificultades encontradas y cómo se resolvieron.

### **Dificultades Encontradas y Soluciones**

**Manejo de entradas inválidas:**

* **Ejercicio 8 (División):** La principal dificultad fue garantizar que el programa no fallara ante entradas no numéricas o intentos de dividir por cero. Esto se resolvió utilizando bloques `try` y `except`, asegurando un manejo robusto de excepciones y proporcionando mensajes claros al usuario.  
* **Ejercicio 11 (Validación de edades):** Fue un desafío verificar que la entrada del usuario estuviera dentro de un rango lógico (0-120) y manejar valores no numéricos o fuera del rango. Se resolvió de manera similar a la consulta 8, utilizando excepciones y validaciones adicionales.  
  **Uso de argumentos variables:**  
* **Ejercicio 37 (Procesar texto):** Este ejercicio requería manejar diferentes tipos y cantidades de argumentos según la operación seleccionada (`contar_palabras`, `reemplazar_palabras`, `eliminar_palabra`). La dificultad principal fue garantizar que cada opción recibiera los argumentos necesarios. Esto se resolvió usando `*args` y verificando su longitud antes de proceder.  
  **Normalización de texto:**  
* **Ejercicios 31, 32 y 37:** En ejercicios relacionados con búsquedas y procesamiento de texto, surgieron inconsistencias debido a la presencia de puntuación y diferencias entre mayúsculas y minúsculas. Esto se abordó eliminando signos de puntuación con `strip()` y normalizando el texto con `lower()` para garantizar comparaciones consistentes.  
  **Modelado con clases:**  
* **Ejercicio 34 (Clase `Arbol`):** Un desafío clave fue gestionar dinámicamente los atributos del árbol, como las ramas y su longitud. También se presentó la dificultad de manejar índices incorrectos al eliminar ramas, lo cual se resolvió validando la posición antes de realizar la operación.  
  **Verificación de usuarios y empleados:**  
* **Ejercicio 32 (Buscar puesto en empleados):** Hubo dificultades para comparar nombres ingresados por el usuario con los almacenados en la lista, debido a inconsistencias en el formato (espacios adicionales o diferencias en mayúsculas/minúsculas). Esto se resolvió normalizando las entradas del usuario y los datos de la lista.  
  **Cálculo dinámico de descuentos:**  
* **Ejercicio 41 (Cálculo de monto final con descuento):** Un desafío fue validar que el descuento fuera lógico (mayor a 0 y no superior al precio del artículo). Esto se resolvió añadiendo validaciones explícitas y asegurando que los resultados siempre fueran positivos.

### **Conclusión**

Este proyecto demostró cómo aplicar conceptos básicos y avanzados de Python para resolver problemas comunes. La implementación de buenas prácticas, como el manejo de excepciones, la reutilización de código y la modularidad, permitió crear soluciones efectivas y adaptables. Estas katas sirven como base para proyectos más avanzados y refuerzan habilidades esenciales en el desarrollo con Python.

### **Autor y Agradecimientos**

* **Autor:** Ana Nieto Carrera  
* **Datos Inspirados:** Proyecto de base de datos dado por la plataforma.

