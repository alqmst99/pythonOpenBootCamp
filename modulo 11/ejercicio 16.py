import sqlite3
op= int(input(" ingrese 1 para agregar alumnos o 0 para buscar alumnos: "))
i = 0
if op==1:
    for i in range(0, 7):
        a = str(input("ingrese nombre de alumno: "))
        b = str(input("ingrese apellido de alumno: "))
        c = int(input("ingrese clasificacion: "))
        conn = sqlite3.connect("alumno.db",)
        cursor = conn.cursor()
        cursor.execute("insert into alumno(name, lastname, calif) values (?,?,?)", (a, b, c))
        conn.commit()
        cursor.close()
        conn.close()
elif op==0:
    name = str(input("ingrese el nombre de alumno: "))


    conn = sqlite3.connect("alumnos.db")
    cursor = conn.cursor()
    cursor.execute(f"select * from alumno where name=?", (name,))
    datos = cursor.fetchall()
    print(datos)
    cursor.close()
    conn.close()
