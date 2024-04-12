numero1 = int(input("Ingrese el primer numero"))
numero2 = int(input("Ingrese el segundo numero"))

if numero1 > 0 and numero2 > 0:
    print ("Ambos numeros son positivos")
elif numero1 < 0 and numero2 < 0:
    print("Ambos numeros son negativos")
elif numero1 < 0:
    print ("Numero uno es negativo y el segundo es positivo")
else:
    print ("Numero dos es negativo y el primero es positivo")