#Crea una lista con los números del 1 al 10 e imprime solo los números impares.

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numeros_impar in lista_numeros:
    if numeros_impar % 2 == 1:
        print (numeros_impar)