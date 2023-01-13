#ici on déclare la classe Chapitre
class Chapitre:
    def __init__(self,gold,hp,txt,links):
        self.__orGagne = gold
        self.__pvPerdus = hp
        self.__texte = txt
        self.__listeLiens = links
    def getTexte(self):
        return self.__texte
    def getPvPerdus(self):
        return self.__pvPerdus
    def getOrGagne(self):
        return self.__orGagne
    def getListeLiens(self):
        return self.__listeLiens

#ici on déclare la classe Personnage
class Personnage:
    def __init__(self,name,hp,gold):
        self.__or = gold
        self.__pv = hp
        self.__nom = name
    def getNom(self):
        return self.__nom
    def getPv(self):
        return self.__pv
    def getOr(self):
        return self.__or
    def perdPv(self,nbr_pv_perdus):
        self.__pv -= nbr_pv_perdus
        return self.__pv
    def gagneOr(self,nbr_or_gagne):
        self.__or += nbr_or_gagne
        return self.__or

#on commence le programme principal
chapitre0 = Chapitre(2,10,"Chapitre 0 !!!",[1])

livre = {}
livre[0] = chapitre0
livre[1] = Chapitre(10,42,"1er chapitre !",[])
livre[5] = Chapitre(25,55,"5e chapitre (caché, hahaha) !",[])

xena = Personnage("Xéna",2000,10)
chapitreCourant = 0

while(True): #ici il faudra changer la condition de victoire/défaite
    print(livre[chapitreCourant].getTexte())
    print("Votre personnage, "+xena.getNom()+", possède "+str(xena.getPv())+" points de vie et "+str(xena.getOr())+" pièces d'or.")
    print(str(livre[chapitreCourant].getListeLiens()))

    #ici il faudra bien penser à modifier les valeurs d'or et de points de vie du personnage

    choixJoueur = int(input("Veuillez choisir un numéro de chapitre !"))
    while(choixJoueur not in livre[chapitreCourant].getListeLiens()):
        choixJoueur = int(input("Vous ne pouvez pas aller directement à ce chapitre. Veuillez choisir un numéro de chapitre valable !"))
    chapitreCourant=int(choixJoueur)