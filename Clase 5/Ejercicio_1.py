from data_stark import lista_personajes

def nombre_superheroe():
    for superheroe in lista_personajes:
        print ("El nombre del  superheoe es: {0}".format(superheroe["nombre"]))
        
def nombre_altura_superheroe():
    for nombre_altura in lista_personajes:
        print ("El nombre del  superheoe es: {0} y su altura es de {1}".format(nombre_altura["nombre"],nombre_altura["altura"]))
        
def superheroe_mas_alto():
    for indice in range(len(lista_personajes)):
        if (indice == 0 or float(lista_personajes[indice]["altura"]) > altura_maxima):
            indice_maximo = indice
            altura_maxima = float(lista_personajes[indice]["altura"])
        
    print("\nSuperheroe {0} - altura {1}\n\n".format(lista_personajes[indice_maximo]["nombre"],lista_personajes[indice_maximo]["altura"]))
    
def superheroe_mas_bajo():
    for indice in range(len(lista_personajes)):
        if (indice == 0 or float(lista_personajes[indice]["altura"]) < altura_minima):
            indice_minimo = indice
            altura_minima = float(lista_personajes[indice]["altura"])
        
    print("\nSuperheroe {0} - altura {1}\n\n".format(lista_personajes[indice_minimo]["nombre"],lista_personajes[indice_minimo]["altura"]))

def altura_promedio():
    acumulador_altura = 0
    for altura in lista_personajes:
        acumulador_altura += float(altura["altura"])
        
    altura_promedio_superheroe = acumulador_altura / float(altura["altura"])
    input("La altura promedio es: {0}".format(altura_promedio_superheroe))

def identidad():
    for indice in range(len(lista_personajes)):
        if (indice == 0 or float(lista_personajes[indice]["altura"]) < altura_minima):
            indice_minimo = indice
            altura_minima = float(lista_personajes[indice]["altura"])
            
    for indice in range(len(lista_personajes)):
        if (indice == 0 or float(lista_personajes[indice]["altura"]) > altura_maxima):
            indice_maximo = indice
            altura_maxima = float(lista_personajes[indice]["altura"])

    print("\nIdentidad del mas bajo es {0} y la identidad del mas alto es {1}\n\n".format(lista_personajes[indice_minimo]["identidad"],lista_personajes[indice_maximo]["identidad"]))
        
def mas_y_menos_pesado():
    for indice in range(len(lista_personajes)):
        if (indice == 0 or float(lista_personajes[indice]["peso"]) < peso_minimo):
            indice_minimo = indice
            peso_minimo = float(lista_personajes[indice]["peso"])
            
    for indice in range(len(lista_personajes)):
        if (indice == 0 or float(lista_personajes[indice]["peso"]) > peso_maximo):
            indice_maximo = indice
            peso_maximo = float(lista_personajes[indice]["peso"])

    print("\nEl superheroe mas liviano es {0} y pesa {1} y el mas pesado es {2} y pesa {3}\n\n".format(lista_personajes[indice_minimo]["nombre"],lista_personajes[indice_minimo]["peso"],lista_personajes[indice_maximo]["nombre"],lista_personajes[indice_maximo]["peso"]))
    
def mostrar_lista():
    for superheroe in range(len(lista_personajes)):
                print(lista_personajes[superheroe])

while True:
    respuesta = int(input("1-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe \n2-Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo \n3-Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO) \n4-Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO) \n5-Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO) \n6-Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO) \n7-Calcular e informar cual es el superhéroe más y menos pesado.\n8-Mostrar lista de superheroes \n9-Salir\n\n"))
    
    match respuesta:
        case 1:
            nombre_superheroe()
        case 2:
            nombre_altura_superheroe()
        case 3:
            superheroe_mas_alto()
        case 4:
            superheroe_mas_bajo()
        case 5:
            altura_promedio()
        case 6:
            identidad()
        case 7:
            mas_y_menos_pesado()
        case 8:
            mostrar_lista()
        case 9:
            break
            