import random

sujet = ["un homme", "une femme", "une licorne", "un chat", "Liam le margoulin"]
verbe = ["caresse", "mange","a battu","naylérise"]
complement = ["dans la rue", "devant la télé", "en lechant un kinder bueno"]

rand1 = random.randint(0, len(sujet)-1)
rand2 = random.randint(0, len(verbe)-1)
rand3 = random.randint(0, len(complement)-1)

for i in range(0,len(sujet)):
    print(rand1, rand2, rand1, rand3,)