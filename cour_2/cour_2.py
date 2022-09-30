import random

gobelinPv = 10
gobelinLvl = 1
gobelinVaincu = 0
degat = 0

xpJoueur = 0
lvlJoueur = 1
hpJoueur = 100 +(2.5*lvlJoueur)

potion = 20



while (True):   
    gobelinPv = random.randint(4,6)*gobelinLvl
    print("vous rencontrez un gobelin de lvl", gobelinLvl, ", il a", gobelinPv, "PdV")
    while (gobelinPv > 0):
        
        print("quel action souhaitez vous éxecuter ?")
        action = input("1 attaquer, 2 boire une potion, 3 fuir")

        if (action == "1"):
            degat = random.randint(1,3)
            gobelinPv -= degat
            print ("le gobelin a", gobelinPv ,"PdV restant")
            input()
            print ("Le gobelin vous attaque")
            hpJoueur -= (random.randint(1,3))
            if (gobelinPv < 0):               
                print ("vous avez vaincu le Gobelin.")
        if (action == "2"):
            print("vous prenez une potion")
            if (hpJoueur <= 80):
                hpJoueur = hpJoueur + potion
                print ("vous avez ", hpJoueur,"PDV")

            else:
                hpJoueur = 100
                print("vous avez", hpJoueur,"PDV")


        if (action == "3"):
            fuite = random.randint(1,20)
            if (fuite >=16):
                print("vous avez fuis")


        #gestion xp gobelin
        gobelinVaincu +=1
        if (gobelinVaincu>= 7):
            gobelinVaincu = 0
            gobelinLvl +=1

        #gestion xp joueur 
        xpJoueur += (gobelinLvl * 2)
        if(xpJoueur>=lvlJoueur*100):
            print("Felicitation tu as pris un level")
            input()
            lvlJoueur = lvlJoueur+1


