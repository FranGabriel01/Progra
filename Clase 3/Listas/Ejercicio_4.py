#Crea una lista vacía y pide al usuario que ingrese una palabra. Luego, muestra la primera letra de la palabra. 
#Repite este proceso hasta que el usuario ingrese una palabra que comience con la letra "z".

lista_palabras = []

while True:
    palabra = input("Ingrese una palabra que no comiense con z: ")

    if palabra[0] == "z":
        break
    lista_palabras.append(palabra)
    
    primera_letra = palabra[0]
    print("La primera letra de {1} es {0}".format(primera_letra,palabra))