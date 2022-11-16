list = [25,14,3,12,99,5,43,34,24,54,70]



for i in range(len(list)):
    stock = list[0]
    if (list[i] < stock):
        stock2 = list[i]
        list.pop(i)
        list.insert(0,stock2)

print(list)