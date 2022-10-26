list = [25,14,3,12]
stock = list[0]
nList = 0


while (list[0] > list[1] or list[1] > list[2] or list[2] > list[3]):
    for i in range(0,len(list)):
        if (list[i] < stock):
            stock = list[i]
            nList = i
            print("la plus petite valeur est :", stock)
            print("l'index de la plus petite valeur est :", nList)
        else:
            i = i + 1

        
