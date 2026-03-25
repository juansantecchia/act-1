import random
import string

categorias = {
    "deportes": [
        "futbol",
        "tenis",
        "padel",
        "golf",
        "voley",
        "rugby",
    ],
    "paises": [
        "argentina",
        "brasil",
        "chile",
        "mexico",
        "canada",
        "espana",
    ],
    "comidas": [
        "pizza",
        "milanesa",
        "empanada",
        "asado",
        "pasta",
        "hamburguesa",
    ],
}

print("Categorías disponibles:")
print("1 - deportes")
print("2 - paises")
print("3 - comidas")

opcion = input("Elegí una categoría: ").strip()

if opcion == "1":
    words = categorias["deportes"]
elif opcion == "2":
    words = categorias["paises"]
elif opcion == "3":
    words = categorias["comidas"]
else:
    print("Opción no válida. Se usará deportes.")
    words = categorias["deportes"]

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