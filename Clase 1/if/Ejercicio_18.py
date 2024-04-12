numero = int(input("Ingrese un numero"))

if numero % 2 == 0 and numero % 3 == 0:
    print("El numero es par y multiplo de 3")
elif numero % 2 == 0 or numero % 3 == 0:
    print("El numero solo cumple una condicion")
else:
    print("El numero no cumple ninguna condicion")