edad = int(input("Que edad tenes?"))

if edad < 12:
    print ("Eres niño")
elif edad >= 12 and edad <= 17:
    print ("Eres adolescente")
else:
    print("Eres adulto")