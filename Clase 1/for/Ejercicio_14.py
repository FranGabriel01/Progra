numero = 30

for numero_perfecto in range (1, numero+1):
    divisores_suma = 0
    for verificador in range (1, numero_perfecto):
        if numero_perfecto % verificador == 0:
            divisores_suma += verificador
    if divisores_suma == numero_perfecto:
        print(numero_perfecto)
