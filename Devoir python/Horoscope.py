#ABAL KHASSIM TRAORE

import datetime


#fonction qui verifie si l'année est bissextile
def is_bissextile(annee):
    return annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)

    
#fonction qui donne signe astrologique en fonction du jour et du mois
#Utilise la liste des correspondances précédente pour déterminer le signe astrologique associé àla date de naissance

def signe_astrologique(jour, mois):
    
    if (mois == 3 and 21 <= jour <= 31) or (mois == 4 and 1 <= jour <= 19):
        return "Bélier"
    elif (mois == 4 and 20 <= jour <= 30) or (mois == 5 and 1 <= jour <= 20):
        return "Taureau"
    elif (mois == 5 and 21 <= jour <= 31) or (mois == 6 and 1 <= jour <= 20):
        return "Gémeaux"
    elif (mois == 6 and 21 <= jour <= 30) or (mois == 7 and 1 <= jour <= 22):
        return "Cancer"
    elif (mois == 7 and 23 <= jour <= 31) or (mois == 8 and 1 <= jour <= 22):
        return "Lion"
    elif (mois == 8 and 23 <= jour <= 31) or (mois == 9 and 1 <= jour <= 22):
        return "Vierge"
    elif (mois == 9 and 23 <= jour <= 30) or (mois == 10 and 1 <= jour <= 22):
        return "Balance"
    elif (mois == 10 and 23 <= jour <= 31) or (mois == 11 and 1 <= jour <= 21):
        return "Scorpion"
    elif (mois == 11 and 22 <= jour <= 30) or (mois == 12 and 1 <= jour <= 21):
        return "Sagittaire"
    elif (mois == 12 and 22 <= jour <= 31) or (mois == 1 and 1 <= jour <= 19):
        return "Capricorne"
    elif (mois == 1 and 20 <= jour <= 31) or (mois == 2 and 1 <= jour <= 18):
        return "Verseau"
    else:
        return "Poisson"

#fonction qui fait le controle de saisie sur les jours les moi et les annees
#limite_inf et limite_sup variables qui vont servir a s'assurer que les jours les mois et les années 
# ne sorte pas de leurs intervalle
def saisie_entier(val, limite_inf, limite_sup):
    valide = False
    while not valide:
        valeur = input(val)
        if valeur.isdigit() and limite_inf <= int(valeur) <= limite_sup:
            valeur = int(valeur)
            valide = True
        else:
            print(f"Erreur, veuillez entrer une valeur valide entre {limite_inf} et {limite_sup}.")
    return valeur


continuer = True
while continuer:
    print("Veuillez saisir votre date de naissance")

    # Saisie du jour
    jour = saisie_entier("Jour : ", 1, 31)

    # Saisie du mois
    mois = saisie_entier("Mois : ", 1, 12)

    #recupere l'année courante 
    #dans notre cas l'année maximun est l'année courante donc 2023
    annee_courante = int(datetime.datetime.now().year)

    
    # Saisie de l'année
    annee = saisie_entier("Année : ", 1801, annee_courante)

    # Vérification de la date de naissance
    # Vérification de la date de naissance
    if mois == 2 and (jour > 29 or (jour == 29 and not is_bissextile(annee))):
        print("Erreur, le mois de février ne dépasse pas 29 jours pour cette année.")
        annee = saisie_entier("Année : ", 1801, annee_courante)
    elif mois in [4, 6, 9, 11] and jour > 30:
        print("Erreur, ce mois ne dépasse pas 30 jours.")
        annee = saisie_entier("Année : ", 1801, annee_courante)
    elif jour > 31:
        print("Erreur, ce jour n'existe pas dans le calendrier.")
        annee = saisie_entier("Année : ", 1801, annee_courante)
    else:
        # Afficher le signe astrologique associé.
        resultat = signe_astrologique(jour, mois)
        print("Votre signe astrologique est :", resultat)

    
    
    # Demande a l'utilisateur s'il veut continuer
    choix = input("Voulez-vous continuer ? (O:oui/N:non) : ")
    while choix.lower() not in ["oui", "o", "non", "n"]:
        choix = input("Veuillez saisir une option valide (O:oui/N:non) : ")

    if choix.lower() in ["non", "n"]:
        continuer = False

print("Fin du programme")
print("Au revoir !")
