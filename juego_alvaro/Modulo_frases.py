import random

#Bloque pistas si el número es demasiado bajo.
def pista_bajo():
    frases = [
        "⬆️ Más alto...",
        "🔍 Estás cerca, pero sube un poco.",
        "❄️ Frío frío, tienes que aumentar el número.",
        "🔥 Caliente, pero te falta subir.",
        "🧭 Sigue buscando... más arriba."
    ]
    return random.choice(frases)

#Bloque pistas si el número es demasiado alto.
def pista_alto():
    frases = [
        "⬇️ Más bajo...",
        "📉 Te has pasado, baja un poco.",
        "❄️ Frío frío, el número es menor.",
        "👌 Vas bien, pero reduce el número.",
        "🎯 Estás cerca… pero baja un pelín."
    ]
    return random.choice(frases)