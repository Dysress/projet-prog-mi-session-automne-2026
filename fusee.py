#=========================================================================================================================
#------------ Importations -----------------------------------------------------------------------------------------------
#=========================================================================================================================

from scipy.constants import g as gravite_terre
from outils_graphiques import afficher_graphique 

#=========================================================================================================================
#------------ Variables Globales -----------------------------------------------------------------------------------------
#=========================================================================================================================

PRENOM = "Maika"
NOM = "Grenon"
MATRICULE = "2568163"
rayon_terre = 6371000

#=========================================================================================================================
#------------ Fonctions créer pour project -------------------------------------------------------------------------------
#=========================================================================================================================

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


#etats = temps (t) altitude(h) vitesse(v)
def simuler_lancement(fusee, duree, dt) :
    etat_initiale = (0, 0, 0)
    trajectoire = []
    nombre_etat = int(duree/dt)+1
    for i in range(0,nombre_etat):
        if i == 0 :
            trajectoire.append(etat_initiale)
        else :
            etat_suivant = calculer_etat_suivant(fusee, etat_initiale, dt)
            etat = (etat_suivant[0], etat_suivant[1], etat_suivant[2])
            trajectoire.append(etat)
            etat_initiale = etat
    return trajectoire


def trouver_apogee(trajectoire : tuple):
    altitude_maximum = 0
    temps_altitude_maximum = 0
    for i in trajectoire:  # retourne trajectoire[i]
      if i[1] > altitude_maximum:
          altitude_maximum = i[1]
          temps_altitude_maximum = i[0]
    return temps_altitude_maximum, altitude_maximum


def vitesse_maximum(trajectoire):
    vitesse_maximum = 0
    for i in trajectoire :
        if i[2] > vitesse_maximum:
            vitesse_maximum = i[2]
    return vitesse_maximum


def temps_combustion(trajectoire):
    temps_combustion = 0
    for i in trajectoire :
        if i[0] > 0 :
            temps_combustion = i[0]
    return temps_combustion


def altitude_finale(trajectoire):
    altitude_finale = 0
    temps_final = temps_combustion(trajectoire)
    for i in trajectoire :
        if i[0] == temps_final :
            altitude_finale = i[1]
    return altitude_finale


def retrouver_fusee(nom_fusee, liste_fusees : list):
    for i in liste_fusees:
        if i[0] == nom_fusee:
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

#=========================================================================================================================
#------------ Fonction Main() --------------------------------------------------------------------------------------------
#=========================================================================================================================

