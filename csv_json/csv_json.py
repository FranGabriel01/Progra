import json
import csv

# LEER CSV ----------------------------------------
def leer_csv(ruta: str)->list:
    '''
    Descripción: Esta función lee un archivo CSV y devuelve su contenido
    como una lista de listas, donde cada lista representa una fila en el archivo.
    
    Parámetros:
    "ruta" (str): La ruta del archivo CSV que se desea leer.
    
    Retorno: "lista_retorno" (list): Una lista de listas que representa el contenido del
    archivo CSV. Cada lista interna representa una fila del archivo.
    '''
    lista_retorno = list()

    with open(ruta, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        for fila in lector_csv:
            lista_retorno.append(fila)

    return lista_retorno

# LEER JSON --------------------------------------
def leer_json(ruta: str) -> dict:
    '''
    Esta función lee un archivo JSON y devuelve su contenido como un diccionario.
    
    Parametro:
    ruta: El parámetro "ruta" es una cadena que representa la ruta del archivo JSON que queremos
    leer y cargar en un diccionario de Python
    
    Retorno: Un diccionario que contiene los datos del archivo JSON ubicado en la ruta especificada.
    '''
    with open(ruta, 'r') as archivo:
        diccionario = json.load(archivo)
    return diccionario

# -------------------------------------------------
# GUARDAR CSV ------------------------------------
def guardar_csv(ruta: str, lista: list):
    with open(ruta, 'w') as archivo:
        for elemento in lista:
            archivo.write(",".join(elemento) + '\n')

# GUARDAR JSON -----------------------------------
def guardar_json(ruta: str, diccionario: dict):
    with open(ruta, 'w') as archivo:
        json.dump(diccionario, archivo)
