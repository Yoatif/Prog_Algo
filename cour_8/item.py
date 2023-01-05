class Item:
    def __init__(self,name,number, power):
        self.__nom = name
        self.__quantite = number
        self.__puissance = power
    def affiche(self):
        if(self.__quantite>0):
            print(str(self.__quantite) + " " + self.__nom)
    def utilise(self):
        if(self.__puissance==0):
            print("Aucun effet")
        else:
            self.__quantite -=1
            if(self.__puissance>0):
                print("On utilise 1 "+self.__nom+" pour soigner "+str(self.__puissance)+" points de vie !")
            else:
                print("On utilise 1 "+self.__nom+" pour faire "+str(self.__puissance)+" dégâts !")

    

inventaire = [Item("potion de soin",3, 10), Item("épée",1,0), Item("fléchette",2,-20)]

inventaire[0].affiche()
inventaire[1].affiche()
inventaire[2].affiche()

inventaire[0].utilise()
inventaire[1].utilise()
inventaire[2].utilise()

inventaire[0].affiche()
inventaire[1].affiche()
inventaire[2].affiche()