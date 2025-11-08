# Paquetes necesarios
import random as rdm
from datetime import datetime
import openpyxl
import pandas as pd
import os
import time
import getpass

# Validar opción y/o dificultad
def valida(minimo, maximo):
    mensaje = f"Elige una opción entre {minimo} y {maximo}: "
    while True: #bucle infinito hasta que se introduzca una opción válida
        try:
            opcion = int(input(mensaje))
            if minimo <= opcion <= maximo:
                return opcion
            else:
                mensaje = f"⚠️ Opción no válida. Debe estar entre {minimo} y {maximo}: "
        except ValueError:
            mensaje = f"🚫 Valor no válido. Introduce un número entre {minimo} y {maximo}: " # Cuando no se introduce un número

def menu():
    print("\n🎯==============================🎯")
    print("     ¡ADIVINA EL NÚMERO! 🎲")
    print("🎯==============================🎯\n")
    print("1️⃣  Modo Solitario")
    print("   🤖 Ponte a prueba contra el ordenador. ¡Demuestra lo que vales!")
    print("\n2️⃣  Modo Multijugador")
    print("   👥 Un jugador elige el número, el otro intenta adivinarlo.")
    print("\n3️⃣  Estadísticas")
    print("   📊 Consulta tus logros y puntuaciones guardadas.")
    print("\n4️⃣  Salir")
    print("   🚪 Cierra el juego.\n")

def salir():
    print("👋 ¡Hasta luego!")
    print("\nSaliendo", end="", flush=True)
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    time.sleep(0.5)
    print("✨ Has salido del juego. ¡Vuelve pronto! 🎯\n")
    return

# ¡A jugar!
def jugar():
    menu()
    opcion = valida(1, 4)
    if opcion == 1:
        modo_solitario()
    elif opcion == 2:
        modo_multijugador()
    elif opcion == 3:
        estadistica()
    else:
        salir()
    return

# Menu de dificultad
def submenu():
    print("\n==================================")
    print("💪 ELIGE TU NIVEL DE DIFICULTAD 💪")
    print("==================================\n")
    print("🐣 1️⃣  Fácil — 20 intentos")
    print("   🌼 Ideal para calentar motores y disfrutar sin prisas.\n")
    print("🔥 2️⃣  Medio — 12 intentos")
    print("   ⚡ Un desafío equilibrado: ¡demuestra tu instinto!\n")
    print("💀 3️⃣  Difícil — 5 intentos")
    print("   💣 Solo para valientes. ¿Te atreves?\n")
    print("↩️ 4️⃣  Volver al menú principal")
    print("   🔙 ¿Cambiaste de idea?, ¡no pasa nada!\n")
    dificultad = valida(1, 4)
    if dificultad == 1:
        return 20
    elif dificultad == 2:
        return 12
    elif dificultad == 3:
        return 5
    else:
        print("\nVolviendo", end="", flush=True)
        for _ in range(3):
            time.sleep(0.4)
            print(".", end="", flush=True)
        time.sleep(0.5)
        print("\n")
        jugar()  # Volver al menú principal si la opción no es válida


