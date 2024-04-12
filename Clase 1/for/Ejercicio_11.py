numero = 20

for numeros_primos in range(2, numero+1):
    es_primo = True #BANDERA si asumimos que el numero es PRIMO
    for verificacion_primo in range (2, numeros_primos): #Aca verificamos si el numero es primo
        if numeros_primos % verificacion_primo == 0:
            es_primo = False
            break #El break sirve para que no siga verificando si es primo o no cuando ya no se cumple la condicion
    if es_primo:
        print (numeros_primos)