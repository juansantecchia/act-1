import random
import string

words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]

word = random.choice(words)
guessed = []
attempts = 6
score = 0

print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "

    print(progress)

    if "_" not in progress:
        print("¡Ganaste!")
        score += 6
        print(f"Puntaje final: {score}")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ").lower().strip()

    if len(letter) != 1 or letter not in string.ascii_lowercase:
        print("Entrada no válida")
        print()
        continue

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        score -= 1
        print("Esa letra no está en la palabra.")

    print()
else:
    score = 0
    print(f"¡Perdiste! La palabra era: {word}")
    print(f"Puntaje final: {score}")