# Exercice 2 : Manipulation des chaînes de caractères

nom = "     sommet a     "
type_graphe = "graphe non oriente"
description = "A-B-C-D-E"

# Nettoyage du nom
nom = nom.strip()

# Mise en majuscules
nom = nom.upper()

# Modification du type de graphe
type_graphe = type_graphe.replace("non oriente", "oriente")

# Modification de la description
description = description.replace("-", ", ")

# Affichage
print(f"Le graphe s'appelle {nom}.")
print(f"C'est un {type_graphe}.")
print(f"Voici sa description : {description}")
