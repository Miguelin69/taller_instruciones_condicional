a = int(input("ingrese el valor del peso en kg: "))
b = float(input("ingrese el valor de la altura en m: "))


k = a/(b**2)


if k<16:
    rta= "Criterio de ingreso al hospital"
else:
    if 16<=k<17:
        rta = "infrapeso"
    else:
        if 17<=k<18:
            rta= "Bajo peso"
        else:
            if 18<=k<25:
                rta="peso normal (saludable)"
            else:
                if 25<=k<30:
                    rta= "Sobrepeso (obesidad grado I)"
                else:
                    if 30<=k<35:
                        rta= "Sobrepeso cronico (obesidad grado II)"
                    else:
                        if 35<=k<40:
                            rta="Obesidad premorbida (obesidad grado III)"
                        else:
                            rta= "Obesidad morbida (obesidad de grado IV)"
print(rta)