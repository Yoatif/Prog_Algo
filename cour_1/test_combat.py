import random

from cour_1.code_louis_cour_1 import MobVaincu

gobHP = 100
gobAtk = random.randint(1,15)
hpJoueur = 100
atkJoueur = random.randint(1,20)
potion = 20
mortGob = "Le gobelin est mort !"
MobVaincu = False

print("vous rencontrez un gobelin")
while(gobHP > 0 or hpJoueur > 0):
    
    action = int(input("vous utiliser 1 attaque 2 potion"))
    if (action == 1 and gobHP > 0):
        gobHP = gobHP - random.randint(1,10)
        print("il reste ", gobHP, "au gobelin")
    elif (action == 2):
        if (hpJoueur <= 80):
            hpJoueur = hpJoueur + potion
            print ("vous avez ", hpJoueur,"PDV")
        else:
            hpJoueur = 100
            print("vous avez", hpJoueur,"PDV")
    hpJoueur = hpJoueur - random.randint(1,5)
    print ("il vous reste", hpJoueur, "PDV")


    


