# Ajoutez vos includes ici
from scipy.constants import g as gravity
from outils_graphiques import afficher_graphique 

PRENOM = "Maika"
NOM = "Grenon"
MATRICULE = "2568163"
rayon_terre = 6371000

# Ajoutez votre code ici

#nom de la fusee(str), masse seche(kg, int ou float), masse carburant initial(kg,int ou float)
#poussee du moteur(N, or kg * m/s, int ou float), debit de carburant(kg/s, int ou float)  
def creer_fusee(nom :str ,masse_seche :float,masse_carburant : float,pousse :float ,debit :float):
    fusee = (nom,masse_seche,masse_carburant,pousse,debit)
    return fusee


#masse total fusse = masse seche + (carburant restant, doit etre +) au temps t
def calculer_masse(fusee,t):
    carburant_restant = fusee[2] - (fusee[4] * t)
    if carburant_restant <= 0 :
        masse_total_fusee = fusee[1] 
    else :
        masse_total_fusee = fusee[1] + carburant_restant

    return masse_total_fusee

#kg * m/s
#poids * vitesse = force de pousser
#doit retravailler
def calculer_poussee(fusee,t):
    pousse_initiale = fusee[3]
    carburant_restant = fusee[2] - (fusee[4]* t)
    if carburant_restant <= 0 :
        pousse_temps_t = 0
        return pousse_temps_t
    else:
        vitesse = pousse_initiale / calculer_masse(fusee,t)
        poids = calculer_masse(fusee,t) 
        pousee_progressive = poids * vitesse
        return pousee_progressive


#gravite = g * (R/(R+altitude))**2
def calculer_gravite(altitude):
    gravite_terre = 9.81
    gravite = gravite_terre * ((rayon_terre/(rayon_terre+altitude))**2)
    return gravite



#(pousse au temps t -(masse totale  * gravite)) / masse total
def calculer_acceleration(fusee,t,altitude):
    pousse = calculer_poussee(fusee,t)
    masse_total = calculer_masse(fusee,t)
    gravite = calculer_gravite(altitude) 
    calcule = ( pousse - (masse_total * gravite )) / masse_total
    return calcule

#etats =temps (t) altitude(h) vitesse(v)

def calculer_etat_suivant(fusee, etat : tuple , dt):
    temps_t = etat[0]
    altitude_h = etat[1]    
    vitesse_v = etat[2]
    temps_t +=  dt
    vitesse_v += calculer_acceleration(fusee, etat[0], altitude_h) * dt
    altitude_h += vitesse_v * dt
    etat_test = (temps_t, altitude_h, vitesse_v)
    if altitude_h <= 0 :
        etat_test = (temps_t, 0, 0)
    return etat_test

def simuler_lancement(fusee, duree, dt) :
    etat_initiale = (0, 0, 0)
    trajectoire = []
    nombre_etat = int(duree/dt)+1
    for i in range(0,nombre_etat):
        if i == 0 :
            trajectoire.append(etat_initiale)
        else :
            test = calculer_etat_suivant(fusee, etat_initiale, dt)
            etat = (test[0], test[1], test[2])
            trajectoire.append(etat)
            etat_initiale = etat
            

    return trajectoire

def trouver_apogee(trajectoire : tuple):
    altitude_maximum = 0
    for i in trajectoire:  # retourne trajectoire[i]
      if i[2] > altitude_maximum:
          altitude_maximum = i[2]
          temps_maximum = i[0]
    return temps_maximum, altitude_maximum

 
def retrouver_fusee(nom_fusee, liste_fusees : list):
    for i in liste_fusees:
        if i == nom_fusee:
            return i 
    return None


#afficher_graphique(x : list de nombres, y : list de nombres, titre : str, label_x : str, label_y : str)
#needs hard rework
def graphique(trajectoire):
    liste_x = []
    liste_y = []
    for i in range(len(trajectoire)):
        valeur = trajectoire[i] #(0,0,0)
        for j in range(len(valeur)):
            liste_y.append(valeur[1])
            liste_x.append(valeur[0])
    return afficher_graphique(liste_x, liste_y, "Lancement de la fusée", " Temps (s) ", " Altitude (m) ")

def main():
    fusee = creer_fusee('Alpha', 500, 1500, 30000, 50)
    print(graphique(simuler_lancement(fusee, 100, 1)))
    

if __name__ == "__main__" : 
    #main()
    print('\n~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°~')
    print('|                                                                            |')
    print('|             BIENVENUE AU SIMULATEUR DE LANCEMENT DE FUSÉE !!               |')
    print('|                                                                            |')
    print('~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°~\n')

    print("VEUILLER CHOISIR L'UNE DES OPTIONS SUIVANTE : \n")
    print("     1. Créer une fusée. ") # et la conserver dans une liste
    print("     2. Lancer la simulation d'une fusée. ") #durée et dt doivent être demandés à l'utilisateur
    print("     3. Afficher les résultats d'un lancement : apogée, vitesse maxiamle, temps de combustion et altitude finale.")#apoge (temps et altitude)
    print("     4. Afficher le graphique de l'altitude en fonction du temps pour un lancement. ")
    print("     5. Quitter le programme. \n")

    choix_de_utilisateur = input(" Veuillez entrer votre choix (1-5) : ")
    #creer_fusee(nom :str ,masse_seche :float,masse_carburant : float,pousse :float ,debit :float)
    if choix_de_utilisateur == "1": 
        print("\n Vous avez choisi l'option 1, creer une fusee. \n")
        fusee_creer = []
        nom_fusee = str(input(" Veuillez entrer le nom de votre fusée : "))
        masse_seche = float(input(" Veuillez entrer la masse a vide de votre fusée (kg) : "))
        masse_carburant = float(input(" Veuillez entrer la masse du carburant initiale de votre fusée (kg) : "))
        pousse = float(input(" Veuillez entrer la pousse du moteur de votre fusee (N) : "))
        debit = float(input(" Veuillez entrer le debit d'epuisement du carburant (kg/s) :"))
        fusee = nom_fusee
        nom_fusee = creer_fusee(fusee, masse_seche, masse_carburant, pousse, debit)
        fusee_creer.append(nom_fusee)
        print(fusee_creer[0])

    elif choix_de_utilisateur == '2':
        print(" \n Vouz avez choisi l'option 2, lancer la simulation d'une fusee. ")
        duree = float(input(" Veuillez entrer la duree de la simulation : "))
        pas_de_temps = float(input(" Veuillez entrer le pas de temps pour la simulation: "))


