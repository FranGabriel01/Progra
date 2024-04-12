dict_alumno = {"legajo": 205664, "nombre": "Juan", "apellido": "Lopez"}

# print("El legajo es {0} el nombre es {1} y el apellido es {2}".format(
#     dict_alumno["legajo"], dict_alumno["nombre"], dict_alumno["apellido"]))

dict_alumno["cuit"] = "22-1233444-9" #se agrega un elemento al diccionario

claves = dict_alumno.keys()
print(claves)

# for clave in dict_alumno.keys():
#    print("La clave: {0} tiene el valor: {1}".format(clave,clave))

# for clave,valor in dict_alumno.items(): #.items te devuelve clave y valor
#     print("La clave: {0} tiene el valor: {1}".format(clave,valor))