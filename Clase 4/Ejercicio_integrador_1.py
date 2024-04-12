'''
Gimnasio - Listas paralelas
Un gimnasio desea llevar el control de sus miembros. Cada miembro tiene un número de identificación, nombre, edad y tipo de membresía 
(por ejemplo, mensual o anual). La información se encuentra almacenada en cuatro listas paralelas: una lista con los números de 
identificación, otra lista con los nombres, una lista con las edades y una lista con los tipos de membresía.

Escriba un programa que permita a los usuarios realizar las siguientes operaciones:

Agregar un nuevo miembro: el programa debe pedir al usuario que ingrese el número de identificación, nombre, edad y tipo de membresía 
del nuevo miembro. La información debe ser agregada a las listas paralelas.


Mostrar toda la información de todos los miembros (número de identificación, nombre, edad y tipo de membresía).

Actualizar el tipo de membresía de un miembro: el programa debe pedir al usuario que ingrese el número de identificación del miembro y el 
nuevo tipo de membresía. El programa debe buscar el número de identificación en la lista de números de identificación y actualizar el tipo 
de membresía correspondiente en la lista de tipos de membresía. En caso de no encontrar al miembro informar con un mensaje de que el 
mismo no se encontró

Buscar información de un miembro: el programa debe pedir al usuario que ingrese el número de identificación del miembro. El programa debe 
buscar el número de identificación en la lista de números de identificación y mostrar el nombre, edad y tipo de membresía correspondientes 
en las listas de nombres, edades y tipos de membresía.


Calcular el promedio de edad de los miembros: el programa debe recorrer la lista de edades y calcular el promedio de edad de los miembros.

Buscar el miembro más joven y el más viejo: el programa debe buscar la edad máxima y mínima en la lista de edades y mostrar el nombre y 
número de identificación correspondientes en las listas de nombres y números de identificación.

El programa debe permitir al usuario realizar estas operaciones tantas veces como desee, hasta que decida salir del programa. El programa 
debe mostrar un menú de opciones para que el usuario pueda elegir la operación que desea realizar.
'''


lista_id = []
nombre_miembro = []
edad_miembro = []
tipo_membresia = []


while True:
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1. Agregar un nuevo miembro")
    print("2. Mostrar la informacion de todos los miembros")
    print("3. Actualizar el tipo de membresía de un miembro")
    print("4. Buscar información de un miembro")
    print("5. Calcular el promedio de edad de los miembros")
    print("6. Buscar el miembro más joven y el más viejo")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")

    #Agregar un nuevo miembro
    if opcion == "1":
        id = int(input("Ingresar numero identificacion: "))
        nombre = input("Ingrese nombre: ")
        edad = int(input("Ingrese edad: "))
        membresia = input ("Ingrese el tipo de membresia: ")
        lista_id.append(id)
        nombre_miembro.append(nombre)
        edad_miembro.append(edad)
        tipo_membresia.append(membresia)
        pass

    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
            for miembro in range(len(lista_id)):
                print("Numero id {0} nombre {1} edad {2} tipo membresia {3}".format(lista_id[miembro],nombre_miembro[miembro],
                                                                                    edad_miembro[miembro],tipo_membresia[miembro]))

     # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        id = int(input("Ingrese su id: "))
        indice_modificar = -1
        for i in range (len(lista_id)):
            if id == lista_id[i]:
                indice_modificar = i
                break
            else:
                print("Esa id no existe")
            
            if indice_modificar != -1:
                nueva_membresia = input("Ingrese la nueva membresia para: {0} ".format(nombre_miembro[indice_modificar]))
                tipo_membresia[indice_modificar] = nueva_membresia

            print("{0} - {1} - {2} - {3}".format(lista_id[indice_modificar],nombre_miembro[indice_modificar],edad_miembro[indice_modificar],
                                                 tipo_membresia[indice_modificar]))
            
    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        id = int(input("ingrese su id: "))
        for id in lista_id:
            if id == lista_id:
                print("{0} - {1} - {2} - {3}".format(lista_id[id],nombre_miembro[id],edad_miembro[id],tipo_membresia[id])) 

        pass

        # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        pass

    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        pass

    elif opcion == "0":
        break