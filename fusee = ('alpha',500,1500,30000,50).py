fusee = ('alpha',500,1500,30000,50)
liste_fusees = [('alha',500,1500,30000,50),('alph',500,1500,30000,50),('ala',500,1500,30000,50)]
noms= 'alpha'

def retrouver(nom, liste):
    for i in liste :
        if nom == i[0]:
            return i 
    return None 

print(retrouver(noms,liste_fusees))