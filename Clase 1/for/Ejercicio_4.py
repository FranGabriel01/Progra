numero = int(input("Ingrese un numero"))
suma = 0

for l in range(1, numero+1):
    if l % 2 == 1:
        suma += l
        
print("La suma de los impares menores a {0} es {1}".format(numero,suma))