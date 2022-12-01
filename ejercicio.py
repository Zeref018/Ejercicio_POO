# Enunciado
# Crear estas clases
# Define los atributos, métodos, constructores... que consideres
# necesarios.
#
# cursos:id,nombre, creditos, añosdeestudio
# alumno:id, nombre, email
# matricula:idmatricula, fechamatricula, idalumno, idcurso
#
# Necesitamos.
# mostrar la ficha del curso
# mostrar la ficha de alumno
# alumno1 se matricula en un curso
# alumno2 se matricula en dos cursos
# mostrar los datos de matrículo
# reto*:método que muestra las mátriculas realizadas en mi centro
import time
from datetime import datetime


class Cursos:
    def __init__(self, idcurso, nombre, creditos, anosdeestudio):
        self.idcurso = idcurso
        self.nombre = nombre
        self.creditos = creditos
        self.anosdeestudio = anosdeestudio
    def mostrarFichaCurso(self):
        print(f'id: {self.idcurso}, nombre: {self.nombre}, creditos: {self.creditos}, años de estudio: {self.anosdeestudio}')

class Alumno:
    def __init__(self, idalumno, nombreA, email):
        self.idalumno = idalumno
        self.nombreA = nombreA
        self.email = email

    def mostrarFichaAlumno(self):
        print(f'id: {self.idalumno}, nombre: {self.nombreA}, email: {self.email}')
class Matricula(Cursos, Alumno):
    def __init__(self,idmatricula, fechamatricula, idalumno, idcurso, nombre, nombreA, creditos, anosdeestudio, email):
        self.idmatricula = idmatricula
        self.fechamatricula = fechamatricula.strftime("%m/%d/%Y, %H:%M:%S.%f")
        super().__init__(idcurso, nombre, creditos, anosdeestudio)

        super(Cursos, self).__init__(idalumno, nombreA, email)

    def mostrarDatos(self):


        print(f'alumno: {self.idalumno}, idcurso: {self.idcurso}, fechamatricula: {self.fechamatricula}, idmatricula: {self.idmatricula}')

#instanciar clases
#voy a suponer que 1 alumno al tener 2 cursos tendría que realizar 2 matriculas
matriculas = []
alumno1 = Alumno(1, 'Alex', 'alex@yahoo.com')
alumno2 = Alumno(2, 'Carmela','carmela@yahoo.com')
alumno1.mostrarFichaAlumno() # mostrar la ficha de alumno
curso1 = Cursos(1, 'Ingenieria de Software', 240, 4)
curso2 = Cursos(2, 'Ingenieria de Caminos', 300, 5)
curso1.mostrarFichaCurso() # mostrar la ficha del curso
matricula1 = Matricula(1, datetime.now(), alumno1.idalumno, curso1.idcurso, curso1.nombre, alumno1.nombreA, curso1.creditos, curso1.anosdeestudio, alumno1.email)
time.sleep(1) #el ordenador me hace los datetime.now en el mismo milisegundo todos, asi que le pongo un segundo de retraso para poder ver las diferencias en datetime.now
matricula2 = Matricula(2, datetime.now(), alumno2.idalumno, curso1.idcurso, curso1.nombre, alumno2.nombreA, curso1.creditos, curso1.anosdeestudio, alumno2.email)
time.sleep(1)
matricula3 = Matricula(3, datetime.now(), alumno2.idalumno, curso2.idcurso, curso2.nombre, alumno2.nombreA, curso2.creditos, curso2.anosdeestudio, alumno2.email)
matricula1.mostrarDatos() # mostrar los datos de matrículo

matriculas.append(matricula1)
matriculas.append(matricula2)
matriculas.append(matricula3)

# reto*:método que muestra las mátriculas realizadas en mi centro
i = 0
for matricula in matriculas:
    matricula.mostrarDatos()
    i = i +1

print(f'hay un total de {i} matriculas')