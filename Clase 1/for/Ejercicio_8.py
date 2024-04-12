numero = 10

acumulador_pares = 0

for n in range(0, numero+1, 2):
    if n % 2 == 0:
        acumulador_pares += n

print (acumulador_pares)