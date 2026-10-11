temperatura = float(input("Ingrese temperatura:"))
grado = input("Es Farenheit(F) o Celsius(C)").upper()

if grado == "F":
    print((temperatura - 32) * 5 / 9)
elif grado == "C":
    print((temperatura * (9 / 5)) + 32)
else:
    print("Formato incorrecto, intente otra vez")
