# Consulta 1: 
# Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario 
# con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def calcular_frecuencia_letras(cadena):
    """
    Calcula las frecuencias de cada letra en una cadena de texto, ignorando espacios.

    Args:
        cadena (str): La cadena de texto de entrada.

    Returns:
        dict: Un diccionario con las letras como claves y sus frecuencias como valores.
    """
    # Eliminar espacios y convertir a minúsculas para un conteo consistente
    cadena = cadena.replace(" ", "").lower()

    # Inicializar el diccionario de frecuencias
    frecuencias = {}

    # Recorrer cada letra en la cadena
    for letra in cadena:
        if letra.isalpha():  # Considerar solo letras
            frecuencias[letra] = frecuencias.get(letra, 0) + 1

    return frecuencias

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    # Cadena predeterminada
    texto_predeterminado = "Hoy hace frío"
    print(f"Calculando frecuencias para la frase: '{texto_predeterminado}'\n")

    # Calcular la frecuencia de letras
    resultado = calcular_frecuencia_letras(texto_predeterminado)

    # Mostrar el resultado
    print("Frecuencia de letras:")
    for letra, frecuencia in resultado.items():
        print(f"'{letra}': {frecuencia}")

# Consulta 2:
# Dada una lista de números, obtén una nueva lista con el doble de cada valor.
# Usa la función map() sin encapsularla en una función adicional.

# Lista de números de ejemplo
lista_numeros = [1, 2, 3, 4, 5]

print(f"Lista original: {lista_numeros}")

# Aplicar la función map() directamente
lista_duplicada = list(map(lambda x: x * 2, lista_numeros))

print(f"Lista con valores duplicados: {lista_duplicada}")

# Consulta 3:
# Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.
# La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def filtrar_palabras(lista_palabras, palabra_objetivo):
    """
    Filtra una lista de palabras para devolver solo aquellas que contienen la palabra objetivo.

    Args:
        lista_palabras (list): Lista de palabras originales.
        palabra_objetivo (str): Palabra que debe estar contenida en las palabras filtradas.

    Returns:
        list: Lista de palabras que contienen la palabra objetivo.
    """
    return [palabra for palabra in lista_palabras if palabra_objetivo in palabra]

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    # Lista de palabras y palabra objetivo
    lista = ["perro", "gato", "ratón", "periquito", "caballo", "pato"]
    objetivo = "per"

    print(f"Lista original: {lista}")
    print(f"Palabra objetivo: '{objetivo}'")

    # Filtrar las palabras
    resultado = filtrar_palabras(lista, objetivo)

    print(f"Palabras que contienen '{objetivo}': {resultado}")

# Consulta 4:
# Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

def calcular_diferencias(lista1, lista2):
    """
    Calcula la diferencia entre los valores correspondientes de dos listas.

    Args:
        lista1 (list): Primera lista de valores numéricos.
        lista2 (list): Segunda lista de valores numéricos.

    Returns:
        list: Lista con las diferencias entre los valores de las dos listas.
    """
    if len(lista1) != len(lista2):
        raise ValueError("Las listas deben tener la misma longitud.")

    return list(map(lambda x, y: x - y, lista1, lista2))

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    # Listas de ejemplo
    lista_a = [10, 20, 30, 40, 50]
    lista_b = [5, 15, 25, 35, 45]

    print(f"Lista 1: {lista_a}")
    print(f"Lista 2: {lista_b}")

    # Calcular diferencias
    diferencias = calcular_diferencias(lista_a, lista_b)

    print(f"Diferencias entre las listas: {diferencias}")

# Consulta 5:
# Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, 
# que por defecto es 5. La función debe calcular la media de los números en la lista y determinar 
# si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado", de lo contrario, 
# será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def calcular_estado(lista_numeros, nota_aprobado=5):
    """
    Calcula la media de una lista de números y determina si el estado es "aprobado" o "suspenso".

    Args:
        lista_numeros (list): Lista de números.
        nota_aprobado (float): Nota mínima para aprobar (por defecto 5).

    Returns:
        tuple: Una tupla con la media y el estado ("aprobado" o "suspenso").
    """
    if not lista_numeros:
        raise ValueError("La lista de números no puede estar vacía.")
    
    # Calcular la media
    media = sum(lista_numeros) / len(lista_numeros)

    # Determinar el estado
    estado = "aprobado" if media >= nota_aprobado else "suspenso"

    return media, estado

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    # Lista de números de ejemplo
    lista_notas = [6, 7, 5, 8, 9]

    # Calcular estado con el valor por defecto de nota_aprobado
    media, estado = calcular_estado(lista_notas)

    print(f"Notas: {lista_notas}")
    print(f"Media: {media:.2f}")
    print(f"Estado: {estado}")

    # Calcular estado con un valor diferente de nota_aprobado
    nueva_nota_aprobado = 7
    media, estado = calcular_estado(lista_notas, nueva_nota_aprobado)

    print(f"\nCon nota de aprobado: {nueva_nota_aprobado}")
    print(f"Media: {media:.2f}")
    print(f"Estado: {estado}")

