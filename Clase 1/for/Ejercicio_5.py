# #lista_numero = [3, 5, 1, 10, 5, 65, 7]
# primer_numero_ingresado = True

# for numero in lista_numero:
#     if primer_numero_ingresado == True or numero < numero_mas_pequeño:
#         numero_mas_pequeño = numero
#         primer_numero_ingresado = False

# print("El numero mas pequeño es {0}".format(numero_mas_pequeño))

# lista_numero = [3, 5, 1, 10, 5, 65, 7]

# for i in range(len(lista_numero)):
#     if i == 0 or lista_numero[i] < numero_mas_pequeño:
#         numero_mas_pequeño = lista_numero[i]
# print("El numero mas pequeño es {0}".format(numero_mas_pequeño))

# lista_numeros = [3, 6, 2, 77, 21]
# primer_numero_ingresado = True #BANDERA

# for numero in lista_numeros: 
#     if primer_numero_ingresado == True or numero < numero_mas_pequeño:
#         numero_mas_pequeño = numero
#         primer_numero_ingresado = False
        
# print (numero_mas_pequeño)




lista_numeros = [3, 5, 33, 1, 25, 2, 4, -1, 23]
bandera_mas_chico = True

for numero in lista_numeros:
    if bandera_mas_chico == True or numero < numero_mas_chico:
        numero_mas_chico = numero
        bandera_mas_chico = False
        
print (numero_mas_chico)