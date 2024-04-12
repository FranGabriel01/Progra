#Crea una lista vacía y pide al usuario que ingrese números enteros hasta que ingrese un número negativo. Luego, muestra la suma de todos los números ingresados.

lista_numeros = []
suma = 0
while True:
    numeros = int(input("Ingrese un numero para agregar"))

    if numeros < 0:
        break
    lista_numeros.append(numeros)

for numero in lista_numeros:    
    suma += numero

print (suma)