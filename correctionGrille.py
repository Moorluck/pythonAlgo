import os
import random

grille = []

for i in range(5):
    grille.append(
        ["_", "_", "_", "_", "_"]
    )

objet_cache = (random.randint(0, 4), random.randint(0, 4))

gagner = False
while not gagner:
    os.system("cls")

    for element in grille:
        print(element)

    x_prop = int(input("Coordonnée X : "))
    y_prop = int(input("Coordonnée Y : "))

    if x_prop == objet_cache[0] and y_prop == objet_cache[1]:
        gagner = True
        grille[x_prop][y_prop] = "O"
    else:
        grille[x_prop][y_prop] = "X"

for element in grille:
    print(element)

input()