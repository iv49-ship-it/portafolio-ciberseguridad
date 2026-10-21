"""
========================================
CHEATSHEET - PROGRAMACIÓN AVANZADA IACC
Semana 1: Control de Flujo + Cadenas de Texto
========================================
"""

# ========================================
# 1. ESTRUCTURAS CONDICIONALES
# ========================================

# IF - Ejecuta si la condición es True
# if condición:
#     código

edad = 18
if edad >= 18:
    print("Eres mayor de edad")

# IF-ELSE - Ejecuta un código si es True, otro si es False
# if condición:
#     código True
# else:
#     código False

edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# IF-ELIF-ELSE - Múltiples condiciones
# if condición1:
#     código1
# elif condición2:
#     código2
# else:
#     código3

calificacion = 85
if calificacion >= 90:
    print("Excelente")
elif calificacion >= 80:
    print("Muy bien")
elif calificacion >= 70:
    print("Bien")
elif calificacion >= 60:
    print("Regular")
else:
    print("Insuficiente")

# Operadores lógicos para condiciones compuestas
# and → ambas condiciones deben ser True
# or  → al menos una condición debe ser True
# not → invierte el valor

edad = 25
if edad >= 18 and edad <= 80:
    print("Elegible para el puesto")


# ========================================
# 2. ESTRUCTURAS REPETITIVAS (BUCLES)
# ========================================

# WHILE - Repite MIENTRAS la condición sea True
# while condición:
#     código

contador = 0
while contador <= 5:
    print(f"Vuelta {contador}")
    contador = contador + 1  # ¡Importante! Si falta, bucle infinito

# FOR - Itera sobre una secuencia (lista, rango, cadena, etc.)
# for variable in secuencia:
#     código

# Con range(inicio, fin, paso)
for i in range(1, 11):      # i = 1,2,3,4,5,6,7,8,9,10
    print(i)

for i in range(5):          # i = 0,1,2,3,4
    print(i)

# Sobre una lista
nombres = ["Ana", "Luis", "Carlos"]
for nombre in nombres:
    print(nombre)

# Sobre una cadena de texto
for letra in "Python":
    print(letra)


# ========================================
# 3. CADENAS DE TEXTO (STRINGS)
# ========================================

# Creación
cadena1 = 'Hola, Chile!'
cadena2 = "Python es increíble"

# Longitud
texto = "Python"
longitud = len(texto)      # 6

# Acceso por índice (empieza en 0)
primer_caracter = texto[0]   # 'P'
ultimo_caracter = texto[-1]  # 'n'

# Slicing (rebanado) [inicio:fin]
texto = "Python"
subcadena = texto[2:5]       # 'tho' (índices 2,3,4)
inicio = texto[:3]           # 'Pyt'
final = texto[3:]            # 'hon'

# Concatenación (+)
saludo = "Hola" + " " + "mundo"   # 'Hola mundo'

# Formateo con f-strings (recomendado)
nombre = "Juan"
edad = 29
mensaje = f"Hola, {nombre}! Tienes {edad} años."

# Método split() - divide en lista por un separador
frase = "Hola, cómo estás?"
palabras = frase.split(", ")   # ['Hola', 'cómo estás?']

# Método join() - une lista en cadena con un separador
palabras = ['Hola', 'mundo']
frase = " ".join(palabras)     # 'Hola mundo'


# ========================================
# 4. ACTIVIDADES DEL IACC (Ejemplos)
# ========================================

"""
Actividad 1: Clasificar calificación
------------------------------------
Programa que ingrese la calificación de un estudiante y muestre:
- >= 90: "Excelente"
- 80-89: "Muy bien"
- 70-79: "Bien"
- 60-69: "Regular"
- < 60: "Insuficiente"
"""

def clasificar_calificacion(nota):
    if nota >= 90:
        return "Excelente"
    elif nota >= 80:
        return "Muy bien"
    elif nota >= 70:
        return "Bien"
    elif nota >= 60:
        return "Regular"
    else:
        return "Insuficiente"

# Prueba
print(clasificar_calificacion(85))  # Muy bien


"""
Actividad 2: Suma de números naturales (1 hasta N)
---------------------------------------------------
Solicitar un número entero positivo y sumar 1 + 2 + ... + N
"""

