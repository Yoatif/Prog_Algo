class Animal :
    def __init__(self,nom,poid, repas):
        self.nom = nom 
        self.poid = poid
        self.repas = repas
    def mange(self):
        print(self.nom,"mange :",self.repas) 
        self.poid += 1
        print("et fait dorénavant,",self.poid)
    def dort(self):
        print("il dort paisiblement")

class Chat(Animal) :
    def __init__(self,nom,poid,repas,race,couleur):
        Animal.__init__(self,nom,poid,repas)
        self.race = race
        self.couleur = couleur
        self.cri = "miaouw"
    
    def griffe(self):
        print(self.nom,"done un coup de griffe.")

    def ronronne(self):
        print(self.cri)

class Pangolin(Animal):
    def __init__(self, nom, poid, repas):
        Animal.__init__(self,nom, poid, repas)
        self.cri = "bonne question, c'est quoi le cri d'un pangolin ?"

margoulin =Chat("Alexandre", 80,"Space mushroom","Dev","brun")
Marie = Pangolin("Marie", 50, "des petit Suisses.")


print(margoulin.nom)
print("de la race des, ", margoulin.race)
print(margoulin.mange())
print(margoulin.ronronne())
print(margoulin.griffe())


print(Marie.cri)    