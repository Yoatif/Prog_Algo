import random

gobelinPv = 10
gobelinLvl = 1
gobelinVaincus =0
xpJoueur = 0
lvJoueur =1
degats =0
touche = ' '

while(True):
    gobelinPv = random.randint(4,6)*gobelinLvl
    print("Un Goblin Sauvage apparait il a ", gobelinPv, "Pvs")
    while(gobelinPv>0):
        
        print ("que voulez vous faire ?")
        print ("A - Attaquer, B - Se Defendre, C - Fuir")
        
        touche = input()
        
        #Attaquer 
        if(touche == 'a'):
            degats = random.randint(1,3*lvJoueur)
            gobelinPv = gobelinPv - degats
            print("Le gobelin a ", gobelinPv, " pvs")
            input()
        else:
            print("Merci d'appuyer sur une touche correcte")
    print("Vous avez vaincu le gobelin")
    
    #Gestion xp Gobelin
    gobelinVaincus += 1
    if(gobelinVaincus>=7):
        gobelinVaincus = 0
        gobelinLvl+=1
    
    #Gestion xp Joueur
    xpJoueur += gobelinLvl*2
    if(xpJoueur>lvJoueur*5):
        lvJoueur+=1
        xpJoueur=0
        print ("Felicitation ma geulle tu es niveau ", lvJoueur)
    
    
    input()