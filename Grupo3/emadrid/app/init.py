import utils
import cruds
from time import sleep

__log = utils.log("Principal")
__log.info("Inicio del sistema")

def mantenimientoEmpleado():
    tplEmpleado = ("1. Alumno", "2. Docente", "3. Cursos", "4. Salones", 
                    "5. Periodo Escolar", "6. Matricula", "7. Regresar")
    menuEmpleado = utils.Menu("Menu Empleado", tplEmpleado)
    resmenuEmpleado = menuEmpleado.MostrarMenu()

    stopMenuEmpleado = True
    while stopMenuEmpleado:
        if resmenuEmpleado == 1:
            __log.info("Menu Empleado --> Alumno")
            stopMenuAlumno = True
            while stopMenuAlumno:
                tplAlumno = ("1. Agregar Alumno", "2.")
                menuAlumno = utils.Menu("Menu Alumno", tplAlumno)
                resmenuAlumno = menuAlumno.MostrarMenu()
                if resmenuAlumno == 1:
                    cruds.ingresarAlumno()
                elif resmenuAlumno == 2:
                    pass               
                else:
                    pass
        elif resmenuEmpleado == 2:
             __log.info("Menu Empleado --> Docente")
             stopMenuDocente = True
             while stopMenuDocente:
                #Sub Menu CRUD Docente 
                tplDocente = ("1. Agregar Docente", "2. Listar Docente", "3. Actualizar Docente", "4. Eliminar Docente", "5. Regresar")
                menuDocente = utils.Menu("Menu Docente", tplDocente)
                resmenuDocente = menuDocente.MostrarMenu()
                if resmenuDocente == 1:
                    cruds.ingresarDocente()
                elif resmenuDocente == 2:
                    cruds.listarDocente()    
                    sleep(5)
                elif resmenuDocente == 3:
                    cruds.listarDocente()
                    idDocente = cruds.buscarDocente()
                    cruds.modificarDocente(idDocente)
                    sleep(5)
                elif resmenuDocente == 4:
                    __log.error("Menu eliminar")
                    cruds.listarDocente()
                    idDocente = cruds.buscarDocente()
                    #sleep(5)
                    cruds.eliminaDocente(idDocente)
                    sleep(5)
                else:
                    pass
        elif resmenuEmpleado == 6:
             __log.info("Menu Empleado --> Matricula")
             stopMenuMatricula = True
             while stopMenuMatricula:
                #Sub Menu CRUD Matricula 
                tplMatricula = ("1. Registrar Matricula", "2. Listar Matricula", "3. Actualizar Matricula", "4. Eliminar Matricula", "5. Regresar")
                menuMatricula = utils.Menu("Menu Matricula", tplMatricula)
                resmenuMatricula = menuMatricula.MostrarMenu()
                if resmenuMatricula == 1:
                    cruds.ingresarMatricula()
                elif resmenuMatricula == 2:
                    cruds.listarDocente()    
                    sleep(5)
                elif resmenuMatricula == 3:
                    cruds.listarDocente()
                    idDocente = cruds.buscarDocente()
                    cruds.modificarDocente(idDocente)
                    sleep(5)
                elif resmenuMatricula == 4:
                    __log.error("Menu eliminar")
                    cruds.listarDocente()
                    idDocente = cruds.buscarDocente()
                    #sleep(5)
                    cruds.eliminaDocente(idDocente)
                    sleep(5)
                else:
                    pass           
        else:
            pass
            
stopMenuInicio = True
while stopMenuInicio:
    dicMenuInicio = ("1. Empleado", "2. Alumno", "3. Docente")
    menuInicio = utils.Menu("Menu Inicio", dicMenuInicio)
    resMenuInicio = menuInicio.MostrarMenu()
    if(resMenuInicio == 1):
        __log.debug("Mostramos el Menu Empleado")
        mantenimientoEmpleado()
        #cargarObjetos()

    elif(resMenuInicio == 2):
        __log.debug("Mostramos el Menu Alumno")
        print("Alumno") 

    elif(resMenuInicio == 3):
        __log.debug("Mostramos el Menu Docente")
        print("Docente")

    else:
        __log.debug("Volvemos a mostrar menu")
        utils.Salir()