# Consulta 6:
# Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    """
    Calcula el factorial de un número de manera recursiva.

    Args:
        n (int): Número para calcular el factorial (debe ser >= 0).

    Returns:
        int: El factorial de n.

    Raises:
        ValueError: Si n es negativo.
    """
    if n < 0:
        raise ValueError("El número debe ser mayor o igual a 0.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    # Número de ejemplo
    numero = 5

    # Calcular el factorial
    try:
        resultado = factorial(numero)
        print(f"El factorial de {numero} es: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")

# Consulta 7:
# Genera una lista de strings a partir de una lista de tuplas usando la función map().

# Lista de tuplas de ejemplo
lista_tuplas = [(1, 2), (3, 4), ("hola", "mundo"), ("Python", 3.9)]

print(f"Lista original: {lista_tuplas}")

# Convertir la lista de tuplas en una lista de strings usando map()
lista_strings = list(map(lambda tupla: " ".join(map(str, tupla)), lista_tuplas))

print(f"Lista convertida a strings: {lista_strings}")


# Consulta 8:
# Escribe un programa que pida al usuario dos números e intente dividirlos.
# Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada.
# Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

def dividir_numeros():
    """
    Pide dos números al usuario, intenta dividirlos y maneja excepciones en caso de errores.
    """
    try:
        # Solicitar los números al usuario
        numerador = float(input("Introduce el numerador: "))
        denominador = float(input("Introduce el denominador: "))
        
        # Realizar la división
        resultado = numerador / denominador
        print(f"La división fue exitosa. El resultado es: {resultado:.2f}")

    except ValueError:
        # Manejar el caso de entrada no numérica
        print("Error: Por favor, introduce valores numéricos válidos.")

    except ZeroDivisionError:
        # Manejar el caso de división por cero
        print("Error: No se puede dividir entre cero.")

    except Exception as e:
        # Manejar cualquier otro tipo de error inesperado
        print(f"Ha ocurrido un error inesperado: {e}")

# Ejemplo para ejecutar el programa
if __name__ == "__main__":
    dividir_numeros()
 # Comentario sobre dificultad:
    # Uno de los desafíos fue recordar incluir la conversión a float al leer la entrada,
    # ya que la función input devuelve siempre una cadena. Esto provocaba errores
    # al intentar realizar operaciones matemáticas directamente sin conversión.


# Consulta 9:
# Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista 
# excluyendo ciertas mascotas prohibidas en España. 
# La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().

def filtrar_mascotas(lista_mascotas):
    """
    Filtra una lista de nombres de mascotas, excluyendo aquellas que están prohibidas en España.

    Args:
        lista_mascotas (list): Lista de nombres de mascotas.

    Returns:
        list: Nueva lista con las mascotas permitidas.
    """
    # Lista de mascotas prohibidas
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

    # Filtrar mascotas usando filter
    mascotas_permitidas = filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas)

    return list(mascotas_permitidas)

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    # Lista de mascotas de ejemplo
    lista_mascotas_usuario = ["Perro", "Gato", "Mapache", "Canario", "Serpiente Pitón", "Conejo"]

    print(f"Lista original: {lista_mascotas_usuario}")

    # Filtrar mascotas
    lista_permitidas = filtrar_mascotas(lista_mascotas_usuario)

    print(f"Lista permitida: {lista_permitidas}")

# Consulta 10:
# Escribe un programa que reciba una lista de números y calcule su promedio.
# Si la lista está vacía, lanza una excepción estándar y maneja el error adecuadamente.

def calcular_promedio(lista_numeros):
    """
    Calcula el promedio de una lista de números.

    Args:
        lista_numeros (list): Lista de números.

    Returns:
        float: Promedio de los números en la lista.

    Raises:
        ValueError: Si la lista está vacía.
    """
    if not lista_numeros:  # Verificar si la lista está vacía
        raise ValueError("La lista está vacía. No se puede calcular el promedio.")

    return sum(lista_numeros) / len(lista_numeros)

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    try:
        # Lista de ejemplo
        lista = [10, 20, 30, 40, 50]  # Cambia esta lista a [] para probar el error

        print(f"Lista: {lista}")

        # Calcular el promedio
        promedio = calcular_promedio(lista)

        print(f"El promedio es: {promedio:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")


# Consulta 11:
# Escribe un programa que pida al usuario que introduzca su edad.
# Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120),
# maneja las excepciones adecuadamente.

def pedir_edad():
    """
    Pide al usuario que introduzca su edad y maneja errores si la entrada no es válida.
    """
    try:
        # Solicitar edad al usuario
        edad = int(input("Introduce tu edad: "))

        # Verificar si la edad está en el rango válido
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120 años.")

        print(f"Edad introducida correctamente: {edad} años.")

    except ValueError as e:
        # Manejar errores de entrada no válida o rango fuera de lo permitido
        print(f"Error: {e}")

    except Exception as e:
        # Manejar cualquier otro error inesperado
        print(f"Ha ocurrido un error inesperado: {e}")

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    pedir_edad()
# Comentario sobre dificultad:
    # Una dificultad fue considerar el caso en el que el usuario ingresa una edad 
    # como número flotante (por ejemplo, 25.5), ya que `int(input())` generará un error.
    # Este caso puede requerir una validación adicional si se permite el uso de números enteros y decimales.


# Consulta 12:
# Genera una lista con la longitud de cada palabra en una frase usando la función map().

# Frase de ejemplo
frase_ejemplo = "Hoy es un buen día para aprender Python"

print(f"Frase: '{frase_ejemplo}'")

# Obtener la lista de longitudes usando map() directamente
longitudes = list(map(len, frase_ejemplo.split()))

print(f"Longitudes de las palabras: {longitudes}")


# Consulta 13:
# Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas
# con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas.
# Usa la función map().

def letras_mayusculas_minusculas(conjunto):
    """
    Devuelve una lista de tuplas con cada letra en mayúsculas y minúsculas, 
    sin repetir caracteres.

    Args:
        conjunto (iterable): Conjunto de caracteres (string, lista, etc.).

    Returns:
        list: Lista de tuplas con las letras en formato (mayúscula, minúscula).
    """
    # Eliminar duplicados y considerar solo caracteres alfabéticos
    caracteres_unicos = set(filter(str.isalpha, conjunto))

    # Generar la lista de tuplas usando map()
    return list(map(lambda c: (c.upper(), c.lower()), caracteres_unicos))

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    # Conjunto de caracteres de ejemplo
    conjunto_caracteres = "aAbBccDd123!!"

    print(f"Conjunto original: '{conjunto_caracteres}'")

    # Generar la lista de tuplas
    resultado = letras_mayusculas_minusculas(conjunto_caracteres)

    print(f"Lista de tuplas (mayúscula, minúscula): {resultado}")

# Consulta 14:
# Crea una función que retorne las palabras de una lista de palabras que comiencen con una letra en específico.
# Usa la función filter().

def palabras_con_letra(lista_palabras, letra):
    """
    Filtra las palabras de una lista que comienzan con una letra específica.

    Args:
        lista_palabras (list): Lista de palabras.
        letra (str): Letra con la que deben comenzar las palabras.

    Returns:
        list: Lista de palabras que comienzan con la letra dada.
    """
    if len(letra) != 1 or not letra.isalpha():
        raise ValueError("La letra debe ser un único carácter alfabético.")

    # Convertir la letra a minúscula para comparación
    letra = letra.lower()

    # Filtrar palabras que comiencen con la letra específica
    return list(filter(lambda palabra: palabra.lower().startswith(letra), lista_palabras))

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    # Lista de palabras de ejemplo
    lista = ["manzana", "mango", "pera", "plátano", "melocotón", "sandía"]

    # Letra específica
    letra_especifica = "m"

    print(f"Lista original: {lista}")
    print(f"Letra específica: '{letra_especifica}'")

    # Filtrar palabras
    palabras_filtradas = palabras_con_letra(lista, letra_especifica)

    print(f"Palabras que comienzan con '{letra_especifica}': {palabras_filtradas}")

# Consulta 15:
# Crea una función lambda que sume 3 a cada número de una lista dada.

# Usando map() con una función lambda
sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    # Lista de números de ejemplo
    lista_numeros = [1, 2, 3, 4, 5]

    print(f"Lista original: {lista_numeros}")

    # Aplicar la función lambda
    nueva_lista = sumar_tres(lista_numeros)

    print(f"Lista después de sumar 3 a cada número: {nueva_lista}")

# Consulta 16:
# Escribe una función que tome una cadena de texto y un número entero n como parámetros
# y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().

def palabras_mas_largas(cadena, n):
    """
    Devuelve una lista de palabras en la cadena que tienen una longitud mayor que n.

    Args:
        cadena (str): Cadena de texto de entrada.
        n (int): Número entero que define la longitud mínima de las palabras a incluir.

    Returns:
        list: Lista de palabras más largas que n.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("El parámetro n debe ser un número entero positivo.")

    # Dividir la cadena en palabras
    palabras = cadena.split()

    # Filtrar las palabras más largas que n
    return list(filter(lambda palabra: len(palabra) > n, palabras))

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    # Cadena de ejemplo y valor de n
    cadena_ejemplo = "Python es un lenguaje de programación increíble"
    n = 5

    print(f"Cadena original: '{cadena_ejemplo}'")
    print(f"Palabras más largas que {n} caracteres:")

    # Llamar a la función
    palabras_filtradas = palabras_mas_largas(cadena_ejemplo, n)

    print(palabras_filtradas)

