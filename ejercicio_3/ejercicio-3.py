p = int(input("Ingrese el valor del costo del articulo: "))


if p< 3000:
    m = (15*p)/100
    
else:
    if 3000 <= p <= 6000:
        m = 500
    else: 
      m = (25* p)/100


o = p + m

print(o)