class Querys:

#  █████  ██      ██    ██ ███    ███ ███    ██  ██████  
# ██   ██ ██      ██    ██ ████  ████ ████   ██ ██    ██ 
# ███████ ██      ██    ██ ██ ████ ██ ██ ██  ██ ██    ██ 
# ██   ██ ██      ██    ██ ██  ██  ██ ██  ██ ██ ██    ██ 
# ██   ██ ███████  ██████  ██      ██ ██   ████  ██████ 

    def ListarAllAlumno(self):
        query = "SELECT * FROM alumnos;"
        return query

    def BuscarAlumno(self, Id):
        query = f"SELECT * FROM alumnos where idalumnos = '{Id}'"
        return query

    def InsertAlumno(self, Nombre, Apellido, Correo, Fechanac):
        query = "INSERT INTO alumnos (nombrealumno, apellidoalumno, correoalumno, nacalumno) VALUES ('"+Nombre+"', '"+Apellido+"', '"+Correo+"', '"+Fechanac+"');"
        return query

    def ModificarAlumno(self, Nombre, Apellido, Correo, FechaNac, IdAlumno):
        query = "UPDATE alumnos SET nombrealumno = '"+Nombre+"', apellidoalumno = '"+Apellido+"', correoalumno = '"+Correo+"', nacalumno = '"+str(FechaNac)+"' WHERE idalumnos = '"+str(IdAlumno)+"';"
        return query

    def EliminarAlumno(self, Id):
        query = ""
        return query



# ██████   ██████   ██████ ███████ ███    ██ ████████ ███████ ███████ 
# ██   ██ ██    ██ ██      ██      ████   ██    ██    ██      ██      
# ██   ██ ██    ██ ██      █████   ██ ██  ██    ██    █████   ███████ 
# ██   ██ ██    ██ ██      ██      ██  ██ ██    ██    ██           ██ 
# ██████   ██████   ██████ ███████ ██   ████    ██    ███████ ███████ 
    
    def ListarAllDocente(self):
        query = "SELECT * FROM docentes;"
        return query

    def BuscarDocente(self, Id):
        query = f"SELECT * FROM docente where iddocentes = '{Id}'"
        return query

    def InsertDocente(self, Nombre, Dni, Correo, Fechanac):
        query = "INSERT INTO docentes (nombredocente, dnidocente, correodocente, nacdocente) VALUES ('"+Nombre+"', '"+Dni+"', '"+Correo+"', '"+Fechanac+"');"
        return query

    def ModificarDocente(self, Nombre, Dni, Correo, FechaNac, IdDocente):
        query = "UPDATE docentes SET nombredocente = '"+Nombre+"', dnidocente = '"+Dni+"', correodocente = '"+Correo+"', nacdocente = '"+str(FechaNac)+"' WHERE iddocentes = '"+str(IdDocente)+"';"
        return query

    def EliminarDocente(self, Id):
        query = ""
        return query



# ███████  █████  ██       ██████   ██████  ███    ██ ███████ ███████ 
# ██      ██   ██ ██      ██    ██ ██    ██ ████   ██ ██      ██      
# ███████ ███████ ██      ██    ██ ██    ██ ██ ██  ██ █████   ███████ 
#      ██ ██   ██ ██      ██    ██ ██    ██ ██  ██ ██ ██           ██ 
# ███████ ██   ██ ███████  ██████   ██████  ██   ████ ███████ ███████

    def ListarAllSalones(self):
        query = "SELECT * FROM salones;"
        return query

    def BuscarSalon(self, Id):
        query = f"SELECT * FROM docente where iddocentes = '{Id}'"
        return query

    def InsertSalon(self, Nombre):
        query = "INSERT INTO salones (nombresalon) VALUES ('"+Nombre+"');"
        return query

    def ModificarSalon(self, Nombre, IdSalon):
        query = "UPDATE salones SET nombresalon = '"+Nombre+"' WHERE idsalones = '"+str(IdSalon)+"';"
        return query

    def EliminarSalon(self, Id):
        query = ""
        return query



#  ██████ ██    ██ ██████  ███████  ██████  ███████ 
# ██      ██    ██ ██   ██ ██      ██    ██ ██      
# ██      ██    ██ ██████  ███████ ██    ██ ███████ 
# ██      ██    ██ ██   ██      ██ ██    ██      ██ 
#  ██████  ██████  ██   ██ ███████  ██████  ███████

    def ListarAllCursos(self):
        query = "SELECT * FROM cursos;"
        return query

    def BuscarCurso(self, Id):
        query = f"SELECT * FROM cursos where idcursos = '{Id}'"
        return query

    def InsertCurso(self, Nombre):
        query = "INSERT INTO cursos (nombrecurso) VALUES ('"+Nombre+"');"
        return query

    def ModificarCurso(self, Nombre, IdCurso):
        query = "UPDATE cursos SET nombrecurso = '"+Nombre+"' WHERE idcursos = '"+str(IdCurso)+"';"
        return query

    def EliminarCurso(self, Id):
        query = ""
        return query



# ██████  ███████ ██████  ██  ██████  ██████   ██████      ███████ ███████  ██████  ██████  ██       █████  ██████  
# ██   ██ ██      ██   ██ ██ ██    ██ ██   ██ ██    ██     ██      ██      ██      ██    ██ ██      ██   ██ ██   ██ 
# ██████  █████   ██████  ██ ██    ██ ██   ██ ██    ██     █████   ███████ ██      ██    ██ ██      ███████ ██████  
# ██      ██      ██   ██ ██ ██    ██ ██   ██ ██    ██     ██           ██ ██      ██    ██ ██      ██   ██ ██   ██ 
# ██      ███████ ██   ██ ██  ██████  ██████   ██████      ███████ ███████  ██████  ██████  ███████ ██   ██ ██   ██ 

    def ListarAllPeriodos(self):
        query = "SELECT * FROM periodoEscolar;"
        return query

    def BuscarPeriodo(self, Id):
        query = f"SELECT * FROM periodoEscolar where idperiodoEscolar = '{Id}'"
        return query

    def InsertPeriodo(self, Nombre):
        query = "INSERT INTO periodoEscolar (desperiodo) VALUES ('"+Nombre+"');"
        return query

    def ModificarPeriodo(self, Nombre, IdPeriodo):
        query = "UPDATE periodoEscolar SET desperiodo = '"+Nombre+"' WHERE idperiodoEscolar = '"+str(IdPeriodo)+"';"
        return query

    def EliminarPeriodo(self, Id):
        query = ""
        return query



# ███    ██  ██████  ████████  █████  ███████ 
# ████   ██ ██    ██    ██    ██   ██ ██      
# ██ ██  ██ ██    ██    ██    ███████ ███████ 
# ██  ██ ██ ██    ██    ██    ██   ██      ██ 
# ██   ████  ██████     ██    ██   ██ ███████ 

    def ListarAllNotas(self):
        query = "SELECT * FROM docentes_has_cursos;"
        return query

    def BuscarNota(self, Nota):
        query = f"SELECT * FROM docentes_has_cursos where nota = '{Nota}'"
        return query

    def InsertNota(self, Nota):
        query = "INSERT INTO docentes_has_cursos (nota) VALUES ('"+Nota+"');"
        return query

    def ModificarNota(self, Nota):
        query = "UPDATE docentes_has_cursos SET nota = '"+Nota+"' WHERE nota = '"+str(Nota)+"';"
        return query

    def EliminarNota(self):
        query = ""
        return query
