from builtins import sorted

lista = []

for x in range(10):
    b = 0
    b += 1
    a = str(input(f'ingrese nombre de pais {b} :'))
    lista.append(a)

paises = set(lista)

print(sorted(list(paises)))
