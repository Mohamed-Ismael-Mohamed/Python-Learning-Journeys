# Exercice 3 : Parcours des arêtes pondérées

depart = ["A", "B", "C", "D"]
arrivee = ["B", "C", "D", "E"]
poids = ["5.0", "3.5", "8.0", "2.5"]

i = 1
total_poids = 0

# Parcours simultané des trois listes
for d, a, p in zip(depart, arrivee, poids):

    # Conversion du poids en nombre décimal
    p = float(p)

    # Calcul du poids total
    total_poids = total_poids + p

    # Affichage de l'arête
    print(f"Arête n°{i} : {d} -> {a}, poids = {p:g}")

    i = i + 1

# Affichage du bilan
print("\n--- Bilan du graphe ---")
print(f"Nombre total d'arêtes : {i - 1}")
print(f"Poids total : {total_poids:g}")
