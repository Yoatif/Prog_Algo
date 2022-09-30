class Personnage:
    def __init__(self, nom, pdv, degat):
        self.__nom = nom
        self.__pdv = pdv
        self.__degat = degat

    def getName(self):
        return self.__nom

    def getpdv(self):
        return self.__pdv

    def setDegat(self,pdv,degat):
        degat = random.randint(1,10)

   