list = [25,14,3,12,99,5,43,34,24,54,70]



for i in range(len (list)):
        stock=i
        for j in range(i+1, len (list)):
            if list[j]<list[stock] :
                stock = j
        list[i], list[stock] = list[stock], list[i]
        print(list)
    