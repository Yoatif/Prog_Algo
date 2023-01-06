import random
import os
import json

class Chapitre :
    def __init__(self,orGagne,pvPerdu,text,):
        self.orGagne = orGagne
        self.pvPerdu = pvPerdu
        self.text = text
        self.listeLien = {1:chapitre0,2:chapitre1,3:chapitre2,4:chapitre3,5:chapitre4,6:chapitre5,7:chapitre6}
    
    def getText(self):
        print(self.text)
    
    def getPvPerdu(self,pvPerdu):
        Personnage.hp -= pvPerdu
    
    def goldGagne(self,orGagne):
        Personnage.gold += orGagne
    def ListeLien(self):
        print(self.listeLien)

chapitre0 = Chapitre("Vous entrez a l'académie militaire de rorcia, après une séance d'orentation, vous décidé de devenir : 1) guerrier 2 ) mage noir 3) mage blanc 4)archer",0,0,0 1)
chapitre1 = Chapitre("vous choisisez la voie du guerrier, vous recevez une épée en fer et un cadeau de 5 pièce d'or.",0,5,)

    

class Personnage:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
        self.gold = 0
        self.atk = random()
    def getNom(self):
        print(self.name)

    def getHp(self):
        print(self.hp)

    def getOr(self):
        print(self.gold)
    def pvPerdu(self):
        self.hp -= Chapitre.pvPerdu
    def orGagne(self):
        self.gold = Chapitre.orGagne