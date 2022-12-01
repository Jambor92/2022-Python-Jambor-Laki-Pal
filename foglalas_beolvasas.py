from hely_kivalasztas import hely_kivalasztas

def fog_beolvasas(filename):

    foglalas=[]
    ulo_hely=[]

    with open (filename, "r", encoding="utf-8") as befile:
        befile.readline()
        for sor in befile:
            foglalt_hely=sor.strip()
            fog_lista=foglalt_hely.split(" ")
            ulo_hely=hely_kivalasztas(int(fog_lista[0]),int(fog_lista[1]),int(fog_lista[2]),int(fog_lista[3]),int(fog_lista[4]))
            foglalas.append(ulo_hely)

    return foglalas