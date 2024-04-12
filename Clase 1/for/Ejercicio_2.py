palabras = ["Jota", "Rodrigo", "peluca", "dinosaurio"]
palabra_mas_larga = palabras [0]

for palabra in palabras:
    if len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra
print ("La palabra mas larga es", palabra_mas_larga)