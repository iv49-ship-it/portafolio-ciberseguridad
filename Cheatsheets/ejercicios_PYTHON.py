def es_impar(numero):
    return numero % 2 != 0

print(es_impar(4))
print(es_impar(3))

def es_positivo(numero):
    return numero > 0

print(es_positivo(-5))
print(es_positivo(6))

def clasificar_numero(numero):
    if numero > 0 and numero % 2 == 0:
        return "Positivo y Par"
    if numero > 0 and numero % 2 != 0:
        return "Positivo e impar"
    if numero < 0 and numero % 2 == 0:
        return "Negativo e par"
    if numero < 0 and numero % 2 != 0:
        return "Negativo y impar"
    if numero == 0:
        return "Cero"
    
print(clasificar_numero(5))


def calcular_nota(numero):
    if numero >= 90 and numero <= 100:
        return "Excelente"
    elif numero >= 70 and numero <= 89:
        return "Bueno"
    elif numero >= 50 and numero <= 69:
        return "Suficiente"
    elif numero >= 0 and numero <= 49:
        return "Insuficiente"
    else:
        return "Error, porque es un número negativo"
    
print(calcular_nota(56))

def lista_visitantes():
    sala1 = ["Luis", "Armando","Francisca", "Ana"]
    sala2 = ["Carlos", "Amanda", "Fernando", "Camila","Valentina"]
    sala3 = ["Mariana","Marcela", "Eduardo", "Juan"]

    visitantes_unicos = list(set(sala1 + sala2 + sala3))
    return visitantes_unicos

resultado = lista_visitantes()
print(f"Lista única de visitantes{resultado}") 
    
# ==========================================
# PROGRAMA PARA REGISTRO DE VISITANTES DEL MUSEO
# ==========================================

# 1. Registro de visitantes por sala (usando listas)
sala1 = ["Pedro", "Carlos", "Laura", "Elena"]
sala2 = ["Manuel", "Laura", "Juan", "Pedro"]
sala3 = ["Pedro", "Elena", "Luis", "Ana"]

# 2. Función para obtener lista única usando conjuntos
def obtener_lista_unica(s1, s2, s3):
    """
    Recibe tres listas de visitantes y retorna una lista única sin duplicados.
    Utiliza conjuntos para eliminar automáticamente los repetidos.
    """
    # Unir todas las listas y convertir a conjunto para eliminar duplicados
    visitantes_unicos = set(s1 + s2 + s3)
    # Convertir de vuelta a lista y ordenar alfabéticamente
    return sorted(list(visitantes_unicos))

# 3. Mostrar los registros por sala
print("=" * 50)
print("REGISTRO DE VISITANTES POR SALA")
print("=" * 50)
print(f"Sala 1: {sala1}")
print(f"Sala 2: {sala2}")
print(f"Sala 3: {sala3}")

# 4. Obtener y mostrar la lista única
print("\n" + "=" * 50)
print("LISTA ÚNICA DE VISITANTES")
print("=" * 50)

lista_final = obtener_lista_unica(sala1, sala2, sala3)
print(f"Visitantes únicos: {lista_final}")
print(f"Total de visitantes únicos: {len(lista_final)}")

def calcular_imc(peso,altura):

    if peso < 0:
        return "ERROR: El peso no puede ser negativo"
    if altura < 0:
        return "ERROR: La altura no puede ser negativa"
    if altura == 0:
        return "ERROR: La altura no puede ser CERO"
    
    IMC = peso / (altura **2)
    return  round(IMC,1)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

resultado = calcular_imc(peso, altura)
print(f"Su IMC es: {resultado}")


def numeros(lista):
    lista.append(60)
    lista.insert(1, 15)
    lista.remove(40)
    lista.reverse()
    print(f"Adentro de la función:{lista}")

mi_lista = [10, 20, 30, 40, 50]
numeros(mi_lista)

print(f"Fuera de la función: {mi_lista}")

def tiempos_de_entrenamiento(cliente_A, cliente_B):
    cliente_A.append(55)
    del cliente_B[1]

cliente_A = [30, 45, 60, 40]
cliente_B = [50, 55, 45, 30, 65]

print(f"Lista cliente A: {cliente_A}")
print(f"Lista cliente B: {cliente_B}")

tiempos_de_entrenamiento(cliente_A, cliente_B)

print(f"Después - Cliente A: {cliente_A}") 
print(f"Después - Cliente B: {cliente_B}") 


