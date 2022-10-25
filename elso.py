import math

x = float(input("Adja meg, hogy hol helyezkedik el az első pont az x tengelyen: ")) #x 
y = float(input("Adja meg, hogy hol helyezkedik el az első pont az y tengelyen: ")) #y
x_ketto = float(input("Adja meg, hogy hol helyezkedik el a második pont az x tengelyen: ")) # x a másodikon
y_ketto = float(input("Adja meg, hogy hol helyezkedik el a második pont az y tengelyen: ")) # y a másodikon

c_negyzetx = math.pow(x_ketto - x,2)
c_negyzety = math.pow(y_ketto - y,2)
c_osszeg = c_negyzetx + c_negyzety
vegeredmeny = math.sqrt(c_osszeg)

print(vegeredmeny)