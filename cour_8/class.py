class personnage:
    #on déclare d'abord une méthode "__init__" qui est le constructeur
    def __init__(self,name):#le 1er paramètre est obligatoire,
        #ensuite il y en a autant que vous voulez
        
        self.nom = name # 1ere donnée : le nom du personnage
        self.pv = 100# 2nde donnée : son nombre actuel de points de vie

    def perdPv(self, nombre):
        self.pv = self.pv - nombre
        print (self.nom + "perd" + str(nombre) + "points de vie")
        if (self.pv <=0):
            self.pv = 0
            print(self.nom + "meurt")

zagreus = ("zagreus") #appelle le constructeur de Personnage  
celeste = ("celeste")

zagreus.perdPv(12) #le personnage va perdre 12 pv
