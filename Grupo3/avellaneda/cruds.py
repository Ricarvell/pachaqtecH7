import conexion
import querys
from time import sleep

conn = conexion.conexionBDD(1)
query = querys.Querys()



#  █████  ██      ██    ██ ███    ███ ███    ██  ██████  
# ██   ██ ██      ██    ██ ████  ████ ████   ██ ██    ██ 
# ███████ ██      ██    ██ ██ ████ ██ ██ ██  ██ ██    ██ 
# ██   ██ ██      ██    ██ ██  ██  ██ ██  ██ ██ ██    ██ 
# ██   ██ ███████  ██████  ██      ██ ██   ████  ██████ 

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

#Buscar Alumno
def buscarAlumno():
    try:
        idAlumno = int(input("Ingrese el id del alumno que desea buscar:\n"))
        consulta = query.BuscarAlumno(idAlumno)
        resconn = conn.consultarBDD(consulta)
        for tplAlumno in resconn:
            print(tplAlumno[0], tplAlumno[1], tplAlumno[2], tplAlumno[3], tplAlumno[4])
        return idAlumno
    except Exception as e:
        print("Debe ingresar un numero")
        print(e)
        sleep(2)

#Modificar Alumno   
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

#Eliminar Alumno
def eliminarAlumno(idAlumno):
    consulta = query.EliminarAlumno(idAlumno)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print(f"Se elimino al alumno {idAlumno}")
    else:
        print("No fue posible eliminar al alumno")
    input("Desea continuar")



# ██████   ██████   ██████ ███████ ███    ██ ████████ ███████ ███████ 
# ██   ██ ██    ██ ██      ██      ████   ██    ██    ██      ██      
# ██   ██ ██    ██ ██      █████   ██ ██  ██    ██    █████   ███████ 
# ██   ██ ██    ██ ██      ██      ██  ██ ██    ██    ██           ██ 
# ██████   ██████   ██████ ███████ ██   ████    ██    ███████ ███████ 


#Ingresar Docente
def ingresarDocente():
    #Datos del docente
    nombre = input("Ingrese Nombre del Docente:\n")
    dni = input(f"Ingrese Dni del Docente {nombre}:\n")
    correo = input(f"Ingrese Correo del Docente {nombre}:\n")
    fechanac = input(f"Ingrese Fecha de Nacimiento del Docente {nombre}:\n")
    try:
        consulta = query.InsertDocente(nombre, dni, correo, fechanac)
        resconn = conn.ejecutarBDD(consulta)
        if resconn:
            print("Se agrego correctamente")
        else:
            print("No fue posible agregar al docente")
        input("Desea continuar")
    except ValueError as e:
        print(e)
    
#Listar Docente
def listarDocente():
    consulta = query.ListarAllDocente()
    resconn = conn.consultarBDD(consulta)
    for tplDocente in resconn:
        print(tplDocente[0], tplDocente[1], tplDocente[2], tplDocente[3], tplDocente[4])

#Buscar Docente
def buscarDocente():
    try:
        idDocente = int(input("Ingrese el id del docente que desea buscar:\n"))
        consulta = query.BuscarDocente(idDocente)
        resconn = conn.consultarBDD(consulta)
        for tplDocente in resconn:
            print(tplDocente[0], tplDocente[1], tplDocente[2], tplDocente[3], tplDocente[4])
        return idDocente
    except Exception as e:
        print("Debe ingresar un numero")
        print(e)
        sleep(2)

#Modificar Docente  
def modificarDocente(idDocente):
    Nombre = input("Ingrese el nuevo nombre del docente:\n")
    Dni = input(f"Ingrese el nuevo Dni del docente {Nombre}:\n")
    Correo = input(f"Ingrese el nuevo correo del docente {Nombre}:\n")
    FechaNac = input(f"Ingrese la nueva fecha de nacimiento del docente {Nombre}:\n")
    consulta = query.ModificarDocente(Nombre, Dni, Correo, FechaNac, idDocente)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print("Se modifico correctamente")
    else:
        print("No fue posible modificar al alumno")
    input("Desea continuar")

#Eliminar Docente
def eliminarDocente(idDocente):
    consulta = query.EliminarDocente(idDocente)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print(f"Se elimino al docente {idDocente}")
    else:
        print("No fue posible eliminar al docente")
    input("Desea continuar")