def main():

    print('\n~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°~')
    print('|                                                                            |')
    print('|             BIENVENUE AU SIMULATEUR DE LANCEMENT DE FUSÉE !!               |')
    print('|                                                                            |')
    print('~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°°~~~°°~\n')
    
    boucle_principale_simulation = True
    entrer_invalide_menu = True
    while boucle_principale_simulation == True :
    
        print(" \n \n VEUILLER CHOISIR L'UNE DES OPTIONS SUIVANTE : \n")
        print("     1. Créer une fusée. ") # et la conserver dans une liste
        print("     2. Lancer la simulation d'une fusée. ") #durée et dt doivent être demandés à l'utilisateur
        print("     3. Afficher les résultats d'un lancement : apogée, vitesse maximale, temps de combustion et altitude finale.")#apoge (temps et altitude)
        print("     4. Afficher le graphique de l'altitude en fonction du temps pour un lancement. ")
        print("     5. Quitter le programme. \n")
    
        choix_de_utilisateur = input(" Veuillez entrer votre choix (1-5) : ")
        #creer_fusee(nom :str ,masse_seche :float,masse_carburant : float,pousse :float ,debit :float)
    
    #=========================================================================================================================
    #------------ option 1 : creer une fusee ---------------------------------------------------------------------------------
    #=========================================================================================================================
        if choix_de_utilisateur == "1": 
            print("\n","°"*100)
            print("\n Vous avez choisi l'option 1, créer une fusée. \n")
            fusee_creer = []
    
            nom_fusee = input(" Veuillez entrer le nom de votre fusée : ")
            while nom_fusee.isalpha() == False :
                print(" Erreur d'entrer, veuillez reessayer ")
                nom_fusee = input(" Veuillez entrer le nom de votre fusee : ")
    
            masse_seche = input(" Veuillez entrer la masse a vide de votre fusée (kg) : ")
            while masse_seche.isdigit() == False : 
                print(" Erreur d'entrer, veuillez reessayer ") 
                masse_seche = input(" Veuillez entrer la masse a vide de votre fusée (kg) : ")
            masse_seche = float(masse_seche)    
    
            masse_carburant = input(" Veuillez entrer la masse du carburant initiale de votre fusée (kg) : ")
            while masse_carburant.isdigit() == False :
                print(" Erreur d'entrer, veuillez reessayer ") 
                masse_carburant = input(" Veuillez entrer la masse du carburant initiale de votre fusée (kg) : ")   
            masse_carburant = float(masse_carburant)
    
            pousse = input(" Veuillez entrer la pousse du moteur de votre fusee (N) : ")
            while pousse.isdigit() == False :
                print(" Erreur d'entrer, veuillez reessayer ")
                pousse = input(" Veuillez entrer la pousse du moteur de votre fusee (N) : ")
            pousse = float(pousse)
    
            debit = input(" Veuillez entrer le debit d'epuisement du carburant (kg/s) :")
            while debit.isdigit() == False:
                print(" Erreur d'entrer, veuillez reessayer ")     
                debit = input(" Veuillez entrer le debit d'epuisement du carburant (kg/s) :") 
            debit = float(debit)
    
            fusee = creer_fusee(nom_fusee, masse_seche, masse_carburant, pousse, debit)
            fusee_creer.append(fusee)
            print(f"\n La fusée {nom_fusee} a été créée avec succès. \n")
            print("\n","°"*100)
    #=========================================================================================================================
    #------------ option 2 : lancer la simulation d'une fusee -----------------------------------------------------------------------------------------------
    #=========================================================================================================================
        elif choix_de_utilisateur == '2':
            print("\n","°"*100)
            print(" \n Vouz avez choisi l'option 2, lancer la simulation d'une fusee.\n") 
    
            duree = input(" Veuillez entrer la duree de la simulation (s): ")
            while duree.isdigit() == False :
                print(" Erreur d'entrer, veuillez reessayer ")   
                duree = input(" Veuillez entrer la duree de la simulation (s): ")
            duree = float(duree)   
    
            pas_de_temps = input(" Veuillez entrer le pas de temps pour la simulation (s): ")
            while pas_de_temps.isdigit() == False :
                print(" Erreur d'entrer, veuillez reessayer ") 
                pas_de_temps = float(input(" Veuillez entrer le pas de temps pour la simulation (s): "))
            pas_de_temps = float(pas_de_temps)
    
            fusee = input(" Veuillez entrer le nom de la fusée que vous voulez lancer : \n ")
            while fusee.isalpha() == False :
                print(" Erreur d'entrer, veuillez reessayer ") 
                fusee = input(" Veuillez entrer le nom de la fusée que vous voulez lancer : \n ")
    
            fusee_trouver = retrouver_fusee(fusee, fusee_creer)
            while fusee_trouver == None :
                print(" La fusee demander n'a pas ete trouver, veuillez reessayer. ")
                fusee = input(" Veuillez entrer le nom de la fusée que vous voulez lancer : \n ")
                fusee_trouver = retrouver_fusee(fusee, fusee_creer)
    
            simulation_fusee = simuler_lancement(fusee_trouver, duree, pas_de_temps)
            print(" \n La simulation de la fusée a été un succès.\n ")
            print("\n","°"*100)
    #=========================================================================================================================
    #------------ option 3 : afficher les résultats d'un lancement -----------------------------------------------------------------------------------------------
    #=========================================================================================================================
        elif choix_de_utilisateur == '3': #apogée, vitesse maximale, temps de combustion et altitude finale
            print("\n","°"*100)
            print(" \n Vous avez choisi l'option 3, afficher les résultats d'un lancement. \n")
            apogee = trouver_apogee(simulation_fusee)
            vitesse_max = vitesse_maximum(simulation_fusee)
            temps_comb = temps_combustion(simulation_fusee)
            altitude_fin = altitude_finale(simulation_fusee)
            print(f"\n L'apogée de la fusée est de {apogee[1]} m, atteinte à {apogee[0]} s. ")
            print(f"\n La vitesse maximale de la fusée est de {vitesse_max} m/s. ")
            print(f"\n Le temps de combustion de la fusée est de {temps_comb} s. ")
            print(f" \n L'altitude finale de la fusée est de {altitude_fin} m. ")
            print("\n","°"*100)
    #=========================================================================================================================
    #------------ option 4 : afficher le graphique de l'altitude en fonction du temps -----------------------------------------------------------------------------------------------
    #========================================================================================================================= 
        elif choix_de_utilisateur == '4':
            print("\n","°"*100)
            print(" \n Vous avez choisi l'option 4, afficher le graphique de l'altitude en fonction du temps pour un lancement. \n")
            afficher_graphique = graphique(simulation_fusee)
            print(afficher_graphique)
            print("\n", "°"*100)
    #=========================================================================================================================
    #------------ option 5 : quitter le programme -----------------------------------------------------------------------------------------------
    #=========================================================================================================================
        elif choix_de_utilisateur == '5':
            print("\n","°"*100  )
            print(" \n Vous avez choisi l'option 5, quitter le programme. \n")
            boucle_principale_simulation = False
    #=========================================================================================================================
    #------------ Mauvais entrer dans menu -----------------------------------------------------------------------------------------------
    #=========================================================================================================================    
        else:
            print("\n","°"*100)
            print(" \n Entrée invalide, veuillez entrer un chiffre entre 1 et 5. \n")
            entrer_invalide_menu = False 
            print("\n","°"*100)
    #=========================================================================================================================
    #------------ recommence la boucle  -----------------------------------------------------------------------------------------------
    #=========================================================================================================================
        if entrer_invalide_menu == True :
            continuer = input("\n Voulez vous retouner au menu ou arrêter la simulation? (Continuer(c) / arreter (a)) : \n ")
            if continuer.upper() == 'C':
                boucle_principale_simulation = True
            elif continuer.upper() == 'A':
                print(" Merci d'avoir utilisé le simulateur de lancement de fusée. Au revoir !")
                boucle_principale_simulation = False
            else:
                print(" Entrée invalide, le programme va continuer automatiquement.")
    
    

if __name__ == "__main__" : 
    main()
    