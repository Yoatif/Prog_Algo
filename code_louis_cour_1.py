import random

Xp = 0
Lvl = 1
Monstres = 0
Dice = 0
MobHp = 10
MobVaincu = False

while(True):
    Dice = random.randint(1+Lvl,20+Lvl)
    
    if(Dice>=MobHp):
        print("Felicitation a toi GIGA CHAD, tu as tué 1 monstre")
        input()
        Xp = Xp + 72
        MobVaincu = True
    else:
        print("GIGA Nul.le, tu as pas tué 1 monstre")
        input()
        MobVaincu = False

    if(Xp>=Lvl*100):
        print("Felicitation tu as pris un level")
        input()
        Lvl = Lvl+1

    if(MobVaincu == True):
        MobHp = MobHp + 1