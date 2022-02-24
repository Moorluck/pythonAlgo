import os

produits = [
    ["Banane", 5, 1.5],
    ["TV", 2, 150],
    ["Machine à laver", 3, 350]
]
panier = []

print("Bienvenue dans notre magasin")

quitter = False
while not quitter:

    print("Que voulez-vous faire ?")
    i = 0
    for produit in produits:
        print(i + 1, "- Acheter un", produit[0], "pour", produit[2], " euros")
        i = i + 1
    print("R - Régler")
    print("Q - Quitter")
    choix = input()

    os.system("cls")

    if choix.isdigit():
        position = int(choix) - 1
        produit = produits[position]
        if produit[1] > 0:
            panier.append((produit[0], produit[2]))
            produits[position][1] -= 1
            print("Produit ajouté")
        else:
            print("Produit pas en stock")

    elif choix == "R":
        somme = 0
        for produit in panier:
            prix = produit[1]
            somme = somme + prix
        if somme >= 50:
            print("La livraison est offerte")
            print("Le total est de", somme, "euros")
        else:
            frais_de_port = somme*5/100
            somme = somme + frais_de_port
            print("Le total est de", somme, "euros")

    elif choix == "Q":
        quitter = True