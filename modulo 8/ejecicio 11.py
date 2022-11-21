import pickle


class vehiculo:
    color = None
    puertas = None
    velmax = None

    def __init__(self, color, puertas, velmax):
        self.color = color
        self.puertas = puertas
        self.velmax = velmax

    def __str__(self):
        print(f'la tiene un color {self.color}'); print(f' tiene {self.puertas} puertas');print(f' va a una velocidad maxima de {self.color} km/h')


color = str(input("ingrese color: "))
puertas = int(input("ingrese la cantidas de puertas: "))
velmax = int(input("ingrese la velociadad maxima: "))

v1 = vehiculo(color, puertas, velmax)

f = open('car.bat', 'wb')
pickle.dump(v1, f)
f.close()
print("vehiculo guardado")

f = open('car.bat', 'rb')
v1 = pickle.load(f)
f.close()
print(str(v1))
