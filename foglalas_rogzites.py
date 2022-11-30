from hely_kivalasztas import hely_kivalasztas

def fog_rogzites(foglalt_helyek):
    
    kilepes=0
    duplikalt=0

    while (kilepes !=1):
        terem=int (input("Kérlek add meg a kiválasztott termet (1-3):"))
        napszak=int (input("Kérlek add meg a kiválasztott napszakot (1-3):"))
        sor=int (input("Kérlek add meg a kiválasztott teremben a kiválasztott ülőhely sorszámát (1-10):"))
        oszlop=int (input("Kérlek add meg a kiválasztott teremben a kiválasztott ülőhely oszlopszámát (1-10):"))

        foglalt_hely=hely_kivalasztas(terem,napszak,sor,oszlop)
        for i in foglalt_helyek:
            if (foglalt_hely == i):
                print("A megadott hely már foglalt!")
                duplikalt=1
                break
        if (duplikalt == 0):
            foglalt_helyek.append(foglalt_hely)

        kilepes= int(input("Szeretnél újabb foglalást rögzíteni? (Igen-0, Nem-1):"))

    return foglalt_helyek
