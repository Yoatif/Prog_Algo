class Escargot:
    
    def __init__(self,name,number,distance,pari):
        
        
        self.__name = name 
        self.__motivation = 100
        self.__number = number
        self.__distance = distance
        self.__pari = pari

    def getName(self):
        name = self.__name
        return name

    def getLook(self):
        return "@" + str(self.__number)

    def getDistance(self):
        return self.__distance

    def getMotivation(self):
        return self.__motivation
    
    def setAdvance(self):
        self.__distance += 1
        self.__motivation -= 1
        if self.__motivation < 1:
            self.__motivation = 0
    def motive(self):
        self.__motivation +=1
    def pari(self):
        if self.__pari >= 100:
            self.__motivation = 200
            return self.__motivation
    def augmentePari(self):
        self.__pari += 10
        return self.__pari

alexandre = Escargot("Ashiyro",7,0,100)
marie = Escargot("TrucquibaveH24",2,0,20)
lisa = Escargot("Sail",6662266622666,0,0)
yoann = Escargot("Kirryu",8,0,200)
monDico = {1:alexandre,2:marie,3:lisa,4:yoann}

def affichage():
    print(' ')
    print('----------')

    for variable in monDico:
        print (monDico[variable].getDistance())

while(alexandre.getDistance()!=10 or marie.getDistance()!=10 or lisa.getDistance()!=10 or yoann.getDistance()!=10):
    affichage()
    choix = int(input("joueur d'"+ alexandre.getName() +" que veux tu faire ? 1) avancer 2) motiver 3) augmenter le pari"))
    if choix == 1:
        alexandre.setAdvance()
    elif choix ==2:
        alexandre.setAdvance()
    else:
        alexandre.augmentePari()
    print(alexandre.getLook())
    print(marie.getLook())
    print(lisa.getLook())
    print(yoann.getLook())
    choix = int(input("joueur de "+ marie.getName() +" que veux tu faire ? 1) avancer 2) motiver 3) augmenter le pari"))
    if choix == 1:
        marie.setAdvance()
    elif choix ==2:
        marie.setAdvance()
    else:
        marie.augmentePari()
    choix = int(input("joueur de"+ lisa.getName() +" que veux tu faire ? 1) avancer 2) motiver 3) augmenter le pari"))
    if choix == 1:
        lisa.setAdvance()
    elif choix ==2:
        lisa.setAdvance()
    else:
        lisa.augmentePari()
        choix = int(input("joueur de "+ yoann.getName() +" que veux tu faire ? 1) avancer 2) motiver 3) augmenter le pari"))
    if choix == 1:
        yoann.setAdvance()
    elif choix ==2:
        yoann.setAdvance()
    else:
        yoann.augmentePari()

if (alexandre.getDistance()==10):
    print("félicitation! Le vainqueur est" + alexandre.getName)
elif (alexandre.getDistance()==10):
    print("félicitation! Le vainqueur est" + marie.getName)
elif (alexandre.getDistance()==10):
    print("félicitation! Le vainqueur est" + lisa.getName)
else:
    print("félicitation! Le vainqueur est" + yoann.getName)
    

