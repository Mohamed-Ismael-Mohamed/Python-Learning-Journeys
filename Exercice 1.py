# Exercice 1 : Variables et types

nom_graphe = "   Mon premier graphe    "
nombre_sommets = "5"
nombre_aretes = "7"
oriente = True
pondere = False
poids = None

# Nettoyage et conversion
nom_graphe = nom_graphe.strip()
nombre_sommets = int(nombre_sommets)
nombre_aretes = int(nombre_aretes)

# Affichage des informations
print(f"Nom : {nom_graphe}")
print(f"Nombre de sommets : {nombre_sommets}")
print(f"Nombre d'arêtes : {nombre_aretes}")
print(f"Orienté : {oriente}")
print(f"Pondéré : {pondere}")

# Affichage des types
print("\n--- Types des variables ---")
print(type(nom_graphe))
print(type(nombre_sommets))
print(type(nombre_aretes))
print(type(oriente))
print(type(pondere))
print(type(poids))

# Vérification de la présence d'un poids
if poids is None:
    print("Le graphe n'a pas de poids.")
else:
    print(f"Poids du graphe : {poids}")
