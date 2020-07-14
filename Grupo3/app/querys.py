class Querys:

    #Alumno
    def ListarAllAlumno(self):
        query = "SELECT * FROM alumnos;"
        return query

    def BuscarAlumno(self, Id):
        query = f"SELECT * FROM alumnos where idalumnos = '{Id}'"
        return query

    def InsertAlumno (self, Nombre, Apellido, Correo, Fechanac):
        query = "INSERT INTO alumnos (nombrealumno, apellidoalumno, correoalumno, nacalumno) VALUES ('"+Nombre+"', '"+Apellido+"', '"+Correo+"', '"+Fechanac+"');"
        return query

    def ModificarAlumno (self, Nombre, Apellido, Correo, FechaNac, IdAlumno):
        query = "UPDATE alumnos SET nombrealumno = '"+Nombre+"', apellidoalumno = '"+Apellido+"', correoalumno = '"+Correo+"', nacalumno = '"+str(FechaNac)+"' WHERE idalumnos = '"+str(IdAlumno)+"';"
        return query

    def EliminarAlumno (self, Id):
        query = ""
        return query