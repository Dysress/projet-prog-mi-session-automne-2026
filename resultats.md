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
|calculer_etat_suivant(fusee, (40, 5000, 100), 1) retourne environ (41, 5090.205, 90.205) (chute libre à 5 km)|❌|0/1|Valeur attendue `[41, 5090.205379789122, 90.20537978912256]`, obtenue `(41, 4990.190307950684, 5090.190307950684)`|
|simuler_lancement(fusee, 200, 0.5) : trajectoire complète (apogée ≈ 19 356 m à t = 83,5 s)|❌|0/1|Valeur attendue `[[0, 0, 0], [0.5, 1.2975, 2.595], [1.0, 3.9399693533686246, 5.284938706737249], [1.5, 7.97609558625034, 8.07225246576343], [2.0, 13.455831855979222, 10.959472539457764], [2.5, 20.430446906303374, 1...`, obtenue `[(0, 0, 0), (0.5, 2.595, 1.2975), (1.0, 5.284938706737249, 3.9399693533686246), (1.5, 8.07225246576343, 7.97609558625034), (2.0, 10.959472539457764, 13.455831855979222), (2.5, 13.949230100648306, 2...`|

Votre pointage final est : 8/10