def gestion_de_vuelos(vuelo_A, vuelo_B):
    # Mostrar información de los vuelos
    print(f"Información del Vuelo A: {vuelo_A}")
    print(f"Destino del Vuelo B: {vuelo_B[1]}")  # Índice 1 = destino

# Datos iniciales
vuelo_A = ("AirlineX", "Nueva York", "12:30")
vuelo_B = ("AirlineY", "París", "15:45")

# Llamar a la función con ambos argumentos
gestion_de_vuelos(vuelo_A, vuelo_B)

# Las tuplas NO se modifican (son inmutables)
print(f"\nVuelo A original: {vuelo_A}")
print(f"Vuelo B original: {vuelo_B}")

# Mostrar que NO se pueden modificar
# vuelo_A[0] = "NewAirline"  # Esto genera TypeError
# 

def palabras_unicas():
    documento = "Este es un ejemplo de un documento con palabras únicas. Este documento contiene palabras únicas"
    
    # 1. Dividir el documento en palabras (split por espacio)
    palabras = documento.split()
    
    # 2. Crear un conjunto para eliminar duplicados
    palabras_unicas_set = set(palabras)
    
    # 3. Mostrar las palabras únicas
    print("Palabras Únicas en el Documento:")
    for palabra in palabras_unicas_set:
        print(f"- {palabra}")

# Llamar a la función
palabras_unicas()


import random

def seleccionar_ganador(lista_participantes):
    # Verificar si la lista está vacía
    if not lista_participantes:
        return "No hay participantes"
    
    # Seleccionar un ganador al azar
    ganador = random.choice(lista_participantes)
    
    # Mostrar y retornar el resultado
    print(f"🎉 El ganador es: {ganador}")
    return ganador

# Datos de prueba
lista_nombres = ["Nicolás", "Alberto", "Carlos"]

# Llamar a la función
ganador = seleccionar_ganador(lista_nombres)
print(f"Ganador retornado: {ganador}")

def calcular_edad(fecha_nacimiento):
    #verificar que la fecha sea válida
    if not fecha_nacimiento:
        return "Fecha inválida"
    #Recibe una fecha de nacimiento como string
    fecha_nacimiento = "dd/mm/YYYY"
    #Retornar la edad en años
    edad = fecha_nacimiento.datetime.date.today()


#TAREA SEMANA 6
import json

# ==========================================
# FUNCIONES DE ARCHIVO
# ==========================================

def leer_archivo(nombre):
    try:
        with open(nombre, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def escribir_archivo(nombre, datos):
    with open(nombre, 'w') as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)

def agregar_libro(titulo, genero, año, autor):
    return {
        "titulo": titulo,
        "genero": genero,
        "año": año,
        "autor": autor
    }

def agregar_autor(nombre, nacionalidad):
    return {
        "nombre": nombre,
        "nacionalidad": nacionalidad
    }

def mostrar_info(libros, autores):
    print("\n" + "=" * 50)
    print("📚 LIBROS REGISTRADOS")
    print("=" * 50)
    print(json.dumps(libros, indent=2, ensure_ascii=False) if libros else "No hay libros registrados.")
    
    print("\n" + "=" * 50)
    print("👤 AUTORES REGISTRADOS")
    print("=" * 50)
    print(json.dumps(autores, indent=2, ensure_ascii=False) if autores else "No hay autores registrados.")

def main():
    libros = leer_archivo("libros.json")
    autores = leer_archivo("autores.json")
    
    while True:
        print("\n" + "=" * 40)
        print("📚 SISTEMA DE GESTIÓN DE LIBROS Y AUTORES")
        print("=" * 40)
        print("1. Agregar Libro")
        print("2. Agregar Autor")
        print("3. Mostrar Información")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            titulo = input("Título: ")
            genero = input("Género: ")
            año = input("Año de publicación: ")
            autor = input("Nombre del autor: ")
            
            libros.append(agregar_libro(titulo, genero, año, autor))
            escribir_archivo("libros.json", libros)
            print("✅ Libro agregado con éxito.")
            
        elif opcion == '2':
            nombre = input("Nombre del autor: ")
            nacionalidad = input("Nacionalidad: ")
            
            autores.append(agregar_autor(nombre, nacionalidad))
            escribir_archivo("autores.json", autores)
            print("✅ Autor agregado con éxito.")
            
        elif opcion == '3':
            mostrar_info(libros, autores)
            
        elif opcion == '4':
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    main()

def caja_magica(numero):
    return numero * 3

print(caja_magica(5))











    
