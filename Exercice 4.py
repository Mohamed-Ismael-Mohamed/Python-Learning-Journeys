# Exercice 4 : Affichage des degrés des sommets

sommets = ["A", "B", "C", "D", "E"]
degres = [2, 3, 1, 4, 2]

# Affichage de l'en-tête
print("Indice".ljust(10) + "Sommet".ljust(10) + "Degré")

# Parcours des sommets avec leur indice
for indice, sommet in enumerate(sommets, start=1):

    print(
        str(indice).ljust(10)
        + sommet.ljust(10)
        + str(degres[indice - 1])
    )

# Affichage du nombre total de sommets
print("-" * 30)
print(f"Nombre total de sommets : {len(sommets)}")
