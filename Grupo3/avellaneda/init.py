import utils
import cruds
from time import sleep

__log = utils.log("Principal")
__log.info("Inicio del sistema")

#menu empleado
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
                tplAlumno = ("1. Agregar Alumno", "2. Listar Alumnos", "3. Modificar Alumno", "4. Eliminar Alumno")
                menuAlumno = utils.Menu("Menu Alumno", tplAlumno)
                resmenuAlumno = menuAlumno.MostrarMenu()
                #Agregar Alumno
                if resmenuAlumno == 1:
                    cruds.ingresarAlumno()
                    sleep(2)
                    __log.debug("Se ingresaron los datos del alumno")
                #Listar Alumno
                elif resmenuAlumno == 2:
                    cruds.listarAlumnos()
                    sleep(2)
                #Modificar Alumno
                elif resmenuAlumno == 3:                    
                    cruds.listarAlumnos()                        
                    idAlumno = cruds.buscarAlumno()
                    cruds.modificarAlumno(idAlumno)
                    sleep(2)
                    __log.debug("Se modificaron los datos del alumno")
                #Elimar Alumno
                elif resmenuAlumno == 4:                    
                    cruds.listarAlumnos()                        
                    idAlumno = cruds.buscarAlumno()
                    cruds.eliminarAlumno(idAlumno)
                    sleep(2)
                    __log.debug("Se eliminaron los datos del alumno")
                elif resmenuAlumno == 0:
                    utils.Salir()
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
