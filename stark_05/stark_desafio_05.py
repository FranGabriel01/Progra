import re
import json
from data_stark import lista_personajes


def imprimir_dato(dato: str):
    print(dato)
    
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

def dividir(dividendo: float, divisor: float):
    '''
    RECIBE: dos numeros (dividendo y divisor).
    RETORNA: 0 (si el divisor es 0) o la division entre ambos.
    '''
    if divisor == 0:
        return 0
    else:
        resultado = dividendo / divisor
        return resultado

def sumar_dato_heroe(lista_heroes: list, clave: str)->float:
    '''
    RECIBE: una lista de héroes y un string que representara el dato/key de
    los héroes que se requiere sumar.
    RETORNARA: la suma de todos los datos segun la key pasada por parametro.
    '''
    suma = 0
    for heroe in lista_heroes:
        if not isinstance(heroe, dict) and not heroe:
            return "diccionario vacio"
        else:
            dato_a_sumar = float(heroe[clave])
            suma += dato_a_sumar

    return suma

# -------------
# EJERCICIOS 1
# 1.1
def imprimir_menu_desafio_5():
    '''
    imprime el menu por pantalla
    '''
    imprimir_dato('''
    MENÚ DE OPCIONES:
    A. Recorrer la lista imprimiendo el nombre de cada superhéroe de género M
    B. Recorrer la lista imprimiendo el nombre de cada superhéroe de género F
    C. Cuál es el superhéroe más alto de género M
    D. Cuál es el superhéroe más alto de género F
    E. Cuál es el superhéroe más bajo de género M
    F. Cuál es el superhéroe más bajo de género F
    G. La altura promedio de los superhéroes de género M
    H. La altura promedio de los superhéroes de género F
    I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
    indicadores anteriores (ítems C a F)
    J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
    no tener, Inicializarlo con ‘No Tiene’).
    M. Listar todos los superhéroes agrupados por color de ojos.
    N. Listar todos los superhéroes agrupados por color de pelo.
    O. Listar todos los superhéroes agrupados por tipo de inteligencia
    Z. salir
    ''')

# 1.2
def stark_menu_principal_desafio_5():
    imprimir_menu_desafio_5()
    opcion = input("\nIngrese la opción deseada: ")
    if opcion.isupper():
        opcion = opcion.lower()

    if re.search('^[a-oA-OzZ]$', opcion) != None:
        return opcion
    else:
        return -1

# 1.4
def leer_archivo(ruta: str):
    with open(ruta, 'r') as archivo:
        diccionario_heroes = json.load(archivo)
    return diccionario_heroes["heroes"]

# 1.5
def guardar_archivo(ruta:str, contenido:str)-> bool:
    with open(ruta, "w+") as archivo:
        archivo_creado = archivo.write(contenido)
        if archivo_creado:
            print("Se creó el archivo: {0}".format(ruta))
            return True
        else:
            print("Error al crear el archivo: {0}".format(ruta))
            return False
         
# 1.6
def capitalizar_palabras(frase:str)->str:
    palabras = frase.split()
    resultado = []
    for palabra in palabras:
        resultado.append(palabra.capitalize())
    return " ".join(resultado)

# 1.7
def obtener_nombre_capitalizado(heroe:dict):
    nombre = heroe["nombre"]
    nombre_capitalizado = capitalizar_palabras(nombre)
    return "Nombre: {0}".format(nombre_capitalizado)

# 1.8
def obtener_nombre_y_dato(heroe:dict, key:str)->str:
    nombre = obtener_nombre_capitalizado(heroe)
    dato = heroe.get(key, "N/A")
    return "{0} | {1}: {2}".format(nombre, key.capitalize(), dato)

# ----------------
# EJERCICIOS 2
# 2.1
def es_genero(heroe:dict,genero:str)->bool:
    '''
    recibe: un diccionario que representa a un heroe y un string el cual
    sera evaluado si coincide con el genero de dicho heroe.
    retorna: True si coincide o False si no coincide
    '''
    genero = genero.upper()
    if heroe["genero"] == genero:
        return True
    else:
        return False
    
# 2.2
def stark_guardar_heroe_genero(heroes:list,genero:str)->bool:
    '''
    recibe: una lista de heroes y el genero a evaluar
    retorna: un archivo csv que tiene la lista de heroes que coinciden con el genero
    pasado por el parametro y se encuentran separados por una ","
    '''
    genero = genero.upper()
    lista_nombres = list()
    for heroe in heroes:
        if es_genero(heroe, genero):
            nombre = obtener_nombre_capitalizado(heroe)
            lista_nombres.append(nombre)
            imprimir_dato(nombre)
    archivo = "heroes_{0}.csv".format(genero)
    return guardar_archivo(archivo, ",".join(lista_nombres))

# ----------------
# EJERCICIOS 3
# 3.1
def calcular_min_genero(listado_heroes: list, clave: str, genero:str):
    '''
    recibe: la lista de héroes y una key, la cual representará el dato a evaluar
    y ademas el genero.
    retorna: dependiendo el genero el o la mas bajo/a en la lista.
    '''
    #stark_normalizar_datos(listado_heroes)
    flag_genero = False
    if clave in ["altura", "peso", "fuerza"]:
        for heroe in listado_heroes:
            if heroe["genero"] == genero:
                if flag_genero == False:
                    minimo_valor = heroe[clave]
                    minimo_heroe = heroe
                    flag_genero = True
                elif minimo_valor > heroe[clave]:
                    minimo_valor = heroe[clave]
                    minimo_heroe = heroe

    return minimo_heroe

