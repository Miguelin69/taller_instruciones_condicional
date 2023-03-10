print("ingrese el valor de x: ")
x = int(input())
print("ingrese el valor de y: ")
y = int(input())

if x > 0 and y > 0:
    print("el punto pertenece al primer cuadrante")
elif x > 0 and y < 0:
    print("el punto pertenece al segundo cuadrante")
elif x < 0 and y < 0:
    print("el punto pertenece al tercer cuadrante")
elif x < 0 and y > 0:
    print("el punto pertenece al cuarto cuarante")
else :
    print("el punto se ubica en el origen")