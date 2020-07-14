#Clase alumnoss
class alumnos:
      __log = utils.log("alumnos")
  def __init__(self, idalumnos, nombrealumno, apellidoalumno, correoalumno, nacalumno):
    self.idalumnos = idalumnos
    self.nombrealumno = nombrealumno
    self.apellidoalumno = apellidoalumno
    self.correoalumno = correoalumno
    self.nacalumno = nacalumno
    