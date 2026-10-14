# Ajoutez vos includes ici

from modulefinder import test


PRENOM = "Maika"
NOM = "Grenon"
MATRICULE = "2568163"

# Ajoutez votre code ici

#nom de la fusee(str), masse seche(kg, int ou float), masse carburant initial(kg,int ou float)
#poussee du moteur(N, or kg * m/s, int ou float), debit de carburant(kg/s, int ou float)  
def creer_fusee(nom :str ,masse_seche :float,masse_carburant : float,pousse :float ,debit :float):
    fusee = (nom,masse_seche,masse_carburant,pousse,debit)
    return fusee


#masse total fusse = masse seche + (carburant restant, doit etre +) au temps t
def calculer_masse(creer_fusee,t):
    carburant_restant = creer_fusee[2] - (creer_fusee[4] * t)
    if carburant_restant <= 0 :
        masse_total_fusee = creer_fusee[1] 
    else :
        masse_total_fusee = creer_fusee[1] + carburant_restant

    return masse_total_fusee

#kg * m/s
#poids * vitesse = force de pousser
#pousser initiale = 
#doit retravailler
def calculer_poussee(creer_fusee,t):
    pousse_initiale = creer_fusee[3]
    carburant_restant = creer_fusee[2] - (creer_fusee[4]* t)
    if carburant_restant <= 0 :
        pousse_temps_t = 0
        return pousse_temps_t
    else:
        vitesse = pousse_initiale / calculer_masse(creer_fusee,t)
        poids = calculer_masse(creer_fusee,t) 
        pousee_progressive = poids * vitesse
        return pousee_progressive


#gravite = g * (R/(R+altitude))**2
def calculer_gravite(altitude):
    gravite_terre = 9.81
    rayon_terre = 6371000
    gravite = gravite_terre * ((rayon_terre/(rayon_terre+altitude))**2)
    return gravite



#(pousse au temps t -(masse totale  * gravite)) / masse total
def calculer_acceleration(creer_fusee,t,altitude):
    pousse = calculer_poussee(creer_fusee,t)
    masse_total = calculer_masse(creer_fusee,t)
    gravite = calculer_gravite(altitude) 
    calcule = ( pousse - (masse_total * gravite )) / masse_total
    return calcule

#etats =temps (t) altitude(h) vitesse(v)

def calculer_etat_suivant(creer_fusee, etat : tuple , dt):
    temps_t = etat[0]
    altitude_h = etat[1]    
    vitesse_v = etat[2]
    temps_t = (temps_t + dt)
    vitesse_v = (vitesse_v + (calculer_acceleration(creer_fusee, etat[0], altitude_h) * dt))
    altitude_h =( altitude_h + vitesse_v * dt)
    etat_test = (temps_t, vitesse_v,altitude_h)
    if altitude_h <= 0 :
        etat_test = (temps_t, 0, 0)
    return etat_test

def simuler_lancement(creer_fusee, duree, dt) :
    etat_initiale = (0, 0, 0)
    trajectoire = []
    nombre_etat = int(duree/dt)+1
    for i in range(0,nombre_etat):
        if i == 0 :
            trajectoire.append(etat_initiale)
        else :
            test = calculer_etat_suivant(creer_fusee, etat_initiale, dt)
            etat = (test[0], test[1], test[2])
            trajectoire.append(etat)
            etat_initiale = etat
            

    return trajectoire


#etat_test = (temps_t, vitesse_v,altitude_h)
# def trouver_apogee(trajectoire : tuple):
#     altitude_maximum = 0
#     temps_maximum = 0
#     for (temps_t,vitesse_v,altitude_h) in trajectoire:
#         if altitude_h > altitude_maximum :
#             altitude_maximum = altitude_h
#             temps_maximum = temps_t
#     return (temps_maximum, altitude_maximum)

def trouver_apogee(trajectoire : tuple):
    altitude_max = 0
    for i in trajectoire:
      if i[2] > altitude_max:
          altitude_max = i[2]
          temps_max = i[0]
    return temps_max, altitude_max

def retrouver_fusee():
    pass
        
        

def main():
    fusee = creer_fusee('Alpha', 500, 1500, 30000, 50)
    print(trouver_apogee(simuler_lancement(fusee, 200, 0.5)))

if __name__ == "__main__" : 
    main()