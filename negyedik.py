import random

print("Ebben a játékban az a cél hogy eltalálja, hogy fej vagy írás.")
print("A tipp résznél így irja be a tippjét: Ha fejre gondolt akkor 1-et irjon be Ha írásra akkor 2-öt irjon be.")
felhasznalo = int(input("Adja meg a tippét. Fej vagy írás?: "))

gep = random.randint(1, 2)

if gep == felhasznalo:
    print("Eltalálta!","")
else:
    print("Nem találta el!")