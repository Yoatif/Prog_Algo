def afficheGrille (grille):
    for i in range (0,9,3):
        print (grille[i], grille[i+1], grille[i+2],)

def ajoutesymbole (grille,tour):
    caseValable = False
    while(not caseValable):
        numeroCase= int(input("quel case ?"))
        if (numeroCase <9 and grille[numeroCase] !="O" and grille[numeroCase] !="X"):
            caseValable = True
    symbole="O"
    if (tour%2==1):
        symbole="X"
    grille[numeroCase] = symbole
def testVictoireHorizontale (grille):
    for i in range (0,9,3):
        if ((grille[i] == grille[i+1] == grille[i+2]) and (grille[i]=="O" or grille[i]=="X")):
            return True
    return False
def testVictoireVerticale(grille):
    for i in range(0, 9, 3):
        if ((grille[i] == grille[i+3] == grille[i+6]) and (grille[i]=="O" or grille[i]=="X")):
            return True
    return False
def testVictoireDiagonale(grille):
    if (grille[4]=="O" or grille[4]=="X"):
        if (grille[0] == grille[4] == grille[8]):
            return True
        if (grille[0] == grille[4] == grille[8]):
            return True
    return False

#ici débute le programme
grille = (" "," "," "," "," "," "," "," "," ")
tour = 0
victoire = False
while (not victoire and tour < 9):
    tour +=1
    afficheGrille(grille)
    ajoutesymbole(grille,tour)
    victoire = testVictoireHorizontale(grille) or testVictoireVerticale(grille) or testVictoireDiagonale(grille)
if (victoire):
    print ("GG")
else:
    print("noob")