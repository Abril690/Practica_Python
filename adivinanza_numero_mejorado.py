import random

def pedir_numero(mensaje, minimo, maximo):
    """Pide al usuario un número dentro de un rango y gestiona errores."""
    while True:
        try:
            num = int(input(mensaje))
            if num < minimo or num > maximo:
                print(f"Por favor, ingresa un número entre {minimo} y {maximo}.")
                continue
            return num
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")

def mostrar_historial(intentos_historial):
    if intentos_historial:
        print("\nHistorial de intentos anteriores:")
        for num in intentos_historial:
            print(f"- {num}")
    else:
        print("Aún no has hecho intentos.")

def juego_adivinanza():
    print("¡Bienvenido al juego de adivinanza mejorado!")
    print("Debes adivinar el número secreto entre 1 y 100.")
    print("Tienes 10 intentos. ¡Suerte!\n")
    
    while True:
        secreto = random.randint(1, 100)
        intentos_restantes = 10
        intentos_historial = []

        while intentos_restantes > 0:
            mostrar_historial(intentos_historial)
            adivinanza = pedir_numero(f"\nIntentos restantes: {intentos_restantes}. Ingresa tu número: ", 1, 100)
            intentos_historial.append(adivinanza)

            if adivinanza < secreto:
                print("Demasiado bajo.")
            elif adivinanza > secreto:
                print("Demasiado alto.")
            else:
                print(f"\n¡Felicidades! Has adivinado el número {secreto} en {len(intentos_historial)} intentos.")
                break
            intentos_restantes -= 1

        if intentos_restantes == 0 and adivinanza != secreto:
            print(f"\n¡Te has quedado sin intentos! El número secreto era: {secreto}")

        opcion = input("\n¿Deseas jugar de nuevo? (s/n): ").strip().lower()
        if opcion != 's':
            print("¡Gracias por jugar! ¡Hasta la próxima!")
            break

if __name__ == "__main__":
    juego_adivinanza()
