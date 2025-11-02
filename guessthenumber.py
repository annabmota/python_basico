# Validar opción y/o dificultad
def valida(minimo, maximo):
    opcion = minimo - 1
    while opcion < minimo or opcion > maximo:
        opcion = int(input(f"Escribe una opción {minimo} y {maximo}: ")) # incluir mensaje si la dificultad no es correcta
    return opcion

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
import random as rdm
def modo_solitario():
    intentos = submenu()
    numero_a_adivinar = rdm.randint(1, 1000)
    for i in range(intentos):
        numero_introducido = int(input("Adivina el número entre 1 y 1000: "))
        if numero_introducido < numero_a_adivinar:
            print("El número es mayor.")
        elif numero_introducido > numero_a_adivinar:
            print("El número es menor.")
        else:
            print(f"🎉 ¡Has adivinado el número en {i+1} intentos!")
            return
    else:
        print(f"😢 Se acabaron los intentos. El número era {numero_a_adivinar}.")        