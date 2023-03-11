g = int(input("Ingrese el valor de su prestamo: "))

if g<945200 :
    print( "fue denegado tu crédito")

else :
    x = int(input("si tiene deudas ingrese el número 1, de lo contrario ingrese cualquier otro número: "))

if x==1 :
    print( "tu crédito fue denegado, lo sentimos")

else : 
     print( "tu crédito fue aprovado")