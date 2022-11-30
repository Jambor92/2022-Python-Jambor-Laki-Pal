from foglalas_beolvasas import fog_beolvasas
from foglalas_rogzites import fog_rogzites
from foglalas_kiiras import fog_kiiras

f_lista=[]
uj_foglalasok=[]

f_lista=fog_beolvasas("foglalas.txt")
uj_foglalasok=fog_rogzites(f_lista)
fog_kiiras("foglalas.txt",uj_foglalasok)