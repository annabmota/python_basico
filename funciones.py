#######################
# Paquetes necesarios #
#######################
import os
import time
import getpass
import random as rdm
from datetime import datetime
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Ocultar el mensaje de bienvenida de pygame
# Manejo de errores por librerías no instaladas
try:
    import openpyxl
    import pandas as pd
    import pygame
except ModuleNotFoundError as e:
    print("⚠️ Falta una librería necesaria:", e.name)
    print("Instala las dependencias con: pip install -r requirements.txt")


################
# Validaciones #
################


# Validar opción y/o dificultad
def valida(minimo, maximo):
    mensaje = f"Elige una opción entre {minimo} y {maximo}: "
    while True: #bucle infinito hasta que se introduzca una opción válida
        try:
            opcion = int(input(mensaje))
            if minimo <= opcion <= maximo:
                return opcion
            else:
                mensaje = f"⚠️ Opción no válida. Debe estar entre {minimo} y {maximo}: " # Cuando el número no está en el rango
        except ValueError:
            mensaje = f"🚫 Valor no válido. Introduce un número entre {minimo} y {maximo}: " # Cuando no se introduce un número

# Validar número introducido (igual que la validación de opción)
def valida_numero(nombre_jugador):
    # Establecemos el mínimo y el máximo
    minimo = 1 
    maximo = 1000
    mensaje = f"{nombre_jugador}, adivina el número entre {minimo} y {maximo}: "
    while True:
        try:
            numero = int(input(mensaje))
            if minimo <= numero <= maximo:
                return numero
            else:
                mensaje = f"⚠️ Número no válido. Debe estar entre {minimo} y {maximo}: "
        except ValueError:
            mensaje = f"🚫 Valor no válido. Introduce un número entre {minimo} y {maximo}: "

# Validar el número oculto introducido (igual que las dos validaciones anteriores)
def valida_numero_oculto(nombre_jugador):
    minimo = 1
    maximo = 1000
    mensaje = f"{nombre_jugador}, introduce el número a adivinar (entre {minimo} y {maximo}): "
    while True:
        try:
            numero = int(getpass.getpass(mensaje))
            if minimo <= numero <= maximo:
                return numero
            else:
                mensaje = f"⚠️ Número no válido. Debe estar entre {minimo} y {maximo}: "
        except ValueError:
            mensaje = f"🚫 Valor no válido. Introduce un número entre {minimo} y {maximo}: "


#######################
# Funciones de sonido #
#######################


# Los sonidos deben estar en la misma carpeta que el script

# Música de fondo
def musica_fondo():
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "game_music.mp3")
    pygame.mixer.music.stop()
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.play(-1) # Reproducir en bucle

# Música de fondo según dificultad
def musica_fondo_facil():
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "easy_mode_music.mp3")
    pygame.mixer.music.stop()
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.play(-1)

def musica_fondo_medio():
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "medium_mode_music.mp3")
    pygame.mixer.music.stop()
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.play(-1)

def musica_fondo_dificil():
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hard_mode_music.mp3")
    pygame.mixer.music.stop()
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.play(-1)

# Sonido de victoria al adivinar el número
def sonido_victoria():
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "victory_sound.mp3")
    sonido = pygame.mixer.Sound(ruta)
    sonido.play()

# Sonido de derrota al no adivinar el número
def sonido_derrota():
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "defeat_sound.mp3")
    sonido = pygame.mixer.Sound(ruta)
    sonido.play()


############
# Visuales #
############

# Menú principal del juego
def menu():
    print("\n🎯==============================🎯")
    print("       ¡ADIVINA EL NÚMERO! 🎲")
    print("🎯==============================🎯\n")
    print("1️⃣  Modo Solitario")
    print("   🤖 Ponte a prueba contra el ordenador. ¡Demuestra lo que vales!")
    print("\n2️⃣  Modo Multijugador")
    print("   👥 Un jugador elige el número, el otro intenta adivinarlo.")
    print("\n3️⃣  Estadísticas")
    print("   📊 Consulta tus logros y puntuaciones guardadas.")
    print("\n4️⃣  Salir")
    print("   🚪 Cierra el juego.\n")

# Salir del juego (con animación)
def salir():
    print("👋 ¡Hasta luego!")
    print("\nSaliendo", end="", flush=True)
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    time.sleep(0.5)
    print("✨ Has salido del juego. ¡Vuelve pronto! 🎯\n")
    pygame.mixer.quit()
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