from abc import ABC

class Persona(ABC):
    def __init__(self):
        self.nombre=""
        self.apellido=""
        self.edad=""
        self.DNI=""

    def set_nombre(self, nombre):
        self.nombre=nombre

    def set_apellido(self, apellido):
        self.apellido=apellido

    def set_DNI(self, DNI):
        self.DNI=DNI

    def set_edad(self, edad):
        if edad<0:
            raise Exception("La edad no puede ser negativa")
        else:
            self.edad=edad

    def get_data(self, dato):
        dato.lower()
        if dato=="nombre":
            if self.nombre=="":
                print("El nombre está vacío")
            else:
                return self.nombre
        elif dato=="apellido":
            if self.apellido=="":
                print("El apellido está vacío")
            else:
                return self.apellido
        elif dato=="edad":
            if self.edad=="":
                print("La edad está vacía")
            else:
                return self.edad
        elif dato=="DNI":
            if self.DNI=="":
                print("El DNI está vacío")
            else:
                return self.DNI
        else:
            raise Exception("El dato ingresado no corresponde a ningún atributo")

#una_persona=Persona()
#una_persona.set_nombre("Carla")
#una_persona.set_apellido("Schmidt")
#una_persona.set_edad(18)
#una_persona.set_DNI("1123446")
#print(una_persona.get_data("nombre"))
#print(una_persona.get_data("edad"))

class Estudiante(Persona):
    def __init__(self):
        self.cursos=[]
        self.cantidad_cursos=0

    def Matricularse(self, curso):
        if isinstance(curso, Curso):
            if curso in self.cursos:
                raise Exception("Usted ya está matriculado en este curso")
            else:
                curso.cupo+=1
                curso.estudiantes.append(self.nombre+ " "+self.apellido) 
                self.cantidad_cursos+=1
                self.cursos.append(curso)
        else:
            raise Exception("Sólo puede matricularse a cursos")

    def Darse_de_baja(self, curso):
        if isinstance(curso, Curso):
            if curso in self.cursos:
                self.cantidad_cursos=self.cantidad_cursos-1
                index=self.cursos.index(curso)
                self.cursos.pop(index)
                curso.cupo=curso.cupo-1
                index=curso.estudiantes.index(self.nombre+" "+self.apellido)
                curso.estudiantes.pop(index)
            else:
                raise Exception("Usted no está matriculado en dicho curso")
        else:
            raise Exception("El argumento debe ser un curso")
        

class Profesor(Persona):
    def __init__(self):
        self.cantidad_cursos=0
        self.cursos=[]
        self.depto=""
        self.director=""

    # def Concursar(self, curso):
    #     if curso in self.cursos:
    #         raise Exception("Usted ya está dando clases en este curso")
    #     else:
    #         self.cantidad_cursos+=1
    #         self.cursos.append(curso)

    def Renunciar(self, curso):
        if isinstance(curso, Curso):
            if curso.nombre in self.cursos:
                index=self.cursos.index(curso.nombre)
                self.cursos.pop(index)
                self.cantidad_cursos=self.cantidad_cursos-1
                index2=curso.cátedra.index(self.nombre+" "+self.apellido)
                curso.cátedra.pop(index2)
            else:
                raise Exception("Usted no da clases en este curso")
        else:
            raise Exception("El parámetro debe ser un curso")

#class Curso:
#    def _init_(self, matrícula):
#        self.matrícula=matrícula
#        self.cátedra=[]
#        self.estudiantes=0
#        self.jdc=""

#la matrícula (cupo) debería poder elegirse al crear un curso
class Curso:
    def __init__(self, nombre):
        self.cupo=0 #cupo es la cantidad de estudiantes en el curso
        self.nombre=nombre
        self.cátedra=[]
        self.estudiantes=[]
        self.jdc=""

    def Asignar_profesor(self, profesor):
        if isinstance(profesor, Profesor):
            self.cátedra.append(profesor.nombre+" "+profesor.apellido)
            profesor.cantidad_cursos+=1
            profesor.cursos.append(self.nombre)
        else:
            raise Exception("El parámetro debe ser un profesor")
        
    def Asignar_jdc(self, jdc):
        if isinstance(jdc, Profesor):
            if jdc.nombre+" "+jdc.apellido in self.cátedra:
                self.jdc=jdc.get_data("nombre")
            else:
                raise Exception("El Jefe de Cátedra debe pertenecer a la cátedra")
        else:
            raise Exception("El parámetro debe ser un profesor")

    def Listar(self):
        for i in self.estudiantes:   
            print(i)


class Departamento:
    def __init__(self, nombre):
        self.profesores=[]
        self.miembros=0
        self.director=""
        self.nombre=nombre

    def Agregar_profesor(self, profesor):
        if isinstance(profesor, Profesor):
            self.miembros+=1
            self.profesores.append(profesor)
            profesor.depto=self.nombre
        else:
            raise Exception("El parámetro debe ser un profesor")

    def Asignar_director(self, director):
        if isinstance(director, Profesor):
            if director in self.profesores:
                self.director=director.get_data("nombre")
                director.director=self.nombre
                self.depto=self.nombre
            else:
                raise Exception("El director debe pertenecer al departamento")
        else:
            raise Exception("Sólo puede ser director del departamento un profesor")

class Facultad:
    def __init__(self, nombre_depto):
        self.Depto_default=Departamento(nombre_depto)
        self.__departamentos=[self.Depto_default] #para que no puedan modificar los deptos accediento al atributo
        self.estudiantes=[]
        self.cantidad_deptos=1
        self.matrícula=0

    def Crear_departamento(self, nombre_depto):
        nuevo_departamento=Departamento(nombre_depto)
        self.__departamentos.append(nuevo_departamento)
        self.cantidad_deptos+=1

#para no acceder al método del departamento como atributo de facultad
    def Agregar_profesor_a_depto(self, depto, profesor): #depto tiene que ser un str con el nombre del departamento y profesor, un objeto
        for departamento in self.__departamentos:
            if departamento.nombre==depto:
                departamento.Agregar_profesor(profesor)
        
    def Asignar_director_a_depto(self, depto, director):
        for departamento in self.__departamentos:
            if departamento.nombre==depto:
                departamento.Asignar_director(director)

    def Agregar_estudiante(self, estudiante):
        if isinstance(estudiante, Estudiante):
            if estudiante in self.estudiantes:
                raise Exception("El estudiante ya está matriculado")
            else:
                self.estudiantes.append(estudiante)
                self.matrícula+=1
        else:
            raise Exception("El parámetro debe ser un estudiante")

    def Listar_estudiantes(self):
        for i in range(self.matrícula):
            print(self.estudiantes[i])






