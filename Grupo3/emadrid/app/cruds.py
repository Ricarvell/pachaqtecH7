import conexion
import querys
from time import sleep

#Empleado -- Alumno
def ingresarAlumno():
    nombre = input("Ingrese Nombre del Alumno:\n")
    apellido = input("Ingrese Apellido del Alumno:\n")
    correo = input("Ingrese Correo del Alumno:\n")
    fechanac = input("Ingrese Fecha Nacimiento del Alumno:\n")
    conn = conexion.conexionBDD(1)
    query = querys.Querys()
    consulta = query.InsertAlumno(nombre, apellido, correo, fechanac)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print("Añadido")
    else:
        print("Fallaste")
    input("Desea continuar")

#Metodo Listar Alumnos
def listarAlumno():
    conn = conexion.conexionBDD(1)
    query = querys.Querys()
    consulta = query.ListarAllAlumno()
    resconn = conn.consultarBDD(consulta)
    #Imprime Cabecera
    print("ID\t", "Nombres\t\t", "Apellidos\t\t\t", "Correo\t\t\t", "Fecha Nacimiento""\t")
    #Mostrar Lista de Alumnos
    for tplAlumno in resconn:
        print(tplAlumno[0],"\t", tplAlumno[1],"\t\t", tplAlumno[2],"\t\t\t", tplAlumno[3],"t\t\t", tplAlumno[4])

#Metodo Buscar Alumno por ID
def buscarAlumno():
    try:
        idAlumno = int(input("Ingrese el ID del Alumno que desea modificar:\n"))
        conn = conexion.conexionBDD(1)
        query = querys.Querys()
        consulta = query.BuscarAlumno(idAlumno)
        resconn = conn.consultarBDD(consulta)
        for tplAlumno in resconn:
            print(tplAlumno[0], tplAlumno[1], tplAlumno[2], tplAlumno[3], tplAlumno[4])
        return idAlumno
    except Exception as e:
        print("Debe ingresar un numero")
        print(e)
        sleep(2)

####INICIO METODOS DOCENTE####
#Metodo Ingresar Nuevo Docente
def ingresarDocente():
    nombre = input("Ingrese Nombre del Docente:\n")
    dni = input("Ingrese DNI del Docente:\n")
    correo = input("Ingrese Correo del Docente:\n")
    fechanac = input("Ingrese Fecha de Nacimiento del Docente:\n")
    conn = conexion.conexionBDD(1)
    query = querys.Querys()
    consulta = query.InsertDocente(nombre, dni, correo, fechanac)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print("Añadido")
    else:
        print("Fallaste")
    input("Desea continuar")

#Metodo Listar Docentes
def listarDocente():
    conn = conexion.conexionBDD(1)
    query = querys.Querys()
    consulta = query.ListarAllDocentes()
    resconn = conn.consultarBDD(consulta)
    #Imprime Cabecera
    print("ID\t", "Nombre\t\t", "DNI\t\t", "Correo\t\t\t", "Fecha Nacimiento""\t")
    #Mostrar Lista de Docentes
    for tplDocente in resconn:
        print(tplDocente[0],"\t", tplDocente[1],"\t", tplDocente[2],"\t", tplDocente[3],"\t\t", tplDocente[4])

#Metodo Buscar Docentes por ID
def buscarDocente():
    try:
        idDocente = int(input("Ingrese el ID del Docente que desea modificar:\n"))
        conn = conexion.conexionBDD(1)
        query = querys.Querys()
        consulta = query.BuscarDocente(idDocente)
        resconn = conn.consultarBDD(consulta)
        for tplDocente in resconn:
            print(tplDocente[0], tplDocente[1], tplDocente[2], tplDocente[3], tplDocente[4])
        return idDocente
    except Exception as e:
        print("Debe ingresar un numero")
        print(e)
        sleep(2)

#Metodo Modifica Docente
def modificarDocente(idDocente):
    Nombre = input("Ingrese el nuevo nombre del Docente:\n")
    Dni = input(f"Ingrese el nuevo DNI del Docente {Nombre}:\n")
    Correo = input(f"Ingrese el nuevo correo del Docente {Nombre}:\n")
    FechaNac = input(f"Ingrese la nueva fecha de nacimiento del Docente {Nombre}:\n")
    conn = conexion.conexionBDD(1)
    query = querys.Querys()
    consulta = query.ModificarDocente(Nombre, Dni, Correo, FechaNac, idDocente)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
       print("Se modifico correctamente")
    else:
       print("No fue posible modificar al Docente")
       input("Desea continuar")

