class Chapitre:
    def __init__(self,gold,hp,txt,links):
        self.__orGagne = gold
        self.__pvPerdu = hp
        self.__ListeLiens = links
        self.__text = txt

    #renvoie la valeur d'or gagner par le joueur
    def GetorGagne(self,):
        return self.__orGagne

    def getpvPerdus(self,):
        if (self.__pvPerdu > 150) :
            self.__pvPerdu = 150
        else : 
            self.__pvPerdu = self.__pvPerdu + 1
        return self.__pvPerdu

    def getListeLiens(self):
        listeLiens = {0 : chapitre0, 1 : chapitre1, 2 : chapitre2, 3 : chapitre3, 4 : chapitre4, 5 : chapitre5, 6 : chapitre6, 7 : chapitre7,8: chapitre8,9: chapitre9, 10: chapitre10}
        for i in range(self.__ListeLiens):
            if(i == self.__ListeLiens):
                self.__ListeLiens = listeLiens[i]
        return self.__ListeLiens

    def GetOrGagne(self, change):
        self.__modifGold = self.__modifGold + change
        return self.__modifGold
    
    def getText(self):
        print(self.__text)

chapitre0 = Chapitre(0,0,"Vous entrez a l'académie militaire de rorcia, après une séance d'orentation, vous décidé de devenir : 1) guerrier 2 ) mage noir 3) mage blanc 4)archer",1,2,3,4)
chapitre1 = Chapitre(5,0,"vous choisisez la voie du guerrier, vous recevez une épée en fer et un cadeau de 5 pièce d'or.",5)
chapitre2 = Chapitre(5,0,"vous choisisez la voie du mage noir, vous recevez un baton échardé et un cadeau de 5 pièce d'or.",6)
chapitre3 = Chapitre(5,0,"vous choisisez la voie du mage blanc, vous recevez un sceptre banal et un cadeau de 5 pièce d'or.",7)
chapitre4 = Chapitre(5,0,"vous choisisez la voie de l'archer, vous recevez un arc tordu et un cadeau de 5 pièce d'or.",8)
chapitre5 = Chapitre(10,5,"vous finissez votre entrainement de guerrier avec une belle entaille dans le mollet mais vous remporter 10 pièce d'or.",9)
chapitre6 = Chapitre(10,5,"vous finissez votre entrainement de mage noir a moitiè bruler par un sort raté, mais vous remporter 10 pièce d'or.",9)
chapitre7 = Chapitre(0,10,"en allant a votre entrainement de mage blanc, vous vous prenez les pieds dans votre toge et tombez dans les escaliers.",10)
chapitre8 = Chapitre(0,10,"a la fin de votre entrainement d'archer, vous ressemblez plus a un hérison, qu'a un archer.",10)
chapitre9 = Chapitre(-15,0,"vous sortez de l'infirmerie, les soins vous ont couté 15 pièces d'or et décidé de changer de classe.",0)
chapitre10 = Chapitre(-15,0,"votre dieu vous réincarne, mais récupère d'abord votre or.",0)

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
        self.hp -= Chapitre.__pvPerdu
    def orGagne(self):
        self.gold = Chapitre.__orGagne

jean = Personnage("jean", 15)


print(chapitre0)
while(chapitre0):
    choix = int(input())
    if (choix == 1):
        print(chapitre1)
        print(jean.getHp)
        print(jean.getOr)
        input()
        print(chapitre5)
        print(jean.getHp)
        print(jean.getOr)
        input()
        print(chapitre9)
        print(jean.getHp)
        print(jean.getOr)
        input()
        print(chapitre0)
    elif (choix == 2):
        print(chapitre2)
        print(jean.getHp)
        print(jean.getOr)
        input()
        print(chapitre6)
        print(jean.getHp)
        print(jean.getOr)
        input()
        print(chapitre9)
        print(jean.getHp)
        print(jean.getOr)
        input()
        print(chapitre0)
    elif (choix == 3):
        print(chapitre3)
        print(jean.getHp)
        print(jean.getOr)
        input()
        print(chapitre7)
        print(jean.getHp)
        print(jean.getOr)
        input()
        print(chapitre10)
        print(jean.getHp)
        print(jean.getOr)
        input()
        print(chapitre0)
    elif (choix == 4):
        print(chapitre4)
        print(jean.getHp)
        print(jean.getOr)
        input()
        print(chapitre8)
        print(jean.getHp)
        print(jean.getOr)
        input()
        print(chapitre10)
        print(jean.getHp)
        print(jean.getOr)
        input()
        print(chapitre0)