def suma_naturales(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

print(suma_naturales(16))  # 136


"""
Actividad 3: Datos personales con f-string
-------------------------------------------
Solicitar nombre y edad, mostrar mensaje personalizado
"""

def mensaje_personalizado():
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    print(f"Hola, {nombre}! Tienes {edad} años.")


# ========================================
# 5. CONCEPTOS CLAVE (para tu resumen)
# ========================================

"""
CONTROL DE FLUJO: Estructuras que permiten controlar la ejecución
de un programa (condicionales, bucles, saltos)

CONDICIONALES: if, elif, else - evalúan condiciones True/False

BUCLES:
- while: repite MIENTRAS condición sea True
- for: itera sobre una secuencia (range, lista, cadena)

STRING: Tipo de dato para texto, creado con '' o ""

OPERACIONES IMPORTANTES DE STRINGS:
- len(cadena) → longitud
- cadena[indice] → acceso a carácter
- cadena[inicio:fin] → slicing
- f"texto {variable}" → formateo
- split() → divide en lista
- join() → une lista en cadena
"""


# ========================================
# 6. ERRORS COMUNES (y cómo evitarlos)
# ========================================

"""
1. Olvidar los dos puntos (:) después de if, elif, else, while, for
   ❌ if edad > 18
   ✅ if edad > 18:

2. Olvidar la indentación (el código debe estar dentro del bloque)
   ❌ if edad > 18:
   print("Mayor")
   ✅ if edad > 18:
          print("Mayor")

3. Bucle while infinito (falta actualizar la variable)
   ❌ contador = 0
      while contador < 5:
          print("Hola")
   ✅ contador = 0
      while contador < 5:
          print("Hola")
          contador += 1

4. Confundir = (asignación) con == (comparación)
   ❌ if edad = 18:
   ✅ if edad == 18:
"""


# ========================================
# 7. EJERCICIOS PARA PRACTICAR (soluciones abajo)
# ========================================

"""
Ejercicio 1: Calificación de examen
Escribe un programa que solicite una calificación (0-100) y diga si aprobó (>=60)

Ejercicio 2: Elegibilidad por edad
Solicita una edad y determina si es elegible (entre 18 y 80 años)

Ejercicio 3: Suma hasta N
Solicita un número positivo N y suma desde 1 hasta N

Ejercicio 4: Juego de adivinanza
Un número fijo (ej: 17), el usuario tiene 5 intentos para adivinarlo.
Dar pistas si el número es mayor o menor.

Ejercicio 5: Datos de películas
Solicita título, director, año y género de 2 películas y muestra un resumen.
"""


# ========================================
# 8. SOLUCIONES DE LOS EJERCICIOS
# ========================================

"""
# Solución Ejercicio 1
calificacion = float(input("Ingresa tu calificación (0-100): "))
if calificacion >= 60:
    print("¡Felicidades! Has aprobado")
else:
    print("Lo siento, has reprobado")

# Solución Ejercicio 2
edad = int(input("Ingresa tu edad: "))
if edad >= 18 and edad <= 80:
    print("¡Eres elegible para el puesto!")
else:
    print("Lo siento, no eres elegible")

# Solución Ejercicio 3
numero = int(input("Ingresa un número entero positivo: "))
suma = 0
for i in range(1, numero + 1):
    suma += i
print(f"La suma hasta {numero} es: {suma}")

# Solución Ejercicio 4
numero_secreto = 17
intentos = 5
for i in range(intentos):
    intento = int(input("Adivina el número (1-20): "))
    if intento == numero_secreto:
        print(f"¡Felicidades! Lo adivinaste en {i+1} intentos")
        break
    elif intento < numero_secreto:
        print("El número es MAYOR")
    else:
        print("El número es MENOR")
else:
    print(f"Se acabaron los intentos. El número era {numero_secreto}")

# Solución Ejercicio 5
print("=== PELÍCULA 1 ===")
titulo1 = input("Título: ")
director1 = input("Director: ")
anio1 = input("Año: ")
genero1 = input("Género: ")

print("=== PELÍCULA 2 ===")
titulo2 = input("Título: ")
director2 = input("Director: ")
anio2 = input("Año: ")
genero2 = input("Género: ")

print("\n=== RESUMEN ===")
print(f"1. {titulo1} ({anio1}) - Dir: {director1} - Género: {genero1}")
print(f"2. {titulo2} ({anio2}) - Dir: {director2} - Género: {genero2}")
"""

"""
========================================
EJEMPLO PRÁCTICO - TAREA "RUEDA FÁCIL"
Tienda de llantas con facturación por cliente
========================================
"""

# ========================================
# CÓDIGO COMPLETO (como va en la tarea)
# ========================================

def procesar_facturacion():
    """
    Programa completo para la tienda Rueda Fácil.
    Calcula el total a pagar por cada cliente según la cantidad de llantas.
    
    Reglas de precios:
    - Menos de 5 llantas: $35.000 c/u
    - Entre 5 y 10 llantas: $40.000 c/u
    - Más de 10 llantas: $45.000 c/u
    """
    print("=== TIENDA DE LLANTAS 'RUEDA FÁCIL' ===\n")
    
    num_clientes = int(input("Ingrese la cantidad de clientes: "))
    
    for i in range(1, num_clientes + 1):
        print(f"\n--- Cliente {i} ---")
        cantidad = int(input("Cantidad de llantas: "))
        
        if cantidad < 5:
            precio_unitario = 35000
        elif cantidad <= 10:
            precio_unitario = 40000
        else:
            precio_unitario = 45000
        
        total = cantidad * precio_unitario
        print(f"Precio unitario: ${precio_unitario:,}")
        print(f"Total a pagar: ${total:,}")


# Ejecutar el programa
if __name__ == "__main__":
    procesar_facturacion()


# ========================================
# EJEMPLO DE SALIDA (con datos de prueba)
# ========================================

"""
=== TIENDA DE LLANTAS 'RUEDA FÁCIL' ===

Ingrese la cantidad de clientes: 3

--- Cliente 1 ---
Cantidad de llantas: 3
Precio unitario: $35,000
Total a pagar: $105,000

--- Cliente 2 ---
Cantidad de llantas: 6
Precio unitario: $40,000
Total a pagar: $240,000

--- Cliente 3 ---
Cantidad de llantas: 12
Precio unitario: $45,000
Total a pagar: $540,000
"""


# ========================================
# CONCEPTOS APLICADOS EN ESTE CÓDIGO
# ========================================

"""
| Concepto | Dónde aparece | Explicación |
|----------|---------------|-------------|
| input() | num_clientes = int(input(...)) | Solicita datos al usuario |
| int() | int(input(...)) | Convierte texto a número entero |
| for | for i in range(1, num_clientes + 1) | Bucle que repite por cada cliente |
| range() | range(1, num_clientes + 1) | Genera números del 1 al N |
| if/elif/else | if cantidad < 5: ... | Evalúa rangos de cantidad |
| Operadores | <, <=, * | Comparación y multiplicación |
| f-string | f"Total: ${total:,}" | Formatea texto con variables |
| :, | ${total:,} | Formato de miles (1,000) |
"""


# ========================================
# POSIBLES MEJORAS (si quieres extenderlo)
# ========================================

"""
# 1. Validar que la cantidad no sea negativa
if cantidad < 0:
    print("Cantidad no válida")
    continue

# 2. Acumular ventas totales del día
ventas_totales += total

# 3. Mostrar resumen final
print(f"\n=== RESUMEN ===")
print(f"Total de clientes: {num_clientes}")
print(f"Ventas totales: ${ventas_totales:,}")
"""

# ============================================
#  PARÁMETROS Y ARGUMENTOS
# ============================================

# Parámetro: variable en la definición de la función
# Argumento: valor real que se pasa al llamarla

def saludar(nombre):  # 'nombre' es un parámetro
    print(f"Hola {nombre}")

saludar("Ana")  # "Ana" es un argumento

# ============================================
#  ARGUMENTOS POR VALOR (tipos inmutables)
# ============================================

# int, float, str, tuple → no se modifican fuera de la función

def duplicar(x):
    x = x * 2
    print("Dentro:", x)

num = 5
duplicar(num)   # Dentro: 10
print("Fuera:", num)  # Fuera: 5

# ============================================
#  ARGUMENTOS POR REFERENCIA (tipos mutables)
# ============================================

# list, dict, set → sí se modifican fuera de la función

def agregar_elemento(lista):
    lista.append(4)

mi_lista = [1, 2, 3]
agregar_elemento(mi_lista)
print(mi_lista)  # [1, 2, 3, 4]

# ============================================
#  FUNCIONES RECURSIVAS
# ============================================
# - Se llaman a sí mismas
# - Deben tener un caso base (detiene la recursión)
# - Y un caso recursivo (llamada a sí misma)

def factorial(n):
    # Caso base
    if n == 0 or n == 1:
        return 1
    # Caso recursivo
    return n * factorial(n - 1)

print(factorial(5))  # 120

# ============================================
#  ESTRUCTURA COMPLETA
# ============================================

def nombre_funcion(param1, param2):
    """Docstring: explica qué hace la función"""
    # Cuerpo
    resultado = param1 + param2
    return resultado

# ============================================
#  EJEMPLO CON LISTAS (REFERENCIA)
# ============================================

def sumar_elementos_lista(lista):
    lista[0] = lista[1] + lista[2]

numeros = [0, 5, 7]
sumar_elementos_lista(numeros)
print(numeros[0])  # 12

# ============================================================
#  CHEATSHEET: MANEJO DE EXCEPCIONES EN PYTHON (Semana 3)
#  Para usar en VSCode - Ctrl+Shift+P > Snippets
# ============================================================

# ------------------------------------------------------------
# 1. ESTRUCTURA BÁSICA try-except
# ------------------------------------------------------------

try:
    # Código que PUEDE fallar
    numero = int(input("Ingrese un número: "))
except ValueError:
    # Se ejecuta si hay error
    print("❌ Error: Debe ingresar un número")

# ------------------------------------------------------------
# 2. MÚLTIPLES EXCEPCIONES
# ------------------------------------------------------------

try:
    numerador = float(input("Ingrese numerador: "))
    denominador = float(input("Ingrese denominador: "))
    resultado = numerador / denominador
except ValueError:
    print("❌ Error: Debe ingresar números")
except ZeroDivisionError:
    print("❌ Error: No se puede dividir por cero")
except Exception as e:
    print(f"❌ Error inesperado: {e}")

# ------------------------------------------------------------
# 3. try-except-else-finally (COMPLETO)
# ------------------------------------------------------------

try:
    numero = int(input("Ingrese un número: "))
    inverso = 1 / numero
except ValueError:
    print("❌ Error: No es un número")
except ZeroDivisionError:
    print("❌ Error: No se puede dividir por cero")
else:
    # Solo si NO hubo error
    print(f"✅ El inverso es: {inverso}")
finally:
    # Siempre se ejecuta (haya o no error)
    print("📌 Fin del programa")

# ------------------------------------------------------------
# 4. LANZAR EXCEPCIONES CON raise
# ------------------------------------------------------------

def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad < 18:
        raise ValueError("Debes ser mayor de edad")
    return True

# Uso:
try:
    edad = int(input("Ingrese su edad: "))
    validar_edad(edad)
    print("✅ Acceso permitido")
except ValueError as e:
    print(f"❌ Error: {e}")

# ------------------------------------------------------------
# 5. PATRÓN: Validar entrada de usuario (el más usado)
# ------------------------------------------------------------

def pedir_numero_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                raise ValueError("El número debe ser positivo")
            return valor
        except ValueError as e:
            print(f"❌ Error: {e}")
            print("Por favor, intente nuevamente.\n")

# Uso:
stock = pedir_numero_positivo("Cantidad en existencia: ")

# ------------------------------------------------------------
# 6. PATRÓN: Menú interactivo con excepciones
# ------------------------------------------------------------

def menu():
    while True:
        print("\n1. Opción 1")
        print("2. Opción 2")
        print("3. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 3:
                print("👋 ¡Hasta luego!")
                break
            elif opcion == 1:
                print("✅ Ejecutando opción 1")
            elif opcion == 2:
                print("✅ Ejecutando opción 2")
            else:
                print("❌ Opción no válida")
        except ValueError:
            print("❌ Error: Debe ingresar un número")

# ------------------------------------------------------------
# 7. ERRORES MÁS COMUNES (recordatorio)
# ------------------------------------------------------------

# ValueError    → Texto donde va número
# ZeroDivisionError → Dividir por cero
# TypeError     → Operación con tipo incorrecto
# NameError     → Variable no definida
# FileNotFoundError → Archivo no existe
# KeyboardInterrupt → Ctrl+C (interrupción del usuario)

# ------------------------------------------------------------
# 8. ESTRUCTURA COMPLETA PARA TAREAS
# ------------------------------------------------------------

def gestionar_datos():
    while True:
        try:
            # Paso 1: Pedir datos
            dato1 = float(input("Ingrese dato 1: "))
            dato2 = float(input("Ingrese dato 2: "))
            
            # Paso 2: Validar
            if dato1 < 0 or dato2 < 0:
                raise ValueError("Los datos no pueden ser negativos")
            
            # Paso 3: Procesar
            resultado = dato1 + dato2
            
            # Paso 4: Mostrar éxito
            print(f"✅ Resultado: {resultado}")
            break
            
        except ValueError as e:
            print(f"❌ Error: {e}")
            print("Por favor, vuelva a ingresar los datos.\n")
        except KeyboardInterrupt:
            print("\n⚠️ Operación cancelada")
            break

# Ejecutar
gestionar_datos()

# ============================================================
#  FIN CHEATSHEET
# ============================================================

# ============================================
# 1. FUNCIÓN BÁSICA
# ============================================

def nombre_funcion(parametro1, parametro2):
    """Docstring: explica qué hace la función"""
    resultado = parametro1 + parametro2
    return resultado

# Llamada
nombre_funcion(5, 3)  # 8

# ============================================
# 2. TIPOS DE PARÁMETROS
# ============================================

# Parámetro obligatorio
def saludar(nombre):
    print(f"Hola {nombre}")

# Parámetro con valor por defecto
def saludar(nombre="Mundo"):
    print(f"Hola {nombre}")

# Parámetros arbitrarios (*args)
def sumar_todos(*numeros):
    return sum(numeros)

sumar_todos(1, 2, 3, 4)  # 10

# ============================================
# 3. VALOR vs REFERENCIA
# ============================================

# INMUTABLES (por VALOR) → NO cambian fuera
# int, float, str, bool, tuple

def modificar_numero(x):
    x = x + 10
    print(f"Dentro: {x}")

n = 5
modificar_numero(n)  # Dentro: 15
print(f"Fuera: {n}")  # Fuera: 5  ← ¡No cambió!

# MUTABLES (por REFERENCIA) → SÍ cambian fuera
# list, dict, set

def modificar_lista(lista):
    lista.append(10)
    print(f"Dentro: {lista}")

mi_lista = [1, 2, 3]
modificar_lista(mi_lista)  # Dentro: [1, 2, 3, 10]
print(f"Fuera: {mi_lista}")  # Fuera: [1, 2, 3, 10]  ← ¡Sí cambió!

# ============================================
# 4. FUNCIONES RECURSIVAS
# ============================================

# Estructura: Caso Base + Caso Recursivo

def factorial(n):
    # Caso base
    if n <= 1:
        return 1
    # Caso recursivo
    return n * factorial(n - 1)

factorial(5)  # 120

# ============================================
# 5. VALIDACIONES DENTRO DE FUNCIONES
# ============================================

def calcular_descuento(precio, porcentaje):
    # Validar precio
    if precio <= 0:
        return "Error: precio inválido"
    
    # Validar porcentaje
    if porcentaje < 0 or porcentaje > 100:
        return "Error: porcentaje inválido"
    
    # Cálculo
    descuento = precio * (porcentaje / 100)
    return precio - descuento

# ============================================
# 6. RETURN vs PRINT
# ============================================

# RETURN: devuelve un valor para usar después
def suma(a, b):
    return a + b

resultado = suma(5, 3)  # resultado = 8

# PRINT: solo muestra en pantalla
def mostrar_suma(a, b):
    print(a + b)

mostrar_suma(5, 3)  # Imprime 8, pero no guarda nada

# ============================================
# 7. DOCSTRING (documentación)
# ============================================

def area_circulo(radio):
    """
    Calcula el área de un círculo.
    
    Parámetros:
    radio (float): Radio del círculo
    
    Retorna:
    float: Área del círculo
    """
    return 3.1416 * radio ** 2

    ******La regla de oro que descubriste:

    No necesitas crear variables intermedias si solo las vas a usar una vez.

# Ver documentación
help(area_circulo)

Par → % 2 == 0

Impar → % 2 != 0 o not es_par(numero)

# ============================================
# 1. IMPORTACIÓN DE MÓDULOS
# ============================================

import json        # Para trabajar con archivos JSON
import pickle      # Para serializar objetos de Python
import os          # Para operaciones del sistema (rutas, archivos)

# ============================================
# 2. ABRIR Y CERRAR ARCHIVOS (WITH)
# ============================================

# El bloque 'with' abre y cierra el archivo automáticamente

# Modo escritura ('w'): crea o sobreescribe el archivo
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, mundo\n")
    archivo.write("Segunda línea")

# Modo lectura ('r'): lee el contenido del archivo
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# Modo adición ('a'): agrega contenido al final
with open("archivo.txt", "a") as archivo:
    archivo.write("\nNueva línea agregada")

# Modo lectura/escritura ('r+'): lee y escribe
with open("archivo.txt", "r+") as archivo:
    contenido = archivo.read()
    archivo.write("\nLínea agregada en modo r+")

# ============================================
# 3. MÉTODOS DE LECTURA
# ============================================

# read(): Lee todo el archivo
with open("archivo.txt", "r") as archivo:
    todo = archivo.read()

# read(n): Lee n caracteres
with open("archivo.txt", "r") as archivo:
    primeros_10 = archivo.read(10)  # Lee 10 caracteres

# readline(): Lee una línea
with open("archivo.txt", "r") as archivo:
    primera_linea = archivo.readline()

# readlines(): Lee todas las líneas en una lista
with open("archivo.txt", "r") as archivo:
    lineas = archivo.readlines()  # ['Hola, mundo\n', 'Segunda línea']

# ============================================
# 4. MÉTODOS DE ESCRITURA
# ============================================

# write(): Escribe un string
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, mundo\n")

# writelines(): Escribe una lista de strings
with open("archivo.txt", "w") as archivo:
    archivo.writelines(["Línea 1\n", "Línea 2\n", "Línea 3\n"])

# ============================================
# 5. PUNTEROS (SEEK Y TELL)
# ============================================

# tell(): Devuelve la posición actual del puntero
with open("archivo.txt", "r") as archivo:
    print(archivo.tell())  # 0 (inicio)
    archivo.read(5)
    print(archivo.tell())  # 5 (posición actual)

# seek(offset, desde_donde):
# offset: cantidad de bytes a mover
# desde_donde: 0=inicio, 1=posición actual, 2=final

with open("archivo.txt", "r") as archivo:
    # Leer los primeros 10 caracteres
    primeros = archivo.read(10)
    print(primeros)
    
    # Mover al inicio (posición 0)
    archivo.seek(0)
    inicio = archivo.read(5)
    print(inicio)  # Primeros 5 caracteres desde el inicio
    
    # Mover a la posición actual + 3
    archivo.seek(3, 1)  # Desde la posición actual
    
    # Mover al final
    archivo.seek(0, 2)  # Se mueve al final
    final = archivo.read()
    print(final)  # Lee desde el final (vacío si está al final)

# ============================================
# 6. MANEJO DE ERRORES (TRY / EXCEPT)
# ============================================

# Capturar errores al abrir archivos
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("❌ El archivo no existe.")
except PermissionError:
    print("❌ No tienes permisos para leer este archivo.")
except Exception as e:
    print(f"❌ Error inesperado: {e}")

# Verificar si un archivo existe antes de abrirlo
if os.path.exists("archivo.txt"):
    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()
else:
    print("⚠️ El archivo no existe. Se creará uno nuevo.")
    with open("archivo.txt", "w") as archivo:
        archivo.write("Archivo creado automáticamente.")

# ============================================
# 7. MÓDULO JSON
# ============================================

# Guardar datos en JSON (serializar)
datos = {
    "nombre": "Iván",
    "edad": 25,
    "ciudad": "Santiago"
}

with open("datos.json", "w") as archivo:
    json.dump(datos, archivo, indent=2)  # indent=2 mejora la legibilidad

# Cargar datos desde JSON (deserializar)
with open("datos.json", "r") as archivo:
    datos_cargados = json.load(archivo)

print(datos_cargados)  # {'nombre': 'Iván', 'edad': 25, 'ciudad': 'Santiago'}

# Leer JSON desde un string (json.loads)
json_string = '{"nombre": "Ana", "edad": 30}'
datos_desde_string = json.loads(json_string)
print(datos_desde_string)  # {'nombre': 'Ana', 'edad': 30}

# Convertir a string JSON (json.dumps)
string_json = json.dumps(datos, indent=2)
print(string_json)

# ============================================
# 8. MÓDULO PICKLE (objetos complejos)
# ============================================

# Guardar objetos con Pickle (modo binario 'wb')
import pickle

datos_complejos = {
    "lista": [1, 2, 3, 4, 5],
    "tupla": (10, 20, 30),
    "diccionario": {"a": 1, "b": 2}
}

with open("datos.pkl", "wb") as archivo:
    pickle.dump(datos_complejos, archivo)

# Cargar objetos desde Pickle (modo binario 'rb')
with open("datos.pkl", "rb") as archivo:
    datos_cargados = pickle.load(archivo)

print(datos_cargados)  # Se recupera el objeto completo

# ============================================
# 9. DIFERENCIA ENTRE JSON Y PICKLE
# ============================================

# JSON: Texto legible, solo datos básicos (str, int, float, list, dict)
# Pickle: Binario, guarda CUALQUIER objeto de Python (clases, funciones, etc.)

# ============================================
# 10. MANEJO DE ARCHIVOS Y DIRECTORIOS (MÓDULO OS)
# ============================================

import os

# Obtener el directorio actual
directorio_actual = os.getcwd()
print(f"Directorio actual: {directorio_actual}")

# Listar archivos en un directorio
archivos = os.listdir(".")
print(f"Archivos en el directorio: {archivos}")

# Crear una carpeta
os.mkdir("nueva_carpeta")  # Crea la carpeta

# Eliminar un archivo
os.remove("archivo_inexistente.txt")  # Genera error si no existe

# Verificar si un archivo existe
if os.path.exists("archivo.txt"):
    print("✅ El archivo existe.")
else:
    print("❌ El archivo no existe.")

# ============================================
# 11. EJEMPLO COMPLETO: MENÚ CON ARCHIVOS JSON
# ============================================

import json

def leer_datos(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=2)

def main():
    # Cargar datos existentes
    libros = leer_datos("libros.json")
    
    while True:
        print("\n1. Agregar libro")
        print("2. Mostrar libros")
        print("3. Salir")
        opcion = input("Opción: ")
        
        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            nuevo_libro = {"titulo": titulo, "autor": autor}
            libros.append(nuevo_libro)
            guardar_datos("libros.json", libros)
            print("✅ Libro agregado")
        
        elif opcion == "2":
            if libros:
                for libro in libros:
                    print(f"- {libro['titulo']} por {libro['autor']}")
            else:
                print("No hay libros")
        
        elif opcion == "3":
            print("👋 Hasta luego")
            break
        
        else:
            print("❌ Opción inválida")

if __name__ == "__main__":
    main()

# ============================================
# 12. EJERCICIO RÁPIDO PARA PRACTICAR
# ============================================

# 1. Crea un archivo "notas.txt" con 3 líneas de texto
# 2. Lee el archivo y muestra su contenido
# 3. Usa seek(0) para volver al inicio
# 4. Lee solo la primera línea y muéstrala
# 5. Guarda una lista de diccionarios en "datos.json"
# 6. Carga el archivo JSON y muestra los datos

# Solución:
"""
with open("notas.txt", "w") as archivo:
    archivo.write("Línea 1\nLínea 2\nLínea 3")

with open("notas.txt", "r") as archivo:
    print("Contenido:")
    print(archivo.read())
    archivo.seek(0)
    print("Primera línea:", archivo.readline().strip())

libros = [{"titulo": "Python", "autor": "Iván"}]
with open("datos.json", "w") as archivo:
    json.dump(libros, archivo, indent=2)

with open("datos.json", "r") as archivo:
    datos = json.load(archivo)
    print("Datos cargados:", datos)
"""

#Regla de oro:
Para recorrer un diccionario, usa for clave, valor in diccionario.items():

Para agregar elementos a un conjunto, usa conjunto.add(elemento)

# ============================================
# 1. FUNCIONES
# ============================================

# Definir una función
def saludar(nombre):
    """Docstring: explica qué hace la función"""
    return f"Hola, {nombre}!"

# Llamar a una función
saludar("Ana")  # "Hola, Ana!"

# Función con valor por defecto
def saludar(nombre="Mundo"):
    return f"Hola, {nombre}!"

# Función con múltiples parámetros
def suma(a, b):
    return a + b

# ============================================
# 2. LISTAS (Mutables, ordenadas)
# ============================================

# Crear lista
mi_lista = [1, 2, 3, 4, 5]

# Agregar al final
mi_lista.append(6)          # [1,2,3,4,5,6]

# Insertar en posición
mi_lista.insert(1, 10)      # [1,10,2,3,4,5,6]

# Eliminar por valor
mi_lista.remove(10)         # [1,2,3,4,5,6]

# Eliminar por índice
del mi_lista[0]             # [2,3,4,5,6]
mi_lista.pop(0)             # [3,4,5,6]

# Invertir
mi_lista.reverse()          # [6,5,4,3]

# Ordenar
mi_lista.sort()             # [3,4,5,6]
mi_lista.sort(reverse=True) # [6,5,4,3]

# Sumar elementos
sum(mi_lista)               # 18

# Cantidad de elementos
len(mi_lista)               # 4

# Acceder por índice
mi_lista[0]                 # Primer elemento
mi_lista[-1]                # Último elemento

# Slicing (rebanadas)
mi_lista[1:3]               # Elementos de índice 1 a 2
mi_lista[:3]                # Elementos hasta índice 2
mi_lista[2:]                # Elementos desde índice 2

# ============================================
# 3. TUPLAS (Inmutables, ordenadas)
# ============================================

# Crear tupla
mi_tupla = (1, 2, 3, 4)

# Acceder por índice
mi_tupla[0]                 # 1

# NO se puede modificar
# mi_tupla[0] = 10          # ❌ Error: TypeError

# Desempaquetar tupla
a, b, c = (1, 2, 3)         # a=1, b=2, c=3

# ============================================
# 4. CONJUNTOS (Sets) - Elementos únicos
# ============================================

# Crear conjunto
mi_set = {1, 2, 3, 4}

# Convertir lista a conjunto (elimina duplicados)
set([1, 2, 2, 3])           # {1, 2, 3}

# Agregar elemento
mi_set.add(5)               # {1,2,3,4,5}

# Eliminar elemento (con remove, si no existe da error)
mi_set.remove(5)            # {1,2,3,4}

# Eliminar elemento (con discard, si no existe no da error)
mi_set.discard(5)           # {1,2,3,4}

# Operaciones de conjuntos
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1 & set2                 # Intersección: {3}
set1 | set2                 # Unión: {1,2,3,4,5}
set1 - set2                 # Diferencia: {1,2}
set1 ^ set2                 # Diferencia simétrica: {1,2,4,5}

# Verificar si es subconjunto
{1, 2}.issubset({1, 2, 3})  # True

# ============================================
# 5. DICCIONARIOS (Clave-Valor)
# ============================================

# Crear diccionario
mi_dict = {"nombre": "Ana", "edad": 25}

# Acceder por clave
mi_dict["nombre"]           # "Ana"

# Acceder con get (evita error si no existe)
mi_dict.get("ciudad", "No especificada")

# Agregar o modificar
mi_dict["ciudad"] = "Santiago"

# Eliminar
del mi_dict["edad"]
mi_dict.pop("edad")

# Recorrer
for clave, valor in mi_dict.items():
    print(clave, valor)

# Verificar si existe clave
if "nombre" in mi_dict:
    print("Existe")

# Obtener todas las claves o valores
mi_dict.keys()              # dict_keys(['nombre', 'ciudad'])
mi_dict.values()            # dict_values(['Ana', 'Santiago'])

# ============================================
# 6. MÓDULOS
# ============================================

# Importar todo el módulo
import random
random.choice(lista)

# Importar función específica
from random import choice
choice(lista)

# Importar con alias
import random as rnd
rnd.choice(lista)

# ============================================
# 7. MÓDULO RANDOM
# ============================================

import random

# Número aleatorio entre 0.0 y 1.0
random.random()             # 0.374...

# Número entero entre 1 y 10
random.randint(1, 10)       # 7

# Elegir elemento aleatorio de lista
random.choice([1, 2, 3, 4]) # 3

# Mezclar lista (modifica la original)
random.shuffle(lista)

# Número decimal entre 5 y 10
random.uniform(5, 10)       # 7.83

# ============================================
# 8. MÓDULO DATETIME
# ============================================

from datetime import datetime, timedelta

# Fecha y hora actual
hoy = datetime.now()

# Crear fecha específica
fecha = datetime(2025, 12, 31, 18, 30)

# Convertir string a fecha
fecha = datetime.strptime("31/12/2025", "%d/%m/%Y")

# Formatear fecha a string
hoy.strftime("%d/%m/%Y")    # "24/07/2026"
hoy.strftime("%A %d de %B de %Y")

# Calcular diferencia
diferencia = fecha - hoy
diferencia.days             # Días de diferencia
diferencia.total_seconds()  # Segundos

# Sumar o restar días
manana = hoy + timedelta(days=1)
ayer = hoy - timedelta(days=1)

# Extraer componentes
hoy.year
hoy.month
hoy.day
hoy.hour
hoy.minute

# ============================================
# 9. MÓDULO MATH
# ============================================

import math

# Raíz cuadrada
math.sqrt(16)               # 4.0

# Redondear hacia arriba
math.ceil(3.2)              # 4

# Redondear hacia abajo
math.floor(3.8)             # 3

# Pi y Euler
math.pi                     # 3.14159
math.e                      # 2.71828

# Potencia
math.pow(2, 3)              # 8.0

# Valor absoluto
math.fabs(-5)               # 5.0

# Seno, coseno, tangente (en radianes)
math.sin(math.radians(45))  # 0.707
math.cos(math.radians(60))  # 0.5
math.tan(math.radians(45))  # 1.0

# Logaritmos
math.log(100, 10)           # 2.0 (log base 10)
math.log(100)               # 4.605 (log natural)

# ============================================
# 10. ARCHIVOS (TEXTO)
# ============================================

# Escribir (sobrescribe)
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola mundo\n")
    archivo.write("Segunda línea\n")

# Leer todo el contenido
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# Leer línea por línea
with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())

# Leer todas las líneas en una lista
with open("archivo.txt", "r") as archivo:
    lineas = archivo.readlines()

# Agregar al final
with open("archivo.txt", "a") as archivo:
    archivo.write("Nueva línea\n")

# Leer y escribir (modo 'r+')
with open("archivo.txt", "r+") as archivo:
    contenido = archivo.read()
    archivo.write("\nLínea agregada en r+")

# Verificar si archivo existe
import os
if os.path.exists("archivo.txt"):
    print("Existe")

# ============================================
# 11. ARCHIVOS JSON
# ============================================

import json

# Guardar en JSON (escribir)
datos = {"nombre": "Ana", "edad": 25}
with open("datos.json", "w") as archivo:
    json.dump(datos, archivo, indent=2)

# Guardar lista de diccionarios
libros = [
    {"titulo": "El Principito", "autor": "Saint-Exupéry"},
    {"titulo": "1984", "autor": "Orwell"}
]
with open("libros.json", "w") as archivo:
    json.dump(libros, archivo, indent=2)

# Cargar desde JSON (leer)
with open("datos.json", "r") as archivo:
    datos = json.load(archivo)

# JSON a string
json_string = json.dumps(datos, indent=2)

# String a JSON
datos = json.loads(json_string)

# ============================================
# 12. PUNTEROS (seek y tell)
# ============================================

# tell(): Devuelve la posición actual
with open("archivo.txt", "r") as archivo:
    print(archivo.tell())       # 0 (inicio)
    archivo.read(5)
    print(archivo.tell())       # 5 (posición actual)

# seek(offset, desde_donde)
# desde_donde: 0=inicio, 1=actual, 2=final

with open("archivo.txt", "r") as archivo:
    archivo.seek(0)             # Ir al inicio
    archivo.seek(0, 2)          # Ir al final
    archivo.seek(5)             # Ir a posición 5
    archivo.seek(10, 1)         # 10 desde posición actual

# Leer desde una posición específica
with open("archivo.txt", "r") as archivo:
    archivo.seek(10)            # Ir a posición 10
    contenido = archivo.read()  # Leer desde posición 10

# ============================================
# 13. EXCEPCIONES (try/except)
# ============================================

# Estructura básica
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("División por cero")
except Exception as e:
    print(f"Error: {e}")
else:
    print("Todo funcionó")
finally:
    print("Siempre se ejecuta")

# Ejemplo con archivos
try:
    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("Archivo no encontrado")
except PermissionError:
    print("No tienes permisos")
except Exception as e:
    print(f"Error inesperado: {e}")

# ============================================
# 14. TKINTER (Interfaz Gráfica)
# ============================================

import tkinter as tk
from tkinter import messagebox

# Crear ventana
ventana = tk.Tk()
ventana.title("Mi App")
ventana.geometry("400x300")
ventana.config(bg="#f5f5f5")

# Label (etiqueta)
label = tk.Label(ventana, text="Hola", font=("Arial", 12), bg="#f5f5f5")
label.pack(pady=10)

# Entry (entrada de texto)
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Text (multilínea)
texto = tk.Text(ventana, height=5, width=30)
texto.pack(pady=5)

# Button (botón)
def accion():
    valor = entrada.get()
    texto.insert(tk.END, f"\n{valor}")

boton = tk.Button(ventana, text="Presionar", command=accion, bg="#4CAF50", fg="white")
boton.pack(pady=10)

# Frame (contenedor)
frame = tk.Frame(ventana, bg="#f5f5f5")
frame.pack(pady=10)

# Radiobutton (opción única)
var_opcion = tk.StringVar()
radio1 = tk.Radiobutton(frame, text="Opción 1", variable=var_opcion, value="1", bg="#f5f5f5")
radio2 = tk.Radiobutton(frame, text="Opción 2", variable=var_opcion, value="2", bg="#f5f5f5")
radio1.pack(side=tk.LEFT, padx=5)
radio2.pack(side=tk.LEFT, padx=5)

# Checkbutton (múltiple)
var_check = tk.IntVar()
check = tk.Checkbutton(ventana, text="Acepto términos", variable=var_check, bg="#f5f5f5")
check.pack(pady=5)

# Menú desplegable
opciones = ["Opción A", "Opción B", "Opción C"]
var_menu = tk.StringVar()
var_menu.set(opciones[0])
menu = tk.OptionMenu(ventana, var_menu, *opciones)
menu.config(width=20)
menu.pack(pady=5)

# Messagebox (ventana emergente)
def mostrar_mensaje():
    messagebox.showinfo("Título", "Mensaje de información")
    messagebox.showerror("Error", "Ocurrió un error")
    messagebox.askyesno("Confirmación", "¿Estás seguro?")

boton_mensaje = tk.Button(ventana, text="Mostrar Mensaje", command=mostrar_mensaje)
boton_mensaje.pack(pady=5)

# Iniciar bucle principal
ventana.mainloop()

# ============================================
# 15. SENTENCIAS ÚTILES
# ============================================

# Verificar si lista está vacía
if not lista:
    print("Lista vacía")

# Recorrer diccionario
for clave, valor in diccionario.items():
    print(clave, valor)

# Unir lista en string
", ".join(["a", "b", "c"])  # "a, b, c"

# Separar string en lista
"a,b,c".split(",")         # ["a", "b", "c"]

# Verificar tipo de dato
type(variable)              # <class 'list'>

# Verificar si elemento está en lista
if elemento in lista:
    print("Está")

# Verificar si clave está en diccionario
if clave in diccionario:
    print("Está")

# Obtener valor por defecto
diccionario.get("clave", "default")

# Lista por comprensión
[p**2 for p in [1, 2, 3, 4]]   # [1, 4, 9, 16]

# Lista por comprensión con filtro
[p**2 for p in [1, 2, 3, 4] if p % 2 == 0]  # [4, 16]

# Conjunto por comprensión
{p for p in [1, 2, 2, 3]}       # {1, 2, 3}

# Diccionario por comprensión
{i: i**2 for i in range(3)}     # {0: 0, 1: 1, 2: 4}

# ============================================
# 16. BUENAS PRÁCTICAS
# ============================================

# 1. Usar nombres descriptivos
def calcular_promedio(notas):  # ✅ Bueno
    pass

def calc(notas):               # ❌ Malo
    pass

# 2. Usar docstrings
def mi_funcion():
    """Explica qué hace la función."""
    pass

# 3. Manejar excepciones
try:
    resultado = int(input("Número: "))
except ValueError:
    print("Ingresa un número válido")

# 4. Usar with para archivos
with open("archivo.txt", "r") as archivo:  # ✅ Se cierra automáticamente
    contenido = archivo.read()

# 5. Evitar código duplicado (DRY)
def validar_edad(edad):
    return edad >= 18

# 6. Usar constantes
PI = 3.14159

# 7. Verificar tipo de datos
if isinstance(variable, list):
    print("Es una lista")

# 8. Usar if __name__ == "__main__"
def main():
    # Código principal
    pass

if __name__ == "__main__":
    main()