# Consulta 17:
# Crea una función que tome una lista de dígitos y devuelva el número correspondiente.
# Por ejemplo, [5, 7, 2] corresponde al número quinientos setenta y dos (572).
# Usa la función reduce().

from functools import reduce

def convertir_a_numero(lista_digitos):
    """
    Convierte una lista de dígitos en el número correspondiente.

    Args:
        lista_digitos (list): Lista de dígitos (números enteros entre 0 y 9).

    Returns:
        int: Número formado por los dígitos de la lista.

    Raises:
        ValueError: Si algún elemento de la lista no es un dígito válido.
    """
    if not all(isinstance(d, int) and 0 <= d <= 9 for d in lista_digitos):
        raise ValueError("Todos los elementos de la lista deben ser dígitos (enteros entre 0 y 9).")

    # Usar reduce para combinar los dígitos en un número
    return reduce(lambda x, y: x * 10 + y, lista_digitos)

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    # Lista de dígitos de ejemplo
    lista_digitos = [5, 7, 2]

    print(f"Lista de dígitos: {lista_digitos}")

    # Convertir a número
    try:
        numero = convertir_a_numero(lista_digitos)
        print(f"Número correspondiente: {numero}")
    except ValueError as e:
        print(f"Error: {e}")

# Consulta 18:
# Escribe un programa que cree una lista de diccionarios con información de estudiantes
# y use la función filter() para extraer a los estudiantes con una calificación mayor o igual a 90.

# Lista de estudiantes de ejemplo
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 89},
    {"nombre": "María", "edad": 19, "calificacion": 90},
    {"nombre": "Juan", "edad": 21, "calificacion": 72},
    {"nombre": "Sofía", "edad": 23, "calificacion": 99}
]

print("Lista de estudiantes:")
for estudiante in estudiantes:
    print(estudiante)

# Filtrar estudiantes con calificación mayor o igual a 90 usando filter() directamente
destacados = list(filter(lambda estudiante: estudiante['calificacion'] >= 90, estudiantes))

