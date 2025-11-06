# Paquetes necesarios
import random as rdm
from datetime import datetime
import openpyxl
import pandas as pd
import os

# Validar opción y/o dificultad
def valida(minimo, maximo):
    mensaje = f"Elige una opción entre {minimo} y {maximo}: "
    while True: #bucle infinito hasta que se introduzca una opción válida
        try:
            opcion = int(input(mensaje))
            if minimo <= opcion <= maximo:
                return opcion
            else:
                mensaje = f"Opción no válida. Debe estar entre {minimo} y {maximo}: "
        except ValueError:
            mensaje = f"Valor no válido. Introduce un número entre {minimo} y {maximo}: " # Cuando no se introduce un número

# ¡A jugar!
def jugar():
    print("=== Adivina el número === \n1. Modo solitario \n2. Modo multijugador \n3. Estadística \n4. Salir")
    opcion = valida(1, 4)
    if opcion == 1:
        modo_solitario()
    elif opcion == 2:
        modo_multijugador()
    elif opcion == 3:
        estadistica()
    else:
        print("¡Hasta luego!") # Opción salir
    return

# Menu de dificultad
def submenu():
    print("1. Fácil (20 intentos) \n2. Medio (12 intentos) \n3. Difícil (5 intentos)")
    dificultad = valida(1, 3)
    if dificultad == 1:
        intentos = 20
    elif dificultad == 2:
        intentos = 12
    else:
        intentos = 5
    return intentos

# Modo solitario
def modo_solitario():
    modo = "Solitario"
    intentos = submenu()
    numero_a_adivinar = rdm.randint(1, 1000)
    nombre_jugador = input("Introduce tu nombre para guardar tu progreso: ")
    estadisticas_jugador = []
    for i in range(intentos):
        numero_introducido = int(input(f"{nombre_jugador}, adivina el número entre 1 y 1000: ")) # Validar que el número esté entre 1 y 1000
        if numero_introducido < numero_a_adivinar:
            print("El número es mayor.")
        elif numero_introducido > numero_a_adivinar:
            print("El número es menor.")
        else:
            print(f"🎉 ¡Has adivinado el número en {i+1} intentos!")
            fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            estadisticas_jugador.append((modo, nombre_jugador, numero_a_adivinar, i+1, fecha_hora_actual))
            guardar_stats(estadisticas_jugador)
            jugar()
            return
    else:
        print(f"😢 Se acabaron los intentos. El número era {numero_a_adivinar}.")
        fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        estadisticas_jugador.append((modo, nombre_jugador, numero_a_adivinar, i+1, fecha_hora_actual))
        guardar_stats(estadisticas_jugador)
        jugar()
        return
    
# Modo multijugador
def modo_multijugador():
    modo = "Multijugador"
    intentos = submenu()
    nombre_jugador1 = input("Jugador 1, introduce tu nombre: ")
    nombre_jugador2 = input("Jugador 2, introduce tu nombre: ")
    numero_a_adivinar_jugador1 = int(input((f"{nombre_jugador1}, introduce el número a adivinar (entre 1 y 1000): ")))
    estadisticas_jugador = [] # Hacer que los números no se vean al escribir
    for i in range(intentos):
        numero_introducido_jugador2 = int(input(f"{nombre_jugador2}, adivina el número entre 1 y 1000: "))
        if numero_introducido_jugador2 < numero_a_adivinar_jugador1:
            print("El número es mayor.")
        elif numero_introducido_jugador2 > numero_a_adivinar_jugador1:
            print("El número es menor.")
        else:
            print(f"🎉 ¡Has adivinado el número en {i+1} intentos!")
            fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            estadisticas_jugador.append((modo, nombre_jugador2, numero_a_adivinar_jugador1, i+1, fecha_hora_actual))
            guardar_stats(estadisticas_jugador)
            jugar()
            return
    else:
        print(f"😢 Se acabaron los intentos. El número era {numero_a_adivinar_jugador1}.")
        fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        estadisticas_jugador.append((modo, nombre_jugador2, numero_a_adivinar_jugador1, i+1, fecha_hora_actual))
        guardar_stats(estadisticas_jugador)
        jugar()
        return  
    
# Guardar estadísticas
def guardar_stats(estadisticas_jugador):
    bbdd_guessthenumber_act = pd.DataFrame(estadisticas_jugador, columns=["Modo", "Nombre", "Número a adivinar", "Intentos", "Fecha y hora"])

    if os.path.exists("estadisticas_jugador.xlsx"):
        bbdd_guessthenumber_ant = pd.read_excel("estadisticas_jugador.xlsx")
        bbdd_guessthenumber = pd.concat([bbdd_guessthenumber_ant, bbdd_guessthenumber_act], ignore_index=True)
    else:
        bbdd_guessthenumber = bbdd_guessthenumber_act

    bbdd_guessthenumber.to_excel("estadisticas_jugador.xlsx", index=False)
    return

# Estadísticas
def estadistica():
    if os.path.exists("estadisticas_jugador.xlsx"):
        bbdd_guessthenumber = pd.read_excel("estadisticas_jugador.xlsx")
        print(bbdd_guessthenumber)
    else:
        print("No hay estadísticas guardadas.")
    jugar()
    return