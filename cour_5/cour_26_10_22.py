score = [0,0,0,0]
moyScore = 0
scoreTotal = 0

for i in range (0,len(score)):
    score[i] = int(input("veuillez rentrer un entier svp"))
    print(score)
    scoreTotal = scoreTotal + score[i]
    print(scoreTotal)
    moyScore = (moyScore + score[i])/len(score)
    print(moyScore)