# ███████  █████  ██       ██████   ██████  ███    ██ ███████ ███████ 
# ██      ██   ██ ██      ██    ██ ██    ██ ████   ██ ██      ██      
# ███████ ███████ ██      ██    ██ ██    ██ ██ ██  ██ █████   ███████ 
#      ██ ██   ██ ██      ██    ██ ██    ██ ██  ██ ██ ██           ██ 
# ███████ ██   ██ ███████  ██████   ██████  ██   ████ ███████ ███████


#Ingresar Salon
def ingresarSalon():
    #Datos del Salon
    nombre = input("Ingrese Nombre del Salon:\n")
    try:
        consulta = query.InsertSalon(nombre)
        resconn = conn.ejecutarBDD(consulta)
        if resconn:
            print("Se agrego correctamente")
        else:
            print("No fue posible agregar al salon")
        input("Desea continuar")
    except ValueError as e:
        print(e)
    
#Listar Salones
def listarSalon():
    consulta = query.ListarAllSalones()
    resconn = conn.consultarBDD(consulta)
    for tplSalon in resconn:
        print(tplSalon[0], tplSalon[1])

#Buscar Salon
def buscarSalon():
    try:
        idSalon = int(input("Ingrese el id del salon que desea buscar:\n"))
        consulta = query.BuscarSalon(idSalon)
        resconn = conn.consultarBDD(consulta)
        for tplSalon in resconn:
            print(tplSalon[0], tplSalon[1])
        return idSalon
    except Exception as e:
        print("Debe ingresar un numero")
        print(e)
        sleep(2)

#Modificar Salon   
def modificarSalon(idSalon):
    Nombre = input("Ingrese el nuevo nombre del salon:\n")
    consulta = query.ModificarSalon(Nombre, idSalon)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print("Se modifico correctamente")
    else:
        print("No fue posible modificar el Salon")
    input("Desea continuar")

#Eliminar Salon
def eliminarSalon(idSalon):
    consulta = query.EliminarSalon(idSalon)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print(f"Se elimino al salon {idSalon}")
    else:
        print("No fue posible eliminar al salon")
    input("Desea continuar")



#  ██████ ██    ██ ██████  ███████  ██████  ███████ 
# ██      ██    ██ ██   ██ ██      ██    ██ ██      
# ██      ██    ██ ██████  ███████ ██    ██ ███████ 
# ██      ██    ██ ██   ██      ██ ██    ██      ██ 
#  ██████  ██████  ██   ██ ███████  ██████  ███████


#Ingresar Curso
def ingresarCurso():
    #Datos del Curso
    nombre = input("Ingrese Nombre del Curso:\n")
    try:
        consulta = query.InsertCurso(nombre)
        resconn = conn.ejecutarBDD(consulta)
        if resconn:
            print("Se agrego correctamente")
        else:
            print("No fue posible agregar curso")
        input("Desea continuar")
    except ValueError as e:
        print(e)
    
#Listar Cursos
def listarCurso():
    consulta = query.ListarAllCursos()
    resconn = conn.consultarBDD(consulta)
    for tplCurso in resconn:
        print(tplCurso[0], tplCurso[1])

#Buscar Curso
def buscarCurso():
    try:
        idCurso = int(input("Ingrese el id del curso que desea buscar:\n"))
        consulta = query.BuscarCurso(idCurso)
        resconn = conn.consultarBDD(consulta)
        for tplCurso in resconn:
            print(tplCurso[0], tplCurso[1])
        return idCurso
    except Exception as e:
        print("Debe ingresar un numero")
        print(e)
        sleep(2)

#Modificar Salon   
def modificarCurso(idCurso):
    Nombre = input("Ingrese el nuevo nombre del curso:\n")
    consulta = query.ModificarCurso(Nombre, idCurso)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print("Se modifico correctamente")
    else:
        print("No fue posible modificar el curso")
    input("Desea continuar")

#Eliminar Curso
def eliminarCurso(idCurso):
    consulta = query.EliminarCurso(idCurso)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print(f"Se elimino el curso {idCurso}")
    else:
        print("No fue posible eliminar el curso")
    input("Desea continuar")



