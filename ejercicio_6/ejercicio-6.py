import math

v = int(input("ingrese el valor de a: "))
h = int(input("ingrese el valor de b: "))
p = int(input("ingrese el valor de c: "))


D = (h**2)-(4*v*p)

if (D == 0):
    X = -h/2*v
    rta = "las dos raices son: " + str(X)
else:
    if (D<0):
        rta = "raices imaginarias"
    else:
        X2 = (-(h)+(math.sqrt(D)))/(2*v)
        X1 = (-(h)-(math.sqrt(D)))/(2*v)
        rta = "las raices son: "+" x1: "+ str(X1)+" x2: " + str(X2)

print(rta)
