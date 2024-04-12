from data_stark import lista_personajes

'''
\n1-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
\n2-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
\n3-Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
\n4-Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
\n5-Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
\n6-Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
\n7-Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
\n8-Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
\n9-Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
\n10-Determinar cuántos superhéroes tienen cada tipo de color de ojos.
\n11-Determinar cuántos superhéroes tienen cada tipo de color de pelo.
\n12-Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
\n13-Listar todos los superhéroes agrupados por color de ojos.
\n14-Listar todos los superhéroes agrupados por color de pelo.
\n15-Listar todos los superhéroes agrupados por tipo de inteligencia
'''

def mostrar_un_superheroe(personaje:dict):
   print("Nombre:{0}-Genero:{1}-Altura{2}-Fuerza: {3}".format(personaje["nombre"],personaje["genero"],personaje["altura"],personaje["fuerza"]))

def mostrar_nombre_superheroe(lista:list):
    for nombre in lista:
        mostrar_nombre_superheroe(nombre)

def imprimir_genero_superheroe(genero:str):
    lista_genero = []
    for superheroe in lista_personajes:
        if superheroe["genero"] == genero:
            lista_genero.append(superheroe)

    return lista_genero
           
           


# while True:
#     respuesta = int(input("1-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M \n2-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F \n3-Recorrer la lista y determinar cuál es el superhéroe más alto de género M  \n4-Recorrer la lista y determinar cuál es el superhéroe más alto de género F  \n5-Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M  \n6-Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F  \n7-Recorrer la lista y determinar la altura promedio de los  superhéroes de género M \n8-Recorrer la lista y determinar la altura promedio de los  superhéroes de género F \n9-Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F) \n10-Determinar cuántos superhéroes tienen cada tipo de color de ojos. \n11-Determinar cuántos superhéroes tienen cada tipo de color de pelo. \n12-Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).  \n13-Listar todos los superhéroes agrupados por color de ojos. \n14-Listar todos los superhéroes agrupados por color de pelo. \n15-Listar todos los superhéroes agrupados por tipo de inteligencia"))


lista_fem = imprimir_genero_superheroe("F")
print (lista_fem)