# ██████  ███████ ██████  ██  ██████  ██████   ██████      ███████ ███████  ██████  ██████  ██       █████  ██████  
# ██   ██ ██      ██   ██ ██ ██    ██ ██   ██ ██    ██     ██      ██      ██      ██    ██ ██      ██   ██ ██   ██ 
# ██████  █████   ██████  ██ ██    ██ ██   ██ ██    ██     █████   ███████ ██      ██    ██ ██      ███████ ██████  
# ██      ██      ██   ██ ██ ██    ██ ██   ██ ██    ██     ██           ██ ██      ██    ██ ██      ██   ██ ██   ██ 
# ██      ███████ ██   ██ ██  ██████  ██████   ██████      ███████ ███████  ██████  ██████  ███████ ██   ██ ██   ██ 


#Ingresar Periodo
def ingresarPeriodo():
    #Datos del Periodo
    nombre = input("Ingrese Nombre del Periodo:\n")
    try:
        consulta = query.InsertPeriodo(nombre)
        resconn = conn.ejecutarBDD(consulta)
        if resconn:
            print("Se agrego correctamente")
        else:
            print("No fue posible agregar el periodo escolar")
        input("Desea continuar")
    except ValueError as e:
        print(e)
    
#Listar Periodos
def listarPeriodos():
    consulta = query.ListarAllPeriodos()
    resconn = conn.consultarBDD(consulta)
    for tplPeriodo in resconn:
        print(tplPeriodo[0], tplPeriodo[1])

#Buscar Periodo
def buscarPeriodo():
    try:
        idPeriodo = int(input("Ingrese el id del periodo que desea buscar:\n"))
        consulta = query.BuscarPeriodo(idPeriodo)
        resconn = conn.consultarBDD(consulta)
        for tplPeriodo in resconn:
            print(tplPeriodo[0], tplPeriodo[1])
        return idPeriodo
    except Exception as e:
        print("Debe ingresar un numero")
        print(e)
        sleep(2)

#Modificar Periodo   
def modificarPeriodo(idPeriodo):
    Nombre = input("Ingrese el nuevo nombre del periodo escolar:\n")
    consulta = query.ModificarPeriodo(Nombre, idPeriodo)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print("Se modifico correctamente")
    else:
        print("No fue posible modificar el periodo")
    input("Desea continuar")

#Eliminar Periodo
def eliminarPeriodo(idPeriodo):
    consulta = query.EliminarPeriodo(idPeriodo)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print(f"Se elimino el periodo {idPeriodo}")
    else:
        print("No fue posible eliminar el periodo")
    input("Desea continuar")



# ███    ██  ██████  ████████  █████  ███████ 
# ████   ██ ██    ██    ██    ██   ██ ██      
# ██ ██  ██ ██    ██    ██    ███████ ███████ 
# ██  ██ ██ ██    ██    ██    ██   ██      ██ 
# ██   ████  ██████     ██    ██   ██ ███████ 


#Ingresar Nota
def ingresarNota():
    #Datos de la nota
    nombre = input("Ingrese Nota del Curso:\n")
    try:
        consulta = query.InsertNota(nombre)
        resconn = conn.ejecutarBDD(consulta)
        if resconn:
            print("Se agrego correctamente")
        else:
            print("No fue posible agregar la nota al curso")
        input("Desea continuar")
    except ValueError as e:
        print(e)
    
#Listar Notas
def listarNota():
    consulta = query.ListarAllNotas()
    resconn = conn.consultarBDD(consulta)
    for tplNota in resconn:
        print(tplNota[0])

#Buscar Nota
def buscarNota():
    try:
        idNota = int(input("Ingrese la nota del curso que desea buscar:\n"))
        consulta = query.BuscarNota(idNota)
        resconn = conn.consultarBDD(consulta)
        for tplNota in resconn:
            print(tplNota[0])
        return idNota
    except Exception as e:
        print("Debe ingresar un numero")
        print(e)
        sleep(2)

#Modificar Nota   
def modificarNota(Nota):
    Nombre = input("Ingrese la nueva nota del curso:\n")
    consulta = query.ModificarNota(Nombre, Nota)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print("Se modifico correctamente")
    else:
        print("No fue posible modificar la nota")
    input("Desea continuar")

#Eliminar Nota
def eliminarNota(Nota):
    consulta = query.EliminarNota(Nota)
    resconn = conn.ejecutarBDD(consulta)
    if resconn:
        print(f"Se elimino la nota {Nota}")
    else:
        print("No fue posible eliminar la nota")
    input("Desea continuar")