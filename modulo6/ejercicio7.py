

nombre = str(input("ingrese el nombre del alumno y apellido: "))
nota = int(input("ingrese la calificación: "))


class alumno():
    _nombre = nombre
    _nota = nota

    def estado(_nota):
        if 6 <= nota <= 10:
            print("el alumno, ", nombre, "tiene una nota de ", nota,", alumno aprobado")
        else:
            print("el alumno, ", nombre, "tiene una nota de ", nota,", alumno desaprobado")


a = alumno()
a.estado()
