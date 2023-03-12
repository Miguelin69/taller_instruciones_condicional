import math

print("Introducir primer lado: ")
L1 = int(input())
print("Introducir segundo lado: ")
L2 = int(input())
print("Introducir tercer lado: ")
L3 = int(input())

if L1**2 == L2**2 and L2**2 == L3**2:
    print("El triangulo es AGUDO ")

elif L3**2 == ( L1**2 + L2**2):
    print("El triangulo es RECTO ")
    
elif L3**2 > (L1**2 + L2**2):
    print("El triangulo es OBTUSO ")

else :
    print("El triangulo es diferente")