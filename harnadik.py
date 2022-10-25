elso_szam = float(input("Adja meg az egyik számot: "))
masodik_szam = float(input("Adja meg a második számot: "))

if elso_szam > masodik_szam:
    print(elso_szam, ">" ,masodik_szam)
elif elso_szam == masodik_szam:
    print(elso_szam, "=" , masodik_szam)
else:
    print(elso_szam, "<" , masodik_szam)