print("es año biciesto?")
print()
anio = int(input("ingrese el año: "))
def anioBiciesto(fecha):
    valor= fecha%4
    if valor==0:
        print("el año", fecha,"es biciesto")
    else:
        print("el año", fecha, "no es biciesto es normal")

anioBiciesto(anio)