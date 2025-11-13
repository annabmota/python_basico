# Modulo sonidos (error, derrota y victoria)

# librrías necesarias.
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

# Inicializamos el mixer una sola vez.
pygame.mixer.init()

# Bloque para iniciar snidos.
def reproducir_sonido(nombre_archivo):
    ruta = os.path.join(os.getcwd(), nombre_archivo)
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.play()

# Bloque tipos de sonidos.
def sonido_error():
    reproducir_sonido("sonido_error.mp3")

def sonido_victoria():
    reproducir_sonido("sonido_victoria.mp3")

def sonido_derrota():
    reproducir_sonido("sonido_derrota.mp3")

