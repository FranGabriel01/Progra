'''
Crear una función que recibe una lista de diccionarios con información de películas (título, género, director) y devuelve un diccionario con la cantidad de películas por género.
'''

lista_peliculas = [
    {
        'titulo' : 'Madagascar I',
        'genero' : 'Comedia',
        'director' : 'Andry Rajoelina',
    },
    {
        'titulo' : 'Madagascar II',
        'genero' : 'Comedia',
        'director' : 'Andry Rajoelina',
    },
    {
        'titulo' : 'Nemo',
        'genero' : 'Comedia',
        'director' : 'Andrew Stanton',
    },
    {
        'titulo' : 'Matrix',
        'genero' : 'Ciencia ficcion',
        'director' : 'Lana Wachowski',
    },
    {
        'titulo' : 'Matrix II',
        'genero' : 'Ciencia ficcion',
        'director' : 'Lana Wachowski',
    }
]

def mostrar_cantidad_genero (lista_peli):

    dic_contador_genero = {}

    for pelicula in lista_peliculas:
        texto_genero = pelicula['genero']

        if texto_genero in dic_contador_genero:
            dic_contador_genero[texto_genero] += 1
        else:
            dic_contador_genero[texto_genero] = 1
        
    print (dic_contador_genero)
        

resultado = mostrar_cantidad_genero(lista_peliculas)