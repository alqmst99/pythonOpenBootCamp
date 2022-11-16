print("CALCULADORA DE MASA CORPORAL")
print("")
print()
peso= float(input("ingrese su peso: "))

altura= float(input("ingrese su altura: "))

masa_corporal= peso // altura**2
print("su peso es " + str(peso) + " kg")

print("su altura es " + str(altura) + " m")
print("su índice de masa es " + str(masa_corporal) +"")