from _functools import reduce

lista = []

for x in range(10):
    b = 0
    b += 1
    a = int(input(f'ingrese valor {b} : '))
    lista.append(a)
listas = filter(lambda x: x % 2, lista)
print(list(listas))


def suma(a, b):
    return a + b


suma = reduce(suma, lista)
print(f'el resultado es : {suma}')