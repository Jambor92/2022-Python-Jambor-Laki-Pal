import random
from foglalas_kiiras import fog_kiiras

def random_foglalas():
    
    r_f=[]

    r_f.append(random.randint(1,7))
    r_f.append(random.randint(1,3))
    r_f.append(random.randint(1,3))
    r_f.append(random.randint(1,10))
    r_f.append(random.randint(1,10))

    return r_f

db=0
teljes_lista=[]
hely_foglalas=[]
ismetles=0

while (db != 199):
    hely_foglalas=random_foglalas()
    for i in teljes_lista:
        if (i == hely_foglalas):
            ismetles=1
            break
    if (ismetles==0):
        teljes_lista.append(hely_foglalas)
        db=db+1
    ismetles=0
teljes_lista.sort()
fog_kiiras("foglalas.txt", teljes_lista)



