#variables inmutables (no se cambian)
a="hola mundo!"
print(a)
a=int(2)
print (a)
type (a)
id(a)
variable=('a', 2, 'b')
print(variable)


#variables mutables
lista=[1, 2, 3, 4]
print(lista)
lista[0] = 't'
print(lista)
lista.remove(2)
print(lista)
lista.append(2)
print(lista)
d= lista.pop(3)
print(d)
print(lista)
dicc = {'name' : 'nahuel', 'code': 55}
print(dicc)
conjunto = {1, 2, 3, 5, 4, 6, 5, 8, 2, 4, 5}
print(conjunto)
conj = {11, 8, 9, 5, 6, 0, 17}
print(conj|conjunto)
print(conjunto&conj)
print(conj-conjunto)
print(conj^conjunto)
#metodos y operadores
print('METODOS STRING')
texto= "hola, soy un texto largo"
print(texto.capitalize())
print(texto.title())
print(texto.upper())
print(texto.replace('a', 'o'))
print(texto.find('largo'))
print(texto.split(','))
print(texto.replace(',', '').lower().split())
print('_'.join(texto))
print(''.join(texto))
#operadores