#Metodo Elimina Docente
def eliminaDocente(idDocente):
    conn = conexion.conexionBDD(1)
    query = querys.Querys()
    connsulta = query.EliminarDocente(str(idDocente))
    resconn = conn.ejecutarBDD(connsulta)
    if resconn:
        print(f"Se elimino Docente {idDocente}")
    else:
        print("Fallaste")
        print("No fue posible eliminar al Docente")
    input("Desea continuar")
####FIN METODOS DOCENTE####

####INICIO METODOS PERIODO ESCOLAR####
#Metodo Ingresar Nuevo Periodo Escolar
def ingresarPeriodoEscolar():
    nombre = input("Ingrese Nombre del Periodo Escolar:\n")
    conn = conexion.conexionBDD(1)
    query = querys.Querys()
    consulta = query.InsertPeriodoEscolar(nombre)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print("Añadido")
    else:
        print("Fallaste")
    input("Desea continuar")

#Metodo Listar Docentes
def listarPeriodoEscolar():
    conn = conexion.conexionBDD(1)
    query = querys.Querys()
    consulta = query.ListarAllPeriodoEscolar()
    resconn = conn.consultarBDD(consulta)
    #Imprime Cabecera
    print("ID\t", "Nombre\t")
    #Mostrar Lista de Periodo Escolar
    for tplPeriodoEscolar in resconn:
        print(tplPeriodoEscolar[0],"\t", tplPeriodoEscolar[1])

#Metodo Buscar PeriodoEscolar por ID
def buscarPeriodoEscolar():
    try:
        idPeriodoEscolar = int(input("Ingrese el ID del PeriodoEscolar que desea Modificar/Eliminar:\n"))
        conn = conexion.conexionBDD(1)
        query = querys.Querys()
        consulta = query.BuscarPeriodoEscolar(idPeriodoEscolar)
        resconn = conn.consultarBDD(consulta)
        for tplPeriodoEscolar in resconn:
            print(tplPeriodoEscolar[0], tplPeriodoEscolar[1])
        return idPeriodoEscolar
    except Exception as e:
        print("Debe ingresar un numero")
        print(e)
        sleep(2)

#Metodo Modifica Periodo Escolar
def modificarPeriodoEscolar(idPeriodoEscolar):
    Nombre = input("Ingrese el nuevo nombre del Docente:\n")
    conn = conexion.conexionBDD(1)
    query = querys.Querys()
    consulta = query.ModificarPeriodoEscolar(Nombre, idPeriodoEscolar)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
       print("Se modifico correctamente")
    else:
       print("No fue posible modificar al Docente")
       input("Desea continuar")

#Metodo Elimina Periodo Escolar
def eliminaPeriodoEscolar(idPeriodoEscolar):
    conn = conexion.conexionBDD(1)
    query = querys.Querys()
    connsulta = query.EliminarPeriodoEscolar(str(idPeriodoEscolar))
    resconn = conn.ejecutarBDD(connsulta)
    if resconn:
        print(f"Se elimino Periodo Escolar {idPeriodoEscolar}")
    else:
        print("Fallaste")
        print("No fue posible eliminar al Periodo Escolar")
    input("Desea continuar")
####FIN METODOS PERIODO ESCOLAR####

####INICIO METODOS MATRICULA####
#Metodo Ingresar Nueva Matricula
def ingresarMatricula():
    listarAlumno()
    idAlumno = input("Ingrese ID del Alumno a Matricular:\n")
    listarPeriodoEscolar()
    idPeriodoEscolar = input("Ingrese ID del Periodo Escolar a Matricular:\n")
    conn = conexion.conexionBDD(1)
    query = querys.Querys()
    consulta = query.InsertMatricula(idAlumno, idPeriodoEscolar)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print("Alumno Matriculado")
    else:
        print("Fallaste")
    input("Desea continuar")

####FIN METODOS MATRICULA####