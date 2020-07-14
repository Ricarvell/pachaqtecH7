import conexion
import querys
from time import sleep

conn = conexion.conexionBDD(1)
query = querys.Querys()

#Empleado -- Alumno
#Ingresar Alumno
def ingresarAlumno():
    #Datos del alumno
    nombre = input("Ingrese Nombre del Alumno:\n")
    apellido = input(f"Ingrese Apellido del Alumno {nombre}:\n")
    correo = input(f"Ingrese Correo del Alumno {nombre}:\n")
    fechanac = input(f"Ingrese Fecha de Nacimiento del Alumno {nombre}:\n")
    try:
        consulta = query.InsertAlumno(nombre, apellido, correo, fechanac)
        resconn = conn.ejecutarBDD(consulta)
        if resconn:
            print("Se agrego correctamente")
        else:
            print("No fue posible agregar al alumno")
        input("Desea continuar")
    except ValueError as e:
        print(e)

    
#Listar Alumno
def listarAlumnos():
    consulta = query.ListarAllAlumno()
    resconn = conn.consultarBDD(consulta)
    for tplAlumno in resconn:
        print(tplAlumno[0], tplAlumno[1], tplAlumno[2], tplAlumno[3], tplAlumno[4])

def buscarAlumno():
    try:
        idAlumno = int(input("Ingrese el id del alumno que desea modificar:\n"))
        consulta = query.BuscarAlumno(idAlumno)
        resconn = conn.consultarBDD(consulta)
        for tplAlumno in resconn:
            print(tplAlumno[0], tplAlumno[1], tplAlumno[2], tplAlumno[3], tplAlumno[4])
        return idAlumno
    except Exception as e:
        print("Debe ingresar un numero")
        print(e)
        sleep(2)
    
def modificarAlumno(idAlumno):
    Nombre = input("Ingrese el nuevo nombre del alumno:\n")
    Apellido = input(f"Ingrese el nuevo apellido del alumno {Nombre}:\n")
    Correo = input(f"Ingrese el nuevo correo del alumno {Nombre}:\n")
    FechaNac = input(f"Ingrese la nueva fecha de nacimiento del alumno {Nombre}:\n")
    consulta = query.ModificarAlumno(Nombre, Apellido, Correo, FechaNac, idAlumno)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print("Se modifico correctamente")
    else:
        print("No fue posible modificar al alumno")
    input("Desea continuar")

def eliminarAlumno(idAlumno):
    connsulta = query.EliminarAlumno(idAlumno)
    resconn = conn.ejecutarBDD(connsulta)
    if resconn:
        print(f"Se elimino al alumno {idAlumno}")
    else:
        print("No fue posible eliminar al alumno")
    input("Desea continuar")