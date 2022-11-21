import pickle

class usuario:
    name = None
    lastName = None
    age = None
    country = None

    def __int__(self, name, lastName, age, country):
        self.name = None
        self.lastName = None
        self.age = None
        self.country = None

    def putU(self):
        self.name = str(input("ingrese el nombre: "))
        self.lastName = str(input("ingrese el apellido: "))
        self.age = int(input("ingrese el edad: "))
        self.country = str(input("ingrese pais: "))
        return self.name, self.lastName, self.age, self.country
    def __str__(self):
        print(self.name, self.lastName, self.age, self.lastName)

u1 = usuario().putU()


f= open('usuarios.txt', 'w')
f.write(str(u1))
f.close()
f= open('usuarios.txt', 'r')
u1 = f.read()
print(u1)