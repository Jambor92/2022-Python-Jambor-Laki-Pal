from hely_kivalasztas import hely_kivalasztas


def fog_rogzites(foglalt_helyek):
    kilepes = 0
    duplikalt = 0
    sor_lista=[]
    oszlop_lista=[]
    foglalt=0

    while (kilepes != 1):
        nap = int(input("Kérlek add meg a kiválasztott napot(1-7):"))
        terem = int(input("Kérlek add meg a kiválasztott termet (1-3):"))
        napszak = int(input("Kérlek add meg a kiválasztott napszakot (1-3):"))
        print()
        print("1 2 3 4 5 6 7 8 9 10")

        for adat in foglalt_helyek:
            if (nap == adat[0] and terem == adat[1] and napszak== adat[2]):
                sor_lista.append(adat[3])
                oszlop_lista.append(adat[4])
        
        for j in range(1,11):
            for k in range(1,11):
                for l in range(0,len(sor_lista)):
                    if (sor_lista[l] == j and oszlop_lista[l] == k):
                        foglalt=1
                if (foglalt == 1):
                    print("x", end=" ")
                else:
                    print("o", end=" ")
                foglalt=0
            print(j)
                
        print()
        sor_lista.clear()
        oszlop_lista.clear()
        sor = int(input("Kérlek add meg a kiválasztott teremben a kiválasztott ülőhely sorszámát (1-10):"))
        oszlop = int(input("Kérlek add meg a kiválasztott teremben a kiválasztott ülőhely oszlopszámát (1-10):"))

        foglalt_hely = hely_kivalasztas(nap, terem, napszak, sor, oszlop)
        for i in foglalt_helyek:
            if (foglalt_hely == i):
                print("A megadott hely már foglalt!")
                duplikalt = 1
                break
        if (duplikalt == 0):
            foglalt_helyek.append(foglalt_hely)

        kilepes = int(input("Szeretnél újabb foglalást rögzíteni? (Igen-0, Nem-1):"))

    return foglalt_helyek