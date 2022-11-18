class vehiculo():
    color ="negro"
    ruedas = 4
    puertas =4


class coche():
    vehiculo = vehiculo()
    velocidad = 120
    cilindrada = 500


c = coche()
print("el color es, ", c.vehiculo.color)
print("tiene", c.vehiculo.ruedas," ruedas,")
print( "tiene ", c.vehiculo.puertas, "puertas,")
print("va a una velocidad de ", c.velocidad, "km/h,")
print("posee una cilindarade ", c.cilindrada, "rpm")