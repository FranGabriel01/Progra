#Crea una lista de palabras y muestra las palabras que tienen más de 5 letras.

lista_palabras = ["Raton", "Cocodrilo", "Leon", "Cabra", "Perro", "Rinoceronte", "Jirafa", "Hipopotamo" ]
acumulador_de_palabras = " "

for palabra in lista_palabras:
    if len(palabra) > 5:
        acumulador_de_palabras += palabra + " "
        
print("Las palabras con mas de 5 letras son {0}".format(acumulador_de_palabras))