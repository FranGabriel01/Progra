from data_stark import lista_personajes



def mostrar_un_superheroe_por_nombre(personaje:dict):
    print("Nombre:{0}-Genero:{1}-Altura{2}-Fuerza: {3}".format(personaje["nombre"],personaje["genero"],personaje["altura"],personaje["fuerza"]))

def mostrar_superheroes_por_nombre(lista:list):
    '''
    Funcion que se encarga de mostrar los nombres de los superheroes
    '''
    for personaje in lista:
        mostrar_un_superheroe_por_nombre(personaje)


def obtener_superheroes_por_genero(genero:str):
    lista_genero = []

    for personaje in lista_personajes:
        if personaje["genero"] == genero:
            lista_genero.append(personaje)

    return lista_genero

def obtener_elemento_maximo(lista:list,clave:str):
    flag_del_primero = True

    for personaje in lista:
        if flag_del_primero == True or float(personaje[clave]) > maximo:
            flag_del_primero = False
            maximo = float(personaje[clave])

    return maximo

def determinar_mayor(lista:list,clave:str):
    '''
    Me determina el personaje o los personajes mayores pasandole una lista especifica
    '''
    maximo = obtener_elemento_maximo(lista, clave)
    lista_mayor = []

    for personaje in lista:
        if float(personaje[clave]) == maximo:
            lista_mayor.append(personaje)

    return lista_mayor


lista_fem = obtener_superheroes_por_genero("F")
mostrar_superheroes_por_nombre(lista_fem)