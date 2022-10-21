import random

monstreLvl = 1
monstresVaincus =0
xpJoueur = 0
lvJoueur =1
degats =0
touche = ' '

gobelin = ["Gobelin",10,10]
geant = ["Geant",20,22]
louis = ["Louis the prog overlord",12,1]
allMonster = [gobelin,geant,louis]

selectedMonster = allMonster[random.randint(0,len(allMonster)-1)]

while(True):
    
    monstrePV = selectedMonster[1]*monstreLvl
    monstreName = selectedMonster[0]
    monstreXP = selectedMonster[2]*monstreLvl

    print("Un ",monstreName," Sauvage apparait il a ", monstrePV, "Pvs")
    while(monstrePV>0):
        
        print ("que voulez vous faire ?")        
        touche = input("A - Attaquer, B - Se Defendre, C - Fuir")
        
        #Attaquer 
        if(touche == 'a'):
            degats = random.randint(1,3*lvJoueur)
            monstrePV = monstrePV - degats
            print("Le gobelin a ", monstrePV, " pvs")
            input()
        else:
            print("Merci d'appuyer sur une touche correcte")
    print("Vous avez vaincu le gobelin")
    
    #Gestion xp Gobelin
    monstresVaincus += 1
    if(monstresVaincus>=7):
        monstresVaincus = 0
        monstreLvl+=1
    
    #Gestion xp Joueur
    xpJoueur += monstreXP
    if(xpJoueur>lvJoueur*5):
        lvJoueur+=1
        xpJoueur=0
        print ("Felicitation ma geulle tu es niveau ", lvJoueur)
    
    
    input()