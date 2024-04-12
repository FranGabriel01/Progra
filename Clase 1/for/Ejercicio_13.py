palabras = ["Jota", "Rodrigo", "peluca", "dinosaurio", "cacas"]
contador_de_palabras_impares = 0
for palabras_impares in palabras:
    if len(palabras_impares) % 2 == 1:
        contador_de_palabras_impares += 1

print (contador_de_palabras_impares)