lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
contador_de_impares = 0

for impar in lista_numeros:
    if impar % 2 == 1:
        contador_de_impares += 1
print (contador_de_impares)