from ctypes.wintypes import HPALETTE
import random



def combat ():

    gobelinPv = 10
    gobelinLvl = 1
    gobelinVaincus =0
    xpJoueur = 0
    lvJoueur =1
    pvJoueur = 100
    degats =0
    touche = ' '
    degatGobelin = 0
    monstre = ["Lapin","Gobelin","Satan"]
    pdvMonstre = [10, 25, 9999]
    

    while (pvJoueur >=0 a):
        x = random.randint(1,3)
        
        pdvMonstre[x] = random.randint(4,6)*pdvMonstre[x]
        print("Un ",monstre[x]," Sauvage apparait il a ", pdvMonstre[x], "Pvs")
        while(pdvMonstre[x]>0):
            
            print ("que voulez vous faire ?")
            print ("A - Attaquer, B - Se défendre, C - Fuir")
            
            touche = input()

            while (touche != 'a' or touche != 'b' or touche != 'c'):
            
                #Attaquer 
                if(touche == 'a'):
                    degats = random.randint(1,3*lvJoueur)
                    pdvMonstre[x] = pdvMonstre[x] - degats
                    print("Le ",monstre[x]," a ", pdvMonstre[x], " pvs")
                    input()
                elif(touche == 'b'):
                    degats = 0
                elif(touche == 'c'):
                    fuite = random.randint(1,20)
                    if (fuite >= 15):
                        print("vous fuiez le combat")
                        combat()
                    else:
                        print("le gobelin vous rattrape")
                
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
combat()