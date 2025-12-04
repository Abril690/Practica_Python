import random

def juego_adivinanza():
    print("¡Bienvenido al juego de adivinanza!")
    secreto = random.randint(1, 100)
    intentos = 0

    while True:
        try:
            adivinanza = int(input("Adivina el número secreto entre 1 y 100: "))
            intentos += 1

            if adivinanza < secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif adivinanza > secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor ingresa un número válido.")

if __name__ == "__main__":
    juego_adivinanza()