# Modo solitario
def modo_solitario():
    # Establecer número de intentos según dificultad
    intentos = submenu()
    if intentos is None: # Volver al menú principal si no hay intentos guardados (opción 4)
        return
    # Datos que se van a guardar
    modo = "Solitario"
    numero_a_adivinar = rdm.randint(1, 1000)
    nombre_jugador = input("Introduce tu nombre para guardar tu progreso: ")
    estadisticas_jugador = []
    
    # Frases aleatorias para pistas
    pistas_mayor = [
        "\n🔺 ¡Más arriba, más arriba!\n",
        "\n📈 Sube un poco más, ¡casi llegas!\n",
        "\n😏 El número es más grande...\n",
        "\n🚀 Necesitas apuntar más alto.\n",
        "\n🧗‍♂️ Piensa en algo más grande.\n"
    ]

    pistas_menor = [
        "\n🔻 ¡Demasiado alto, bájale un poco!\n",
        "\n📉 Ups, te pasaste. Prueba un número menor.\n",
        "\n😅 No tan alto, intenta más bajo.\n",
        "\n🏂 Baja un poco, que te pasaste.\n",
        "\n🐜 El número es más pequeño que ese.\n"
    ]

    for i in range(intentos):
        numero_introducido = int(input(f"{nombre_jugador}, adivina el número entre 1 y 1000: ")) # Validar que el número esté entre 1 y 1000
        if numero_introducido < numero_a_adivinar:
            print(rdm.choice(pistas_mayor))
        elif numero_introducido > numero_a_adivinar:
            print(rdm.choice(pistas_menor))
        else:
            print(f"\n🎉 ¡Has adivinado el número en {i+1} intentos!\n")
            print(f"\n🏆 ¡Eres una máquina de adivinar números, {nombre_jugador}!\n")
            fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            estadisticas_jugador.append((modo, nombre_jugador, numero_a_adivinar, i+1, fecha_hora_actual))
            guardar_stats(estadisticas_jugador)
            jugar()
            return
    else:
        print(f"\n😢 Se acabaron los intentos. El número era {numero_a_adivinar}.\n")
        print(f"\n💪 ¡No te rindas {nombre_jugador}! La próxima vez seguro lo consigues.\n")
        fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        estadisticas_jugador.append((modo, nombre_jugador, numero_a_adivinar, i+1, fecha_hora_actual))
        guardar_stats(estadisticas_jugador)
        jugar()
        return
    
# Modo multijugador
def modo_multijugador():
    # Establecer número de intentos según dificultad
    intentos = submenu()
    if intentos is None: # Volver al menú principal si no hay intentos guardados (opción 4)
        return
    # Datos que se van a guardar
    modo = "Multijugador"
    nombre_jugador1 = input("Jugador 1, introduce tu nombre: ")
    nombre_jugador2 = input("Jugador 2, introduce tu nombre: ")
    numero_a_adivinar_jugador1 = int(getpass.getpass((f"{nombre_jugador1}, introduce el número a adivinar (entre 1 y 1000): ")))
    estadisticas_jugador = [] 

    # Frases aleatorias para pistas
    pistas_mayor = [
        "\n🔺 ¡Más arriba, más arriba!\n",
        "\n📈 Sube un poco más, ¡casi llegas!\n",
        "\n😏 El número es más grande...\n",
        "\n🚀 Necesitas apuntar más alto.\n",
        "\n🧗‍♂️ Piensa en algo más grande.\n"
    ]

    pistas_menor = [
        "\n🔻 ¡Demasiado alto, bájale un poco!\n",
        "\n📉 Ups, te pasaste. Prueba un número menor.\n",
        "\n😅 No tan alto, intenta más bajo.\n",
        "\n🏂 Baja un poco, que te pasaste.\n",
        "\n🐜 El número es más pequeño que ese.\n"
    ]

    for i in range(intentos):
        numero_introducido_jugador2 = int(input(f"{nombre_jugador2}, adivina el número entre 1 y 1000: "))
        if numero_introducido_jugador2 < numero_a_adivinar_jugador1:
            print(rdm.choice(pistas_mayor))
        elif numero_introducido_jugador2 > numero_a_adivinar_jugador1:
            print(rdm.choice(pistas_menor))
        else:
            print(f"\n🎉 ¡Has adivinado el número en {i+1} intentos!\n")
            print(f"\n🏆 ¡{nombre_jugador1} no ha podido contigo {nombre_jugador2}!\n")
            fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            estadisticas_jugador.append((modo, nombre_jugador2, numero_a_adivinar_jugador1, i+1, fecha_hora_actual))
            guardar_stats(estadisticas_jugador)
            jugar()
            return
    else:
        print(f"\n😢 Se acabaron los intentos. El número era {numero_a_adivinar_jugador1}.\n")
        print(f"\n💪 ¡Vaya número te ha puesto {nombre_jugador1}! La próxima vez seguro lo consigues {nombre_jugador2}.\n")
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
    print("\nCargando", end="", flush=True)
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    time.sleep(0.5)
    print("\n")
    if os.path.exists("estadisticas_jugador.xlsx"):
        bbdd_guessthenumber = pd.read_excel("estadisticas_jugador.xlsx")
        print("\n📊 ESTADÍSTICAS DE JUEGO 📊")
        print("-" * 70)
        print(bbdd_guessthenumber.to_string(index=False))
        print("-" * 70)
        jugar()
        return
    else:
        print("No hay estadísticas guardadas.")
        jugar()
        return