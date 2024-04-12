'''
Crea una lista de números enteros y pide al usuario que ingrese otro número entero. Luego, busca el número ingresado en la lista y 
muestra la posición en la que se encuentra. Si el número no se encuentra en la lista, muestra un mensaje indicando que no se encontró
'''

lista_numeros = [1,2,3,4,5,6]

usuario = int(input("Ingrese un nuevo numero: "))

for i in range (len(lista_numeros)):
    if lista_numeros[i] == usuario:
        print("El numero {0} se encuentra en la posicion {1} de la lista".format(usuario,i))
        break
    
else:
    print("El numero {0} no se encotro".format(usuario))

# # Creamos una lista de números enteros
# numeros = [5, 3, 8, 1, 9, 2, 7]

# # Pedimos al usuario que ingrese un número entero
# numero_buscar = int(input("Ingresa un número entero: "))

# # Buscamos el número en la lista y mostramos su posición
# encontrado = False
# for i in range(len(numeros)):
#     if numeros[i] == numero_buscar:
#         encontrado = True
#         print(f"El número {numero_buscar} se encuentra en la posición {i} de la lista.")
#         break

# if not encontrado:
#     print(f"El número {numero_buscar} no se encuentra en la lista.")
