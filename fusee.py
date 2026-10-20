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
    temps_t = (temps_t + dt)
    vitesse_v = (vitesse_v + (calculer_acceleration(fusee, etat[0], altitude_h) * dt))
    altitude_h =( altitude_h + vitesse_v * dt)
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
    for i in trajectoire:
      if i[2] > altitude_maximum:
          altitude_maximum = i[2]
          temps_maximum = i[0]
    return temps_maximum, altitude_maximum


#a revoir et tester 
def retrouver_fusee(nom_fusee, liste_fusees : list):
    for i in range(len(liste_fusees)):
        for j in range(len(liste_fusees[i])):
            if liste_fusees[j] == nom_fusee :
                fusee_temporaire = liste_fusees[j]
                fusee = creer_fusee(fusee_temporaire[0],fusee_temporaire[1],fusee_temporaire[2],fusee_temporaire[3],fusee_temporaire[4])
    return fusee

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
    return afficher_graphique(liste_x, liste_y, "Lancement de la fusée", "Altitude (m)", "Temps (s)")

    #return afficher_graphique([i[0] for i in trajectoire],[i[1] for i in trajectoire], "Lancement de la fusée", "Temps (s)", "Altitude (m)")
    



def main():
    fusee = creer_fusee('Alpha', 500, 1500, 30000, 50)
    print(graphique(simuler_lancement(fusee, 100, 1)))
    

if __name__ == "__main__" : 
    main()