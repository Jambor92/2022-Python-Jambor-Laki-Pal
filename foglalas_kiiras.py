def fog_kiiras(fname,foglalasok):
    foglalasok.sort()
    with open (fname,"w", encoding="utf-8") as kifile:
        kifile.write("N;T;Nsz;S;O\n")
        for sor in foglalasok:
            for i in sor:
                kifile.write((f"{i} "))
            kifile.write("\n")
    print("A foglalás(ok) rögzítésre került(ek)")