from foglalas_beolvasas import fog_beolvasas
from foglalas_rogzites import fog_rogzites
from foglalas_kiiras import fog_kiiras
from nap_kivalasztas import nap_kivalasztas


f_lista=[]
uj_foglalasok=[]
lekert_napok=[]
napi_foglalasok=[]
menupont=0
ossz_bevetel=0

while (menupont !=3):
    menupont=int (input("Kérlek válassz az alábbi menüpontok közül (Foglalás-1, Bevétel lekérdezés-2, Kilépés-3): "))
    if (menupont ==1):
        f_lista=fog_beolvasas("foglalas.txt")
        uj_foglalasok=fog_rogzites(f_lista)
        fog_kiiras("foglalas.txt",uj_foglalasok)
    if (menupont ==2):
        f_lista=fog_beolvasas("foglalas.txt")
        napok=int (input("Kérlek add meg hány nap bevételét szeretnéd lekérdezni (1-7):"))
        for i in range(napok):
            nap=int (input(f"Kérlek add meg a(z) {i+1}. lekérdezni kívánt napot (1-7):"))
            lekert_napok.append(nap)
        print()
        for j in lekert_napok:
            napi_foglalas=nap_kivalasztas(f_lista,j)
            napi_foglalasok.append(napi_foglalas)
        for k in range(len(lekert_napok)):
            print(f"A {lekert_napok[k]}. napon a bevétel: {napi_foglalasok[k]*2000} Ft\n")
            ossz_bevetel=ossz_bevetel+napi_foglalasok[k]
        print(f"Az össz bevétel a lekérdezett napokon: {ossz_bevetel*2000} Ft\n")
        lekert_napok.clear()
        napi_foglalasok.clear()
        ossz_bevetel=0