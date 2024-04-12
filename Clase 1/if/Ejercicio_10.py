numero = int(input("Ingrese un numero: "))

if numero > 0 and numero % 2 == 0:
    print ("El numero es positivo y par")
elif numero > 0:
    print ("El numero es mayor que 0 pero no es par")
else:
    print ("El numero no cumple ninguna condicion.")