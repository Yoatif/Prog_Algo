list = [25,14,3,12,99,5,43,34,24,54,70]



for i in range(len(list)):
    for j in range(0,i):
        if (list[i] < list[j]):
            list.insert(j,list[i])
            list.pop(i+1)    

print(list)