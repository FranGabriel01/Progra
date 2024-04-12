edad = int(input("Ingrese su edad"))
if edad > 0:
    if edad >= 13 and edad <= 17:
        print("Eres adolescente")
    elif edad >= 18 and edad <= 64:
        print("Eres adulto")
    elif edad >= 65:
        print("Eres adulto mayor")