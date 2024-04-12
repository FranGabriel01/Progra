# lista_palabras = ["Pepe", "dinosaurio", "ramon"]
# cantidad_vocales = 0

# for palabras in lista_palabras:
#     for letras in palabras:
#         if letras in 'aeiou':
#             cantidad_vocales += 1
        
# print (cantidad_vocales)

lista_palabras = ["Pepe", "dinosaurio", "ramon"]
contador_vocales = 0

for palabras in lista_palabras:
    for letras in palabras:
        if letras in 'aeiou':
            contador_vocales += 1

print (contador_vocales)