#ABAL KHASSIM TRAORE

import re #import pour les foction Regex


# Fonction pour calculer la racine d'un nombre
def racine(n):
    while n > 9:
        somme = 0
        while n != 0:
            somme += n % 10
            n //= 10
        n = somme
    return n

# Fonction pour associer un résultat à une valeur numérique
def switche(res):
    switcher = {
        1: "individualite",
        2: "interaction",
        3: "completude",
        4: "stabilite",
        5: "instabilite",
        6: "harmonie",
        7: "empathie",
        8: "succes",
        9: "completude"
    }
    return switcher.get(res, "ouroboros")

# Fonction pour calculer l'expression d'un nom
def exp(nom):
    val = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
        'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 6, 'p': 7, 'q': 8, 'r': 9,
        's': 1, 't': 2, 'u': 3, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8
    }
    somme = sum(val[char] for char in nom if char in val and char != ' ')
    res = racine(somme)
    return switche(res)

# Fonction pour calculer l'intimité d'un nom
def intime(nom):
    val = {
        'a': 1, 'e': 5, 'i': 9, 'o': 6, 'u': 3, 'y': 7
    }
    somme = sum(val[char] for char in nom if char in val)
    res = racine(somme)
    return switche(res)

# Fonction pour calculer la réalisation d'un nom
def realisation(nom):
    val = {
        'b': 2, 'c': 3, 'd': 4, 'f': 6, 'g': 7, 'h': 8, 'j': 1, 'k': 2,
        'l': 3, 'm': 4, 'n': 5, 'p': 7, 'q': 8, 'r': 9, 's': 1, 't': 2,
        'v': 4, 'w': 5, 'x': 6, 'z': 8
    }
    somme = sum(val[char] for char in nom if char in val)
    res = racine(somme)
    return switche(res)

def saisie_entier(val, limite_inf):
    valide = False
    while not valide:
        valeur = input(val)
        if valeur.isdigit() and limite_inf <= int(valeur):
            valeur = int(valeur)
            valide = True
        else:
            print(f"Erreur, veuillez entrer une valeur valide superieur ou égale à {limite_inf}.")
    return valeur

# Demander le nombre de noms à l'utilisateur
# while True:
    # try:
    #     t = int(input("Entrez le nombre de noms a tester (doit être un entier): "))
    #     break
    # except ValueError:
    #     print("Erreur : le nombre de noms doit être un entier.")

t = saisie_entier("Entrez le nombre de noms a tester (doit être un entier entre ) : ", 1)
    


# Demander les noms à l'utilisateur et les stocker dans une liste
tab_nom = []
for i in range(t):
    nom = input("Entrez un nom "+str(i+1)+" : ")

    if not nom.isalpha() and not nom.isspace():
        print("Attention  : la chaîne saisie contient des caractères non alphabétiques et va etre formater.")
        nom = re.sub(r'[^a-zA-Z]', '', nom)  # Supprimer les caractères spéciaux en les remplaçant par une chaîne vide
        

    if len(nom) > 1000:
        print("Erreur : la chaîne saisie dépasse les 1 000 caractères.")
    else:
        nom = nom.lower()  # Convertir le nom en minuscules
        tab_nom.append(nom)
        print(tab_nom)
# Afficher les résultats pour chaque nom dans la liste
for nom in tab_nom:
    print(nom, end=' ')
    print(exp(nom), end=' ')
    print(intime(nom), end=' ')
    print(realisation(nom))
