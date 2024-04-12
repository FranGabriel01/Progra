edad = int(input("Ingrese su edad"))

if edad >= 18:
    print("Eres mayor de edad")
elif edad < 18 and edad >= 13:
    print("Eres adolescente")
elif edad < 13 and edad > 0:
    print("Eres un niño") 