# 3.2
def calcular_max_genero(listado_heroes: list, clave: str, genero:str):
    '''
    recibe: la lista de héroes y una key, la cual representará el dato a evaluar
    y ademas el genero.
    retorna: dependiendo el genero el o la mas alto/a en la lista.
    '''
    stark_normalizar_datos(listado_heroes)
    flag_genero = False
    if clave in ["altura", "peso", "fuerza"]:
        for heroe in listado_heroes:
            if heroe["genero"] == genero:
                if flag_genero == False:
                    maximo_valor = heroe[clave]
                    maximo_heroe = heroe
                    flag_genero = True
                elif maximo_valor < heroe[clave]:
                    maximo_valor = heroe[clave]
                    maximo_heroe = heroe

    return maximo_heroe

# 3.3
def calcular_max_min_dato_genero(heroes:list, tipo_calculo:str, dato:str, genero:str):
    '''
    RECIBE: la lista de héroes, el tipo de calculo: 'maximo'
    o 'minimo' y un string que representa la key del dato a calcular y ademas el genero.
    RETORNA: al herore que cumpla con las condiciones.
    '''
    stark_normalizar_datos(heroes)
    if tipo_calculo == "maximo":
        return calcular_max_genero(heroes, dato, genero)
    elif tipo_calculo == "minimo":
        return calcular_min_genero(heroes, dato, genero)
    else:
        return -1
    
# 3.4
def stark_calcular_imprimir_guardar_heroe_genero(personajes:list, calculo:str, dato:str, genero:str)->str:
    '''
    recibe como parametro una lista y 3 strings (calculo, dato y genero)
    '''
    personaje = calcular_max_min_dato_genero(personajes,calculo, dato, genero)
    if calculo == 'maximo':
        mensaje = 'Mayor {0}: {1}'.format(dato, obtener_nombre_y_dato(personaje, dato))
    else:
        mensaje = 'Menor {0}: {1}'.format(dato, obtener_nombre_y_dato(personaje, dato))
        
    ruta = './DESAFIO_STALK/heroes_{0}_{1}_{2}.csv'.format(calculo, dato, genero)
    return guardar_archivo(ruta, mensaje)

# ----------------
# EJERCICIOS 4
# 4.1
def sumar_dato_heroe_genero(heroes: list[dict], clave: str, genero: str)->int:
    '''
    Suma el valor de la clave de los héroes o heroínas que cumplen las condiciones de género.
    
    Args:
        heroes (list): Lista de héroes.
        clave (str): Clave del dato a sumar.
        genero (str): Género a evaluar.
    
    Return:
        int: Suma del valor de la clave de los héroes o heroínas que cumplen las condiciones, o -1 en caso de que no se cumplan las validaciones.
    '''
    suma = 0
    for heroe in heroes:
        if not isinstance(heroe, dict) and not heroe and not heroe["genero"] == genero:
            return "diccionario vacio"
        else:
            dato_a_sumar = float(heroe[clave])
            suma += dato_a_sumar

    return suma

# 4.2
def cantidad_heroes_genero(heroes:list, genero:str)->int:
    '''
    Iterar y sumar la cantidad de heroes o heroinas que cumplan con la condicion del genero pasada por parametro
    
    Args:
        heroes (list): lista de heroes
        genero (str): genero a buscar
        
    Return:
        int: suma de la cantidad de heroes o heroinas que cumplan con la condicion del genero.
    '''
    suma = 0
    
    for heroe in heroes:
        if es_genero(heroe, genero):
            suma +=1
    
    return suma

# 4.3
def calcular_promedio_genero(heroes:list, clave:str, genero:str)->float:
    '''
    Calcula el promedio del valor de una clave específica para los héroes o heroínas de un género dado.

    Args:
        heroes (list): Lista de diccionarios que representan a los héroes.
        clave (str): Clave del diccionario que se utilizará para calcular el promedio.
        genero (str): Género a considerar para seleccionar los héroes o heroínas.

    Return:
        float: El promedio del valor de la clave para los héroes o heroínas del género especificado.
    '''
    suma = sumar_dato_heroe_genero(heroes, clave, genero)
    cantidad = cantidad_heroes_genero(heroes, genero)
    promedio = dividir(suma, cantidad)
    
    return promedio
    
# 4.4 (basado en el 5.2 del SD_02)
def stark_calcular_imprimir_guardar_promedio_altura_genero(heroes:list[dict], genero:str):
    if not heroes:
        mensaje = "lista vacia"
    else:
        promedio = calcular_promedio_genero(heroes, "altura", genero)
        mensaje = "Altura promedio género {0} : {1}".format(genero, promedio)
    
    imprimir_dato(mensaje)
    
    ruta = './DESAFIO_STALK/heroes_promedio_altura_{0}.csv'.format(genero)
    
    datos = 'genero: {0}, promedio_altura: {1}'.format(genero, promedio)
    if guardar_archivo(ruta, datos):
        return True
    else :
        return False
    
# ----------------
# EJERCICIOS 5


# 1.3
def stark_marvel_app_5(lista_heroes: list):
    '''
    RECIBE: la lista de héroes
    REALIZA: la ejecución principal de nuestro programa
    INFORMAR: por consola en caso de seleccionar una opcion incorrecta y
    volver a pedir el dato al usuario 
    '''

    while True:
        # Mostrar menú de opciones
        opcion = stark_menu_principal_desafio_5()

        match(opcion):

            case "a":
                print("ingrese a la opcion a")

            case "b":
                print("opcion B ingresada")

            case _:
                print("opcion no valida")


stark_marvel_app_5(lista_personajes)