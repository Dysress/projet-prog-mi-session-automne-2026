|Nom du test|Succès ou échec|Pointage obtenu|Explication|
|:-----------|:-------------:|:-------------:|:----------|
|calculer_masse(fusee, 10) retourne 1500|✅|1/1||
|calculer_masse(fusee, 40) retourne 500 (le carburant restant ne peut pas être négatif)|✅|1/1||
|calculer_poussee(fusee, 30) retourne 0 (carburant épuisé à t = 30 s)|✅|1/1||
|calculer_gravite(0) retourne 9.81|✅|1/1||
|calculer_gravite(100000) retourne environ 9.509|✅|1/1||
|calculer_acceleration(fusee, 0, 0) retourne 5.19|✅|1/1||
|calculer_acceleration(fusee, 40, 100000) retourne environ -9.509 (chute libre à 100 km)|✅|1/1||
|calculer_etat_suivant(fusee, (0, 0, 0), 1) retourne (1, 5.19, 5.19)|✅|1/1||
|calculer_etat_suivant(fusee, (40, 5000, 100), 1) retourne environ (41, 5090.205, 90.205) (chute libre à 5 km)|✅|1/1||
|simuler_lancement(fusee, 200, 0.5) : trajectoire complète (apogée ≈ 19 356 m à t = 83,5 s)|✅|1/1||

Votre pointage final est : 10/10