print("\nEstudiantes con calificación mayor o igual a 90:")
for estudiante in destacados:
    print(estudiante)


# Consulta 19:
# Crea una función lambda que filtre los números impares de una lista dada.

# Usando filter() con una función lambda
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    # Lista de números de ejemplo
    lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(f"Lista original: {lista_numeros}")

    # Filtrar los números impares
    lista_impares = filtrar_impares(lista_numeros)

    print(f"Números impares en la lista: {lista_impares}")

# Consulta 20:
# Para una lista con elementos tipo integer y string, obtén una nueva lista solo con los valores int.
# Usa la función filter() sin encapsularla en una función.

# Lista de ejemplo con elementos mixtos
lista_mixta = [1, "hola", 3.5, 42, "Python", -7, 0, True]

print(f"Lista original: {lista_mixta}")

# Filtrar valores enteros usando filter() directamente
lista_enteros = list(filter(lambda x: isinstance(x, int) and not isinstance(x, bool), lista_mixta))

print(f"Lista con solo enteros: {lista_enteros}")


# Consulta 21:
# Crea una función que calcule el cubo de un número dado mediante una función lambda.

# Función lambda para calcular el cubo
calcular_cubo = lambda x: x ** 3

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    # Número de ejemplo
    numero = 4

    print(f"El número es: {numero}")

    # Calcular el cubo
    cubo = calcular_cubo(numero)

    print(f"El cubo de {numero} es: {cubo}")

# Consulta 22:
# Dada una lista numérica, obtén el producto total de los valores de dicha lista.
# Usa la función reduce() sin encapsularla en una función.

from functools import reduce  # Se importa solo una vez en el archivo

# Lista de números de ejemplo
lista = [2, 3, 4, 5]

print(f"Lista de números: {lista}")

# Verificar que la lista no esté vacía
if not lista:
    print("Error: La lista no puede estar vacía.")
else:
    # Calcular el producto total usando reduce() directamente
    resultado = reduce(lambda x, y: x * y, lista)
    print(f"El producto total de los valores es: {resultado}")


# Consulta 23:
# Concatena una lista de palabras. Usa la función reduce() sin encapsularla en una función.

from functools import reduce  # Se importa una sola vez en el archivo

# Lista de palabras de ejemplo
lista_palabras = ["Hola", "mundo", "Python", "es", "genial"]

print(f"Lista de palabras: {lista_palabras}")

# Verificar que la lista no esté vacía
if not lista_palabras:
    print("Error: La lista no puede estar vacía.")
else:
    # Concatenar palabras usando reduce() directamente
    resultado = reduce(lambda x, y: x + " " + y, lista_palabras)
    print(f"Cadena concatenada: '{resultado}'")


# Consulta 24:
# Calcula la diferencia total en los valores de una lista usando la función reduce() sin encapsularla en una función.

# Lista de números de ejemplo
lista_numeros = [100, 20, 10, 5]

print(f"Lista de números: {lista_numeros}")

# Verificar que la lista tenga al menos dos elementos
if len(lista_numeros) < 2:
    print("Error: La lista debe contener al menos dos números para calcular la diferencia total.")
else:
    # Calcular la diferencia total usando reduce() directamente
    resultado = reduce(lambda x, y: x - y, lista_numeros)
    print(f"Diferencia total: {resultado}")


# Consulta 25:
# Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(cadena):
    """
    Cuenta el número de caracteres en una cadena de texto.

    Args:
        cadena (str): La cadena de texto de entrada.

    Returns:
        int: Número total de caracteres en la cadena.
    """
    return len(cadena)

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    # Cadena de texto de ejemplo
    texto = "Python es un lenguaje increíble"

    print(f"Cadena de texto: '{texto}'")

    # Contar caracteres
    numero_caracteres = contar_caracteres(texto)

    print(f"Número de caracteres en la cadena: {numero_caracteres}")

# Consulta 26:
# Crea una función lambda que calcule el resto de la división entre dos números dados.

# Función lambda para calcular el resto
calcular_resto = lambda x, y: x % y

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    # Números de ejemplo
    numero1 = 10
    numero2 = 3

    print(f"Números: {numero1}, {numero2}")

    # Calcular el resto
    resto = calcular_resto(numero1, numero2)

    print(f"El resto de dividir {numero1} entre {numero2} es: {resto}")

# Consulta 27:
# Crea una función que calcule el promedio de una lista de números.

