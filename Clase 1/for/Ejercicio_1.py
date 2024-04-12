numeros = [1, 2, 3, 4, 5, 6, 7]
maximo = numeros[0]

for numero in numeros:
    if numero > maximo:
        maximo = numero
        
print ("El numero maximo de la lista es ", maximo)