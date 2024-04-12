lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lista_numeros:
    for digito in str(i):
        if i % int(digito) == 0:
            print (i)
    