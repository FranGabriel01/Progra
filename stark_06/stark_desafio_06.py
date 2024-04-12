'''
Alumno: Valverde, Cristian.
Division: H
Tutor: Villegas, Octavio.
'''

import json


def leer_archivo(ruta:str):
    with open(ruta, 'r') as archivo:
        diccionario_heroes = json.load(archivo)
    return diccionario_heroes["heroes"]

def stark_normalizar_datos(lista_de_heroes:list):
    '''
    RECIBE: la lista de heroes
    REALIZA: recorre la lista y convierte al tipo de dato correcto las keys, que
    representen datos numericos.
    '''
    # verificamos que la lista ingresada no este vacia
    if not lista_de_heroes:
        print("Error: Lista de héroes vacía")

    # inicializamos la variable 'dato_normalizado' en False porque aun no se modifico ningun dato
    datos_normalizados = False

    # recorro la lista de personajes
    for personaje in lista_de_heroes:
        # para cada personaje recorro su clave y su valor
        for clave, valor in personaje.items():
            if clave in ["altura", "peso", "fuerza"]:
                # verifico que los valores de las claves no sean float antes de castear
                if not isinstance(valor, float):
                    personaje[clave] = float(valor)
                    # si entro al if significa que normalizamos algun valor de alguna clave
                    datos_normalizados = True

    # si se realiza al menos un cambio se imprime el mensaje
    if datos_normalizados:
        return ("Datos Normalizados")
    # por ultimo imprimimos la lista de heroes con los cambios realizados
    # return (lista_de_heroes)
    
# 1
def ordenar_por_altura(lista_original:list, flag_orden = False)->list:
    
    lista_heroes = lista_original[:]    # esto es una copia
    
    rango_lista = len(lista_heroes)-1   # no olvidar el -1
    flag_swap = True

    while(flag_swap):   # esto es un while True
        flag_swap = False
        
        # este for es para ordenar la lista:
        for indice_A in range(rango_lista):
            if  flag_orden == False and lista_heroes[indice_A]["altura"] < lista_heroes[indice_A+1]["altura"] \
             or flag_orden == True and lista_heroes[indice_A]["altura"] > lista_heroes[indice_A+1]["altura"]:
                lista_heroes[indice_A],lista_heroes[indice_A+1] = lista_heroes[indice_A+1],lista_heroes[indice_A]
                flag_swap = True
                
    return lista_heroes
                
# 2
def ordenar_por_peso(lista_original:list, flag_orden = False)->list:
    
    lista_heroes = lista_original[:]    # esto es una copia
    
    rango_lista = len(lista_heroes)-1   # no olvidar el -1
    flag_swap = True

    while(flag_swap):   # esto es un while True
        flag_swap = False
        
        # este for es para ordenar la lista:
        for indice_A in range(rango_lista):
            if  flag_orden == False and lista_heroes[indice_A]["peso"] < lista_heroes[indice_A+1]["peso"] \
             or flag_orden == True and lista_heroes[indice_A]["peso"] > lista_heroes[indice_A+1]["peso"]:
                lista_heroes[indice_A],lista_heroes[indice_A+1] = lista_heroes[indice_A+1],lista_heroes[indice_A]
                flag_swap = True
                
    return lista_heroes
                
# 3
def ordenar_por_nombre(lista_original:list, flag_orden = False)->list:
    
    lista_heroes = lista_original[:]    # esto es una copia
    
    rango_lista = len(lista_heroes)-1   # no olvidar el -1
    flag_swap = True

    while(flag_swap):   # esto es un while True
        flag_swap = False
        
        # este for es para ordenar la lista:
        for indice_A in range(rango_lista):
            if  flag_orden == True and lista_heroes[indice_A]["nombre"] < lista_heroes[indice_A+1]["nombre"] \
             or flag_orden == False and lista_heroes[indice_A]["nombre"] > lista_heroes[indice_A+1]["nombre"]:
                lista_heroes[indice_A],lista_heroes[indice_A+1] = lista_heroes[indice_A+1],lista_heroes[indice_A]
                flag_swap = True
                
    return lista_heroes

# 4
def ordenar_por_nombre_longitud(lista_original:list, flag_orden = False)->list:
    
    lista_heroes = lista_original[:]    # esto es una copia
    
    rango_lista = len(lista_heroes)-1   # no olvidar el -1
    flag_swap = True

    while(flag_swap):   # esto es un while True
        flag_swap = False
        
        # este for es para ordenar la lista:
        for indice_A in range(rango_lista):
            if  flag_orden == True and len(lista_heroes[indice_A]["nombre"]) < len(lista_heroes[indice_A+1]["nombre"]) \
             or flag_orden == False and len(lista_heroes[indice_A]["nombre"]) > len(lista_heroes[indice_A+1]["nombre"]):
                lista_heroes[indice_A],lista_heroes[indice_A+1] = lista_heroes[indice_A+1],lista_heroes[indice_A]
                flag_swap = True
                
    return lista_heroes

# 5
def ordenar_por_key(lista_original :list, clave:str, sentido:True)->list:
    lista_heroes = lista_original[:]    # esto es una copia
    
    rango_lista = len(lista_heroes)-1   # no olvidar el -1
    flag_swap = True

    while(flag_swap):   # esto es un while True
        flag_swap = False
        
        # este for es para ordenar la lista:
        for indice_A in range(rango_lista):
            if  sentido == True and lista_heroes[indice_A][clave] < lista_heroes[indice_A+1][clave] \
             or sentido == False and lista_heroes[indice_A][clave] > lista_heroes[indice_A+1][clave]:
                lista_heroes[indice_A],lista_heroes[indice_A+1] = lista_heroes[indice_A+1],lista_heroes[indice_A]
                flag_swap = True
    
    return lista_heroes

# main
# Mostrar menú de opciones
def main(lista_personajes):

    while True:
        print("Menú de opciones:")
        print("1. Lista ordenada por altura")
        print("2. Lista ordenada por peso")
        print("3. Lista ordenada por nombre alfabeticamente")
        print("4. Ordenar por la longitud del nombre")
        print("5. Ordenar segun la clave")
        print("6. Salir del programa")
    
        opcion_str = input("\nIngrese la opción deseada: ")
        opcion_int = int(opcion_str)

        match(opcion_int):
            case 1:
                lista_ordenado_por_altura = ordenar_por_altura(lista_personajes)
                for personaje in lista_ordenado_por_altura:
                    print(personaje["nombre"], personaje["altura"])

            case 2:
                lista_ordenado_por_peso = ordenar_por_peso(lista_personajes, True)
                for personaje in lista_ordenado_por_peso:
                    print(personaje["nombre"], personaje["peso"])

            case 3:
                lista_ordenada_por_nombre = ordenar_por_nombre(lista_personajes)
                for personaje in lista_ordenada_por_nombre:
                    print(personaje["nombre"])

            case 4:
                lista_ordenada_nombre_longitud = ordenar_por_nombre_longitud(lista_personajes)
                for personaje in lista_ordenada_nombre_longitud:
                    print(personaje["nombre"])

            case 5:
                lista_ordenada_por_clave = ordenar_por_key(lista_personajes, "identidad", True)
                for personaje in lista_ordenada_por_clave:
                    print(personaje["nombre"], personaje["identidad"])

            case 6:
                print("salio del programa")
                break

            case _:
                print("opcion no valida")

# Fin del menu



rutaJSON = '.\DESAFIO_STALK\data_stark_json.json'

lista_personajes = leer_archivo(rutaJSON)

stark_normalizar_datos(lista_personajes)

main(lista_personajes)