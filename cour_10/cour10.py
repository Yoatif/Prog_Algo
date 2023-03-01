class PocketMonster :
    def __init__(self,name,hp,force,res,element):
        self.__name = name
        self.__hp = hp
        self.__str = force
        self.__res = res 
        self.__type = element
        
    
    def attaque (self):
        degat = (self.__str-self.__res)
        self.__hp -= degat

    def getHp(self):
        return self.__hp
    
    def getName(self):
        return self.__name
        

    def compareType (self,advElement):
        if(self.__type == "feu"):
            if(advElement == "plante"):
                bonus = 2
                return bonus
            else:
                bonus = 1
                return bonus
        if(self.__type == "plante"):
            if(advElement == "eau"):
                bonus = 2
                return bonus
            else:
                bonus = 1
                return bonus
        if(self.__type == "eau"):
            if(advElement == "feu"):
                bonus = 2
                return bonus
            else:
                bonus = 1
                return bonus
class Attaque:
    def __init__(self,name,element,puissance,text):
        self.__name = name
        self.__type = element
        self.__puissance = puissance
        self.__text = text

                

mob1 = PocketMonster("gentil Alexandre", 100, 5, 2, "eau")
mob2 = PocketMonster("vilain Alexandre", 100, 5, 2,"feu")

griffe = Attaque("griffe", "neutre", 2, "utilise ses griffes sur le")
bougieSM = Attaque("bougieSM", "feu", 3, "fait couler de la cire sur le")




# ici commence le programme

print("En vous promenant sur le dos de Gabin, vous rencontrez un membre de la team Sail et lancé", mob1.getName())
print("le membre de la team Sail, dénomé Marie lance",mob2.getName())
while (mob1.__hp != 0 or mob2.__hp != 0):
    choix = int(input(print("quel action souhaitez vous faire ? 1) attaque 2) ")))