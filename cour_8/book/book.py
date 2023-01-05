class Chapitre :
    def __init__(self,orGagne,pvPerdu,text,lien):
        self.orGagne = orGagne
        self.pvPerdu = pvPerdu
        self.text = text
        self.listeLien = lien
    
    def getText(self):
        print(self.text)
    
    def getPvPerdu(self,pvPerdu):
        Personnage.hp -= pvPerdu
    
    def goldGagne(self,orGagne):
        Personnage.gold += orGagne
    def ListeLien(self):
        print(self.listeLien)

chapitre0 = Chapitre("Vous entrez a l'académie militaire de rorcia, après une séance d'orentation, vous décidé de devenir : 1) guerrier 2 ) mage noir 3) mage blanc 4)archer",0,0,{0:chapitre1,1:chapitre2,2:chapitre3,3:chapitre4})
chapitre1 = Chapitre("vous choisisez la voie du guerrier, vous recevez une épée en fer et un cadeau de 5 pièce d'or.",0,5,)

    

class Personnage:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
        self.gold = 0
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