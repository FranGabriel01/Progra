numeros = [1, 2, 3, 4, 5, 6, 7]

contador_pares = 0

for pares in numeros:
    if pares % 2 == 0:
        contador_pares += 1
        
print("La cantidad de numeros pares en la lista es {0}".format(contador_pares))
        