def calcular_promedio(lista_numeros):
    """
    Calcula el promedio de una lista de números.

    Args:
        lista_numeros (list): Lista de números.

    Returns:
        float: Promedio de los números en la lista.

    Raises:
        ValueError: Si la lista está vacía.
    """
    if not lista_numeros:
        raise ValueError("La lista no puede estar vacía.")

    return sum(lista_numeros) / len(lista_numeros)

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    # Lista de números de ejemplo
    lista = [10, 20, 30, 40, 50]

    print(f"Lista de números: {lista}")

    # Calcular el promedio
    try:
        promedio = calcular_promedio(lista)
        print(f"El promedio es: {promedio:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

# Consulta 28:
# Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    """
    Encuentra el primer elemento duplicado en una lista.

    Args:
        lista (list): Lista de elementos.

    Returns:
        object: Primer elemento duplicado encontrado o None si no hay duplicados.
    """
    vistos = set()  # Conjunto para rastrear los elementos ya vistos

    for elemento in lista:
        if elemento in vistos:
            return elemento  # Devuelve el primer duplicado encontrado
        vistos.add(elemento)

    return None  # Si no se encuentran duplicados

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    # Lista de ejemplo
    lista_ejemplo = [1, 2, 3, 4, 5, 3, 6, 7]

    print(f"Lista de ejemplo: {lista_ejemplo}")

    # Buscar el primer duplicado
    duplicado = primer_duplicado(lista_ejemplo)

    if duplicado is not None:
        print(f"El primer duplicado es: {duplicado}")
    else:
        print("No se encontraron duplicados en la lista.")

# Consulta 29:
# Crea una función que convierta una variable en una cadena de texto y enmascare
# todos los caracteres con el carácter '#' excepto los últimos cuatro.

def enmascarar_variable(variable):
    """
    Convierte una variable en una cadena de texto y enmascara todos los caracteres
    con el carácter '#' excepto los últimos cuatro.

    Args:
        variable (any): La variable a enmascarar.

    Returns:
        str: Cadena enmascarada.
    """
    # Convertir la variable a cadena
    cadena = str(variable)

    # Enmascarar todos los caracteres excepto los últimos cuatro
    if len(cadena) > 4:
        return "#" * (len(cadena) - 4) + cadena[-4:]
    else:
        return cadena  # Si tiene 4 o menos caracteres, no enmascara

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    # Variable de ejemplo
    variable_ejemplo = 123456789

    print(f"Variable original: {variable_ejemplo}")

    # Enmascarar la variable
    resultado = enmascarar_variable(variable_ejemplo)

    print(f"Variable enmascarada: {resultado}")

# Consulta 30:
# Crea una función que determine si dos palabras son anagramas, es decir,
# si están formadas por las mismas letras pero en diferente orden.

def son_anagramas(palabra1, palabra2):
    """
    Determina si dos palabras son anagramas.

    Args:
        palabra1 (str): Primera palabra.
        palabra2 (str): Segunda palabra.

    Returns:
        bool: True si son anagramas, False en caso contrario.
    """
    # Eliminar espacios y convertir a minúsculas para asegurar comparación uniforme
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()

    # Comparar las palabras ordenadas por sus letras
    return sorted(palabra1) == sorted(palabra2)

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    # Palabras de ejemplo
    palabra1 = "amor"
    palabra2 = "Roma"

    print(f"Palabra 1: {palabra1}")
    print(f"Palabra 2: {palabra2}")

    # Determinar si son anagramas
    if son_anagramas(palabra1, palabra2):
        print("Las palabras son anagramas.")
    else:
        print("Las palabras NO son anagramas.")

# Consulta 31:
# Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista.
# Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

def buscar_nombre():
    """
    Solicita al usuario una lista de nombres y un nombre para buscar en esa lista.
    Si el nombre está en la lista, imprime un mensaje. Si no está, lanza una excepción.

    Raises:
        ValueError: Si el nombre no se encuentra en la lista.
    """
    try:
        # Solicitar al usuario que ingrese una lista de nombres
        nombres = input("Introduce una lista de nombres separados por comas: ").split(',')

        # Limpiar espacios en los nombres
        nombres = [nombre.strip() for nombre in nombres]

        # Solicitar el nombre a buscar
        nombre_buscar = input("Introduce el nombre que deseas buscar: ").strip()

        # Verificar si el nombre está en la lista
        if nombre_buscar in nombres:
            print(f"El nombre '{nombre_buscar}' fue encontrado en la lista.")
        else:
            raise ValueError(f"El nombre '{nombre_buscar}' no está en la lista.")
    except ValueError as e:
        print(e)

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    buscar_nombre()
# Comentario sobre dificultad:
    # Una dificultad fue asegurar que los nombres se comparen correctamente sin errores
    # debido a espacios en blanco o diferencias en mayúsculas y minúsculas. 
    # Esto se resolvió limpiando los espacios con strip() y considerando una normalización adicional si es necesario



# Consulta 32:
# Crea una función que tome un nombre completo y una lista de empleados,
# busque el nombre completo en la lista y devuelva el puesto si está,
# de lo contrario, indica que no trabaja aquí.

def buscar_puesto_empleado(nombre_completo, lista_empleados):
    """
    Busca el puesto de un empleado en una lista.

    Args:
        nombre_completo (str): Nombre completo del empleado.
        lista_empleados (list): Lista de diccionarios con 'nombre' y 'puesto'.

    Returns:
        str: Mensaje con el puesto del empleado o indicando que no trabaja aquí.
    """
    # Normalizamos el nombre a buscar y los nombres en la lista
    nombre_completo = nombre_completo.strip().lower()

    for empleado in lista_empleados:
        if empleado['nombre'].strip().lower() == nombre_completo:
            return f"El puesto de {empleado['nombre']} es: {empleado['puesto']}."
    
    return f"La persona {nombre_completo} no trabaja aquí."

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    # Lista de empleados de ejemplo
    empleados = [
        {"nombre": "Ana García", "puesto": "Gerente"},
        {"nombre": "Luis Pérez", "puesto": "Contador"},
        {"nombre": "María López", "puesto": "Analista"},
        {"nombre": "Juan Fernández", "puesto": "Desarrollador"}
    ]

    # Solicitar al usuario el nombre a buscar
    nombre_a_buscar = input("Introduce el nombre completo del empleado: ").strip()

    # Buscar y mostrar el resultado
    resultado = buscar_puesto_empleado(nombre_a_buscar, empleados)
    print(resultado)
# Comentario sobre dificultad:
        # Una dificultad fue manejar casos donde el nombre completo no coincide
        # exactamente con el formato en la lista (espacios extra, diferencias de mayúsculas/minúsculas).
        # Esto se resolvió normalizando el formato con strip() y considerando otras posibles validaciones.


# Consulta 33:
# Crea una función lambda que sume elementos correspondientes de dos listas dadas.

# Función lambda para sumar elementos correspondientes de dos listas
sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    # Listas de ejemplo
    lista1 = [1, 2, 3, 4]
    lista2 = [5, 6, 7, 8]

    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")

    # Sumar las listas
    resultado = sumar_listas(lista1, lista2)
    print(f"Suma de elementos correspondientes: {resultado}")

# Consulta 34: Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. 
# Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . 
# El objetivo es implementar estos métodos para manipular la estructura del árbol.

class Arbol:
    def __init__(self):
        """Inicializa un árbol con un tronco de longitud 1 y una lista vacía de ramas."""
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        """Aumenta la longitud del tronco en una unidad."""
        self.tronco += 1

    def nueva_rama(self):
        """Agrega una nueva rama de longitud 1 a la lista de ramas."""
        self.ramas.append(1)

    def crecer_ramas(self):
        """Aumenta en una unidad la longitud de todas las ramas existentes."""
        self.ramas = [longitud + 1 for longitud in self.ramas]

    def quitar_rama(self, posicion):
        """
        Elimina una rama en una posición específica.

        Args:
            posicion (int): La posición de la rama a eliminar (0-indexada).

        Raises:
            IndexError: Si la posición no es válida.
        """
        if 0 <= posicion < len(self.ramas):
            del self.ramas[posicion]
        else:
            raise IndexError("Posición de rama inválida.")

    def info_arbol(self):
        """
        Devuelve información sobre el árbol.

        Returns:
            str: Información sobre la longitud del tronco, el número de ramas y sus longitudes.
        """
        return (f"Longitud del tronco: {self.tronco}\n"
                f"Número de ramas: {len(self.ramas)}\n"
                f"Longitudes de las ramas: {self.ramas}")


# Caso de uso
if __name__ == "__main__":
    # 1. Crear un árbol
    arbol = Arbol()

    # 2. Hacer crecer el tronco del árbol una unidad
    arbol.crecer_tronco()

    # 3. Añadir una nueva rama al árbol
    arbol.nueva_rama()

    # 4. Hacer crecer todas las ramas del árbol una unidad
    arbol.crecer_ramas()

    # 5. Añadir dos nuevas ramas al árbol
    arbol.nueva_rama()
    arbol.nueva_rama()

    # 6. Retirar la rama situada en la posición 2
    try:
        arbol.quitar_rama(2)
    except IndexError as e:
        print(f"Error: {e}")

    # 7. Obtener información sobre el árbol
    print(arbol.info_arbol())
# Comentario sobre dificultad:
        # Un reto fue manejar los índices en la función quitar_rama para evitar errores
        # al intentar eliminar ramas en posiciones inexistentes. Esto se resolvió 
        # validando si el índice está en el rango válido.


# Consulta 35: No existe

# Consulta 36: Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. 
# Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente=True):
        """
        Inicializa un usuario del banco con su nombre, saldo y estado de cuenta corriente.

        Args:
            nombre (str): Nombre del usuario.
            saldo (float): Saldo inicial del usuario.
            cuenta_corriente (bool): Indica si el usuario tiene cuenta corriente.
        """
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        """
        Retira dinero del saldo del usuario.

        Args:
            cantidad (float): Cantidad de dinero a retirar.

        Raises:
            ValueError: Si la cantidad es mayor al saldo o si el usuario no tiene cuenta corriente.
        """
        if not self.cuenta_corriente:
            raise ValueError(f"{self.nombre} no tiene una cuenta corriente activa.")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad}.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        """
        Transfiere dinero desde el usuario actual a otro usuario.

        Args:
            otro_usuario (UsuarioBanco): Usuario destinatario de la transferencia.
            cantidad (float): Cantidad de dinero a transferir.

        Raises:
            ValueError: Si la cantidad es mayor al saldo o si el usuario no tiene cuenta corriente.
        """
        if not self.cuenta_corriente:
            raise ValueError(f"{self.nombre} no tiene una cuenta corriente activa.")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para transferir {cantidad}.")
        self.saldo -= cantidad
        otro_usuario.agregar_dinero(cantidad)

    def agregar_dinero(self, cantidad):
        """
        Agrega dinero al saldo del usuario.

        Args:
            cantidad (float): Cantidad de dinero a agregar.
        """
        self.saldo += cantidad

    def __str__(self):
        """
        Representación en cadena del usuario del banco.

        Returns:
            str: Información del usuario.
        """
        return f"Usuario: {self.nombre}, Saldo: {self.saldo}, Cuenta Corriente: {self.cuenta_corriente}"


# Caso de uso
if __name__ == "__main__":
    # Crear dos usuarios: Alicia y Bob
    alicia = UsuarioBanco("Alicia", 100)
    bob = UsuarioBanco("Bob", 50)

    # Agregar 20 unidades de saldo a Bob
    bob.agregar_dinero(20)
    print(f"Después de agregar dinero a Bob: {bob}")

    # Hacer una transferencia de 80 unidades desde Bob a Alicia
    try:
        bob.transferir_dinero(alicia, 80)
        print(f"Después de la transferencia de Bob a Alicia:\n{bob}\n{alicia}")
    except ValueError as e:
        print(e)

    # Retirar 50 unidades de saldo a Alicia
    try:
        alicia.retirar_dinero(50)
        print(f"Después del retiro de Alicia: {alicia}")
    except ValueError as e:
        print(e)

# Consulta 37: Crea una función llamada procesar_texto que procesa un texto 
# según la opción especificada: reemplazar_palabras , procesar_texto .

# Función para contar palabras
def contar_palabras(texto):
    """
    Cuenta el número de veces que aparece cada palabra en el texto.

    Args:
        texto (str): Texto a procesar.

    Returns:
        dict: Diccionario con las palabras como claves y su frecuencia como valores.
    """
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        palabra = palabra.strip(".,!?").lower()  # Normaliza las palabras
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia


# Función para reemplazar palabras
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """
    Reemplaza una palabra en el texto por otra.

    Args:
        texto (str): Texto a procesar.
        palabra_original (str): Palabra que será reemplazada.
        palabra_nueva (str): Palabra que reemplazará a la original.

    Returns:
        str: Texto con la palabra reemplazada.
    """
    return texto.replace(palabra_original, palabra_nueva)


# Función para eliminar una palabra del texto
def eliminar_palabra(texto, palabra_a_eliminar):
    """
    Elimina todas las ocurrencias de una palabra en el texto.

    Args:
        texto (str): Texto a procesar.
        palabra_a_eliminar (str): Palabra que será eliminada.

    Returns:
        str: Texto sin la palabra eliminada.
    """
    palabras = texto.split()
    palabras = [palabra for palabra in palabras if palabra != palabra_a_eliminar]
    return " ".join(palabras)


# Función principal para procesar texto
def procesar_texto(texto, opcion, *args):
    """
    Procesa el texto según la opción especificada.

    Args:
        texto (str): Texto a procesar.
        opcion (str): Opción de procesamiento ("contar", "reemplazar", "eliminar").
        *args: Argumentos adicionales necesarios para cada opción.

    Returns:
        dict/str: Resultado del procesamiento, dependiendo de la opción.
    """
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar" and len(args) == 2:
        palabra_original, palabra_nueva = args
        return reemplazar_palabras(texto, palabra_original, palabra_nueva)
    elif opcion == "eliminar" and len(args) == 1:
        palabra_a_eliminar = args[0]
        return eliminar_palabra(texto, palabra_a_eliminar)
    else:
        raise ValueError("Opción inválida o argumentos insuficientes.")


# Caso de uso
if __name__ == "__main__":
    texto_ejemplo = "Hola mundo. Este mundo es maravilloso. Hola a todos."

    # Comentario sobre dificultad:
    # Una dificultad fue manejar palabras con puntuaciones (como 'mundo.' y 'mundo'),
    # ya que estas se consideran diferentes a menos que se normalicen.
    # Esto se resolvió eliminando los signos de puntuación con strip() y 
    # transformando todo a minúsculas con lower().

    # Contar palabras
    resultado_contar = procesar_texto(texto_ejemplo, "contar")
    print("Resultado de contar palabras:")
    print(resultado_contar)

    # Reemplazar una palabra
    resultado_reemplazar = procesar_texto(texto_ejemplo, "reemplazar", "mundo", "universo")
    print("\nResultado de reemplazar 'mundo' por 'universo':")
    print(resultado_reemplazar)

    # Eliminar una palabra
    resultado_eliminar = procesar_texto(texto_ejemplo, "eliminar", "Hola")
    print("\nResultado de eliminar 'Hola':")
    print(resultado_eliminar)


# Consulta 38:
# Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def determinar_momento_del_dia(hora):
    """
    Determina si es de noche, de día o tarde según la hora proporcionada.

    Args:
        hora (int): Hora en formato 24 horas.

    Returns:
        str: Mensaje indicando el momento del día.
    """
    if 0 <= hora < 6:
        return "Es de noche."
    elif 6 <= hora < 12:
        return "Es de día."
    elif 12 <= hora < 18:
        return "Es por la tarde."
    elif 18 <= hora <= 23:
        return "Es de noche."
    else:
        raise ValueError("La hora proporcionada no es válida. Debe estar entre 0 y 23.")

# Programa principal
if __name__ == "__main__":
    try:
        # Solicitar la hora al usuario
        hora_usuario = int(input("Introduce la hora en formato 24 horas (0-23): "))

        # Determinar el momento del día
        resultado = determinar_momento_del_dia(hora_usuario)
        print(resultado)
    except ValueError as e:
        print(f"Error: {e}")

 # Consulta 39:
# Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.

def determinar_calificacion(calificacion):
    """
    Determina la calificación en texto de un alumno basada en su calificación numérica.

    Args:
        calificacion (int): Calificación numérica del alumno.

    Returns:
        str: Calificación en texto.
    """
    if 0 <= calificacion <= 69:
        return "Insuficiente"
    elif 70 <= calificacion <= 79:
        return "Bien"
    elif 80 <= calificacion <= 89:
        return "Muy bien"
    elif 90 <= calificacion <= 100:
        return "Excelente"
    else:
        raise ValueError("La calificación debe estar entre 0 y 100.")

# Programa principal
if __name__ == "__main__":
    try:
        # Solicitar la calificación al usuario
        calificacion_usuario = int(input("Introduce la calificación numérica del alumno (0-100): "))

        # Determinar la calificación en texto
        resultado = determinar_calificacion(calificacion_usuario)
        print(f"La calificación en texto es: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")
       
# Consulta 40:
# Escribe una función que tome dos parámetros: figura (una cadena) y datos (una tupla)
# para calcular el área de "rectángulo", "círculo" o "triángulo".

import math

def calcular_area(figura, datos):
    """
    Calcula el área de una figura en base a sus datos.

    Args:
        figura (str): Tipo de figura ("rectangulo", "circulo", "triangulo").
        datos (tuple): Datos necesarios para calcular el área:
            - Rectángulo: (base, altura)
            - Círculo: (radio,)
            - Triángulo: (base, altura)

    Returns:
        float: Área de la figura.

    Raises:
        ValueError: Si el tipo de figura o los datos no son válidos.
    """
    if figura == "rectangulo":
        if len(datos) == 2:
            base, altura = datos
            return base * altura
        else:
            raise ValueError("Datos incorrectos para un rectángulo. Se necesita (base, altura).")

    elif figura == "circulo":
        if len(datos) == 1:
            radio, = datos
            return math.pi * radio**2
        else:
            raise ValueError("Datos incorrectos para un círculo. Se necesita (radio,).")

    elif figura == "triangulo":
        if len(datos) == 2:
            base, altura = datos
            return 0.5 * base * altura
        else:
            raise ValueError("Datos incorrectos para un triángulo. Se necesita (base, altura).")

    else:
        raise ValueError("Figura no reconocida. Debe ser 'rectangulo', 'circulo' o 'triangulo'.")

# Ejemplo para ejecutar en la consola
if __name__ == "__main__":
    try:
        # Solicitar el tipo de figura al usuario
        figura = input("Introduce la figura (rectangulo, circulo, triangulo): ").strip().lower()

        # Solicitar los datos según la figura
        if figura == "rectangulo":
            datos = tuple(map(float, input("Introduce base y altura separados por espacio: ").split()))
        elif figura == "circulo":
            datos = tuple(map(float, input("Introduce el radio: ").split()))
        elif figura == "triangulo":
            datos = tuple(map(float, input("Introduce base y altura separados por espacio: ").split()))
        else:
            raise ValueError("Figura no válida.")

        # Calcular el área
        area = calcular_area(figura, datos)
        print(f"El área del {figura} es: {area:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

# Consulta 41:
# Programa para calcular el monto final de una compra después de aplicar un descuento.

def calcular_precio_final():
    """
    Calcula el monto final de una compra aplicando un descuento, si es válido.
    """
    try:
        # Solicitar el precio original del artículo
        precio_original = float(input("Introduce el precio original del artículo: "))

        if precio_original <= 0:
            raise ValueError("El precio debe ser mayor a cero.")

        # Preguntar si el usuario tiene un cupón de descuento
        tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

        if tiene_cupon == "sí":
            # Solicitar el valor del cupón de descuento
            valor_cupon = float(input("Introduce el valor del cupón de descuento: "))

            if valor_cupon <= 0:
                raise ValueError("El valor del cupón debe ser mayor a cero.")
            
            # Calcular el precio final con descuento
            precio_final = max(0, precio_original - valor_cupon)  # Asegurarse de que no sea negativo
            print(f"El precio final con descuento es: {precio_final:.2f} €")
        elif tiene_cupon == "no":
            # Sin descuento, el precio final es el precio original
            print(f"No se aplicó descuento. El precio final es: {precio_original:.2f} €")
        else:
            raise ValueError("Respuesta inválida. Por favor, responde 'sí' o 'no'.")
    except ValueError as e:
        print(f"Error: {e}")

# Programa principal
if __name__ == "__main__":
    calcular_precio_final()

# Programa para determinar el monto final de una compra aplicando un descuento si corresponde.

def calcular_precio_final():
    """
    Determina el precio final de un artículo aplicando un descuento, si es válido.
    """
    try:
        # 1. Solicitar el precio original del artículo
        precio_original = float(input("Introduce el precio original del artículo (€): "))
        if precio_original <= 0:
            raise ValueError("El precio debe ser mayor a 0.")

        # 2. Preguntar si tiene un cupón de descuento
        tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

        if tiene_cupon == "sí":
            # 3. Solicitar el valor del cupón de descuento
            valor_cupon = float(input("Introduce el valor del cupón de descuento (€): "))
            if valor_cupon <= 0:
                raise ValueError("El valor del cupón debe ser mayor a 0.")

            # 4. Aplicar el descuento
            precio_final = max(0, precio_original - valor_cupon)  # Asegurarse de que no sea negativo
            print(f"El precio final con descuento es: {precio_final:.2f} €")
        elif tiene_cupon == "no":
            # Sin descuento
            print(f"No se aplicó descuento. El precio final es: {precio_original:.2f} €")
        else:
            raise ValueError("Respuesta inválida. Por favor, responde 'sí' o 'no'.")
    except ValueError as e:
        print(f"Error: {e}")

# Ejemplo para ejecutar
if __name__ == "__main__":
    print("\n--- Ejemplo con descuento de 15 € ---")
    try:
        # Ejemplo con valores predefinidos para facilitar la prueba
        precio_original = 50  # Precio inicial
        tiene_cupon = "sí"  # Usuario tiene un cupón
        valor_cupon = 15  # Descuento

        print(f"Precio original: {precio_original} €")
        print(f"Tiene cupón: {'Sí' if tiene_cupon == 'sí' else 'No'}")
        print(f"Valor del cupón: {valor_cupon} €")

        # Calcular el precio final aplicando el cupón
        if tiene_cupon == "sí" and valor_cupon > 0:
            precio_final = max(0, precio_original - valor_cupon)
        else:
            precio_final = precio_original

        print(f"El precio final es: {precio_final:.2f} €\n")
    except ValueError as e:
        print(f"Error: {e}")
                        
    # Llamar a la función para ejecución interactiva
    calcular_precio_final()
# Comentario sobre dificultad:
        # Una dificultad fue manejar descuentos inválidos (como valores negativos),
        # lo que requería una validación adicional para evitar resultados incorrectos.
