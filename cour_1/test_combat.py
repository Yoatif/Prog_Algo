import random



gobHP = 100
gobAtk = 0.5
xp = 0
lvl = 1
hpJoueur = 100
atkJoueur = 1


potion = 20
mortGob = "Le gobelin est mort !"
MobVaincu = False


print("vous rencontrez un gobelin.")
print("il vous menace avec son couteau")

while (lvl != 100):
    while(MobVaincu == False):

        action = int(input("vous utiliser 1 attaque 2 potion"))

        
        if (action == 1 and gobHP > 0):
            gobHP = gobHP - (atkJoueur * random.randint(1,15)) 
            print("il reste ", gobHP, "au gobelin")

            if (gobHP <= 0):
                print("Félicitation, tu as tué le gobelin")
                xp += 72

                if(xp>=lvl*100):
                    print("Felicitation tu as pris un level")
                    input()
                    lvl = lvl+1

                if(MobVaincu == True):
                    MobHp = MobHp + 1
                    MobVaincu = False

        elif (action == 2):
            if (hpJoueur <= 80):
                hpJoueur = hpJoueur + potion
                print ("vous avez ", hpJoueur,"PDV")

            else:
                hpJoueur = 100
                print("vous avez", hpJoueur,"PDV")
        hpJoueur = hpJoueur - (gobAtk * random.randint(1,5))
        print ("il vous reste", hpJoueur, "PDV")




    


