import operadores

o=int(input("ingrese que operacion desea, 1(suma), 2(resta),3 (multiplicacion), 4 (divicion): "))
a=int(input("ingrese el primer valor: "))
b=int(input("ingrese el segundo valor: "))
def main():
    s= operadores.suma(a,b)
    r=operadores.resta(a,b)
    m=operadores.multi(a,b)
    d=operadores.div(a,b)
    if o==1:
         return s
    elif o==2:
        return r
    elif o==3:
        return m
    elif o==4:
        return d
    else:
        print("ingrese una obcion valida")
if __name__ == '__main__':
    main()
print("el resulta de  la operacion es :", main())